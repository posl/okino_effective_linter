"""Fixer for format string"""

import re

from .. import fixer_base
from ..fixer_util import String
from ..refactor import MessageContainer  # 移動したい


class FixFormatStr(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = """
              term< text=any '%' atom< '(' items=testlist_gexp ')' > >
              """

    CODE = 'ef004'
    MESSAGE = 'f文字列を使え'
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        text = results["text"]
        items = results["items"]

        new_text = text.value
        args = [child.value for child in items.children if child.value != ',']

        repattern = re.compile(r'([^%])%\w')

        for arg in args:
            new_text, _ = repattern.subn(f'\\1{{{arg}}}', new_text, count=1)

        new_stmt = String(f'f{new_text}', prefix=node.prefix)

        msg = MessageContainer(
            node.get_lineno()-1,
            node.get_columnno(),
            node.get_end_lineno()-1,
            node.get_end_columnno(),
            self.CODE,
            self.MESSAGE,
            self.SEVERITY,
            self.CORRECTABLE,
            str(new_stmt)
        )

        return new_stmt, msg
