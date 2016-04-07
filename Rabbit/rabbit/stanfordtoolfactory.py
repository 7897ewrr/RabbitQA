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
                config.new_logger.debug("return old parser")
                return ParserFactory.parser
            parser = StanfordParser(
                "/Users/Tony/Desktop/CMU-COURSE/NLP/stanford-parser-full-2015-01-30/stanford-parser-3.5.1-models.jar",
                "/Users/Tony/Desktop/CMU-COURSE/NLP/stanford-parser-full-2015-01-30/stanford-parser.jar"
            )
            ParserFactory.parser = parser
            config.new_logger.debug("generate new parser")
            return parser
        elif instance_type == 'ner':
            if ParserFactory.ner is not None:
                config.new_logger.debug("return old ner")
                return ParserFactory.ner
            ner = NERTagger(
                '/Users/Tony/Desktop/CMU-COURSE/NLP/stanford-ner-2015-01-30/'
                'classifiers/english.all.7class.distsim.crf.ser.gz',
                '/Users/Tony/Desktop/CMU-COURSE/NLP/stanford-ner-2015-01-30/stanford-ner-3.5.1.jar'
            )
            ParserFactory.ner = ner
            config.new_logger.debug("generate new ner")
            return ner
