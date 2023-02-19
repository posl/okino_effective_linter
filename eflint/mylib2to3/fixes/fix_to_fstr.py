"""Fixer for format string"""

import re

from .. import fixer_base
from ..fixer_util import String, is_string
from ..msg_container import build_message


class FixToFstr(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = """
              term< text=any '%' atom< '(' items=testlist_gexp ')' > >
              """

    CODE = 'ef004'
    MESSAGE = """
    修正案
    {}
    """
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        text = results["text"]
        items = results["items"]

        text_quote = text.value[0]
        new_text = text.value
        args = [str(child).strip() for child in items.children if str(child) != ',']
        repattern = re.compile(r'([^%])%([+ ]?)(-?)(\d*)(\.?\d*)(\w)')

        for arg in args:
            # クオートの種類が被らないように切り替える
            if arg[0] == text_quote:
                arg = self.switch_quotes(arg)

            m = repattern.search(new_text)
            colon = ''
            try:
                esc, sign, left, pad, cat, form = m.groups()
            except AttributeError:
                return None, None

            if sign or pad or cat:
                colon = ':'

            # padding
            # Cフォーマット
            # 「-」なしのパディングでは，種類によらず右寄せになる
            #
            # f文字列
            # 「<>」なしのパディングでは，文字列は左寄せ，数値は右寄せになる
            if pad:
                if form == 's':
                    pad = ('' if left == '-' else '>') + pad
                else:
                    pad = ('<' if left == '-' else '') + pad

            # repr, asciiの変換 （strはデフォルトで変換されるので不要？）
            if form in 'ra':
                form = '!' + form
            # signがあるときはformを残す必要がある
            elif not sign:
                form = ''

            new_text, _ = repattern.subn(f'{esc}{{{arg}{colon}{sign}{pad}{cat}{form}}}', new_text, count=1)

        new_stmt = String(f'f{new_text}', prefix=node.prefix)
        msg = build_message(self, node, message=self.MESSAGE.format(str(new_stmt)), replacement=new_stmt)

        return new_stmt, msg

    def switch_quotes(self, text):
        if text[0] == "'":
            return '"' + text[1:-1] + '"'
        if text[0] == '"':
            return "'" + text[1:-1] + "'"
        return text

    def match(self, node):
        r = super(FixToFstr, self).match(node)
        if r:
            if is_string(r["text"]):
                return r
            return None
        return r
