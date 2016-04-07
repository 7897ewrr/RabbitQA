# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.


class BaseWorker:
    def __init__(self):
        pass

    def process(self):
        pass


class ProcessPipeline(object):
    def __init__(self):
        self._content = None
        self._pipeline = None

    def process(self):
        for worker in self._pipeline:
            worker.process(self._content)

    def add_worker(self, worker):
        self._pipeline.append(worker)

    def add_workers(self, workers):
        for worker in workers:
            self._pipeline.append(worker)

    def add_init_to_content(self, k, v):
        self._content[k] = v
