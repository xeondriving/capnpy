# THIS FILE HAS BEEN GENERATED AUTOMATICALLY BY capnpy
# do not edit by hand
# generated on 2016-12-28 16:42

from capnpy.ptr import E_IS_FAR_POINTER as _E_IS_FAR_POINTER
from capnpy.struct_ import Struct as _Struct
from capnpy.struct_ import check_tag as _check_tag
from capnpy.struct_ import undefined as _undefined
from capnpy.enum import enum as _enum
from capnpy.blob import Types as _Types
from capnpy.builder import Builder as _Builder
from capnpy.list import PrimitiveList as _PrimitiveList
from capnpy.list import StructList as _StructList
from capnpy.list import StringList as _StringList
from capnpy.util import text_repr as _text_repr
from capnpy.util import float32_repr as _float32_repr
from capnpy.util import float64_repr as _float64_repr
from capnpy.util import extend_module_maybe as _extend_module_maybe

#### FORWARD DECLARATIONS ####

class CodeGeneratorRequest_RequestedFile_Import(_Struct): pass
CodeGeneratorRequest_RequestedFile_Import.__name__ = 'CodeGeneratorRequest.RequestedFile.Import'

class CodeGeneratorRequest_RequestedFile(_Struct): pass
CodeGeneratorRequest_RequestedFile.__name__ = 'CodeGeneratorRequest.RequestedFile'

class CodeGeneratorRequest(_Struct): pass
CodeGeneratorRequest.__name__ = 'CodeGeneratorRequest'

class Method(_Struct): pass
Method.__name__ = 'Method'

class Enumerant(_Struct): pass
Enumerant.__name__ = 'Enumerant'

ElementSize = _enum('ElementSize', ['empty', 'bit', 'byte', 'twoBytes', 'fourBytes', 'eightBytes', 'pointer', 'inlineComposite'])

class Type_anyPointer_parameter(_Struct): pass
Type_anyPointer_parameter.__name__ = 'Type.anyPointer.parameter'

class Type_anyPointer_implicitMethodParameter(_Struct): pass
Type_anyPointer_implicitMethodParameter.__name__ = 'Type.anyPointer.implicitMethodParameter'

class Type_anyPointer(_Struct): pass
Type_anyPointer.__name__ = 'Type.anyPointer'

class Type_struct(_Struct): pass
Type_struct.__name__ = 'Type.struct'

class Type_enum(_Struct): pass
Type_enum.__name__ = 'Type.enum'

class Type_interface(_Struct): pass
Type_interface.__name__ = 'Type.interface'

class Type_list(_Struct): pass
Type_list.__name__ = 'Type.list'

class Type(_Struct): pass
Type.__name__ = 'Type'

class Field_group(_Struct): pass
Field_group.__name__ = 'Field.group'

class Field_ordinal(_Struct): pass
Field_ordinal.__name__ = 'Field.ordinal'

class Field_slot(_Struct): pass
Field_slot.__name__ = 'Field.slot'

class Field(_Struct): pass
Field.__name__ = 'Field'

class Superclass(_Struct): pass
Superclass.__name__ = 'Superclass'

class Value(_Struct): pass
Value.__name__ = 'Value'

class Brand_Binding(_Struct): pass
Brand_Binding.__name__ = 'Brand.Binding'

class Brand_Scope(_Struct): pass
Brand_Scope.__name__ = 'Brand.Scope'

class Brand(_Struct): pass
Brand.__name__ = 'Brand'

class Annotation(_Struct): pass
Annotation.__name__ = 'Annotation'

class Node_interface(_Struct): pass
Node_interface.__name__ = 'Node.interface'

class Node_const(_Struct): pass
Node_const.__name__ = 'Node.const'

class Node_struct(_Struct): pass
Node_struct.__name__ = 'Node.struct'

class Node_annotation(_Struct): pass
Node_annotation.__name__ = 'Node.annotation'

class Node_enum(_Struct): pass
Node_enum.__name__ = 'Node.enum'

class Node_NestedNode(_Struct): pass
Node_NestedNode.__name__ = 'Node.NestedNode'

class Node_Parameter(_Struct): pass
Node_Parameter.__name__ = 'Node.Parameter'

class Node(_Struct): pass
Node.__name__ = 'Node'


#### DEFINITIONS ####

@CodeGeneratorRequest_RequestedFile_Import.__extend__
class CodeGeneratorRequest_RequestedFile_Import(_Struct):
    __static_data_size__ = 1
    __static_ptrs_size__ = 1
    
    
    @property
    def id(self):
        # no union check
        value = self._read_data(0, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def name(self):
        # no union check
        return self._read_str_text(0)
    
    def get_name(self):
        return self._read_str_text(0, default_="")
    
    def has_name(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @staticmethod
    def __new(id=0, name=None):
        builder = _Builder(1, 1)
        builder.set(ord('Q'), 0, id)
        builder.alloc_text(8, name)
        return builder.build()
    
    def __init__(self, id=0, name=None):
        _buf = self.__new(id, name)
        _Struct.__init__(self, _buf, 0, 1, 1)
    
    def shortrepr(self):
        parts = []
        parts.append("id = %s" % self.id)
        if self.has_name(): parts.append("name = %s" % _text_repr(self.get_name()))
        return "(%s)" % ", ".join(parts)


@CodeGeneratorRequest_RequestedFile.__extend__
class CodeGeneratorRequest_RequestedFile(_Struct):
    __static_data_size__ = 1
    __static_ptrs_size__ = 2
    
    Import = CodeGeneratorRequest_RequestedFile_Import
    
    @property
    def id(self):
        # no union check
        value = self._read_data(0, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def filename(self):
        # no union check
        return self._read_str_text(0)
    
    def get_filename(self):
        return self._read_str_text(0, default_="")
    
    def has_filename(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def imports(self):
        # no union check
        return self._read_list(8, _StructList, CodeGeneratorRequest.RequestedFile.Import)
    
    def get_imports(self):
        res = self.imports
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, CodeGeneratorRequest.RequestedFile.Import)
        return res
    
    def has_imports(self):
        ptr = self._read_fast_ptr(8)
        return ptr != 0
    
    @staticmethod
    def __new(id=0, filename=None, imports=None):
        builder = _Builder(1, 2)
        builder.set(ord('Q'), 0, id)
        builder.alloc_text(8, filename)
        builder.alloc_list(16, _StructList, CodeGeneratorRequest.RequestedFile.Import, imports)
        return builder.build()
    
    def __init__(self, id=0, filename=None, imports=None):
        _buf = self.__new(id, filename, imports)
        _Struct.__init__(self, _buf, 0, 1, 2)
    
    def shortrepr(self):
        parts = []
        parts.append("id = %s" % self.id)
        if self.has_filename(): parts.append("filename = %s" % _text_repr(self.get_filename()))
        if self.has_imports(): parts.append("imports = %s" % self.get_imports().shortrepr())
        return "(%s)" % ", ".join(parts)


@CodeGeneratorRequest.__extend__
class CodeGeneratorRequest(_Struct):
    __static_data_size__ = 0
    __static_ptrs_size__ = 2
    
    RequestedFile = CodeGeneratorRequest_RequestedFile
    
    @property
    def nodes(self):
        # no union check
        return self._read_list(0, _StructList, Node)
    
    def get_nodes(self):
        res = self.nodes
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Node)
        return res
    
    def has_nodes(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def requestedFiles(self):
        # no union check
        return self._read_list(8, _StructList, CodeGeneratorRequest.RequestedFile)
    
    def get_requestedFiles(self):
        res = self.requestedFiles
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, CodeGeneratorRequest.RequestedFile)
        return res
    
    def has_requestedFiles(self):
        ptr = self._read_fast_ptr(8)
        return ptr != 0
    
    @staticmethod
    def __new(nodes=None, requestedFiles=None):
        builder = _Builder(0, 2)
        builder.alloc_list(0, _StructList, Node, nodes)
        builder.alloc_list(8, _StructList, CodeGeneratorRequest.RequestedFile, requestedFiles)
        return builder.build()
    
    def __init__(self, nodes=None, requestedFiles=None):
        _buf = self.__new(nodes, requestedFiles)
        _Struct.__init__(self, _buf, 0, 0, 2)
    
    def shortrepr(self):
        parts = []
        if self.has_nodes(): parts.append("nodes = %s" % self.get_nodes().shortrepr())
        if self.has_requestedFiles(): parts.append("requestedFiles = %s" % self.get_requestedFiles().shortrepr())
        return "(%s)" % ", ".join(parts)


@Method.__extend__
class Method(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 5
    
    
    @property
    def name(self):
        # no union check
        return self._read_str_text(0)
    
    def get_name(self):
        return self._read_str_text(0, default_="")
    
    def has_name(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def codeOrder(self):
        # no union check
        value = self._read_data(0, ord('H'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def paramStructType(self):
        # no union check
        value = self._read_data(8, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def resultStructType(self):
        # no union check
        value = self._read_data(16, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def annotations(self):
        # no union check
        return self._read_list(8, _StructList, Annotation)
    
    def get_annotations(self):
        res = self.annotations
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Annotation)
        return res
    
    def has_annotations(self):
        ptr = self._read_fast_ptr(8)
        return ptr != 0
    
    @property
    def paramBrand(self):
        # no union check
        offset = 16
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Brand.__new__(Brand)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_paramBrand(self):
        res = self.paramBrand
        if res is None:
            return Brand.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_paramBrand(self):
        ptr = self._read_fast_ptr(16)
        return ptr != 0
    
    @property
    def resultBrand(self):
        # no union check
        offset = 24
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Brand.__new__(Brand)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_resultBrand(self):
        res = self.resultBrand
        if res is None:
            return Brand.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_resultBrand(self):
        ptr = self._read_fast_ptr(24)
        return ptr != 0
    
    @property
    def implicitParameters(self):
        # no union check
        return self._read_list(32, _StructList, Node.Parameter)
    
    def get_implicitParameters(self):
        res = self.implicitParameters
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Node.Parameter)
        return res
    
    def has_implicitParameters(self):
        ptr = self._read_fast_ptr(32)
        return ptr != 0
    
    @staticmethod
    def __new(name=None, codeOrder=0, paramStructType=0, resultStructType=0, annotations=None, paramBrand=None, resultBrand=None, implicitParameters=None):
        builder = _Builder(3, 5)
        builder.alloc_text(24, name)
        builder.set(ord('H'), 0, codeOrder)
        builder.set(ord('Q'), 8, paramStructType)
        builder.set(ord('Q'), 16, resultStructType)
        builder.alloc_list(32, _StructList, Annotation, annotations)
        builder.alloc_struct(40, Brand, paramBrand)
        builder.alloc_struct(48, Brand, resultBrand)
        builder.alloc_list(56, _StructList, Node.Parameter, implicitParameters)
        return builder.build()
    
    def __init__(self, name=None, codeOrder=0, paramStructType=0, resultStructType=0, annotations=None, paramBrand=None, resultBrand=None, implicitParameters=None):
        _buf = self.__new(name, codeOrder, paramStructType, resultStructType, annotations, paramBrand, resultBrand, implicitParameters)
        _Struct.__init__(self, _buf, 0, 3, 5)
    
    def shortrepr(self):
        parts = []
        if self.has_name(): parts.append("name = %s" % _text_repr(self.get_name()))
        parts.append("codeOrder = %s" % self.codeOrder)
        parts.append("paramStructType = %s" % self.paramStructType)
        parts.append("resultStructType = %s" % self.resultStructType)
        if self.has_annotations(): parts.append("annotations = %s" % self.get_annotations().shortrepr())
        if self.has_paramBrand(): parts.append("paramBrand = %s" % self.get_paramBrand().shortrepr())
        if self.has_resultBrand(): parts.append("resultBrand = %s" % self.get_resultBrand().shortrepr())
        if self.has_implicitParameters(): parts.append("implicitParameters = %s" % self.get_implicitParameters().shortrepr())
        return "(%s)" % ", ".join(parts)


@Enumerant.__extend__
class Enumerant(_Struct):
    __static_data_size__ = 1
    __static_ptrs_size__ = 2
    
    
    @property
    def name(self):
        # no union check
        return self._read_str_text(0)
    
    def get_name(self):
        return self._read_str_text(0, default_="")
    
    def has_name(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def codeOrder(self):
        # no union check
        value = self._read_data(0, ord('H'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def annotations(self):
        # no union check
        return self._read_list(8, _StructList, Annotation)
    
    def get_annotations(self):
        res = self.annotations
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Annotation)
        return res
    
    def has_annotations(self):
        ptr = self._read_fast_ptr(8)
        return ptr != 0
    
    @staticmethod
    def __new(name=None, codeOrder=0, annotations=None):
        builder = _Builder(1, 2)
        builder.alloc_text(8, name)
        builder.set(ord('H'), 0, codeOrder)
        builder.alloc_list(16, _StructList, Annotation, annotations)
        return builder.build()
    
    def __init__(self, name=None, codeOrder=0, annotations=None):
        _buf = self.__new(name, codeOrder, annotations)
        _Struct.__init__(self, _buf, 0, 1, 2)
    
    def shortrepr(self):
        parts = []
        if self.has_name(): parts.append("name = %s" % _text_repr(self.get_name()))
        parts.append("codeOrder = %s" % self.codeOrder)
        if self.has_annotations(): parts.append("annotations = %s" % self.get_annotations().shortrepr())
        return "(%s)" % ", ".join(parts)


@Type_anyPointer_parameter.__extend__
class Type_anyPointer_parameter(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 1
    
    
    @property
    def scopeId(self):
        # no union check
        value = self._read_data(16, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def parameterIndex(self):
        # no union check
        value = self._read_data(10, ord('H'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    def shortrepr(self):
        parts = []
        parts.append("scopeId = %s" % self.scopeId)
        parts.append("parameterIndex = %s" % self.parameterIndex)
        return "(%s)" % ", ".join(parts)


@Type_anyPointer_implicitMethodParameter.__extend__
class Type_anyPointer_implicitMethodParameter(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 1
    
    
    @property
    def parameterIndex(self):
        # no union check
        value = self._read_data(10, ord('H'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    def shortrepr(self):
        parts = []
        parts.append("parameterIndex = %s" % self.parameterIndex)
        return "(%s)" % ", ".join(parts)


@Type_anyPointer.__extend__
class Type_anyPointer(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 1
    
    
    __tag_offset__ = 8
    __tag__ = _enum('anyPointer.__tag__', ['unconstrained', 'parameter', 'implicitMethodParameter'])
    
    def is_unconstrained(self):
        return self._read_data_int16(8) == 0
    def is_parameter(self):
        return self._read_data_int16(8) == 1
    def is_implicitMethodParameter(self):
        return self._read_data_int16(8) == 2
    
    @property
    def unconstrained(self):
        self._ensure_union(0)
        return None
    
    @property
    def parameter(self):
        self._ensure_union(1)
        obj = Type_anyPointer_parameter.__new__(Type_anyPointer_parameter)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Parameter(scopeId=0, parameterIndex=0):
        return scopeId, parameterIndex,
    
    @property
    def implicitMethodParameter(self):
        self._ensure_union(2)
        obj = Type_anyPointer_implicitMethodParameter.__new__(Type_anyPointer_implicitMethodParameter)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Implicitmethodparameter(parameterIndex=0):
        return parameterIndex,
    
    def shortrepr(self):
        parts = []
        if self.is_unconstrained(): parts.append("unconstrained = %s" % "void")
        if self.is_parameter(): parts.append("parameter = %s" % self.parameter.shortrepr())
        if self.is_implicitMethodParameter(): parts.append("implicitMethodParameter = %s" % self.implicitMethodParameter.shortrepr())
        return "(%s)" % ", ".join(parts)


@Type_struct.__extend__
class Type_struct(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 1
    
    
    @property
    def typeId(self):
        # no union check
        value = self._read_data(8, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def brand(self):
        # no union check
        offset = 0
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Brand.__new__(Brand)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_brand(self):
        res = self.brand
        if res is None:
            return Brand.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_brand(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    def shortrepr(self):
        parts = []
        parts.append("typeId = %s" % self.typeId)
        if self.has_brand(): parts.append("brand = %s" % self.get_brand().shortrepr())
        return "(%s)" % ", ".join(parts)


@Type_enum.__extend__
class Type_enum(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 1
    
    
    @property
    def typeId(self):
        # no union check
        value = self._read_data(8, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def brand(self):
        # no union check
        offset = 0
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Brand.__new__(Brand)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_brand(self):
        res = self.brand
        if res is None:
            return Brand.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_brand(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    def shortrepr(self):
        parts = []
        parts.append("typeId = %s" % self.typeId)
        if self.has_brand(): parts.append("brand = %s" % self.get_brand().shortrepr())
        return "(%s)" % ", ".join(parts)


@Type_interface.__extend__
class Type_interface(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 1
    
    
    @property
    def typeId(self):
        # no union check
        value = self._read_data(8, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def brand(self):
        # no union check
        offset = 0
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Brand.__new__(Brand)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_brand(self):
        res = self.brand
        if res is None:
            return Brand.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_brand(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    def shortrepr(self):
        parts = []
        parts.append("typeId = %s" % self.typeId)
        if self.has_brand(): parts.append("brand = %s" % self.get_brand().shortrepr())
        return "(%s)" % ", ".join(parts)


@Type_list.__extend__
class Type_list(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 1
    
    
    @property
    def elementType(self):
        # no union check
        offset = 0
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Type.__new__(Type)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_elementType(self):
        res = self.elementType
        if res is None:
            return Type.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_elementType(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    def shortrepr(self):
        parts = []
        if self.has_elementType(): parts.append("elementType = %s" % self.get_elementType().shortrepr())
        return "(%s)" % ", ".join(parts)


@Type.__extend__
class Type(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 1
    
    
    __tag_offset__ = 0
    __tag__ = _enum('Type.__tag__', ['void', 'bool', 'int8', 'int16', 'int32', 'int64', 'uint8', 'uint16', 'uint32', 'uint64', 'float32', 'float64', 'text', 'data', 'list', 'enum', 'struct', 'interface', 'anyPointer'])
    
    def is_void(self):
        return self._read_data_int16(0) == 0
    def is_bool(self):
        return self._read_data_int16(0) == 1
    def is_int8(self):
        return self._read_data_int16(0) == 2
    def is_int16(self):
        return self._read_data_int16(0) == 3
    def is_int32(self):
        return self._read_data_int16(0) == 4
    def is_int64(self):
        return self._read_data_int16(0) == 5
    def is_uint8(self):
        return self._read_data_int16(0) == 6
    def is_uint16(self):
        return self._read_data_int16(0) == 7
    def is_uint32(self):
        return self._read_data_int16(0) == 8
    def is_uint64(self):
        return self._read_data_int16(0) == 9
    def is_float32(self):
        return self._read_data_int16(0) == 10
    def is_float64(self):
        return self._read_data_int16(0) == 11
    def is_text(self):
        return self._read_data_int16(0) == 12
    def is_data(self):
        return self._read_data_int16(0) == 13
    def is_list(self):
        return self._read_data_int16(0) == 14
    def is_enum(self):
        return self._read_data_int16(0) == 15
    def is_struct(self):
        return self._read_data_int16(0) == 16
    def is_interface(self):
        return self._read_data_int16(0) == 17
    def is_anyPointer(self):
        return self._read_data_int16(0) == 18
    
    @property
    def void(self):
        self._ensure_union(0)
        return None
    
    @property
    def bool(self):
        self._ensure_union(1)
        return None
    
    @property
    def int8(self):
        self._ensure_union(2)
        return None
    
    @property
    def int16(self):
        self._ensure_union(3)
        return None
    
    @property
    def int32(self):
        self._ensure_union(4)
        return None
    
    @property
    def int64(self):
        self._ensure_union(5)
        return None
    
    @property
    def uint8(self):
        self._ensure_union(6)
        return None
    
    @property
    def uint16(self):
        self._ensure_union(7)
        return None
    
    @property
    def uint32(self):
        self._ensure_union(8)
        return None
    
    @property
    def uint64(self):
        self._ensure_union(9)
        return None
    
    @property
    def float32(self):
        self._ensure_union(10)
        return None
    
    @property
    def float64(self):
        self._ensure_union(11)
        return None
    
    @property
    def text(self):
        self._ensure_union(12)
        return None
    
    @property
    def data(self):
        self._ensure_union(13)
        return None
    
    @property
    def list(self):
        self._ensure_union(14)
        obj = Type_list.__new__(Type_list)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def List(elementType=None):
        return elementType,
    
    @property
    def enum(self):
        self._ensure_union(15)
        obj = Type_enum.__new__(Type_enum)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Enum(typeId=0, brand=None):
        return typeId, brand,
    
    @property
    def struct(self):
        self._ensure_union(16)
        obj = Type_struct.__new__(Type_struct)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Struct(typeId=0, brand=None):
        return typeId, brand,
    
    @property
    def interface(self):
        self._ensure_union(17)
        obj = Type_interface.__new__(Type_interface)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Interface(typeId=0, brand=None):
        return typeId, brand,
    
    @property
    def anyPointer(self):
        self._ensure_union(18)
        obj = Type_anyPointer.__new__(Type_anyPointer)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Anypointer(unconstrained=_undefined, parameter=_undefined, implicitMethodParameter=_undefined):
        return unconstrained, parameter, implicitMethodParameter,
    
    @staticmethod
    def __new(void=_undefined, bool=_undefined, int8=_undefined, int16=_undefined, int32=_undefined, int64=_undefined, uint8=_undefined, uint16=_undefined, uint32=_undefined, uint64=_undefined, float32=_undefined, float64=_undefined, text=_undefined, data=_undefined, list=_undefined, enum=_undefined, struct=_undefined, interface=_undefined, anyPointer=_undefined):
        builder = _Builder(3, 1)
        anonymous__curtag = None
        anyPointer__curtag = None
        if void is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'void')
            builder.set(ord('h'), 0, 0)
        if bool is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'bool')
            builder.set(ord('h'), 0, 1)
        if int8 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'int8')
            builder.set(ord('h'), 0, 2)
        if int16 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'int16')
            builder.set(ord('h'), 0, 3)
        if int32 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'int32')
            builder.set(ord('h'), 0, 4)
        if int64 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'int64')
            builder.set(ord('h'), 0, 5)
        if uint8 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'uint8')
            builder.set(ord('h'), 0, 6)
        if uint16 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'uint16')
            builder.set(ord('h'), 0, 7)
        if uint32 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'uint32')
            builder.set(ord('h'), 0, 8)
        if uint64 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'uint64')
            builder.set(ord('h'), 0, 9)
        if float32 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'float32')
            builder.set(ord('h'), 0, 10)
        if float64 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'float64')
            builder.set(ord('h'), 0, 11)
        if text is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'text')
            builder.set(ord('h'), 0, 12)
        if data is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'data')
            builder.set(ord('h'), 0, 13)
        if list is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'list')
            builder.set(ord('h'), 0, 14)
            list_elementType, = list
            builder.alloc_struct(24, Type, list_elementType)
        if enum is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'enum')
            builder.set(ord('h'), 0, 15)
            enum_typeId, enum_brand, = enum
            builder.set(ord('Q'), 8, enum_typeId)
            builder.alloc_struct(24, Brand, enum_brand)
        if struct is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'struct')
            builder.set(ord('h'), 0, 16)
            struct_typeId, struct_brand, = struct
            builder.set(ord('Q'), 8, struct_typeId)
            builder.alloc_struct(24, Brand, struct_brand)
        if interface is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'interface')
            builder.set(ord('h'), 0, 17)
            interface_typeId, interface_brand, = interface
            builder.set(ord('Q'), 8, interface_typeId)
            builder.alloc_struct(24, Brand, interface_brand)
        if anyPointer is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'anyPointer')
            builder.set(ord('h'), 0, 18)
            anyPointer_unconstrained, anyPointer_parameter, anyPointer_implicitMethodParameter, = anyPointer
            if anyPointer_unconstrained is not _undefined:
                anyPointer__curtag = _check_tag(anyPointer__curtag, 'unconstrained')
                builder.set(ord('h'), 8, 0)
            if anyPointer_parameter is not _undefined:
                anyPointer__curtag = _check_tag(anyPointer__curtag, 'parameter')
                builder.set(ord('h'), 8, 1)
                anyPointer_parameter_scopeId, anyPointer_parameter_parameterIndex, = anyPointer_parameter
                builder.set(ord('Q'), 16, anyPointer_parameter_scopeId)
                builder.set(ord('H'), 10, anyPointer_parameter_parameterIndex)
            if anyPointer_implicitMethodParameter is not _undefined:
                anyPointer__curtag = _check_tag(anyPointer__curtag, 'implicitMethodParameter')
                builder.set(ord('h'), 8, 2)
                anyPointer_implicitMethodParameter_parameterIndex, = anyPointer_implicitMethodParameter
                builder.set(ord('H'), 10, anyPointer_implicitMethodParameter_parameterIndex)
        return builder.build()
    
    def __init__(self, void=_undefined, bool=_undefined, int8=_undefined, int16=_undefined, int32=_undefined, int64=_undefined, uint8=_undefined, uint16=_undefined, uint32=_undefined, uint64=_undefined, float32=_undefined, float64=_undefined, text=_undefined, data=_undefined, list=_undefined, enum=_undefined, struct=_undefined, interface=_undefined, anyPointer=_undefined):
        _buf = self.__new(void, bool, int8, int16, int32, int64, uint8, uint16, uint32, uint64, float32, float64, text, data, list, enum, struct, interface, anyPointer)
        _Struct.__init__(self, _buf, 0, 3, 1)
    
    @classmethod
    def new_void(cls, void=None):
        buf = cls.__new(void=void)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_bool(cls, bool=None):
        buf = cls.__new(bool=bool)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_int8(cls, int8=None):
        buf = cls.__new(int8=int8)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_int16(cls, int16=None):
        buf = cls.__new(int16=int16)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_int32(cls, int32=None):
        buf = cls.__new(int32=int32)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_int64(cls, int64=None):
        buf = cls.__new(int64=int64)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_uint8(cls, uint8=None):
        buf = cls.__new(uint8=uint8)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_uint16(cls, uint16=None):
        buf = cls.__new(uint16=uint16)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_uint32(cls, uint32=None):
        buf = cls.__new(uint32=uint32)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_uint64(cls, uint64=None):
        buf = cls.__new(uint64=uint64)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_float32(cls, float32=None):
        buf = cls.__new(float32=float32)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_float64(cls, float64=None):
        buf = cls.__new(float64=float64)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_text(cls, text=None):
        buf = cls.__new(text=text)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_data(cls, data=None):
        buf = cls.__new(data=data)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_list(cls, list=(None,)):
        buf = cls.__new(list=list)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_enum(cls, enum=(0, None,)):
        buf = cls.__new(enum=enum)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_struct(cls, struct=(0, None,)):
        buf = cls.__new(struct=struct)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_interface(cls, interface=(0, None,)):
        buf = cls.__new(interface=interface)
        return cls.from_buffer(buf, 0, 3, 1)
    
    @classmethod
    def new_anyPointer(cls, anyPointer=(_undefined, _undefined, _undefined,)):
        buf = cls.__new(anyPointer=anyPointer)
        return cls.from_buffer(buf, 0, 3, 1)
    
    def shortrepr(self):
        parts = []
        if self.is_void(): parts.append("void = %s" % "void")
        if self.is_bool(): parts.append("bool = %s" % "void")
        if self.is_int8(): parts.append("int8 = %s" % "void")
        if self.is_int16(): parts.append("int16 = %s" % "void")
        if self.is_int32(): parts.append("int32 = %s" % "void")
        if self.is_int64(): parts.append("int64 = %s" % "void")
        if self.is_uint8(): parts.append("uint8 = %s" % "void")
        if self.is_uint16(): parts.append("uint16 = %s" % "void")
        if self.is_uint32(): parts.append("uint32 = %s" % "void")
        if self.is_uint64(): parts.append("uint64 = %s" % "void")
        if self.is_float32(): parts.append("float32 = %s" % "void")
        if self.is_float64(): parts.append("float64 = %s" % "void")
        if self.is_text(): parts.append("text = %s" % "void")
        if self.is_data(): parts.append("data = %s" % "void")
        if self.is_list(): parts.append("list = %s" % self.list.shortrepr())
        if self.is_enum(): parts.append("enum = %s" % self.enum.shortrepr())
        if self.is_struct(): parts.append("struct = %s" % self.struct.shortrepr())
        if self.is_interface(): parts.append("interface = %s" % self.interface.shortrepr())
        if self.is_anyPointer(): parts.append("anyPointer = %s" % self.anyPointer.shortrepr())
        return "(%s)" % ", ".join(parts)


@Field_group.__extend__
class Field_group(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 4
    
    
    @property
    def typeId(self):
        # no union check
        value = self._read_data(16, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    def shortrepr(self):
        parts = []
        parts.append("typeId = %s" % self.typeId)
        return "(%s)" % ", ".join(parts)


@Field_ordinal.__extend__
class Field_ordinal(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 4
    
    
    __tag_offset__ = 10
    __tag__ = _enum('ordinal.__tag__', ['implicit', 'explicit'])
    
    def is_implicit(self):
        return self._read_data_int16(10) == 0
    def is_explicit(self):
        return self._read_data_int16(10) == 1
    
    @property
    def implicit(self):
        self._ensure_union(0)
        return None
    
    @property
    def explicit(self):
        self._ensure_union(1)
        value = self._read_data(12, ord('H'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    def shortrepr(self):
        parts = []
        if self.is_implicit(): parts.append("implicit = %s" % "void")
        if self.is_explicit(): parts.append("explicit = %s" % self.explicit)
        return "(%s)" % ", ".join(parts)


@Field_slot.__extend__
class Field_slot(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 4
    
    
    @property
    def offset(self):
        # no union check
        value = self._read_data(4, ord('I'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def type(self):
        # no union check
        offset = 16
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Type.__new__(Type)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_type(self):
        res = self.type
        if res is None:
            return Type.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_type(self):
        ptr = self._read_fast_ptr(16)
        return ptr != 0
    
    @property
    def defaultValue(self):
        # no union check
        offset = 24
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Value.__new__(Value)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_defaultValue(self):
        res = self.defaultValue
        if res is None:
            return Value.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_defaultValue(self):
        ptr = self._read_fast_ptr(24)
        return ptr != 0
    
    @property
    def hadExplicitDefault(self):
        # no union check
        value = self._read_bit(16, 1)
        if False != 0:
            value = value ^ False
        return value
    
    def shortrepr(self):
        parts = []
        parts.append("offset = %s" % self.offset)
        if self.has_type(): parts.append("type = %s" % self.get_type().shortrepr())
        if self.has_defaultValue(): parts.append("defaultValue = %s" % self.get_defaultValue().shortrepr())
        parts.append("hadExplicitDefault = %s" % str(self.hadExplicitDefault).lower())
        return "(%s)" % ", ".join(parts)


@Field.__extend__
class Field(_Struct):
    __static_data_size__ = 3
    __static_ptrs_size__ = 4
    
    noDiscriminant = 65535
    
    __tag_offset__ = 8
    __tag__ = _enum('Field.__tag__', ['slot', 'group'])
    
    def is_slot(self):
        return self._read_data_int16(8) == 0
    def is_group(self):
        return self._read_data_int16(8) == 1
    
    @property
    def name(self):
        # no union check
        return self._read_str_text(0)
    
    def get_name(self):
        return self._read_str_text(0, default_="")
    
    def has_name(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def codeOrder(self):
        # no union check
        value = self._read_data(0, ord('H'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def annotations(self):
        # no union check
        return self._read_list(8, _StructList, Annotation)
    
    def get_annotations(self):
        res = self.annotations
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Annotation)
        return res
    
    def has_annotations(self):
        ptr = self._read_fast_ptr(8)
        return ptr != 0
    
    @property
    def discriminantValue(self):
        # no union check
        value = self._read_data(2, ord('H'))
        if 65535 != 0:
            value = value ^ 65535
        return value
    
    @property
    def slot(self):
        self._ensure_union(0)
        obj = Field_slot.__new__(Field_slot)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Slot(offset=0, type=None, defaultValue=None, hadExplicitDefault=False):
        return offset, type, defaultValue, hadExplicitDefault,
    
    @property
    def group(self):
        self._ensure_union(1)
        obj = Field_group.__new__(Field_group)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Group(typeId=0):
        return typeId,
    
    @property
    def ordinal(self):
        # no union check
        obj = Field_ordinal.__new__(Field_ordinal)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Ordinal(implicit=_undefined, explicit=_undefined):
        return implicit, explicit,
    
    @staticmethod
    def __new(name=None, codeOrder=0, annotations=None, discriminantValue=65535, slot=_undefined, group=_undefined, ordinal=(_undefined, _undefined,)):
        builder = _Builder(3, 4)
        anonymous__curtag = None
        ordinal__curtag = None
        builder.alloc_text(24, name)
        builder.set(ord('H'), 0, codeOrder)
        builder.alloc_list(32, _StructList, Annotation, annotations)
        discriminantValue ^= 65535
        builder.set(ord('H'), 2, discriminantValue)
        if slot is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'slot')
            builder.set(ord('h'), 8, 0)
            slot_offset, slot_type, slot_defaultValue, slot_hadExplicitDefault, = slot
            builder.set(ord('I'), 4, slot_offset)
            builder.alloc_struct(40, Type, slot_type)
            builder.alloc_struct(48, Value, slot_defaultValue)
            builder.setbool(16, 0, slot_hadExplicitDefault)
        if group is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'group')
            builder.set(ord('h'), 8, 1)
            group_typeId, = group
            builder.set(ord('Q'), 16, group_typeId)
        ordinal_implicit, ordinal_explicit, = ordinal
        if ordinal_implicit is not _undefined:
            ordinal__curtag = _check_tag(ordinal__curtag, 'implicit')
            builder.set(ord('h'), 10, 0)
        if ordinal_explicit is not _undefined:
            ordinal__curtag = _check_tag(ordinal__curtag, 'explicit')
            builder.set(ord('h'), 10, 1)
            builder.set(ord('H'), 12, ordinal_explicit)
        return builder.build()
    
    def __init__(self, name=None, codeOrder=0, annotations=None, discriminantValue=65535, slot=_undefined, group=_undefined, ordinal=(_undefined, _undefined,)):
        _buf = self.__new(name, codeOrder, annotations, discriminantValue, slot, group, ordinal)
        _Struct.__init__(self, _buf, 0, 3, 4)
    
    @classmethod
    def new_slot(cls, name=None, codeOrder=0, annotations=None, discriminantValue=65535, slot=(0, None, None, False,), ordinal=(_undefined, _undefined,)):
        buf = cls.__new(name=name, codeOrder=codeOrder, annotations=annotations, discriminantValue=discriminantValue, slot=slot, ordinal=ordinal)
        return cls.from_buffer(buf, 0, 3, 4)
    
    @classmethod
    def new_group(cls, name=None, codeOrder=0, annotations=None, discriminantValue=65535, group=(0,), ordinal=(_undefined, _undefined,)):
        buf = cls.__new(name=name, codeOrder=codeOrder, annotations=annotations, discriminantValue=discriminantValue, group=group, ordinal=ordinal)
        return cls.from_buffer(buf, 0, 3, 4)
    
    def shortrepr(self):
        parts = []
        if self.has_name(): parts.append("name = %s" % _text_repr(self.get_name()))
        parts.append("codeOrder = %s" % self.codeOrder)
        if self.has_annotations(): parts.append("annotations = %s" % self.get_annotations().shortrepr())
        parts.append("discriminantValue = %s" % self.discriminantValue)
        if self.is_slot(): parts.append("slot = %s" % self.slot.shortrepr())
        if self.is_group(): parts.append("group = %s" % self.group.shortrepr())
        parts.append("ordinal = %s" % self.ordinal.shortrepr())
        return "(%s)" % ", ".join(parts)


@Superclass.__extend__
class Superclass(_Struct):
    __static_data_size__ = 1
    __static_ptrs_size__ = 1
    
    
    @property
    def id(self):
        # no union check
        value = self._read_data(0, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def brand(self):
        # no union check
        offset = 0
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Brand.__new__(Brand)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_brand(self):
        res = self.brand
        if res is None:
            return Brand.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_brand(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @staticmethod
    def __new(id=0, brand=None):
        builder = _Builder(1, 1)
        builder.set(ord('Q'), 0, id)
        builder.alloc_struct(8, Brand, brand)
        return builder.build()
    
    def __init__(self, id=0, brand=None):
        _buf = self.__new(id, brand)
        _Struct.__init__(self, _buf, 0, 1, 1)
    
    def shortrepr(self):
        parts = []
        parts.append("id = %s" % self.id)
        if self.has_brand(): parts.append("brand = %s" % self.get_brand().shortrepr())
        return "(%s)" % ", ".join(parts)


@Value.__extend__
class Value(_Struct):
    __static_data_size__ = 2
    __static_ptrs_size__ = 1
    
    
    __tag_offset__ = 0
    __tag__ = _enum('Value.__tag__', ['void', 'bool', 'int8', 'int16', 'int32', 'int64', 'uint8', 'uint16', 'uint32', 'uint64', 'float32', 'float64', 'text', 'data', 'list', 'enum', 'struct', 'interface', 'anyPointer'])
    
    def is_void(self):
        return self._read_data_int16(0) == 0
    def is_bool(self):
        return self._read_data_int16(0) == 1
    def is_int8(self):
        return self._read_data_int16(0) == 2
    def is_int16(self):
        return self._read_data_int16(0) == 3
    def is_int32(self):
        return self._read_data_int16(0) == 4
    def is_int64(self):
        return self._read_data_int16(0) == 5
    def is_uint8(self):
        return self._read_data_int16(0) == 6
    def is_uint16(self):
        return self._read_data_int16(0) == 7
    def is_uint32(self):
        return self._read_data_int16(0) == 8
    def is_uint64(self):
        return self._read_data_int16(0) == 9
    def is_float32(self):
        return self._read_data_int16(0) == 10
    def is_float64(self):
        return self._read_data_int16(0) == 11
    def is_text(self):
        return self._read_data_int16(0) == 12
    def is_data(self):
        return self._read_data_int16(0) == 13
    def is_list(self):
        return self._read_data_int16(0) == 14
    def is_enum(self):
        return self._read_data_int16(0) == 15
    def is_struct(self):
        return self._read_data_int16(0) == 16
    def is_interface(self):
        return self._read_data_int16(0) == 17
    def is_anyPointer(self):
        return self._read_data_int16(0) == 18
    
    @property
    def void(self):
        self._ensure_union(0)
        return None
    
    @property
    def bool(self):
        self._ensure_union(1)
        value = self._read_bit(2, 1)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def int8(self):
        self._ensure_union(2)
        value = self._read_data(2, ord('b'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def int16(self):
        self._ensure_union(3)
        value = self._read_data(2, ord('h'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def int32(self):
        self._ensure_union(4)
        value = self._read_data(4, ord('i'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def int64(self):
        self._ensure_union(5)
        value = self._read_data(8, ord('q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def uint8(self):
        self._ensure_union(6)
        value = self._read_data(2, ord('B'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def uint16(self):
        self._ensure_union(7)
        value = self._read_data(2, ord('H'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def uint32(self):
        self._ensure_union(8)
        value = self._read_data(4, ord('I'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def uint64(self):
        self._ensure_union(9)
        value = self._read_data(8, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def float32(self):
        self._ensure_union(10)
        value = self._read_data(4, ord('f'))
        if 0.0 != 0:
            value = value ^ 0.0
        return value
    
    @property
    def float64(self):
        self._ensure_union(11)
        value = self._read_data(8, ord('d'))
        if 0.0 != 0:
            value = value ^ 0.0
        return value
    
    @property
    def text(self):
        self._ensure_union(12)
        return self._read_str_text(0)
    
    def get_text(self):
        return self._read_str_text(0, default_="")
    
    def has_text(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def data(self):
        self._ensure_union(13)
        return self._read_str_data(0)
    
    def get_data(self):
        return self._read_str_data(0, default_="")
    
    def has_data(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def list(self):
        self._ensure_union(14)
        if not self.has_list():
            return None
        raise ValueError("Cannot get fields of type AnyPointer")
    
    def has_list(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def enum(self):
        self._ensure_union(15)
        value = self._read_data(2, ord('H'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def struct(self):
        self._ensure_union(16)
        if not self.has_struct():
            return None
        raise ValueError("Cannot get fields of type AnyPointer")
    
    def has_struct(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def interface(self):
        self._ensure_union(17)
        return None
    
    @property
    def anyPointer(self):
        self._ensure_union(18)
        if not self.has_anyPointer():
            return None
        raise ValueError("Cannot get fields of type AnyPointer")
    
    def has_anyPointer(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @staticmethod
    def __new(void=_undefined, bool=_undefined, int8=_undefined, int16=_undefined, int32=_undefined, int64=_undefined, uint8=_undefined, uint16=_undefined, uint32=_undefined, uint64=_undefined, float32=_undefined, float64=_undefined, text=_undefined, data=_undefined, list=_undefined, enum=_undefined, struct=_undefined, interface=_undefined, anyPointer=_undefined):
        builder = _Builder(2, 1)
        anonymous__curtag = None
        if void is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'void')
            builder.set(ord('h'), 0, 0)
        if bool is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'bool')
            builder.set(ord('h'), 0, 1)
            builder.setbool(2, 0, bool)
        if int8 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'int8')
            builder.set(ord('h'), 0, 2)
            builder.set(ord('b'), 2, int8)
        if int16 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'int16')
            builder.set(ord('h'), 0, 3)
            builder.set(ord('h'), 2, int16)
        if int32 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'int32')
            builder.set(ord('h'), 0, 4)
            builder.set(ord('i'), 4, int32)
        if int64 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'int64')
            builder.set(ord('h'), 0, 5)
            builder.set(ord('q'), 8, int64)
        if uint8 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'uint8')
            builder.set(ord('h'), 0, 6)
            builder.set(ord('B'), 2, uint8)
        if uint16 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'uint16')
            builder.set(ord('h'), 0, 7)
            builder.set(ord('H'), 2, uint16)
        if uint32 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'uint32')
            builder.set(ord('h'), 0, 8)
            builder.set(ord('I'), 4, uint32)
        if uint64 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'uint64')
            builder.set(ord('h'), 0, 9)
            builder.set(ord('Q'), 8, uint64)
        if float32 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'float32')
            builder.set(ord('h'), 0, 10)
            builder.set(ord('f'), 4, float32)
        if float64 is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'float64')
            builder.set(ord('h'), 0, 11)
            builder.set(ord('d'), 8, float64)
        if text is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'text')
            builder.set(ord('h'), 0, 12)
            builder.alloc_text(16, text)
        if data is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'data')
            builder.set(ord('h'), 0, 13)
            builder.alloc_data(16, data)
        if list is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'list')
            builder.set(ord('h'), 0, 14)
            raise NotImplementedError('Unsupported field type: (name = "list", codeOrder = 14, discriminantValue = 14, slot = (offset = 0, type = (anyPointer = (unconstrained = void)), defaultValue = (anyPointer = ???), hadExplicitDefault = false), ordinal = (explicit = 14))')
        if enum is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'enum')
            builder.set(ord('h'), 0, 15)
            builder.set(ord('H'), 2, enum)
        if struct is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'struct')
            builder.set(ord('h'), 0, 16)
            raise NotImplementedError('Unsupported field type: (name = "struct", codeOrder = 16, discriminantValue = 16, slot = (offset = 0, type = (anyPointer = (unconstrained = void)), defaultValue = (anyPointer = ???), hadExplicitDefault = false), ordinal = (explicit = 16))')
        if interface is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'interface')
            builder.set(ord('h'), 0, 17)
        if anyPointer is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'anyPointer')
            builder.set(ord('h'), 0, 18)
            raise NotImplementedError('Unsupported field type: (name = "anyPointer", codeOrder = 18, discriminantValue = 18, slot = (offset = 0, type = (anyPointer = (unconstrained = void)), defaultValue = (anyPointer = ???), hadExplicitDefault = false), ordinal = (explicit = 18))')
        return builder.build()
    
    def __init__(self, void=_undefined, bool=_undefined, int8=_undefined, int16=_undefined, int32=_undefined, int64=_undefined, uint8=_undefined, uint16=_undefined, uint32=_undefined, uint64=_undefined, float32=_undefined, float64=_undefined, text=_undefined, data=_undefined, list=_undefined, enum=_undefined, struct=_undefined, interface=_undefined, anyPointer=_undefined):
        _buf = self.__new(void, bool, int8, int16, int32, int64, uint8, uint16, uint32, uint64, float32, float64, text, data, list, enum, struct, interface, anyPointer)
        _Struct.__init__(self, _buf, 0, 2, 1)
    
    @classmethod
    def new_void(cls, void=None):
        buf = cls.__new(void=void)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_bool(cls, bool=False):
        buf = cls.__new(bool=bool)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_int8(cls, int8=0):
        buf = cls.__new(int8=int8)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_int16(cls, int16=0):
        buf = cls.__new(int16=int16)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_int32(cls, int32=0):
        buf = cls.__new(int32=int32)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_int64(cls, int64=0):
        buf = cls.__new(int64=int64)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_uint8(cls, uint8=0):
        buf = cls.__new(uint8=uint8)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_uint16(cls, uint16=0):
        buf = cls.__new(uint16=uint16)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_uint32(cls, uint32=0):
        buf = cls.__new(uint32=uint32)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_uint64(cls, uint64=0):
        buf = cls.__new(uint64=uint64)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_float32(cls, float32=0.0):
        buf = cls.__new(float32=float32)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_float64(cls, float64=0.0):
        buf = cls.__new(float64=float64)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_text(cls, text=None):
        buf = cls.__new(text=text)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_data(cls, data=None):
        buf = cls.__new(data=data)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_list(cls, list=None):
        buf = cls.__new(list=list)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_enum(cls, enum=0):
        buf = cls.__new(enum=enum)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_struct(cls, struct=None):
        buf = cls.__new(struct=struct)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_interface(cls, interface=None):
        buf = cls.__new(interface=interface)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_anyPointer(cls, anyPointer=None):
        buf = cls.__new(anyPointer=anyPointer)
        return cls.from_buffer(buf, 0, 2, 1)
    
    def shortrepr(self):
        parts = []
        if self.is_void(): parts.append("void = %s" % "void")
        if self.is_bool(): parts.append("bool = %s" % str(self.bool).lower())
        if self.is_int8(): parts.append("int8 = %s" % self.int8)
        if self.is_int16(): parts.append("int16 = %s" % self.int16)
        if self.is_int32(): parts.append("int32 = %s" % self.int32)
        if self.is_int64(): parts.append("int64 = %s" % self.int64)
        if self.is_uint8(): parts.append("uint8 = %s" % self.uint8)
        if self.is_uint16(): parts.append("uint16 = %s" % self.uint16)
        if self.is_uint32(): parts.append("uint32 = %s" % self.uint32)
        if self.is_uint64(): parts.append("uint64 = %s" % self.uint64)
        if self.is_float32(): parts.append("float32 = %s" % _float32_repr(self.float32))
        if self.is_float64(): parts.append("float64 = %s" % _float64_repr(self.float64))
        if self.is_text() and (self.has_text() or
                                  not False):
            parts.append("text = %s" % _text_repr(self.get_text()))
        if self.is_data() and (self.has_data() or
                                  not False):
            parts.append("data = %s" % _text_repr(self.get_data()))
        if self.is_list() and (self.has_list() or
                                  not False):
            parts.append("list = %s" % "???")
        if self.is_enum(): parts.append("enum = %s" % self.enum)
        if self.is_struct() and (self.has_struct() or
                                  not False):
            parts.append("struct = %s" % "???")
        if self.is_interface(): parts.append("interface = %s" % "void")
        if self.is_anyPointer() and (self.has_anyPointer() or
                                  not False):
            parts.append("anyPointer = %s" % "???")
        return "(%s)" % ", ".join(parts)


@Brand_Binding.__extend__
class Brand_Binding(_Struct):
    __static_data_size__ = 1
    __static_ptrs_size__ = 1
    
    
    __tag_offset__ = 0
    __tag__ = _enum('Binding.__tag__', ['unbound', 'type'])
    
    def is_unbound(self):
        return self._read_data_int16(0) == 0
    def is_type(self):
        return self._read_data_int16(0) == 1
    
    @property
    def unbound(self):
        self._ensure_union(0)
        return None
    
    @property
    def type(self):
        self._ensure_union(1)
        offset = 0
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Type.__new__(Type)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_type(self):
        res = self.type
        if res is None:
            return Type.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_type(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @staticmethod
    def __new(unbound=_undefined, type=_undefined):
        builder = _Builder(1, 1)
        anonymous__curtag = None
        if unbound is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'unbound')
            builder.set(ord('h'), 0, 0)
        if type is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'type')
            builder.set(ord('h'), 0, 1)
            builder.alloc_struct(8, Type, type)
        return builder.build()
    
    def __init__(self, unbound=_undefined, type=_undefined):
        _buf = self.__new(unbound, type)
        _Struct.__init__(self, _buf, 0, 1, 1)
    
    @classmethod
    def new_unbound(cls, unbound=None):
        buf = cls.__new(unbound=unbound)
        return cls.from_buffer(buf, 0, 1, 1)
    
    @classmethod
    def new_type(cls, type=None):
        buf = cls.__new(type=type)
        return cls.from_buffer(buf, 0, 1, 1)
    
    def shortrepr(self):
        parts = []
        if self.is_unbound(): parts.append("unbound = %s" % "void")
        if self.is_type() and (self.has_type() or
                                  not False):
            parts.append("type = %s" % self.get_type().shortrepr())
        return "(%s)" % ", ".join(parts)


@Brand_Scope.__extend__
class Brand_Scope(_Struct):
    __static_data_size__ = 2
    __static_ptrs_size__ = 1
    
    
    __tag_offset__ = 8
    __tag__ = _enum('Scope.__tag__', ['bind', 'inherit'])
    
    def is_bind(self):
        return self._read_data_int16(8) == 0
    def is_inherit(self):
        return self._read_data_int16(8) == 1
    
    @property
    def scopeId(self):
        # no union check
        value = self._read_data(0, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def bind(self):
        self._ensure_union(0)
        return self._read_list(0, _StructList, Brand.Binding)
    
    def get_bind(self):
        res = self.bind
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Brand.Binding)
        return res
    
    def has_bind(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def inherit(self):
        self._ensure_union(1)
        return None
    
    @staticmethod
    def __new(scopeId=0, bind=_undefined, inherit=_undefined):
        builder = _Builder(2, 1)
        anonymous__curtag = None
        builder.set(ord('Q'), 0, scopeId)
        if bind is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'bind')
            builder.set(ord('h'), 8, 0)
            builder.alloc_list(16, _StructList, Brand.Binding, bind)
        if inherit is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'inherit')
            builder.set(ord('h'), 8, 1)
        return builder.build()
    
    def __init__(self, scopeId=0, bind=_undefined, inherit=_undefined):
        _buf = self.__new(scopeId, bind, inherit)
        _Struct.__init__(self, _buf, 0, 2, 1)
    
    @classmethod
    def new_bind(cls, scopeId=0, bind=None):
        buf = cls.__new(scopeId=scopeId, bind=bind)
        return cls.from_buffer(buf, 0, 2, 1)
    
    @classmethod
    def new_inherit(cls, scopeId=0, inherit=None):
        buf = cls.__new(scopeId=scopeId, inherit=inherit)
        return cls.from_buffer(buf, 0, 2, 1)
    
    def shortrepr(self):
        parts = []
        parts.append("scopeId = %s" % self.scopeId)
        if self.is_bind() and (self.has_bind() or
                                  not True):
            parts.append("bind = %s" % self.get_bind().shortrepr())
        if self.is_inherit(): parts.append("inherit = %s" % "void")
        return "(%s)" % ", ".join(parts)


@Brand.__extend__
class Brand(_Struct):
    __static_data_size__ = 0
    __static_ptrs_size__ = 1
    
    Binding = Brand_Binding
    Scope = Brand_Scope
    
    @property
    def scopes(self):
        # no union check
        return self._read_list(0, _StructList, Brand.Scope)
    
    def get_scopes(self):
        res = self.scopes
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Brand.Scope)
        return res
    
    def has_scopes(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @staticmethod
    def __new(scopes=None):
        builder = _Builder(0, 1)
        builder.alloc_list(0, _StructList, Brand.Scope, scopes)
        return builder.build()
    
    def __init__(self, scopes=None):
        _buf = self.__new(scopes)
        _Struct.__init__(self, _buf, 0, 0, 1)
    
    def shortrepr(self):
        parts = []
        if self.has_scopes(): parts.append("scopes = %s" % self.get_scopes().shortrepr())
        return "(%s)" % ", ".join(parts)


@Annotation.__extend__
class Annotation(_Struct):
    __static_data_size__ = 1
    __static_ptrs_size__ = 2
    
    
    @property
    def id(self):
        # no union check
        value = self._read_data(0, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def value(self):
        # no union check
        offset = 0
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Value.__new__(Value)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_value(self):
        res = self.value
        if res is None:
            return Value.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_value(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def brand(self):
        # no union check
        offset = 8
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Brand.__new__(Brand)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_brand(self):
        res = self.brand
        if res is None:
            return Brand.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_brand(self):
        ptr = self._read_fast_ptr(8)
        return ptr != 0
    
    @staticmethod
    def __new(id=0, value=None, brand=None):
        builder = _Builder(1, 2)
        builder.set(ord('Q'), 0, id)
        builder.alloc_struct(8, Value, value)
        builder.alloc_struct(16, Brand, brand)
        return builder.build()
    
    def __init__(self, id=0, value=None, brand=None):
        _buf = self.__new(id, value, brand)
        _Struct.__init__(self, _buf, 0, 1, 2)
    
    def shortrepr(self):
        parts = []
        parts.append("id = %s" % self.id)
        if self.has_value(): parts.append("value = %s" % self.get_value().shortrepr())
        if self.has_brand(): parts.append("brand = %s" % self.get_brand().shortrepr())
        return "(%s)" % ", ".join(parts)


@Node_interface.__extend__
class Node_interface(_Struct):
    __static_data_size__ = 5
    __static_ptrs_size__ = 6
    
    
    @property
    def methods(self):
        # no union check
        return self._read_list(24, _StructList, Method)
    
    def get_methods(self):
        res = self.methods
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Method)
        return res
    
    def has_methods(self):
        ptr = self._read_fast_ptr(24)
        return ptr != 0
    
    @property
    def superclasses(self):
        # no union check
        return self._read_list(32, _StructList, Superclass)
    
    def get_superclasses(self):
        res = self.superclasses
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Superclass)
        return res
    
    def has_superclasses(self):
        ptr = self._read_fast_ptr(32)
        return ptr != 0
    
    def shortrepr(self):
        parts = []
        if self.has_methods(): parts.append("methods = %s" % self.get_methods().shortrepr())
        if self.has_superclasses(): parts.append("superclasses = %s" % self.get_superclasses().shortrepr())
        return "(%s)" % ", ".join(parts)


@Node_const.__extend__
class Node_const(_Struct):
    __static_data_size__ = 5
    __static_ptrs_size__ = 6
    
    
    @property
    def type(self):
        # no union check
        offset = 24
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Type.__new__(Type)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_type(self):
        res = self.type
        if res is None:
            return Type.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_type(self):
        ptr = self._read_fast_ptr(24)
        return ptr != 0
    
    @property
    def value(self):
        # no union check
        offset = 32
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Value.__new__(Value)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_value(self):
        res = self.value
        if res is None:
            return Value.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_value(self):
        ptr = self._read_fast_ptr(32)
        return ptr != 0
    
    def shortrepr(self):
        parts = []
        if self.has_type(): parts.append("type = %s" % self.get_type().shortrepr())
        if self.has_value(): parts.append("value = %s" % self.get_value().shortrepr())
        return "(%s)" % ", ".join(parts)


@Node_struct.__extend__
class Node_struct(_Struct):
    __static_data_size__ = 5
    __static_ptrs_size__ = 6
    
    
    @property
    def dataWordCount(self):
        # no union check
        value = self._read_data(14, ord('H'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def pointerCount(self):
        # no union check
        value = self._read_data(24, ord('H'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def preferredListEncoding(self):
        # no union check
        value = self._read_enum(26, ElementSize)
        if 0 != 0:
            value = ElementSize(value ^ 0)
        return value
    
    @property
    def isGroup(self):
        # no union check
        value = self._read_bit(28, 1)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def discriminantCount(self):
        # no union check
        value = self._read_data(30, ord('H'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def discriminantOffset(self):
        # no union check
        value = self._read_data(32, ord('I'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def fields(self):
        # no union check
        return self._read_list(24, _StructList, Field)
    
    def get_fields(self):
        res = self.fields
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Field)
        return res
    
    def has_fields(self):
        ptr = self._read_fast_ptr(24)
        return ptr != 0
    
    def shortrepr(self):
        parts = []
        parts.append("dataWordCount = %s" % self.dataWordCount)
        parts.append("pointerCount = %s" % self.pointerCount)
        parts.append("preferredListEncoding = %s" % self.preferredListEncoding)
        parts.append("isGroup = %s" % str(self.isGroup).lower())
        parts.append("discriminantCount = %s" % self.discriminantCount)
        parts.append("discriminantOffset = %s" % self.discriminantOffset)
        if self.has_fields(): parts.append("fields = %s" % self.get_fields().shortrepr())
        return "(%s)" % ", ".join(parts)


@Node_annotation.__extend__
class Node_annotation(_Struct):
    __static_data_size__ = 5
    __static_ptrs_size__ = 6
    
    
    @property
    def type(self):
        # no union check
        offset = 24
        p = self._read_fast_ptr(offset)
        if p == _E_IS_FAR_POINTER:
            offset, p = self._read_far_ptr(offset)
        else:
            offset += self._ptrs_offset
        if p == 0:
            return None
        obj = Type.__new__(Type)
        obj._init_from_pointer(self._buf, offset, p)
        return obj
    
    def get_type(self):
        res = self.type
        if res is None:
            return Type.from_buffer('', 0, data_size=0, ptrs_size=0)
        return res
    
    def has_type(self):
        ptr = self._read_fast_ptr(24)
        return ptr != 0
    
    @property
    def targetsFile(self):
        # no union check
        value = self._read_bit(14, 1)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def targetsConst(self):
        # no union check
        value = self._read_bit(14, 2)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def targetsEnum(self):
        # no union check
        value = self._read_bit(14, 4)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def targetsEnumerant(self):
        # no union check
        value = self._read_bit(14, 8)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def targetsStruct(self):
        # no union check
        value = self._read_bit(14, 16)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def targetsField(self):
        # no union check
        value = self._read_bit(14, 32)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def targetsUnion(self):
        # no union check
        value = self._read_bit(14, 64)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def targetsGroup(self):
        # no union check
        value = self._read_bit(14, 128)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def targetsInterface(self):
        # no union check
        value = self._read_bit(15, 1)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def targetsMethod(self):
        # no union check
        value = self._read_bit(15, 2)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def targetsParam(self):
        # no union check
        value = self._read_bit(15, 4)
        if False != 0:
            value = value ^ False
        return value
    
    @property
    def targetsAnnotation(self):
        # no union check
        value = self._read_bit(15, 8)
        if False != 0:
            value = value ^ False
        return value
    
    def shortrepr(self):
        parts = []
        if self.has_type(): parts.append("type = %s" % self.get_type().shortrepr())
        parts.append("targetsFile = %s" % str(self.targetsFile).lower())
        parts.append("targetsConst = %s" % str(self.targetsConst).lower())
        parts.append("targetsEnum = %s" % str(self.targetsEnum).lower())
        parts.append("targetsEnumerant = %s" % str(self.targetsEnumerant).lower())
        parts.append("targetsStruct = %s" % str(self.targetsStruct).lower())
        parts.append("targetsField = %s" % str(self.targetsField).lower())
        parts.append("targetsUnion = %s" % str(self.targetsUnion).lower())
        parts.append("targetsGroup = %s" % str(self.targetsGroup).lower())
        parts.append("targetsInterface = %s" % str(self.targetsInterface).lower())
        parts.append("targetsMethod = %s" % str(self.targetsMethod).lower())
        parts.append("targetsParam = %s" % str(self.targetsParam).lower())
        parts.append("targetsAnnotation = %s" % str(self.targetsAnnotation).lower())
        return "(%s)" % ", ".join(parts)


@Node_enum.__extend__
class Node_enum(_Struct):
    __static_data_size__ = 5
    __static_ptrs_size__ = 6
    
    
    @property
    def enumerants(self):
        # no union check
        return self._read_list(24, _StructList, Enumerant)
    
    def get_enumerants(self):
        res = self.enumerants
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Enumerant)
        return res
    
    def has_enumerants(self):
        ptr = self._read_fast_ptr(24)
        return ptr != 0
    
    def shortrepr(self):
        parts = []
        if self.has_enumerants(): parts.append("enumerants = %s" % self.get_enumerants().shortrepr())
        return "(%s)" % ", ".join(parts)


@Node_NestedNode.__extend__
class Node_NestedNode(_Struct):
    __static_data_size__ = 1
    __static_ptrs_size__ = 1
    
    
    @property
    def name(self):
        # no union check
        return self._read_str_text(0)
    
    def get_name(self):
        return self._read_str_text(0, default_="")
    
    def has_name(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def id(self):
        # no union check
        value = self._read_data(0, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @staticmethod
    def __new(name=None, id=0):
        builder = _Builder(1, 1)
        builder.alloc_text(8, name)
        builder.set(ord('Q'), 0, id)
        return builder.build()
    
    def __init__(self, name=None, id=0):
        _buf = self.__new(name, id)
        _Struct.__init__(self, _buf, 0, 1, 1)
    
    def shortrepr(self):
        parts = []
        if self.has_name(): parts.append("name = %s" % _text_repr(self.get_name()))
        parts.append("id = %s" % self.id)
        return "(%s)" % ", ".join(parts)


@Node_Parameter.__extend__
class Node_Parameter(_Struct):
    __static_data_size__ = 0
    __static_ptrs_size__ = 1
    
    
    @property
    def name(self):
        # no union check
        return self._read_str_text(0)
    
    def get_name(self):
        return self._read_str_text(0, default_="")
    
    def has_name(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @staticmethod
    def __new(name=None):
        builder = _Builder(0, 1)
        builder.alloc_text(0, name)
        return builder.build()
    
    def __init__(self, name=None):
        _buf = self.__new(name)
        _Struct.__init__(self, _buf, 0, 0, 1)
    
    def shortrepr(self):
        parts = []
        if self.has_name(): parts.append("name = %s" % _text_repr(self.get_name()))
        return "(%s)" % ", ".join(parts)


@Node.__extend__
class Node(_Struct):
    __static_data_size__ = 5
    __static_ptrs_size__ = 6
    
    NestedNode = Node_NestedNode
    Parameter = Node_Parameter
    
    __tag_offset__ = 12
    __tag__ = _enum('Node.__tag__', ['file', 'struct', 'enum', 'interface', 'const', 'annotation'])
    
    def is_file(self):
        return self._read_data_int16(12) == 0
    def is_struct(self):
        return self._read_data_int16(12) == 1
    def is_enum(self):
        return self._read_data_int16(12) == 2
    def is_interface(self):
        return self._read_data_int16(12) == 3
    def is_const(self):
        return self._read_data_int16(12) == 4
    def is_annotation(self):
        return self._read_data_int16(12) == 5
    
    @property
    def id(self):
        # no union check
        value = self._read_data(0, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def displayName(self):
        # no union check
        return self._read_str_text(0)
    
    def get_displayName(self):
        return self._read_str_text(0, default_="")
    
    def has_displayName(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def displayNamePrefixLength(self):
        # no union check
        value = self._read_data(8, ord('I'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def scopeId(self):
        # no union check
        value = self._read_data(16, ord('Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def nestedNodes(self):
        # no union check
        return self._read_list(8, _StructList, Node.NestedNode)
    
    def get_nestedNodes(self):
        res = self.nestedNodes
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Node.NestedNode)
        return res
    
    def has_nestedNodes(self):
        ptr = self._read_fast_ptr(8)
        return ptr != 0
    
    @property
    def annotations(self):
        # no union check
        return self._read_list(16, _StructList, Annotation)
    
    def get_annotations(self):
        res = self.annotations
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Annotation)
        return res
    
    def has_annotations(self):
        ptr = self._read_fast_ptr(16)
        return ptr != 0
    
    @property
    def file(self):
        self._ensure_union(0)
        return None
    
    @property
    def struct(self):
        self._ensure_union(1)
        obj = Node_struct.__new__(Node_struct)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Struct(dataWordCount=0, pointerCount=0, preferredListEncoding=0, isGroup=False, discriminantCount=0, discriminantOffset=0, fields=None):
        return dataWordCount, pointerCount, preferredListEncoding, isGroup, discriminantCount, discriminantOffset, fields,
    
    @property
    def enum(self):
        self._ensure_union(2)
        obj = Node_enum.__new__(Node_enum)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Enum(enumerants=None):
        return enumerants,
    
    @property
    def interface(self):
        self._ensure_union(3)
        obj = Node_interface.__new__(Node_interface)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Interface(methods=None, superclasses=None):
        return methods, superclasses,
    
    @property
    def const(self):
        self._ensure_union(4)
        obj = Node_const.__new__(Node_const)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Const(type=None, value=None):
        return type, value,
    
    @property
    def annotation(self):
        self._ensure_union(5)
        obj = Node_annotation.__new__(Node_annotation)
        _Struct._init_from_buffer(obj, self._buf, self._data_offset,
                                  self._data_size, self._ptrs_size)
        return obj
    
    @staticmethod
    def Annotation(type=None, targetsFile=False, targetsConst=False, targetsEnum=False, targetsEnumerant=False, targetsStruct=False, targetsField=False, targetsUnion=False, targetsGroup=False, targetsInterface=False, targetsMethod=False, targetsParam=False, targetsAnnotation=False):
        return type, targetsFile, targetsConst, targetsEnum, targetsEnumerant, targetsStruct, targetsField, targetsUnion, targetsGroup, targetsInterface, targetsMethod, targetsParam, targetsAnnotation,
    
    @property
    def parameters(self):
        # no union check
        return self._read_list(40, _StructList, Node.Parameter)
    
    def get_parameters(self):
        res = self.parameters
        if res is None:
            return _StructList.from_buffer('', 0, 0, 0, Node.Parameter)
        return res
    
    def has_parameters(self):
        ptr = self._read_fast_ptr(40)
        return ptr != 0
    
    @property
    def isGeneric(self):
        # no union check
        value = self._read_bit(36, 1)
        if False != 0:
            value = value ^ False
        return value
    
    @staticmethod
    def __new(id=0, displayName=None, displayNamePrefixLength=0, scopeId=0, nestedNodes=None, annotations=None, file=_undefined, struct=_undefined, enum=_undefined, interface=_undefined, const=_undefined, annotation=_undefined, parameters=None, isGeneric=False):
        builder = _Builder(5, 6)
        anonymous__curtag = None
        builder.set(ord('Q'), 0, id)
        builder.alloc_text(40, displayName)
        builder.set(ord('I'), 8, displayNamePrefixLength)
        builder.set(ord('Q'), 16, scopeId)
        builder.alloc_list(48, _StructList, Node.NestedNode, nestedNodes)
        builder.alloc_list(56, _StructList, Annotation, annotations)
        if file is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'file')
            builder.set(ord('h'), 12, 0)
        if struct is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'struct')
            builder.set(ord('h'), 12, 1)
            struct_dataWordCount, struct_pointerCount, struct_preferredListEncoding, struct_isGroup, struct_discriminantCount, struct_discriminantOffset, struct_fields, = struct
            builder.set(ord('H'), 14, struct_dataWordCount)
            builder.set(ord('H'), 24, struct_pointerCount)
            builder.set(ord('h'), 26, struct_preferredListEncoding)
            builder.setbool(28, 0, struct_isGroup)
            builder.set(ord('H'), 30, struct_discriminantCount)
            builder.set(ord('I'), 32, struct_discriminantOffset)
            builder.alloc_list(64, _StructList, Field, struct_fields)
        if enum is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'enum')
            builder.set(ord('h'), 12, 2)
            enum_enumerants, = enum
            builder.alloc_list(64, _StructList, Enumerant, enum_enumerants)
        if interface is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'interface')
            builder.set(ord('h'), 12, 3)
            interface_methods, interface_superclasses, = interface
            builder.alloc_list(64, _StructList, Method, interface_methods)
            builder.alloc_list(72, _StructList, Superclass, interface_superclasses)
        if const is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'const')
            builder.set(ord('h'), 12, 4)
            const_type, const_value, = const
            builder.alloc_struct(64, Type, const_type)
            builder.alloc_struct(72, Value, const_value)
        if annotation is not _undefined:
            anonymous__curtag = _check_tag(anonymous__curtag, 'annotation')
            builder.set(ord('h'), 12, 5)
            annotation_type, annotation_targetsFile, annotation_targetsConst, annotation_targetsEnum, annotation_targetsEnumerant, annotation_targetsStruct, annotation_targetsField, annotation_targetsUnion, annotation_targetsGroup, annotation_targetsInterface, annotation_targetsMethod, annotation_targetsParam, annotation_targetsAnnotation, = annotation
            builder.alloc_struct(64, Type, annotation_type)
            builder.setbool(14, 0, annotation_targetsFile)
            builder.setbool(14, 1, annotation_targetsConst)
            builder.setbool(14, 2, annotation_targetsEnum)
            builder.setbool(14, 3, annotation_targetsEnumerant)
            builder.setbool(14, 4, annotation_targetsStruct)
            builder.setbool(14, 5, annotation_targetsField)
            builder.setbool(14, 6, annotation_targetsUnion)
            builder.setbool(14, 7, annotation_targetsGroup)
            builder.setbool(15, 0, annotation_targetsInterface)
            builder.setbool(15, 1, annotation_targetsMethod)
            builder.setbool(15, 2, annotation_targetsParam)
            builder.setbool(15, 3, annotation_targetsAnnotation)
        builder.alloc_list(80, _StructList, Node.Parameter, parameters)
        builder.setbool(36, 0, isGeneric)
        return builder.build()
    
    def __init__(self, id=0, displayName=None, displayNamePrefixLength=0, scopeId=0, nestedNodes=None, annotations=None, file=_undefined, struct=_undefined, enum=_undefined, interface=_undefined, const=_undefined, annotation=_undefined, parameters=None, isGeneric=False):
        _buf = self.__new(id, displayName, displayNamePrefixLength, scopeId, nestedNodes, annotations, file, struct, enum, interface, const, annotation, parameters, isGeneric)
        _Struct.__init__(self, _buf, 0, 5, 6)
    
    @classmethod
    def new_file(cls, id=0, displayName=None, displayNamePrefixLength=0, scopeId=0, nestedNodes=None, annotations=None, file=None, parameters=None, isGeneric=False):
        buf = cls.__new(id=id, displayName=displayName, displayNamePrefixLength=displayNamePrefixLength, scopeId=scopeId, nestedNodes=nestedNodes, annotations=annotations, file=file, parameters=parameters, isGeneric=isGeneric)
        return cls.from_buffer(buf, 0, 5, 6)
    
    @classmethod
    def new_struct(cls, id=0, displayName=None, displayNamePrefixLength=0, scopeId=0, nestedNodes=None, annotations=None, struct=(0, 0, 0, False, 0, 0, None,), parameters=None, isGeneric=False):
        buf = cls.__new(id=id, displayName=displayName, displayNamePrefixLength=displayNamePrefixLength, scopeId=scopeId, nestedNodes=nestedNodes, annotations=annotations, struct=struct, parameters=parameters, isGeneric=isGeneric)
        return cls.from_buffer(buf, 0, 5, 6)
    
    @classmethod
    def new_enum(cls, id=0, displayName=None, displayNamePrefixLength=0, scopeId=0, nestedNodes=None, annotations=None, enum=(None,), parameters=None, isGeneric=False):
        buf = cls.__new(id=id, displayName=displayName, displayNamePrefixLength=displayNamePrefixLength, scopeId=scopeId, nestedNodes=nestedNodes, annotations=annotations, enum=enum, parameters=parameters, isGeneric=isGeneric)
        return cls.from_buffer(buf, 0, 5, 6)
    
    @classmethod
    def new_interface(cls, id=0, displayName=None, displayNamePrefixLength=0, scopeId=0, nestedNodes=None, annotations=None, interface=(None, None,), parameters=None, isGeneric=False):
        buf = cls.__new(id=id, displayName=displayName, displayNamePrefixLength=displayNamePrefixLength, scopeId=scopeId, nestedNodes=nestedNodes, annotations=annotations, interface=interface, parameters=parameters, isGeneric=isGeneric)
        return cls.from_buffer(buf, 0, 5, 6)
    
    @classmethod
    def new_const(cls, id=0, displayName=None, displayNamePrefixLength=0, scopeId=0, nestedNodes=None, annotations=None, const=(None, None,), parameters=None, isGeneric=False):
        buf = cls.__new(id=id, displayName=displayName, displayNamePrefixLength=displayNamePrefixLength, scopeId=scopeId, nestedNodes=nestedNodes, annotations=annotations, const=const, parameters=parameters, isGeneric=isGeneric)
        return cls.from_buffer(buf, 0, 5, 6)
    
    @classmethod
    def new_annotation(cls, id=0, displayName=None, displayNamePrefixLength=0, scopeId=0, nestedNodes=None, annotations=None, annotation=(None, False, False, False, False, False, False, False, False, False, False, False, False,), parameters=None, isGeneric=False):
        buf = cls.__new(id=id, displayName=displayName, displayNamePrefixLength=displayNamePrefixLength, scopeId=scopeId, nestedNodes=nestedNodes, annotations=annotations, annotation=annotation, parameters=parameters, isGeneric=isGeneric)
        return cls.from_buffer(buf, 0, 5, 6)
    
    def shortrepr(self):
        parts = []
        parts.append("id = %s" % self.id)
        if self.has_displayName(): parts.append("displayName = %s" % _text_repr(self.get_displayName()))
        parts.append("displayNamePrefixLength = %s" % self.displayNamePrefixLength)
        parts.append("scopeId = %s" % self.scopeId)
        if self.has_nestedNodes(): parts.append("nestedNodes = %s" % self.get_nestedNodes().shortrepr())
        if self.has_annotations(): parts.append("annotations = %s" % self.get_annotations().shortrepr())
        if self.is_file(): parts.append("file = %s" % "void")
        if self.is_struct(): parts.append("struct = %s" % self.struct.shortrepr())
        if self.is_enum(): parts.append("enum = %s" % self.enum.shortrepr())
        if self.is_interface(): parts.append("interface = %s" % self.interface.shortrepr())
        if self.is_const(): parts.append("const = %s" % self.const.shortrepr())
        if self.is_annotation(): parts.append("annotation = %s" % self.annotation.shortrepr())
        if self.has_parameters(): parts.append("parameters = %s" % self.get_parameters().shortrepr())
        parts.append("isGeneric = %s" % str(self.isGeneric).lower())
        return "(%s)" % ", ".join(parts)



del globals()['CodeGeneratorRequest_RequestedFile']
del globals()['CodeGeneratorRequest_RequestedFile_Import']
del globals()['Brand_Binding']
del globals()['Brand_Scope']
del globals()['Node_NestedNode']
del globals()['Node_Parameter']

_extend_module_maybe(globals(), modname=__name__)
