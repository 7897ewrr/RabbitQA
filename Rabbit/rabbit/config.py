# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.


import logging as new_logger

new_logger.basicConfig(format='%(asctime)s %(levelname)s %(module)s:%(message)s', level=new_logger.INFO)

USE_TEST_INPUT = False
INDEX_SENTENCE_NUM = 5


STANFORD_PARSER_PATH = '/Users/Tony/Desktop/CMU-COURSE/NLP/stanford-parser-full-2015-01-30/stanford-parser.jar'
STANFORD_PARSER_MODEL_PATH = '/Users/Tony/Desktop/CMU-COURSE/NLP/stanford-parser-full-2015-01-30/stanford-parser-3.5.1-models.jar'
STANFORD_NER_PATH = '/Users/Tony/Desktop/CMU-COURSE/NLP/stanford-ner-2015-01-30/stanford-ner-3.5.1.jar'
STANFORD_NER_MODEL_PATH = '/Users/Tony/Desktop/CMU-COURSE/NLP/stanford-ner-2015-01-30/classifiers/english.all.7class.distsim.crf.ser.gz'
