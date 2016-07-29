# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.

import requests
import config
from bs4 import BeautifulSoup
import nltk
from stanfordtoolfactory import ParserFactory
import redis


class DictionaryRedisBuilder(object):
    sentIndex = []
    parser = None
    ner = None
    redisConn = None

    def __init__(self, url):
        self.url = url
        self.parser = ParserFactory.get_instance('parser')
        self.ner = ParserFactory.get_instance('ner')
        self.redisConn = redis.StrictRedis(host='localhost', port=6379, db=0)

    def get_web_content(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        wiki_content = soup.find(id="mw-content-text").extract().get_text()
        return wiki_content

    def filter_string(self, text):
        """filt the string like [12] in sentence
        """
        index = -1
        res = ""
        flag = False
        for i in range(len(text)):
            if text[i] == "[":
                flag = True
                continue

            if text[i] == "]":
                # print index, i
                flag = False
                continue
                # text = text.replace(text[index:i+1],"")
            if flag == True:
                continue
            if flag == False:
                res = res + text[i]
        return res

    def index_sent(self):
        wiki_content = self.get_web_content()
        wiki_sents = nltk.sent_tokenize(wiki_content)
        redis_index = 0
        for sentence in wiki_sents:
            if "\n" in sentence:
                continue
            sentence = self.filter_string(sentence)
            parsetree = list(self.parser.raw_parse(sentence))[0]

            '''with open("par.txt", "w") as f:
                f.write(str(parsetree))'''
            if str(parsetree[0].label()) != "S":
                continue
            self.sentIndex.append(parsetree)

            print sentence
            # print(parsetree)
            res = self.ner.tag(sentence.split())
            for part in res[0]:
                if str(part[1]) != 'O':
                    print(part[0])
                    self.redisConn.sadd(str(part[0]), redis_index)

            # break
            redis_index += 1

    def build_base(self):
        dict = Dictionary()
        self.redisConn = dict.redisConn
        print(self.url)
        self.index_sent()
        dict.sentence_index = self.sentIndex
        return dict


class DictionaryMemBuilder(object):
    def __init__(self, url):
        self.sentence_index = list()
        self.parse_tree_index = list()
        self.url = url
        self.parser = ParserFactory.get_instance('parser')
        self.ner = ParserFactory.get_instance('ner')

    def get_web_content(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content, 'html.parser')
        wiki_content = soup.find(id="mw-content-text").extract().get_text()
        return wiki_content

    @staticmethod
    def filter_string(text):
        """filt the string like [12] in sentence
        """
        res = ""
        flag = False
        for i in range(len(text)):
            if text[i] == "[":
                flag = True
                continue

            if text[i] == "]":
                # print index, i
                flag = False
                continue
                # text = text.replace(text[index:i+1],"")
            if flag:
                continue
            else:
                res = res + text[i]
        return res

    def create_index(self, is_test=False, num=10000):
        wiki_sentences = []
        if is_test:
            with open('tests/testdocument.txt') as f:
                for line in f:
                    wiki_sentences.append(line[:-1])
        else:
            wiki_content = self.get_web_content()
            wiki_sentences = nltk.sent_tokenize(wiki_content)
        index = 0
        for sentence in wiki_sentences:
            if "\n" in sentence:
                continue
            sentence = self.filter_string(sentence)
            parse_tree = list(self.parser.raw_parse(sentence))[0]

            with open("par.txt", "w") as f:
                f.write(str(parse_tree))

            if str(parse_tree[0].label()) != "S":
                continue
            self.sentence_index.append(sentence)
            self.parse_tree_index.append(parse_tree)

            config.new_logger.debug("Sentence is: " + sentence)
            config.new_logger.debug("Parse tree is: " + str(parse_tree))
            '''
            res = self.ner.tag(sentence.split())
            for part in res[0]:
                if str(part[1]) != 'O':
                    print(part[0])
            '''
            index += 1
            if index == num:
                break

    def build_base(self):
        dictionary = Dictionary()
        config.new_logger.debug("WIKI URL IS: " + self.url)
        config.new_logger.info("--------------- start parsing wiki doc --------------")
        self.create_index(config.USE_TEST_INPUT, config.INDEX_SENTENCE_NUM)
        dictionary.sentence_index = self.sentence_index
        dictionary.parse_tree_index = self.parse_tree_index
        return dictionary


class DictionaryBuilder(object):
    @staticmethod
    def get_instance(type, url):
        if type == 'mem':
            dictionary_builder = DictionaryMemBuilder(url)
        elif type == 'redis':
            dictionary_builder = DictionaryRedisBuilder(url)
        else:
            raise Exception('DictionaryBuilder TYPE ERROR')
        return dictionary_builder


class Dictionary(object):
    def __init__(self):
        self.sentence_index = None
        self.parse_tree_index = None
