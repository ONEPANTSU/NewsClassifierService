# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: classifier.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x10\x63lassifier.proto")\n\x19NewsClassificationRequest\x12\x0c\n\x04text\x18\x01 \x01(\t"-\n\x17NewsClassificationReply\x12\x12\n\ncategories\x18\x01 \x03(\t2X\n\x0eNewsClassifier\x12\x46\n\x0c\x43lassifyNews\x12\x1a.NewsClassificationRequest\x1a\x18.NewsClassificationReply"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "classifier_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_NEWSCLASSIFICATIONREQUEST"]._serialized_start = 20
    _globals["_NEWSCLASSIFICATIONREQUEST"]._serialized_end = 61
    _globals["_NEWSCLASSIFICATIONREPLY"]._serialized_start = 63
    _globals["_NEWSCLASSIFICATIONREPLY"]._serialized_end = 108
    _globals["_NEWSCLASSIFIER"]._serialized_start = 110
    _globals["_NEWSCLASSIFIER"]._serialized_end = 198
# @@protoc_insertion_point(module_scope)
