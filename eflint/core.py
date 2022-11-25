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


def main():
    """lib2to3とpylintを実行し，出力を整形する"""

    # args = parser.parse_args()
    params = [{"messages": []}]
    code = sys.stdin.read()

    # mylib
    lib2to3_msgs = mylib(
        fixer_pkg="eflint.mylib2to3.fixes", code=code, args=["--no-diffs", "-"]
    )

    for msg in lib2to3_msgs:
        linter_msg = {
            "lineStart": msg.line_start,
            "columnStart": msg.column_start,
            "lineEnd": msg.line_logical_end,
            "columnEnd": msg.column_logical_end,
            "code": msg.code,
            "message": msg.message,
            "severity": msg.severity,
            "source": "eflint",
            "correctable": msg.correctable,
            "docsUrl": "https://code.visualstudio.com/api",
        }

        if msg.correctable:
            linter_msg["inlineFix"] = {
                "replacement": msg.replacement,
                "start": {"column": msg.column_start, "line": msg.line_start},
                "end": {"column": msg.column_logical_end, "line": msg.line_logical_end},
            }

        params[0]["messages"].append(linter_msg)

    # pylint
    with subprocess.Popen(["echo", code], stdout=subprocess.PIPE) as pipe:
        pylint_output = subprocess.run(
            ["pylint", "--from-stdin", "stdin", "-f", "json"],
            stdin=pipe.stdout,
            capture_output=True,
            text=True,
            check=False,
        ).stdout
    pylint_msgs = json.loads(pylint_output)

    # TODO: lib2to3とかぶってるやつは表示しないようにする
    for msg in pylint_msgs:
        if data := DATAS.get(msg["message-id"]):
            linter_msg = {
                "lineStart": msg["line"] - 1,
                "columnStart": msg["column"],
                "lineEnd": msg["endLine"] or msg["line"] - 1,
                "columnEnd": msg["endColumn"] or msg["column"] + 1,
                "code": f'{msg["message-id"]}:{msg["symbol"]}',
                "message": msg["message"] + textwrap.dedent(data.get("message", "")),
                "severity": data.get("severity", 1),
                "source": "eflint",
                "correctable": 0,
                "docsUrl": URL.format(msg["type"], msg["symbol"]),
            }

            params[0]["messages"].append(linter_msg)

    result = json.dumps(params, ensure_ascii=False)
    print(result)
