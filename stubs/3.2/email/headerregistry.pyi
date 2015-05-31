# Stubs for email.headerregistry (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Address:
    def __init__(self, display_name='', username='', domain='', addr_spec=None): pass
    @property
    def display_name(self): pass
    @property
    def username(self): pass
    @property
    def domain(self): pass
    @property
    def addr_spec(self): pass
    def __eq__(self, other): pass

class Group:
    def __init__(self, display_name=None, addresses=None): pass
    @property
    def display_name(self): pass
    @property
    def addresses(self): pass
    def __eq__(self, other): pass

class BaseHeader(str):
    def __new__(cls, name, value): pass
    def init(self, name, parse_tree, defects): pass
    @property
    def name(self): pass
    @property
    def defects(self): pass
    def __reduce__(self): pass
    def fold(self, policy): pass

class UnstructuredHeader:
    max_count = ...  # type: Any
    value_parser = ...  # type: Any
    @classmethod
    def parse(cls, value, kwds): pass

class UniqueUnstructuredHeader(UnstructuredHeader):
    max_count = ...  # type: Any

class DateHeader:
    max_count = ...  # type: Any
    value_parser = ...  # type: Any
    @classmethod
    def parse(cls, value, kwds): pass
    def init(self, *args, **kw): pass
    @property
    def datetime(self): pass

class UniqueDateHeader(DateHeader):
    max_count = ...  # type: Any

class AddressHeader:
    max_count = ...  # type: Any
    @staticmethod
    def value_parser(value): pass
    @classmethod
    def parse(cls, value, kwds): pass
    def init(self, *args, **kw): pass
    @property
    def groups(self): pass
    @property
    def addresses(self): pass

class UniqueAddressHeader(AddressHeader):
    max_count = ...  # type: Any

class SingleAddressHeader(AddressHeader):
    @property
    def address(self): pass

class UniqueSingleAddressHeader(SingleAddressHeader):
    max_count = ...  # type: Any

class MIMEVersionHeader:
    max_count = ...  # type: Any
    value_parser = ...  # type: Any
    @classmethod
    def parse(cls, value, kwds): pass
    def init(self, *args, **kw): pass
    @property
    def major(self): pass
    @property
    def minor(self): pass
    @property
    def version(self): pass

class ParameterizedMIMEHeader:
    max_count = ...  # type: Any
    @classmethod
    def parse(cls, value, kwds): pass
    def init(self, *args, **kw): pass
    @property
    def params(self): pass

class ContentTypeHeader(ParameterizedMIMEHeader):
    value_parser = ...  # type: Any
    def init(self, *args, **kw): pass
    @property
    def maintype(self): pass
    @property
    def subtype(self): pass
    @property
    def content_type(self): pass

class ContentDispositionHeader(ParameterizedMIMEHeader):
    value_parser = ...  # type: Any
    def init(self, *args, **kw): pass
    @property
    def content_disposition(self): pass

class ContentTransferEncodingHeader:
    max_count = ...  # type: Any
    value_parser = ...  # type: Any
    @classmethod
    def parse(cls, value, kwds): pass
    def init(self, *args, **kw): pass
    @property
    def cte(self): pass

class HeaderRegistry:
    registry = ...  # type: Any
    base_class = ...  # type: Any
    default_class = ...  # type: Any
    def __init__(self, base_class=..., default_class=..., use_default_map=True): pass
    def map_to_type(self, name, cls): pass
    def __getitem__(self, name): pass
    def __call__(self, name, value): pass
