# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.

# run: ask: python rabbit/rabbit.py https://en.wikipedia.org/wiki/Harry_Potter What is Harry Potter?
# if cannot find module, run export PYTHONPATH='.'

import sys
import config
from answersystemcorepipeline import AnswerSystemCorePipeline


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

    document_url = sys.argv[1]
    config.new_logger.debug("document url:" + document_url)

    # use answerSys
    answer_system = AnswerSystemCorePipeline(question, document_url)
    answer_system.run()
