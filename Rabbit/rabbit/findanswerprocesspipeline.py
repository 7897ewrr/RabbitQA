# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.

from processpipelineapi import *
import config


class SearchWorker(BaseWorker):
    @staticmethod
    def process(content):
        document_dictionary = content['document_dictionary']
        document_corpus = document_dictionary.document_corpus
        query = ['dog']
        search_result_index_list = []
        i = 0
        for sentence in document_corpus:
            contain_all = True
            word_set = set()
            for each_word in sentence:
                word_set.add(str(each_word))
            for query_word in query:
                if query_word not in word_set:
                    contain_all = False
                    break
            if contain_all:
                search_result_index_list.append(i)
            i += 1
        config.new_logger.debug(search_result_index_list)


class FindAnswerProcessPipeline(ProcessPipeline):
    def __init__(self, process_container):
        self._content = process_container
        self._pipeline = []
        self.add_workers([
            SearchWorker,
        ])
