# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.

import unittest
from rabbit.utilworkers import ExtractKeyWorker


class TestExtractKeyWorker(unittest.TestCase):
    @staticmethod
    def get_worker(container):
        worker = ExtractKeyWorker()
        worker.container = container
        worker.init_element("test_sent", None)
        return worker

    def test_ner(self):
        # case 1
        container = {
            "test_sent": 'Vivian Carol Sobchack is an American cinema and media theorist and cultural critic.'}
        worker = self.get_worker(container)
        worker.get_name_entities()
        self.assertEquals(worker.name_entities, ['Vivian Carol Sobchack'])
        # case 2
        container = {
            "test_sent": "Since the release of the first novel, Harry Potter and the Philosopher's Stone, "
                         "on 30 June 1997, the books have gained immense popularity, "
                         "critical acclaim and commercial success worldwide."}
        worker = self.get_worker(container)
        worker.get_name_entities()
        self.assertEquals(worker.name_entities, ["Harry Potter", '30 June 1997,'])

    def test_get_nouns(self):
        # case 1
        container = {'test_sent': 'Vivian Carol Sobchack does not like an American cinema'}
        worker = self.get_worker(container)
        worker.get_nouns()
        self.assertEquals(worker.nouns, ['Vivian Carol Sobchack', 'an American cinema'])

        # case 2
        container = {'test_sent': "Since the release of the first novel, "
                                  "Harry Potter and the Philosopher's Stone, on 30 June 1997,"
                                  " the books have gained immense popularity, "
                                  "critical acclaim and commercial success worldwide."}
        worker = self.get_worker(container)
        worker.get_nouns()
        self.assertEquals(worker.nouns, ["the release of the first novel ,"
                                         " Harry Potter and the Philosopher 's Stone , on 30 June 1997",
                                         'the books',
                                         'immense popularity , critical acclaim and commercial success'])


if __name__ == '__main__':
    unittest.main()
