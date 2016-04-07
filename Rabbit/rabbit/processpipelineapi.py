# coding: utf-8

# Copyright (c) 2015 - 2016, Tony.
# license: MIT, see LICENSE for more details.


class BaseWorker:
    def __init__(self):
        pass

    def process(self):
        pass


class ProcessPipeline(object):
    content = None
    pipeline = None

    def __init__(self):
        pass

    def process(self):
        for worker in self.pipeline:
            worker.process(self.content)

    def add_worker(self, worker):
        self.pipeline.append(worker)

    def add_workers(self, workers):
        for worker in workers:
            self.pipeline.append(worker)

    def add_init_to_content(self, k, v):
        self.content[k] = v
