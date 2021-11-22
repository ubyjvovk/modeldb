# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uac/ServiceAccount.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ..uac import UACService_pb2 as uac_dot_UACService__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='uac/ServiceAccount.proto',
  package='ai.verta.uac',
  syntax='proto3',
  serialized_options=b'P\001Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uac',
  serialized_pb=b'\n\x18uac/ServiceAccount.proto\x12\x0c\x61i.verta.uac\x1a\x1cgoogle/api/annotations.proto\x1a\x14uac/UACService.proto\"\x7f\n\x0eServiceAccount\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x1f\n\x17\x61ssociated_workspace_id\x18\x03 \x01(\x04\x12\x1a\n\x12\x63reation_timestamp\x18\x04 \x01(\x04\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\"e\n\x1b\x43reateServiceAccountRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x1f\n\x17\x61ssociated_workspace_id\x18\x02 \x01(\x04\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\">\n\x1bUpdateServiceAccountRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"*\n\x1b\x44\x65leteServiceAccountRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x04\"\xa1\x01\n\x19\x46indServiceAccountRequest\x12\x0b\n\x03ids\x18\x01 \x03(\x04\x12 \n\x18\x61ssociated_workspace_ids\x18\x02 \x03(\x04\x12\x11\n\tusernames\x18\x03 \x03(\t\x1a\x42\n\x08Response\x12\x36\n\x10service_accounts\x18\x01 \x03(\x0b\x32\x1c.ai.verta.uac.ServiceAccount2\xf8\x04\n\x15ServiceAccountService\x12\x94\x01\n\x14\x63reateServiceAccount\x12).ai.verta.uac.CreateServiceAccountRequest\x1a\x1c.ai.verta.uac.ServiceAccount\"3\x82\xd3\xe4\x93\x02-\"(/v1/service_account/createServiceAccount:\x01*\x12\xa2\x01\n\x12\x66indServiceAccount\x12\'.ai.verta.uac.FindServiceAccountRequest\x1a\x30.ai.verta.uac.FindServiceAccountRequest.Response\"1\x82\xd3\xe4\x93\x02+\"&/v1/service_account/findServiceAccount:\x01*\x12\x8b\x01\n\x14\x64\x65leteServiceAccount\x12).ai.verta.uac.DeleteServiceAccountRequest\x1a\x13.ai.verta.uac.Empty\"3\x82\xd3\xe4\x93\x02-*(/v1/service_account/deleteServiceAccount:\x01*\x12\x94\x01\n\x14updateServiceAccount\x12).ai.verta.uac.UpdateServiceAccountRequest\x1a\x1c.ai.verta.uac.ServiceAccount\"3\x82\xd3\xe4\x93\x02-\"(/v1/service_account/updateServiceAccount:\x01*B>P\x01Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uacb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,uac_dot_UACService__pb2.DESCRIPTOR,])




_SERVICEACCOUNT = _descriptor.Descriptor(
  name='ServiceAccount',
  full_name='ai.verta.uac.ServiceAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.uac.ServiceAccount.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ai.verta.uac.ServiceAccount.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='associated_workspace_id', full_name='ai.verta.uac.ServiceAccount.associated_workspace_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_timestamp', full_name='ai.verta.uac.ServiceAccount.creation_timestamp', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ai.verta.uac.ServiceAccount.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=94,
  serialized_end=221,
)


_CREATESERVICEACCOUNTREQUEST = _descriptor.Descriptor(
  name='CreateServiceAccountRequest',
  full_name='ai.verta.uac.CreateServiceAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='ai.verta.uac.CreateServiceAccountRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='associated_workspace_id', full_name='ai.verta.uac.CreateServiceAccountRequest.associated_workspace_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ai.verta.uac.CreateServiceAccountRequest.description', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=223,
  serialized_end=324,
)


_UPDATESERVICEACCOUNTREQUEST = _descriptor.Descriptor(
  name='UpdateServiceAccountRequest',
  full_name='ai.verta.uac.UpdateServiceAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ai.verta.uac.UpdateServiceAccountRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ai.verta.uac.UpdateServiceAccountRequest.description', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=326,
  serialized_end=388,
)


_DELETESERVICEACCOUNTREQUEST = _descriptor.Descriptor(
  name='DeleteServiceAccountRequest',
  full_name='ai.verta.uac.DeleteServiceAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='ai.verta.uac.DeleteServiceAccountRequest.ids', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=390,
  serialized_end=432,
)


_FINDSERVICEACCOUNTREQUEST_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.uac.FindServiceAccountRequest.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_accounts', full_name='ai.verta.uac.FindServiceAccountRequest.Response.service_accounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=530,
  serialized_end=596,
)

_FINDSERVICEACCOUNTREQUEST = _descriptor.Descriptor(
  name='FindServiceAccountRequest',
  full_name='ai.verta.uac.FindServiceAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='ai.verta.uac.FindServiceAccountRequest.ids', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='associated_workspace_ids', full_name='ai.verta.uac.FindServiceAccountRequest.associated_workspace_ids', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usernames', full_name='ai.verta.uac.FindServiceAccountRequest.usernames', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDSERVICEACCOUNTREQUEST_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=596,
)

_FINDSERVICEACCOUNTREQUEST_RESPONSE.fields_by_name['service_accounts'].message_type = _SERVICEACCOUNT
_FINDSERVICEACCOUNTREQUEST_RESPONSE.containing_type = _FINDSERVICEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['ServiceAccount'] = _SERVICEACCOUNT
DESCRIPTOR.message_types_by_name['CreateServiceAccountRequest'] = _CREATESERVICEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['UpdateServiceAccountRequest'] = _UPDATESERVICEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['DeleteServiceAccountRequest'] = _DELETESERVICEACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['FindServiceAccountRequest'] = _FINDSERVICEACCOUNTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceAccount = _reflection.GeneratedProtocolMessageType('ServiceAccount', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEACCOUNT,
  '__module__' : 'uac.ServiceAccount_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.ServiceAccount)
  })
_sym_db.RegisterMessage(ServiceAccount)

CreateServiceAccountRequest = _reflection.GeneratedProtocolMessageType('CreateServiceAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVICEACCOUNTREQUEST,
  '__module__' : 'uac.ServiceAccount_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.CreateServiceAccountRequest)
  })
_sym_db.RegisterMessage(CreateServiceAccountRequest)

UpdateServiceAccountRequest = _reflection.GeneratedProtocolMessageType('UpdateServiceAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESERVICEACCOUNTREQUEST,
  '__module__' : 'uac.ServiceAccount_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.UpdateServiceAccountRequest)
  })
_sym_db.RegisterMessage(UpdateServiceAccountRequest)

DeleteServiceAccountRequest = _reflection.GeneratedProtocolMessageType('DeleteServiceAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESERVICEACCOUNTREQUEST,
  '__module__' : 'uac.ServiceAccount_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.DeleteServiceAccountRequest)
  })
_sym_db.RegisterMessage(DeleteServiceAccountRequest)

FindServiceAccountRequest = _reflection.GeneratedProtocolMessageType('FindServiceAccountRequest', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _FINDSERVICEACCOUNTREQUEST_RESPONSE,
    '__module__' : 'uac.ServiceAccount_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.uac.FindServiceAccountRequest.Response)
    })
  ,
  'DESCRIPTOR' : _FINDSERVICEACCOUNTREQUEST,
  '__module__' : 'uac.ServiceAccount_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.FindServiceAccountRequest)
  })
_sym_db.RegisterMessage(FindServiceAccountRequest)
_sym_db.RegisterMessage(FindServiceAccountRequest.Response)


DESCRIPTOR._options = None

_SERVICEACCOUNTSERVICE = _descriptor.ServiceDescriptor(
  name='ServiceAccountService',
  full_name='ai.verta.uac.ServiceAccountService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=599,
  serialized_end=1231,
  methods=[
  _descriptor.MethodDescriptor(
    name='createServiceAccount',
    full_name='ai.verta.uac.ServiceAccountService.createServiceAccount',
    index=0,
    containing_service=None,
    input_type=_CREATESERVICEACCOUNTREQUEST,
    output_type=_SERVICEACCOUNT,
    serialized_options=b'\202\323\344\223\002-\"(/v1/service_account/createServiceAccount:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='findServiceAccount',
    full_name='ai.verta.uac.ServiceAccountService.findServiceAccount',
    index=1,
    containing_service=None,
    input_type=_FINDSERVICEACCOUNTREQUEST,
    output_type=_FINDSERVICEACCOUNTREQUEST_RESPONSE,
    serialized_options=b'\202\323\344\223\002+\"&/v1/service_account/findServiceAccount:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='deleteServiceAccount',
    full_name='ai.verta.uac.ServiceAccountService.deleteServiceAccount',
    index=2,
    containing_service=None,
    input_type=_DELETESERVICEACCOUNTREQUEST,
    output_type=uac_dot_UACService__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002-*(/v1/service_account/deleteServiceAccount:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='updateServiceAccount',
    full_name='ai.verta.uac.ServiceAccountService.updateServiceAccount',
    index=3,
    containing_service=None,
    input_type=_UPDATESERVICEACCOUNTREQUEST,
    output_type=_SERVICEACCOUNT,
    serialized_options=b'\202\323\344\223\002-\"(/v1/service_account/updateServiceAccount:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICEACCOUNTSERVICE)

DESCRIPTOR.services_by_name['ServiceAccountService'] = _SERVICEACCOUNTSERVICE

# @@protoc_insertion_point(module_scope)
