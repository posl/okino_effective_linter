"""単体のexcept句を変換する
なお，本来はExceptionよりも具体的なエラーを指定すべき

* Change

    try:
        x = x / 0
    except:
        print('Zero divided.')

into

    try:
        x = x / 0
    except Exception:
        print('Zero divided.')
"""


from .. import fixer_base
from ..fixer_util import Except, Name
from ..msg_container import build_message


class FixBareExcept(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = r"""
    try_stmt<
        'try' ':' suite
        except='except' ':' suite
        any*
    >
    """

    CODE = 'W0702'
    MESSAGE = ''
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):
        old_node = node.clone()
        results["except"].replace(Except(Name('Exception', prefix=' ')))
        node.prefix = ''
        msg = build_message(self, old_node, replacement=node)
        return node, msg

    def match(self, node):
        r = super().match(node)
        return r
