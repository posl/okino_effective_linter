"""pylintを上書きする用のデータ"""

URL = "https://pylint.pycqa.org/en/latest/user_guide/messages/{}/{}.html"

DATAS = {
    "E0102": {
        "severity": 2,
        "message": """
        同名関数を再定義している．""",
    },
    "E0401": {
        "severity": 2,
        "message": """
        モジュールのインポートに失敗．""",
    },
    "E1126": {
        "severity": 2,
        "message": """
        インデックスに予期しない値が含まれる．""",
    },
    "E1101": {
        "severity": 2,
        "message": """
        存在しないメンバを参照している．""",
    },
    "E1120": {
        "severity": 2,
        "message": """
        関数の引数が足りない．""",
    },
    "E1133": {
        "severity": 2,
        "message": """
        反復可能でないものを反復しようとしている．""",
    },
    "E1102": {
        "severity": 2,
        "message": """
        関数以外のものを()で呼び出している．""",
    },
    "E0103": {
        "severity": 2,
        "message": """
        ループ外でcontinueやbreakを使用している．""",
    },
    "E0104": {
        "severity": 2,
        "message": """
        関数外でreturnを使用している．""",
    },
    "E0001": {
        "severity": 2,
        "message": """
        構文エラーが発生している．""",
    },
    "E1121": {
        "severity": 2,
        "message": """
        関数の引数が定義よりも多い．""",
    },
    "E0602": {
        "severity": 0,
        "message": """
        未定義変数を使用している．""",
    },
    "E1136": {
        "severity": 2,
        "message": """
        シーケンスでないものを[]で参照している．""",
    },
    "E1137": {
        "severity": 2,
        "message": """
        シーケンスでないものを[]で代入しようとしている．""",
    },
    "E0601": {
        "severity": 2,
        "message": """
        変数に値を代入をする前に参照している．""",
    },
    "W0622": {
        "severity": 2,
        "message": """
        ビルドインと同名の変数や関数を定義している．""",
    },
    "W2901": {
        "severity": 2,
        "message": """
        ループ変数をループ内で再定義している．""",
    },
}
