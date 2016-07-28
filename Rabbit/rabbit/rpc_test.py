from __future__ import print_function

from grpc.beta import implementations

import rpc_utils.search_and_index_pb2 as search_and_index_pb2

_TIMEOUT_SECONDS = 10


def run_clear():
    channel = implementations.insecure_channel('localhost', 50051)
    stub = search_and_index_pb2.beta_create_SearchService_stub(channel)
    response = stub.Index(search_and_index_pb2.IndexRequest(doc="{'id':'-1','content':'CLEAR'}"), _TIMEOUT_SECONDS)
    print(" client received: ", response.status)


def run_add_all_index():
    channel = implementations.insecure_channel('localhost', 50051)
    stub = search_and_index_pb2.beta_create_SearchService_stub(channel)
    response = stub.Index(search_and_index_pb2.IndexRequest(doc="{'id':'1','content':'A beautiful hotel'}"),
                          _TIMEOUT_SECONDS)
    print(" client received: ", response.status)
    response = stub.Index(search_and_index_pb2.IndexRequest(doc="{'id':'2','content':'A bad apple'}"), _TIMEOUT_SECONDS)
    print(" client received: ", response.status)


def run_search():
    channel = implementations.insecure_channel('localhost', 50051)
    stub = search_and_index_pb2.beta_create_SearchService_stub(channel)
    response = stub.Search(search_and_index_pb2.SearchRequest(query='I love beautiful hotel'), _TIMEOUT_SECONDS)
    print(" client received: " + response.docs)


if __name__ == '__main__':
    run_add_all_index()
    run_search()
    run_clear()
