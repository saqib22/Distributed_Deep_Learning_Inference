# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_service.proto',
  package='grpc_service',
  syntax='proto3',
  serialized_options=b'\n\035io.grpc.examples.grpc_serviceB\020GRPCServiceProtoP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12grpc_service.proto\x12\x0cgrpc_service\"\\\n\x03\x42id\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x11\n\tbid_value\x18\x02 \x01(\x02\x12\r\n\x05layer\x18\x03 \x01(\t\x12\x0f\n\x07\x62\x65nefit\x18\x04 \x01(\x02\x12\x0f\n\x07success\x18\x05 \x01(\x08\"X\n\rBiddingResult\x12\x11\n\tserver_id\x18\x01 \x01(\t\x12\x0b\n\x03\x41\x63k\x18\x02 \x01(\x08\x12\x13\n\x0bprice_value\x18\x03 \x01(\x02\x12\x12\n\nNack_layer\x18\x04 \x01(\t\"\x1c\n\x05Price\x12\x13\n\x0bprice_value\x18\x01 \x01(\x02\"\x1d\n\x08ServerID\x12\x11\n\tserver_id\x18\x01 \x01(\t\"!\n\x0eServerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"g\n\nAssignment\x12\x17\n\x0flayers_assigned\x18\x01 \x01(\x08\x12\x15\n\rlayer_profits\x18\x02 \x01(\t\x12\x16\n\x0elayer_benefits\x18\x03 \x01(\t\x12\x11\n\tdevice_id\x18\x04 \x01(\t\"\x19\n\nConnection\x12\x0b\n\x03msg\x18\x01 \x01(\t\">\n\x0c\x41\x64\x64\x44ropLayer\x12\r\n\x05layer\x18\x01 \x01(\t\x12\x0e\n\x06profit\x18\x02 \x01(\x02\x12\x0f\n\x07\x62\x65nefit\x18\x03 \x01(\x02\"L\n\x08\x46\x65\x61tures\x12\x0e\n\x06inputs\x18\x01 \x01(\t\x12\x0b\n\x03\x44\x41G\x18\x02 \x01(\x0c\x12\x12\n\npool_layer\x18\x03 \x01(\x0c\x12\x0f\n\x07\x66latten\x18\x04 \x01(\x08\"&\n\x05Preds\x12\x0e\n\x06output\x18\x01 \x01(\t\x12\r\n\x05layer\x18\x02 \x01(\t2\x82\x05\n\x04\x44\x41MA\x12>\n\nbid_server\x12\x11.grpc_service.Bid\x1a\x1b.grpc_service.BiddingResult\"\x00\x12\x43\n\x10get_server_price\x12\x18.grpc_service.Connection\x1a\x13.grpc_service.Price\"\x00\x12\x43\n\rget_server_id\x12\x18.grpc_service.Connection\x1a\x16.grpc_service.ServerID\"\x00\x12O\n\x13set_layers_assigned\x12\x18.grpc_service.Assignment\x1a\x1c.grpc_service.ServerResponse\"\x00\x12\x42\n\x11start_discounting\x12\x18.grpc_service.Connection\x1a\x11.grpc_service.Bid\"\x00\x12G\n\tack_layer\x12\x1a.grpc_service.AddDropLayer\x1a\x1c.grpc_service.ServerResponse\"\x00\x12J\n\x0creturn_layer\x12\x1a.grpc_service.AddDropLayer\x1a\x1c.grpc_service.ServerResponse\"\x00\x12H\n\nnack_layer\x12\x1a.grpc_service.AddDropLayer\x1a\x1c.grpc_service.ServerResponse\"\x00\x12<\n\x0binfer_layer\x12\x16.grpc_service.Features\x1a\x13.grpc_service.Preds\"\x00\x42\x39\n\x1dio.grpc.examples.grpc_serviceB\x10GRPCServiceProtoP\x01\xa2\x02\x03HLWb\x06proto3'
)




_BID = _descriptor.Descriptor(
  name='Bid',
  full_name='grpc_service.Bid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='grpc_service.Bid.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid_value', full_name='grpc_service.Bid.bid_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='layer', full_name='grpc_service.Bid.layer', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='benefit', full_name='grpc_service.Bid.benefit', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='success', full_name='grpc_service.Bid.success', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=128,
)


_BIDDINGRESULT = _descriptor.Descriptor(
  name='BiddingResult',
  full_name='grpc_service.BiddingResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_id', full_name='grpc_service.BiddingResult.server_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Ack', full_name='grpc_service.BiddingResult.Ack', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price_value', full_name='grpc_service.BiddingResult.price_value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Nack_layer', full_name='grpc_service.BiddingResult.Nack_layer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=218,
)


_PRICE = _descriptor.Descriptor(
  name='Price',
  full_name='grpc_service.Price',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='price_value', full_name='grpc_service.Price.price_value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=248,
)


_SERVERID = _descriptor.Descriptor(
  name='ServerID',
  full_name='grpc_service.ServerID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_id', full_name='grpc_service.ServerID.server_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=279,
)


_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='grpc_service.ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='grpc_service.ServerResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=314,
)


_ASSIGNMENT = _descriptor.Descriptor(
  name='Assignment',
  full_name='grpc_service.Assignment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='layers_assigned', full_name='grpc_service.Assignment.layers_assigned', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='layer_profits', full_name='grpc_service.Assignment.layer_profits', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='layer_benefits', full_name='grpc_service.Assignment.layer_benefits', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='grpc_service.Assignment.device_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=419,
)


_CONNECTION = _descriptor.Descriptor(
  name='Connection',
  full_name='grpc_service.Connection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='grpc_service.Connection.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=446,
)


_ADDDROPLAYER = _descriptor.Descriptor(
  name='AddDropLayer',
  full_name='grpc_service.AddDropLayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='layer', full_name='grpc_service.AddDropLayer.layer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='profit', full_name='grpc_service.AddDropLayer.profit', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='benefit', full_name='grpc_service.AddDropLayer.benefit', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=448,
  serialized_end=510,
)


_FEATURES = _descriptor.Descriptor(
  name='Features',
  full_name='grpc_service.Features',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='grpc_service.Features.inputs', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='DAG', full_name='grpc_service.Features.DAG', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pool_layer', full_name='grpc_service.Features.pool_layer', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flatten', full_name='grpc_service.Features.flatten', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=512,
  serialized_end=588,
)


_PREDS = _descriptor.Descriptor(
  name='Preds',
  full_name='grpc_service.Preds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='output', full_name='grpc_service.Preds.output', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='layer', full_name='grpc_service.Preds.layer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=628,
)

DESCRIPTOR.message_types_by_name['Bid'] = _BID
DESCRIPTOR.message_types_by_name['BiddingResult'] = _BIDDINGRESULT
DESCRIPTOR.message_types_by_name['Price'] = _PRICE
DESCRIPTOR.message_types_by_name['ServerID'] = _SERVERID
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE
DESCRIPTOR.message_types_by_name['Assignment'] = _ASSIGNMENT
DESCRIPTOR.message_types_by_name['Connection'] = _CONNECTION
DESCRIPTOR.message_types_by_name['AddDropLayer'] = _ADDDROPLAYER
DESCRIPTOR.message_types_by_name['Features'] = _FEATURES
DESCRIPTOR.message_types_by_name['Preds'] = _PREDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Bid = _reflection.GeneratedProtocolMessageType('Bid', (_message.Message,), {
  'DESCRIPTOR' : _BID,
  '__module__' : 'grpc_service_pb2'
  # @@protoc_insertion_point(class_scope:grpc_service.Bid)
  })
_sym_db.RegisterMessage(Bid)

BiddingResult = _reflection.GeneratedProtocolMessageType('BiddingResult', (_message.Message,), {
  'DESCRIPTOR' : _BIDDINGRESULT,
  '__module__' : 'grpc_service_pb2'
  # @@protoc_insertion_point(class_scope:grpc_service.BiddingResult)
  })
_sym_db.RegisterMessage(BiddingResult)

Price = _reflection.GeneratedProtocolMessageType('Price', (_message.Message,), {
  'DESCRIPTOR' : _PRICE,
  '__module__' : 'grpc_service_pb2'
  # @@protoc_insertion_point(class_scope:grpc_service.Price)
  })
_sym_db.RegisterMessage(Price)

ServerID = _reflection.GeneratedProtocolMessageType('ServerID', (_message.Message,), {
  'DESCRIPTOR' : _SERVERID,
  '__module__' : 'grpc_service_pb2'
  # @@protoc_insertion_point(class_scope:grpc_service.ServerID)
  })
_sym_db.RegisterMessage(ServerID)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERRESPONSE,
  '__module__' : 'grpc_service_pb2'
  # @@protoc_insertion_point(class_scope:grpc_service.ServerResponse)
  })
_sym_db.RegisterMessage(ServerResponse)

Assignment = _reflection.GeneratedProtocolMessageType('Assignment', (_message.Message,), {
  'DESCRIPTOR' : _ASSIGNMENT,
  '__module__' : 'grpc_service_pb2'
  # @@protoc_insertion_point(class_scope:grpc_service.Assignment)
  })
_sym_db.RegisterMessage(Assignment)

Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTION,
  '__module__' : 'grpc_service_pb2'
  # @@protoc_insertion_point(class_scope:grpc_service.Connection)
  })
_sym_db.RegisterMessage(Connection)

AddDropLayer = _reflection.GeneratedProtocolMessageType('AddDropLayer', (_message.Message,), {
  'DESCRIPTOR' : _ADDDROPLAYER,
  '__module__' : 'grpc_service_pb2'
  # @@protoc_insertion_point(class_scope:grpc_service.AddDropLayer)
  })
_sym_db.RegisterMessage(AddDropLayer)

Features = _reflection.GeneratedProtocolMessageType('Features', (_message.Message,), {
  'DESCRIPTOR' : _FEATURES,
  '__module__' : 'grpc_service_pb2'
  # @@protoc_insertion_point(class_scope:grpc_service.Features)
  })
_sym_db.RegisterMessage(Features)

Preds = _reflection.GeneratedProtocolMessageType('Preds', (_message.Message,), {
  'DESCRIPTOR' : _PREDS,
  '__module__' : 'grpc_service_pb2'
  # @@protoc_insertion_point(class_scope:grpc_service.Preds)
  })
_sym_db.RegisterMessage(Preds)


DESCRIPTOR._options = None

_DAMA = _descriptor.ServiceDescriptor(
  name='DAMA',
  full_name='grpc_service.DAMA',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=631,
  serialized_end=1273,
  methods=[
  _descriptor.MethodDescriptor(
    name='bid_server',
    full_name='grpc_service.DAMA.bid_server',
    index=0,
    containing_service=None,
    input_type=_BID,
    output_type=_BIDDINGRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_server_price',
    full_name='grpc_service.DAMA.get_server_price',
    index=1,
    containing_service=None,
    input_type=_CONNECTION,
    output_type=_PRICE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_server_id',
    full_name='grpc_service.DAMA.get_server_id',
    index=2,
    containing_service=None,
    input_type=_CONNECTION,
    output_type=_SERVERID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='set_layers_assigned',
    full_name='grpc_service.DAMA.set_layers_assigned',
    index=3,
    containing_service=None,
    input_type=_ASSIGNMENT,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='start_discounting',
    full_name='grpc_service.DAMA.start_discounting',
    index=4,
    containing_service=None,
    input_type=_CONNECTION,
    output_type=_BID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ack_layer',
    full_name='grpc_service.DAMA.ack_layer',
    index=5,
    containing_service=None,
    input_type=_ADDDROPLAYER,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='return_layer',
    full_name='grpc_service.DAMA.return_layer',
    index=6,
    containing_service=None,
    input_type=_ADDDROPLAYER,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='nack_layer',
    full_name='grpc_service.DAMA.nack_layer',
    index=7,
    containing_service=None,
    input_type=_ADDDROPLAYER,
    output_type=_SERVERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='infer_layer',
    full_name='grpc_service.DAMA.infer_layer',
    index=8,
    containing_service=None,
    input_type=_FEATURES,
    output_type=_PREDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DAMA)

DESCRIPTOR.services_by_name['DAMA'] = _DAMA

# @@protoc_insertion_point(module_scope)