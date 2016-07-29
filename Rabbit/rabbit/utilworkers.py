# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.


import config
from processpipelineapi import BaseWorker
from stanfordtoolfactory import ParserFactory
from nltk.corpus import wordnet

logger = config.new_logger.getLogger('UtilWorkers')


class ExtractKeyWorker(BaseWorker):
    def __init__(self):
        self.sentence = None
        self.sentence_tree = None
        self.ner = ParserFactory.get_instance('ner')
        self.parse = ParserFactory.get_instance('parser')
        self.word_net = wordnet
        self.container = None
        self.name_entities = None
        self.nouns = None
        self.output_ne_name = None
        self.output_nouns_name = None

    def init_element(self, name, tree_name):
        self.sentence = self.container[name]
        if tree_name is not None:
            self.sentence_tree = self.container[tree_name]

    def process(self, content):
        self.output_ne_name = 'nes'
        self.output_nouns_name = 'nouns'
        self.container = content
        self.init_element('eg: origin_question', None)
        self.run()
        self.container[self.output_ne_name] = self.name_entities
        self.container[self.output_nouns_name] = self.nouns

    def run(self):
        self.get_name_entities()
        self.get_nouns()

    def get_name_entities(self):
        res = self.ner.tag(self.sentence.split())
        config.new_logger.debug('NER tag is:' + str(res))
        nes = []
        curr_ner = ''

        for part in res[0]:
            if str(part[1]) != 'O':
                curr_ner += str(part[0])
                curr_ner += ' '
            elif curr_ner != '':
                nes.append(curr_ner[:-1])
                curr_ner = ''
        if curr_ner != '':
            nes.append(curr_ner[:-1])
        self.name_entities = nes
        # self.container[self.output_ne_name] = nes

    def get_nouns(self):

        def dfs(tree, nouns):
            try:
                if tree.label()[:1] == 'N':
                    nouns.append(str(' '.join(tree.leaves())))
                else:
                    for i in xrange(len(tree)):
                        dfs(tree[i], nouns)
            except AttributeError:
                pass

        if self.sentence_tree is None:
            self.sentence_tree = list(self.parse.raw_parse(self.sentence))[0]
        nouns_collection = []
        dfs(self.sentence_tree, nouns_collection)
        config.new_logger.debug("nouns_collection=" + str(nouns_collection))
        self.nouns = nouns_collection
        self.container[self.output_nouns_name] = nouns_collection
