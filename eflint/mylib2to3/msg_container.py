"Message Container"

from typing import NamedTuple
import textwrap

from .fixer_base import BaseFix
from .pytree import Base

TEMPLATE = """
【修正案】
{}"""


class MessageContainer(NamedTuple):
    """メッセージ受け渡し用のクラス"""

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


def build_message(
    fixer: BaseFix,
    start_node: Base,
    *,
    end_node: Base = None,
    code: str = None,
    message: str = "",
    severity: int = None,
    correctable: int = None,
    replacement: Base = None,
) -> MessageContainer:
    """整形したメッセージを構築する"""

    end_node = end_node or start_node
    code = code or fixer.CODE
    severity = severity if severity is not None else fixer.SEVERITY
    correctable = correctable if correctable is not None else fixer.CORRECTABLE
    replacement = str(replacement) if replacement else None
    template = TEMPLATE.format(replacement) if replacement else ''
    message = textwrap.dedent(message or fixer.MESSAGE).strip() + template

    msg = MessageContainer(
        start_node.get_lineno() - 1,
        start_node.get_columnno(),
        end_node.get_end_lineno(is_logical=True) - 1,
        end_node.get_end_columnno(is_logical=True),
        end_node.get_end_lineno() - 1,
        end_node.get_end_columnno(),
        code,
        message,
        severity,
        correctable,
        replacement,
    )

    return msg
