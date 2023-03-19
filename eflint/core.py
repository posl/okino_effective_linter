"""eflintのメインプログラム"""

import argparse
import json
import subprocess
import sys
import textwrap

from .mylib2to3.main import main as mylib
from .pylint_addition import URL, DATAS

parser = argparse.ArgumentParser(
    prog="eflint",
    usage="how to use",
    description="linter for effective python.",
)
parser.add_argument('path', nargs='?', default=None, help='path to program. If not set, --stdin is required.')
parser.add_argument('--stdin', action='store_true', help='receive code from stdin.')


def main():
    """lib2to3とpylintを実行し，出力を整形する"""

    args = parser.parse_args()
    if args.path:
        with open(args.path, mode='r', encoding='utf_8') as file:
            code = file.read()
    if args.stdin:
        code = sys.stdin.read()

    # pylintの呼び出しの際に末尾の空白行が1つ増える問題の回避策
    if code[-1] == '\n':
        code = code[:-1]

    params = [{"messages": []}]

    ##########
    # pylint
    ##########
    with subprocess.Popen(["echo", code], stdout=subprocess.PIPE) as pipe:
        pylint_output = subprocess.run(
            ["pylint", "--from-stdin", "stdin", "-f", "json"],
            stdin=pipe.stdout,
            capture_output=True,
            text=True,
            check=False,
        ).stdout
    pylint_msgs = json.loads(pylint_output)

    type2severity = {'error': 3, 'warning': 2, 'convention': 1, 'refactor': 1}

    for msg in pylint_msgs:
        if data := DATAS.get(msg["message-id"]):
            linter_msg = {
                "lineStart": msg["line"] - 1,
                "columnStart": msg["column"],
                "lineEnd": (msg["endLine"] or msg["line"]) - 1,
                "columnEnd": msg["endColumn"] or (msg["column"] + 1),
                "code": f'{msg["message-id"]}:{msg["symbol"]}',
                "message": msg["message"] + textwrap.dedent(data.get("message", "")),
                "severity": type2severity.get(msg["type"], 1),
                "priority": data.get("priority", type2severity.get(msg["type"], 1)),
                "source": "eflint",
                "correctable": 0,
                "docsUrl": URL.format(msg["type"], msg["symbol"]),
            }

            params[0]["messages"].append(linter_msg)

    ##########
    # mylib
    ##########
    lib2to3_msgs = mylib(
        fixer_pkg="eflint.mylib2to3.fixes", code=code, args=["--no-diffs", "-"]
    )

    # ドキュメントURLは現状特にないので仮置き
    for msg in lib2to3_msgs:
        linter_msg = {
            "lineStart": msg.line_start,
            "columnStart": msg.column_start,
            "lineEnd": msg.line_logical_end,
            "columnEnd": msg.column_logical_end,
            "code": msg.code,
            "message": msg.message,
            "severity": msg.severity,
            "priority": msg.severity,
            "source": "eflint",
            "correctable": msg.correctable,
            "docsUrl": "https://pylint.pycqa.org/en/latest/user_guide/messages/messages_overview.html",
        }

        if msg.correctable:
            linter_msg["inlineFix"] = {
                "replacement": msg.replacement,
                "start": {"column": msg.column_start, "line": msg.line_start},
                "end": {"column": msg.column_logical_end, "line": msg.line_logical_end},
            }

        params[0]["messages"].append(linter_msg)

    result = json.dumps(params, ensure_ascii=False)
    print(result)
