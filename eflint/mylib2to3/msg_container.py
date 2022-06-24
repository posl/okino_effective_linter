"Message Container"

from typing import NamedTuple

from .pytree import Base
from .fixer_base import BaseFix


class MessageContainer(NamedTuple):
    line_start: int
    column_start: int
    line_logical_end: int
    column_logical_end: int
    line_end: int
    column_end: int
    code: str
    message: str
    severity: int
    correctable: int
    replacement: int


def build_message(fixer: BaseFix, start_node: Base, end_node: Base = None, *, code: str = None, message: str = None,
                  severity: int = None, correctable: int = None, replacement: str = None) -> MessageContainer:
    end_node = end_node or start_node
    code = code or fixer.CODE
    message = message or fixer.MESSAGE
    severity = severity if severity is not None else fixer.SEVERITY
    correctable = correctable if correctable is not None else fixer.CORRECTABLE

    msg = MessageContainer(
        start_node.get_lineno()-1,
        start_node.get_columnno(),
        end_node.get_end_lineno(is_logical=True)-1,
        end_node.get_end_columnno(is_logical=True),
        end_node.get_end_lineno()-1,
        end_node.get_end_columnno(),
        code,
        message,
        severity,
        correctable,
        replacement
    )

    return msg