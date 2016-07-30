# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.


from processpipelineapi import *
from dictionarybuilder import *

'''
    precess document
'''


class FetchDocumentWorker(BaseWorker):
    @staticmethod
    def process(content):
        dictionary_builder = DictionaryBuilder.get_instance('mem', content["document_url"])
        sentence_dictionary = dictionary_builder.build_base()
        content["sentence_dictionary"] = sentence_dictionary


class DocumentProcessPipeline(ProcessPipeline):
    def __init__(self, process_container):
        self._content = process_container
        self._pipeline = []
        self.add_workers([
            FetchDocumentWorker,
        ])
