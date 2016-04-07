# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.

import config
from nltk.parse.stanford import StanfordParser
from nltk.tag.stanford import NERTagger


class ParserFactory(object):
    parser = None
    ner = None

    @staticmethod
    def get_instance(instance_type):
        if instance_type == 'parser':
            if ParserFactory.parser is not None:
                return ParserFactory.parser
            parser = StanfordParser(
                config.STANFORD_PARSER_MODEL_PATH,
                config.STANFORD_PARSER_PATH
            )
            ParserFactory.parser = parser
            return parser
        elif instance_type == 'ner':
            if ParserFactory.ner is not None:
                return ParserFactory.ner
            ner = NERTagger(
                config.STANFORD_NER_MODEL_PATH,
                config.STANFORD_NER_PATH
            )
            ParserFactory.ner = ner
            return ner
