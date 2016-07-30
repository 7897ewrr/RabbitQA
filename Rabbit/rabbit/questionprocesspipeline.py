# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.

from nltk.tree import Tree
from pattern.en import lemma
from nltk.corpus import stopwords

import tags
import config
from processpipelineapi import *
from stanfordtoolfactory import ParserFactory
from utilworkers import ExtractKeyWorker

'''
    precess question pipeline
    Input: the original question
    Output:
        a collection contains:
            origin_question_string: input question
            question_tree: question parse tree
            question_type: type of the question
            reversed_question
            question_query
            question_nes
            question_nouns

'''


class ParseQuestionWorker(BaseWorker):
    @staticmethod
    def process(content):
        parser = ParserFactory.get_instance('parser')
        origin_question_string = content['origin_question_string']
        question_tree = list(parser.raw_parse(origin_question_string))[0]
        content['question_tree'] = question_tree


class GetQuestionTypeWorker(BaseWorker):
    @staticmethod
    def process(content):
        question_tree = content['question_tree']
        if question_tree[0].label() == tags.WH_QUESTION_TYPE:
            config.new_logger.debug("The TYPE of the question is WH")
            content['question_type'] = tags.WH_QUESTION_TYPE
            return
        if question_tree[0].label() == tags.BINARY_QUESTION_TYPE:
            config.new_logger.debug("The TYPE of the question is SQ")
            content['question_type'] = tags.BINARY_QUESTION_TYPE
            return
        else:
            raise Exception('question type error', question_tree[0].label())


class ReverseQuestionWorker(BaseWorker):
    @staticmethod
    def uncap(phrase):
        first = ReverseQuestionWorker.first_word(phrase)
        if first.label() != tags.NOUN_PROPER:
            first[0] = first[0].lower()

    @staticmethod
    def first_word(tree):
        while isinstance(tree[0], Tree):
            tree = tree[0]
        return tree

    @staticmethod
    def tree_to_string(tree):
        return ' '.join(tree.leaves())

    @staticmethod
    def reverse_binary_form_question(question_tree):
        assert (question_tree.label() == tags.BINARY_QUESTION_TYPE)
        aux = question_tree[0]
        ReverseQuestionWorker.uncap(aux)  # uncapitalize the aux
        assert (tags.is_verb(aux.label()))
        # subject gap
        if len(question_tree) < 2:
            return ReverseQuestionWorker.tree_to_string(question_tree)
        subj = question_tree[1]
        assert (subj.label() == tags.NP)
        if len(question_tree) != 2:
            pred = question_tree[2]

            assert (pred.label() == tags.VP or pred.label() == tags.NP or pred.label() == tags.ADJP)
            # do-deletion
            if lemma(aux[0]) == 'do':
                assert (tags.is_verb(pred.label()))
                head_verb = pred[0]
                # re-conjugate head verb with inflection of aux 'do'
                head_verb[0] = tags.conjugate(head_verb[0], tags.get_inflection(aux))
                return ' '.join(
                    [ReverseQuestionWorker.tree_to_string(subj), ReverseQuestionWorker.tree_to_string(pred)])

            # real (non-do) auxiliary
            else:
                return ' '.join(
                    [ReverseQuestionWorker.tree_to_string(subj), aux[0], ReverseQuestionWorker.tree_to_string(pred)])
        else:
            return ' '.join(
                [ReverseQuestionWorker.tree_to_string(subj), aux[0]])

    @staticmethod
    def process(content):
        question_tree = content['question_tree']
        type = content['question_type']
        if type == tags.WH_QUESTION_TYPE:
            config.new_logger.debug("question tree:" + str(question_tree[0][1]))
            try:
                reversed_question = ReverseQuestionWorker.reverse_binary_form_question(question_tree[0][1])
            except:
                reversed_question = ReverseQuestionWorker.tree_to_string(question_tree[0][1])
            pass
        elif type == tags.BINARY_QUESTION_TYPE:
            try:
                reversed_question = ReverseQuestionWorker.reverse_binary_form_question(question_tree[0])
            except:
                reversed_question = ReverseQuestionWorker.tree_to_string(question_tree[1])
        config.new_logger.debug("reversed question is: " + reversed_question)
        content['reversed_question'] = reversed_question


class QuestionExtractKeyWorker(ExtractKeyWorker):
    def process(self, content):
        self.output_ne_name = 'question_nes'
        self.output_nouns_name = 'question_nouns'
        self.container = content
        self.init_element('origin_question_string', 'question_tree')
        self.run()
        self.container[self.output_ne_name] = self.name_entities
        self.container[self.output_nouns_name] = self.nouns


class GenerateQuery(BaseWorker):
    @staticmethod
    def process(content):
        ner = content['question_nes']
        nouns = content['question_nouns']
        word_bag = []
        for words in ner:
            for word in words.split():
                word_bag.append(word)
        for words in nouns:
            for word in words.split():
                word_bag.append(word)
        stop = stopwords.words('english')
        query = [item for item in word_bag if item not in stop]
        content['question_query'] = query
        config.new_logger.debug("query=" + str(query))


class QuestionProcessPipeline(ProcessPipeline):
    def __init__(self, process_container):
        self._content = process_container
        self._pipeline = []
        self.add_workers([
            ParseQuestionWorker,
            GetQuestionTypeWorker,
            ReverseQuestionWorker,
            QuestionExtractKeyWorker(),
            GenerateQuery,
        ])
