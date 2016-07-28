# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search_and_index.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='search_and_index.proto',
  package='rpc',
  syntax='proto3',
  serialized_pb=_b('\n\x16search_and_index.proto\x12\x03rpc\"\x1e\n\rSearchRequest\x12\r\n\x05query\x18\x01 \x01(\t\"\x1b\n\x0bSearchReply\x12\x0c\n\x04\x64ocs\x18\x01 \x01(\t\"\x1b\n\x0cIndexRequest\x12\x0b\n\x03\x64oc\x18\x01 \x01(\t\"\x1c\n\nIndexReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\x32p\n\rSearchService\x12\x30\n\x06Search\x12\x12.rpc.SearchRequest\x1a\x10.rpc.SearchReply\"\x00\x12-\n\x05Index\x12\x11.rpc.IndexRequest\x1a\x0f.rpc.IndexReply\"\x00\x42\"\n\x03rpcB\x13SearchAndIndexProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='rpc.SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='rpc.SearchRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=61,
)


_SEARCHREPLY = _descriptor.Descriptor(
  name='SearchReply',
  full_name='rpc.SearchReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docs', full_name='rpc.SearchReply.docs', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=90,
)


_INDEXREQUEST = _descriptor.Descriptor(
  name='IndexRequest',
  full_name='rpc.IndexRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='doc', full_name='rpc.IndexRequest.doc', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=119,
)


_INDEXREPLY = _descriptor.Descriptor(
  name='IndexReply',
  full_name='rpc.IndexReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='rpc.IndexReply.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=149,
)

DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchReply'] = _SEARCHREPLY
DESCRIPTOR.message_types_by_name['IndexRequest'] = _INDEXREQUEST
DESCRIPTOR.message_types_by_name['IndexReply'] = _INDEXREPLY

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREQUEST,
  __module__ = 'search_and_index_pb2'
  # @@protoc_insertion_point(class_scope:rpc.SearchRequest)
  ))
_sym_db.RegisterMessage(SearchRequest)

SearchReply = _reflection.GeneratedProtocolMessageType('SearchReply', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREPLY,
  __module__ = 'search_and_index_pb2'
  # @@protoc_insertion_point(class_scope:rpc.SearchReply)
  ))
_sym_db.RegisterMessage(SearchReply)

IndexRequest = _reflection.GeneratedProtocolMessageType('IndexRequest', (_message.Message,), dict(
  DESCRIPTOR = _INDEXREQUEST,
  __module__ = 'search_and_index_pb2'
  # @@protoc_insertion_point(class_scope:rpc.IndexRequest)
  ))
_sym_db.RegisterMessage(IndexRequest)

IndexReply = _reflection.GeneratedProtocolMessageType('IndexReply', (_message.Message,), dict(
  DESCRIPTOR = _INDEXREPLY,
  __module__ = 'search_and_index_pb2'
  # @@protoc_insertion_point(class_scope:rpc.IndexReply)
  ))
_sym_db.RegisterMessage(IndexReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\003rpcB\023SearchAndIndexProtoP\001\242\002\003HLW'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class SearchServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Search = channel.unary_unary(
        '/rpc.SearchService/Search',
        request_serializer=SearchRequest.SerializeToString,
        response_deserializer=SearchReply.FromString,
        )
    self.Index = channel.unary_unary(
        '/rpc.SearchService/Index',
        request_serializer=IndexRequest.SerializeToString,
        response_deserializer=IndexReply.FromString,
        )


class SearchServiceServicer(object):

  def Search(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Index(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SearchServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Search': grpc.unary_unary_rpc_method_handler(
          servicer.Search,
          request_deserializer=SearchRequest.FromString,
          response_serializer=SearchReply.SerializeToString,
      ),
      'Index': grpc.unary_unary_rpc_method_handler(
          servicer.Index,
          request_deserializer=IndexRequest.FromString,
          response_serializer=IndexReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rpc.SearchService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaSearchServiceServicer(object):
  def Search(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def Index(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaSearchServiceStub(object):
  def Search(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Search.future = None
  def Index(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Index.future = None


def beta_create_SearchService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('rpc.SearchService', 'Index'): IndexRequest.FromString,
    ('rpc.SearchService', 'Search'): SearchRequest.FromString,
  }
  response_serializers = {
    ('rpc.SearchService', 'Index'): IndexReply.SerializeToString,
    ('rpc.SearchService', 'Search'): SearchReply.SerializeToString,
  }
  method_implementations = {
    ('rpc.SearchService', 'Index'): face_utilities.unary_unary_inline(servicer.Index),
    ('rpc.SearchService', 'Search'): face_utilities.unary_unary_inline(servicer.Search),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_SearchService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('rpc.SearchService', 'Index'): IndexRequest.SerializeToString,
    ('rpc.SearchService', 'Search'): SearchRequest.SerializeToString,
  }
  response_deserializers = {
    ('rpc.SearchService', 'Index'): IndexReply.FromString,
    ('rpc.SearchService', 'Search'): SearchReply.FromString,
  }
  cardinalities = {
    'Index': cardinality.Cardinality.UNARY_UNARY,
    'Search': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'rpc.SearchService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)