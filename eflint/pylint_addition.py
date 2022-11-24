"""pylintを上書きする用のデータ"""

DATAS = {
    "E0102": {
        "severity": 2,
        "url": r"https://pylint.pycqa.org/en/latest/user_guide/messages/error/function-redefined.html",
        "message": """
        同名関数を再定義している．""",
    },
}
