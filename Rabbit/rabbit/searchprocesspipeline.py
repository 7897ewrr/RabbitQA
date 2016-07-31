# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.
from __future__ import print_function
from processpipelineapi import *
import config
import string
from sets import Set


from grpc.beta import implementations
import rpc_utils.search_and_index_pb2 as search_and_index_pb2

_TIMEOUT_SECONDS = 10


class IndexWorker(BaseWorker):
    @staticmethod
    def index_sentence(sentence_id, sentence):
        channel = implementations.insecure_channel('localhost', 50051)
        stub = search_and_index_pb2.beta_create_SearchService_stub(channel)
        sentence = string.replace(sentence, "\"", " ")
        sentence = string.replace(sentence, "\'", " ")
        config.new_logger.debug("indexing sentence=" + "{'id':'" + str(sentence_id) + "','content':'" + sentence + "'}")
        response = stub.Index(search_and_index_pb2.IndexRequest(
            doc="{'id':'" + str(sentence_id) + "','content':'" + sentence + "'}"), _TIMEOUT_SECONDS)
        config.new_logger.debug(" client received: " + str(response.status))

    @staticmethod
    def process(content):
        sentences = content["sentence_dictionary"].index_sentence_id_to_sentence_map

        for sentence_id in sentences:
            IndexWorker.index_sentence(sentence_id, sentences[sentence_id])


class SearchWorker(BaseWorker):
    @staticmethod
    def process(content):
        query_set = set()

        for ne in content["question_nes"]:
            query_set.add(ne)
        for noun in content["question_nouns"]:
            query_set.add(noun)

        query = ""
        for term in query_set:
            query += term + " "

        channel = implementations.insecure_channel('localhost', 50051)
        stub = search_and_index_pb2.beta_create_SearchService_stub(channel)
        config.new_logger.debug("searching, query=" + query)
        response = stub.Search(search_and_index_pb2.SearchRequest(query=query), _TIMEOUT_SECONDS)
        config.new_logger.debug("search result: " + response.docs)
        content["search_result_index_list"] = response.docs


class SearchProcessPipeline(ProcessPipeline):
    def __init__(self, process_container):
        self._content = process_container
        self._pipeline = []
        self.add_workers([
            IndexWorker,
            SearchWorker
        ])
