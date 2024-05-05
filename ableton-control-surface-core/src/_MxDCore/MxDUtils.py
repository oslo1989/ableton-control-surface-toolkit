# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_MxDCore/MxDUtils.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 9496 bytes
import logging

from future.utils import string_types

from ableton.v2.base import old_hasattr

logger = logging.getLogger(__name__)


class TupleWrapper:
    _tuple_wrapper_registry = {}

    def forget_tuple_wrapper_instances():
        TupleWrapper._tuple_wrapper_registry = {}

    forget_tuple_wrapper_instances = staticmethod(forget_tuple_wrapper_instances)

    def get_tuple_wrapper(parent, attribute, element_filter=None, element_transform=None):
        if (parent, attribute) not in TupleWrapper._tuple_wrapper_registry:
            TupleWrapper._tuple_wrapper_registry[(parent, attribute)] = TupleWrapper(
                parent,
                attribute,
                element_filter,
                element_transform,
            )
        return TupleWrapper._tuple_wrapper_registry[(parent, attribute)]

    get_tuple_wrapper = staticmethod(get_tuple_wrapper)

    def __init__(self, parent, attribute, element_filter=None, element_transform=None):
        self._parent = parent
        self._attribute = attribute
        self._element_filter = element_filter
        self._element_transform = element_transform

    def get_list(self):
        result = ()
        parent = self._parent
        if isinstance(parent, dict):
            if self._attribute in list(parent.keys()):
                result = parent[self._attribute]
        else:
            if old_hasattr(parent, self._attribute):
                result = getattr(parent, self._attribute)
        filtered_result = [e if self._element_filter(e) else None for e in result] if self._element_filter else result
        if self._element_transform:
            return list(map(self._element_transform, filtered_result))
        return filtered_result


STATE_NEUTRAL = "neutral"
STATE_QUOTED_STR = "quoted"
STATE_UNQUOTED_STR = "unquoted"
STATE_PENDING_NR = "number"
STATE_PENDING_FLOAT = "float"
QUOTE_ENTITY = "&quot;"
QUOTE_SIMPLE = '"'


class StringHandler:
    def prepare_incoming(string):
        return string.replace(QUOTE_ENTITY, QUOTE_SIMPLE)

    prepare_incoming = staticmethod(prepare_incoming)

    def prepare_outgoing(string):
        result = string.replace(QUOTE_SIMPLE, QUOTE_ENTITY)
        if result.find(" ") >= 0:
            result = QUOTE_SIMPLE + result + QUOTE_SIMPLE
        return result

    prepare_outgoing = staticmethod(prepare_outgoing)

    def parse(string, id_callback):
        return StringHandler(id_callback).parse_string(string)

    parse = staticmethod(parse)

    def __init__(self, id_callback):
        self._state = STATE_NEUTRAL
        self._sub_string = ""
        self._open_quote_index = -1
        self._id_callback = id_callback

    def parse_string(self, string):
        self._arguments = []
        self._sub_string = ""
        self._state = STATE_NEUTRAL
        self._open_quote_index = -1
        for index in range(len(string)):
            char = string[index]
            handle_selector = "_" + str(self._state) + "_handle_char"
            if old_hasattr(self, handle_selector):
                getattr(self, handle_selector)(char, index)
            else:
                logger.info("Unknown state " + str(self._state))

        finalize_selector = "_finalize_" + str(self._state)
        if len(self._sub_string) > 0:
            if old_hasattr(self, finalize_selector):
                getattr(self, finalize_selector)()
        return self._arguments

    def _neutral_handle_char(self, char, index):
        if char == '"':
            self._open_quote_index = index
            self._state = STATE_QUOTED_STR
        else:
            if char != " ":
                self._sub_string += char
                if str(char).isdigit():
                    self._state = STATE_PENDING_NR
                else:
                    self._state = STATE_UNQUOTED_STR

    def _number_handle_char(self, char, index):
        if char == " ":
            if len(self._sub_string) > 0:
                self._finalize_number()
            else:
                self._state = STATE_NEUTRAL
        else:
            if char == ".":
                self._state = STATE_PENDING_FLOAT
            else:
                if not str(char).isdigit():
                    self._state = STATE_UNQUOTED_STR
            self._sub_string += char

    def _float_handle_char(self, char, index):
        if char == " ":
            self._add_argument(float(self._sub_string))
        else:
            if char in (".", "e", "E"):
                if char in self._sub_string:
                    self._state = STATE_UNQUOTED_STR
            else:
                if not str(char).isdigit():
                    self._state = STATE_UNQUOTED_STR
            self._sub_string += char

    def _unquoted_handle_char(self, char, index):
        if char == " ":
            self._add_argument(self._sub_string)
        else:
            if str(char).isdigit():
                if self._sub_string == "-":
                    self._state = STATE_PENDING_NR
                else:
                    if self._sub_string in (".", "-."):
                        self._state = STATE_PENDING_FLOAT
            self._sub_string += char

    def _quoted_handle_char(self, char, index):
        if char == '"':
            self._open_quote_index = -1
            self._add_argument(self._sub_string)
        else:
            self._sub_string += char

    def _finalize_quoted(self):
        raise RuntimeError("no match for quote at index %d found" % self._open_quote_index)

    def _finalize_unquoted(self):
        self._add_argument(self._sub_string)

    def _finalize_float(self):
        self._add_argument(float(self._sub_string))

    def _finalize_number(self):
        argument = int(self._sub_string)
        if str(self._arguments[-1]) == "id":
            self._arguments.pop()
            try:
                argument = self._id_callback(argument)
            except KeyError:
                raise RuntimeError("Invalid id")

        self._add_argument(argument)

    def _add_argument(self, argument):
        if isinstance(argument, string_types):
            argument = StringHandler.prepare_incoming(argument)
        self._arguments.append(argument)
        self._sub_string = ""
        self._state = STATE_NEUTRAL
