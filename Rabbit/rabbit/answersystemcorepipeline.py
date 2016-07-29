# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.

import config
from questionprocesspipeline import QuestionProcessPipeline
from documentprocesspipeline import DocumentProcessPipeline
from searchprocesspipeline import SearchProcessPipeline


class AnswerSystemCorePipeline:
    def __init__(self, question_input, dictionary):
        self.process_container = dict()
        self.process_container['origin_question_string'] = question_input
        self.process_container['document_dictionary'] = dictionary

    def parse_question(self):
        """
            precess question
            questionInput: the original question
            questionProcessResult: a collection contains:
                originQuestion: input question
                questionTree: question parse tree
                questionType: type of the question
        """
        config.new_logger.info("--------------- start parsing question --------------")
        pipeline = QuestionProcessPipeline(self.process_container)
        pipeline.process()
        config.new_logger.debug(self.process_container.keys())

    def parse_document(self):
        config.new_logger.info("--------------- start parsing document --------------")
        pipeline = DocumentProcessPipeline(self.process_container)
        pipeline.process()
        config.new_logger.debug(self.process_container.keys())

    def search_sentence(self):
        config.new_logger.info("--------------- start searching sentence ------------")
        pipeline = SearchProcessPipeline(self.process_container)
        pipeline.process()
        config.new_logger.debug(self.process_container.keys())

    def run(self):
        config.new_logger.info("--------------- start running -----------------------")
        self.parse_question()
        self.parse_document()
        self.search_sentence()
