# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.

import config
from questionprocesspipeline import QuestionProcessPipeline
from documentprocesspipeline import DocumentProcessPipeline
from searchprocesspipeline import SearchProcessPipeline


class AnswerSystemCorePipeline:
    def __init__(self, origin_question_string, document_url):
        self.process_container = dict()
        self.process_container['origin_question_string'] = origin_question_string
        self.process_container['document_url'] = document_url

    def parse_document(self):
        """
        Input: document_url
        Output: sentence_dictionary
                    -index_sentence_id_to_sentence_map
                    -index_sentence_id_to_sentence_tree_map
        """
        config.new_logger.info("--------------- start parsing document --------------")
        pipeline = DocumentProcessPipeline(self.process_container)
        pipeline.process()
        config.new_logger.debug(self.process_container.keys())

    def parse_question(self):
        """
        Input: origin_question_string
        Output: question_tree: question parse tree
                question_type: type of the question
                reversed_question
                question_query
                question_nes
                question_nouns
        """
        config.new_logger.info("--------------- start parsing question --------------")
        pipeline = QuestionProcessPipeline(self.process_container)
        pipeline.process()
        config.new_logger.debug(self.process_container.keys())

    def search_sentence(self):
        """
        Input:  sentence_dictionary
                question_nouns
                question_nes

        Output: search_result_index_list
        """
        config.new_logger.info("--------------- start indexing and searching sentence ------------")
        pipeline = SearchProcessPipeline(self.process_container)
        pipeline.process()
        config.new_logger.debug(self.process_container.keys())

    def run(self):
        config.new_logger.info("--------------- start running -----------------------")
        self.parse_document()
        self.parse_question()
        self.search_sentence()
