"""Fixer for format string"""

import re
from .. import fixer_base
from ..fixer_util import String


class FixFormatStr(fixer_base.BaseFix):

    BM_compatible = True

    # 他パターンの追加
    PATTERN = """
              term< text=any '%' atom< '(' items=testlist_gexp ')' > >          
              """

    # 一意なコード
    CODE = 'ef004'

    MESSAGE = 'f文字列を使え'

    # エラーレベル
    SEVERITY = 2

    # 修正可能か
    CORRECTABLE = 1


    def transform(self, node, results):
        text = results["text"]
        items = results["items"]

        new_text = text.value[1:-1]
        quote = text.value[0]
        args = [child.value for child in items.children if child.value != ',']

        for arg in args:
            new_text, _ = re.subn(r'%\w', f'{{{arg}}}', new_text, count=1)
            # パディング(%10d)，リテラル（'test'），エスケープ（%%d）

        new_stmt = String(f'f{quote}{new_text}{quote}', prefix=node.prefix)
        return new_stmt
