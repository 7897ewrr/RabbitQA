# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.


from processpipelineapi import *
from utilworkers import ExtractKeyWorker
from nltk.corpus import stopwords

'''
    precess document
'''


class GenerateCorpusWorker(BaseWorker):
    @staticmethod
    def process(content):
        document_dictionary = content['document_dictionary']
        trees = document_dictionary.parse_tree_index
        document_dictionary.document_corpus = []
        stop = stopwords.words('english')
        for tree in trees:
            document_dictionary.document_corpus.append([str(item) for item in tree.leaves() if item not in stop])


class DocumentExtractKeyWorker(ExtractKeyWorker):
    def process(self, content):
        self.output_ne_name = 'question_nes'
        self.output_nouns_name = 'question_nouns'
        self.container = content
        self.init_element('origin_question', 'question_tree')
        self.run()
        self.container[self.output_ne_name] = self.name_entities
        self.container[self.output_nouns_name] = self.nouns


class DocumentProcessPipeline(ProcessPipeline):
    def __init__(self, process_container):
        self._content = process_container
        self._pipeline = []
        self.add_workers([
            GenerateCorpusWorker,
        ])
