################################################################################
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
# limitations under the License.
################################################################################
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: walkthrough.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='walkthrough.proto',
  package='walkthrough',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11walkthrough.proto\x12\x0bwalkthrough\"\x16\n\x05Hello\x12\r\n\x05world\x18\x01 \x01(\t\"\x0e\n\x0c\x41notherHello\"\x18\n\x07\x43ounter\x12\r\n\x05value\x18\x01 \x01(\x03\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x07\n\x05\x45ventb\x06proto3')
)




_HELLO = _descriptor.Descriptor(
  name='Hello',
  full_name='walkthrough.Hello',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='world', full_name='walkthrough.Hello.world', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=34,
  serialized_end=56,
)


_ANOTHERHELLO = _descriptor.Descriptor(
  name='AnotherHello',
  full_name='walkthrough.AnotherHello',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=58,
  serialized_end=72,
)


_COUNTER = _descriptor.Descriptor(
  name='Counter',
  full_name='walkthrough.Counter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='walkthrough.Counter.value', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=74,
  serialized_end=98,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='walkthrough.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='walkthrough.HelloReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=100,
  serialized_end=129,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='walkthrough.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=131,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['Hello'] = _HELLO
DESCRIPTOR.message_types_by_name['AnotherHello'] = _ANOTHERHELLO
DESCRIPTOR.message_types_by_name['Counter'] = _COUNTER
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Hello = _reflection.GeneratedProtocolMessageType('Hello', (_message.Message,), dict(
  DESCRIPTOR = _HELLO,
  __module__ = 'walkthrough_pb2'
  # @@protoc_insertion_point(class_scope:walkthrough.Hello)
  ))
_sym_db.RegisterMessage(Hello)

AnotherHello = _reflection.GeneratedProtocolMessageType('AnotherHello', (_message.Message,), dict(
  DESCRIPTOR = _ANOTHERHELLO,
  __module__ = 'walkthrough_pb2'
  # @@protoc_insertion_point(class_scope:walkthrough.AnotherHello)
  ))
_sym_db.RegisterMessage(AnotherHello)

Counter = _reflection.GeneratedProtocolMessageType('Counter', (_message.Message,), dict(
  DESCRIPTOR = _COUNTER,
  __module__ = 'walkthrough_pb2'
  # @@protoc_insertion_point(class_scope:walkthrough.Counter)
  ))
_sym_db.RegisterMessage(Counter)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREPLY,
  __module__ = 'walkthrough_pb2'
  # @@protoc_insertion_point(class_scope:walkthrough.HelloReply)
  ))
_sym_db.RegisterMessage(HelloReply)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'walkthrough_pb2'
  # @@protoc_insertion_point(class_scope:walkthrough.Event)
  ))
_sym_db.RegisterMessage(Event)


# @@protoc_insertion_point(module_scope)
