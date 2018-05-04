# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sayhi.proto

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
  name='sayhi.proto',
  package='demo',
  syntax='proto3',
  serialized_pb=_b('\n\x0bsayhi.proto\x12\x04\x64\x65mo\"\x19\n\tHiRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1a\n\x07HiReply\x12\x0f\n\x07message\x18\x01 \x01(\t24\n\x07Greeter\x12)\n\x05SayHi\x12\x0f.demo.HiRequest\x1a\r.demo.HiReply\"\x00\x62\x06proto3')
)




_HIREQUEST = _descriptor.Descriptor(
  name='HiRequest',
  full_name='demo.HiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='demo.HiRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=21,
  serialized_end=46,
)


_HIREPLY = _descriptor.Descriptor(
  name='HiReply',
  full_name='demo.HiReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='demo.HiReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=48,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['HiRequest'] = _HIREQUEST
DESCRIPTOR.message_types_by_name['HiReply'] = _HIREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HiRequest = _reflection.GeneratedProtocolMessageType('HiRequest', (_message.Message,), dict(
  DESCRIPTOR = _HIREQUEST,
  __module__ = 'sayhi_pb2'
  # @@protoc_insertion_point(class_scope:demo.HiRequest)
  ))
_sym_db.RegisterMessage(HiRequest)

HiReply = _reflection.GeneratedProtocolMessageType('HiReply', (_message.Message,), dict(
  DESCRIPTOR = _HIREPLY,
  __module__ = 'sayhi_pb2'
  # @@protoc_insertion_point(class_scope:demo.HiReply)
  ))
_sym_db.RegisterMessage(HiReply)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='demo.Greeter',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=76,
  serialized_end=128,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHi',
    full_name='demo.Greeter.SayHi',
    index=0,
    containing_service=None,
    input_type=_HIREQUEST,
    output_type=_HIREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
