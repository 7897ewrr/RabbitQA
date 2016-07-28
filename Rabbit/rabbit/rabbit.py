# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.

# run: ask: python rabbit/rabbit.py https://en.wikipedia.org/wiki/Harry_Potter who is Tom?

import sys
import config
from answersystemcorepipeline import AnswerSystemCorePipeline
from dictionarybuilder import DictionaryBuilder

if __name__ == "__main__":

    # build question
    questionArray = []
    length = len(sys.argv)
    for i in range(2, length):
        questionArray.append(sys.argv[i])
    question = " ".join(questionArray)
    question = str(question)
    # logging. question
    config.new_logger.debug("Question Is:" + question)
    # create Dict
    dictionary_builder = DictionaryBuilder.get_instence('mem', sys.argv[1])
    dictionary = dictionary_builder.build_base()

    # use answerSys
    answer_system = AnswerSystemCorePipeline(question, dictionary)
    answer_system.run()
