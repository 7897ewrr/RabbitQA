# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.

import unittest
from rabbit.stanfordtoolfactory import ParserFactory


class ParserFactoryTest(unittest.TestCase):
    def test_get_parser_and_ner(self):
        self.parser = ParserFactory.get_instance('parser')
        self.ner = ParserFactory.get_instance('ner')
        self.assertTrue(str(self.parser.__class__) == "<class 'nltk.parse.stanford.StanfordParser'>")
        self.assertTrue(str(self.ner.__class__) == "<class 'nltk.tag.stanford.NERTagger'>")

    def test_singleton(self):
        try:
            if self.parser is None:
                self.parser = ParserFactory.get_instance('parser')
        except AttributeError:
            self.parser = ParserFactory.get_instance('parser')
        parser2 = ParserFactory.get_instance('parser')
        self.assertTrue(self.parser == parser2)

        try:
            if self.ner is None:
                self.ner = ParserFactory.get_instance('ner')
        except AttributeError:
            self.ner = ParserFactory.get_instance('ner')
        ner2 = ParserFactory.get_instance('ner')
        self.assertTrue(self.ner == ner2)


if __name__ == '__main__':
    unittest.main()
