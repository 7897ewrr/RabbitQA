# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.
from __future__ import print_function
from processpipelineapi import *
import config


from grpc.beta import implementations
import rpc_utils.search_and_index_pb2 as search_and_index_pb2

_TIMEOUT_SECONDS = 10


class IndexWorker(BaseWorker):
    @staticmethod
    def index_sentence(sentence_id, sentence):
        channel = implementations.insecure_channel('localhost', 50051)
        stub = search_and_index_pb2.beta_create_SearchService_stub(channel)
        config.new_logger.debug("indexing sentence=" + "{'id':'" + str(sentence_id) + "','content':'" + sentence + "'}")
        response = stub.Index(search_and_index_pb2.IndexRequest(
            doc="{'id':'" + str(sentence_id) + "','content':'" + sentence + "'}"), _TIMEOUT_SECONDS)
        config.new_logger.debug(" client received: " + str(response.status))

    @staticmethod
    def process(content):
        sentences = content["document_dictionary"].sentence_index
        index_sentence_id_to_sentence_map = {}
        sentence_id = 1
        for sentence in sentences:
            IndexWorker.index_sentence(sentence_id, sentence)
            index_sentence_id_to_sentence_map[sentence_id] = sentence
            sentence_id += 1
        content["index_sentence_id_to_sentence_map"] = index_sentence_id_to_sentence_map


# class SearchWorker(BaseWorker):
#     @staticmethod
#     def process(content):
#         document_dictionary = content['document_dictionary']
#         document_corpus = document_dictionary.document_corpus
#         query = ['dog']
#         search_result_index_list = []
#         i = 0
#         for sentence in document_corpus:
#             contain_all = True
#             word_set = set()
#             for each_word in sentence:
#                 word_set.add(str(each_word))
#             for query_word in query:
#                 if query_word not in word_set:
#                     contain_all = False
#                     break
#             if contain_all:
#                 search_result_index_list.append(i)
#             i += 1
#         config.new_logger.debug(search_result_index_list)


class SearchWorker(BaseWorker):
    @staticmethod
    def process(content):
        query = ""

        for ne in content["question_nes"]:
            query += ne
        for noun in content["question_nouns"]:
            query += noun

        channel = implementations.insecure_channel('localhost', 50051)
        stub = search_and_index_pb2.beta_create_SearchService_stub(channel)
        config.new_logger.debug("searching, query=" + query)
        response = stub.Search(search_and_index_pb2.SearchRequest(query=query), _TIMEOUT_SECONDS)
        config.new_logger.debug("search result: " + response.docs)

        index_sentence_id_to_sentence_map = content["index_sentence_id_to_sentence_map"]


class SearchProcessPipeline(ProcessPipeline):
    def __init__(self, process_container):
        self._content = process_container
        self._pipeline = []
        self.add_workers([
            IndexWorker,
            SearchWorker
        ])
