"""Fixer for key error"""


from .. import fixer_base
from ..fixer_util import Assign, Name, Call, Attr, Comma
from ..msg_container import build_message


class FixKeyError(fixer_base.BaseFix):

    BM_compatible = True

    PATTERN = r"""
        if0=if_stmt<
            'if' comparison< key0=any 'in' dict0=any > ':'
            suite< any any
                simple_stmt< expr_stmt< id0=any '=' power< dict1=any trailer< '[' key1=any ']' > > > any > any
            >
            'else' ':'
            suite< any any simple_stmt< expr_stmt< id1=any '=' val0=any > any > any >
        >
        |
        try0=try_stmt<
            'try' ':'
            suite< any any
                simple_stmt< expr_stmt< id0=any '=' power< dict0=any trailer< '[' key0=any ']' > > > any > any
            >
            except_clause ':'
            suite< any any simple_stmt< expr_stmt< id1=any '=' val0=any > any > any >
        >
    """

    CODE = 'ef016'
    MESSAGE = '欠損値にはgetを使え'
    SEVERITY = 2
    CORRECTABLE = 1
    DOCSURL = ''

    def transform(self, node, results):

        key = results['key0'].clone()
        val = results['val0'].clone()
        _dict = results['dict0'].clone()
        _id = results['id0'].clone()
        key.prefix = ''

        get = Call(Name('get'), args=[key, Comma(), val])
        attr = Attr(_dict, get)
        new = Assign(_id, attr)

        msg = build_message(self, node, replacement=str(new))

        return new, msg

    def match(self, node):
        r = super(FixKeyError, self).match(node)
        if r and 'if0' in r:
            if r['dict0'] == r['dict1'] and r['key0'] == r['key1'] and r['id0'] == r['id1']:
                return r
            return None
        if r and 'try0' in r:
            if r['id0'] == r['id1']:
                return r
            return None
        return r
