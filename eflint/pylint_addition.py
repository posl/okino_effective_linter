"""pylintを上書きする用のデータ"""

URL = "https://pylint.pycqa.org/en/latest/user_guide/messages/{}/{}.html"

DATAS = {
    ##########
    # Error
    ##########
    "E0102": {
        "priority": 3,
        "message": """
        同名関数を再定義しています．先に定義した関数が後のもので上書きされてしまうため，別の名前に変更しましょう．""",
    },
    "E0401": {
        "priority": 3,
        "message": """
        パッケージのインポートにエラーが存在します．以下の点をチェックしてみましょう．
        - パッケージ名などをタイプミスをしていないか．
        - インストールされていないパッケージをインポートしていないか．pipなどを用いてインストールする必要があります．
        - `import パッケージ名`，`from パッケージ名 import 関数名やクラス名`のように正しい順序で記述しているか．""",
    },
    "E1126": {
        "priority": 3,
        "message": """
        インデックス参照に予期しない値が含まれています．以下の点をチェックしてみましょう．
        - リストの周辺に，あるべきカンマが不足していないか．カンマ不足により，このエラーが発生することがあります．
        - 要素を追加したり，拡張しようとしていないか．`append()`や`expand()`など，対応したメソッドがあります．
        - リストの一部分にアクセスしようとしていないか．スライスという機能により実現できます．
        - 多次元リストにアクセスしようとしていないか．Pythonでは，`mylist[0][0]`のようにアクセスします．""",
    },
    "E1130": {
        "priority": 3,
        "message": """
        予期せぬ演算子が使用されています．以下の点をチェックしてみましょう．
        - タイプミスをしていないか．
        - 文字列は引用符で囲われているか．""",
    },
    "E1101": {
        "priority": 3,
        "message": """
        存在しないメンバを参照しています．以下の点をチェックしてみましょう．
        - 辞書とリストを混同していないか．辞書に対して`append()`などは使用できません．
        - タイプミスをしていないか．特に，`random`や`append`の綴りを間違えている例が多いです．
        - インポートの方法と呼び出しの整合性は取れているか．例えば，`import random`とした場合は`random.random()`のように呼び出しますが，`from random import random`とした場合は`random()`と呼び出します．
        - メソッド引数をメンバのように呼び出していないか．`append(x)`を`append.x`としてしまっている例があります．""",
    },
    "E0611": {
        "priority": 3,
        "message": """
        存在しないオブジェクトをインポートしています．以下の点をチェックしてみましょう．
        - 他のパッケージと勘違いしていないか．例えば，`math.random()`としている例があります．
        - タイプミスをしていないか．例えば，`random`の綴りを間違えていないか．""",
    },
    "E1120": {
        "priority": 3,
        "message": """
        関数の引数が不足しています．関数定義に記述した引数を網羅しているかチェックしましょう．""",
    },
    "E0107": {
        "priority": 3,
        "message": """
        存在しない演算子を使用しています．以下の点をチェックしてみましょう．
        - 文字列にすべき部分が正しく引用符で囲われているか．文字列内に演算子が含まれると，このエラーが発生する可能性があります．
        - タイプミスをしていないか．""",
    },
    "E1133": {
        "priority": 3,
        "message": """
        反復可能でないものを反復しようとしています．以下の点をチェックしてみましょう．
        - 辞書やリストなどでないものを反復処理していないか．もう一度for文の仕様について確認しましょう．
        - 整数値を直接反復処理していないか．`range()`を用いることで，値の数だけ反復処理をすることができます．
        - 乗算付近に誤ったカンマが含まれていないか．アンパックという記法になり，このエラーが発生することがあります．
        - リストを誤った方法で記述していないか．例えば，`list[1, 2]`という記述は型ヒントという扱いになり，リストと認識されません．""",
    },
    "E1102": {
        "priority": 3,
        "message": """
        呼び出し可能でないものを呼び出そうとしています．以下の点をチェックしてみましょう．
        - リストや辞書の要素を()で呼び出そうとしていないか．それらの要素は`mylist[key]`のように呼び出します．
        - リストやタプル周辺のカンマが不足していないか．カンマ不足により，このエラーが発生することがあります．
        - パッケージなどを直接呼び出していないか．例えば，`import random`したものは`random.random()`のように呼び出します．
        - 関数と同名の変数を定義していないか．先に定義した関数が変数で上書きされてしまい，関数を呼び出せなくなるため，変数名を変更しましょう．
        - 乗算を正しく記述しているか．Pythonでは，`2*(x+1)`のように乗算演算子を明示する必要があります．""",
    },
    "E0103": {
        "priority": 3,
        "message": """
        ループ外でcontinueやbreakを使用しています．以下の点をチェックしてみましょう．
        - インデントの数がずれていないか．
        - 関数内にreturnの代わりに記述していないか．Pythonにおいて，関数が値を返さない場合は特に何も記述する必要はありません．""",
    },
    "E0104": {
        "priority": 3,
        "message": """
        関数外でreturnを使用しています．以下の点をチェックしてみましょう．
        - インデントの数がずれていないか．
        - 関数外でprint関数のように標準出力を行うことを期待して使用していないか．returnには，関数内で値を返す以外の機能はありません．
        - 関数外でbreakのようにループを脱出することを期待して使用していないか．""",
    },
    "E0114": {
        "priority": 3,
        "message": """
        スター式に代入する値がありません．以下の点をチェックしてみましょう．
        - 乗算の式は正しく記述しているか．乗算の式に誤りがあると，このエラーが発生する可能性があります．""",
    },
    "E0001": {
        "priority": 3,
        "message": """
        構文エラーが発生している．""",
    },
    "E1121": {
        "priority": 3,
        "message": """
        関数の引数が定義よりも多くなっています．以下の点をチェックしてみましょう．
        - 定義した関数の引数よりも多くの引数を渡していないか．もしくは，定義した関数に引数を書き忘れていないか．
        - リストやタプルを展開して引数として渡していないか．
        - 引数の文字列を正しく引用符で囲っているか．文字列内にカンマが含まれると，このエラーが発生する場合があります．""",
    },
    "E0602": {
        "priority": 3,
        "message": """
        未定義の変数を使用しています．以下の点をチェックしてみましょう．
        - その変数の値は初期化されているか．
        - 変数の定義は同じスコープ（場所）に存在するか．変数には寿命があり，別の場所で定義された変数は使用できないことがあります．
        - 必要なものが正しくインポートされているか．""",
    },
    "E1123": {
        "priority": 3,
        "message": """
        関数定義にないキーワード引数を使用しています．以下の点をチェックしてみましょう．
        - 他の関数と間違っていないか．例えば，`print()`関数の`end`キーワードを他の関数に適用していないか．
        - 関数定義に正しくキーワードを設定しているか．""",
    },
    "E0633": {
        "priority": 3,
        "message": """
        シーケンス（リストなど複数の値を持つもの）でないものをアンパックしようとしています．以下の点をチェックしてみましょう．
        - 複数の変数を1行で定義していないか．1行で定義したい場合は，`a, b = 0, 0`，もしくは`a = b = 0`のように定義することができます．
        - インデックス（`a[i]`）の記述ミスをしていないか．記述ミスがあると，このエラーが発生する可能性があります．""",
    },
    "E1136": {
        "priority": 3,
        "message": """
        シーケンス（リストなど複数の値を持つもの）でないものを[]で参照しようとしています．以下の点をチェックしてみましょう．
        - 変数の型がリストや辞書になっているか．
        - 既存の関数と同名の変数を使用していないか．スコープの関係で，意図したものとは違う値が入っている可能性があります．""",
    },
    "E1137": {
        "priority": 3,
        "message": r"""
        予期されていない変数に[]を用いて代入しようとしています．以下の点をチェックしてみましょう．
        - リストや辞書などでないものに対して[]を用いていないか．
        - 変数の初期化は正しく行われているか．変数をリストや辞書として初期化を行うまで，[]を用いた代入は行えません．
        - 標準のオブジェクトと同名の変数を使用していないか．特に，`list`という名前は標準関数`list()`と同名であるため，`list[0]`のような参照は意図した挙動にならない可能性があります．
        - 集合に対して[]を用いたアクセスを行っていないか．辞書と集合の初期化はどちらも{}を用いるため，初期化の段階で誤っている可能性もあります．""",
    },
    "E1135": {
        "priority": 3,
        "message": """
        値がメンバーシップテスト（`A in B`を用いた評価）に対応していません．以下の点をチェックしてみましょう．
        - `A in B`とすべきところを'B in A'と記述していないか．
        - 関数は正しく呼び出されているか．例えば，`mydict.keys`と記述していると，キーの集合ではなくメソッドそのものを取得しまいます．
        - リストや辞書，集合など以外のものを記述していないか．""",
    },
    "E0601": {
        "priority": 3,
        "message": """
        変数に値を代入をする前に参照しています．以下の点をチェックしてみましょう．
        - 変数は正しく初期化されているか．
        - 関数内でグローバル変数（プログラムの一番浅い部分に定義されている変数）に代入しようとしていないか．その場合，グローバル変数に対してglobal宣言を行う必要があります．""",
    },
    ##########
    # Warning
    ##########
    "W1401": {
        "priority": 2,
        "message": """
        文字列中に異常なバックスラッシュが含まれています．バックスラッシュは改行やタブなどを制御するために他の文字とは異なる扱いをする必要があります．バックスラッシュを出力する際は，r文字列を使用するか，バックスラッシュを二つ連続して記述すると出力することができます．""",
    },
    "W1114": {
        "priority": 2,
        "message": """
        関数の仮引数名と呼び出し時の引数の変数名が同名にもかかわらず順番が異なっています．引数の順番をチェックしましょう．""",
    },
    "W0201": {
        "priority": 1,
        "message": """
        __init__()以外でクラスメンバを定義しています．""",
    },
    "W0141": {
        "priority": 1,
        "message": """
        推奨されないビルトインオブジェクトを使用しています．""",
    },
    "W0311": {
        "priority": 3,
        "message": """
        インデントの数に異常が存在します．Blackなどのフォーマッタツールにより，自動で修正を行うことが可能です．""",
    },
    "W0702": {
        "priority": 2,
        "message": """
        単体のexcept句を使用しています．キーボードインタラプション（Ctrl + Cによる停止で発生する例外）などもキャッチしてしまうため好ましくありません．例外クラス名を設定しましょう．""",
    },
    "W0143": {
        "priority": 3,
        "message": """
        関数そのものを比較に使用しています．以下の点をチェックしてみましょう．
        - 定義済みの関数や標準関数と同名の変数を使用していないか．意図しない動作に繋がるため，変数名を変更しましょう．
        - 関数呼び出しのカッコのつけ忘れはないか．カッコがない場合，関数は実行されず，関数そのものを表します．""",
    },
    "W0160": {
        "priority": 2,
        "message": """
        三項演算の使用を検討しましょう．より簡潔に記述することができる場合があります．""",
    },
    "W0109": {
        "priority": 3,
        "message": """
        辞書内に重複したキーを使用しています．キーに重複があると値が上書きされてアクセスできなくなるため，キーが一意になるように変更しましょう．""",
    },
    "W0130": {
        "priority": 3,
        "message": """
        集合内に重複した値があります．以下の点をチェックしてみましょう．
        - 集合の値は一意であるか．重複した値は初期化時にまとめられます．
        - リストなどと間違えていないか．例えば，'[1, 2]'はリスト，`{1, 2}`は集合として扱われます．""",
    },
    "W0106": {
        "priority": 3,
        "message": """
        式が何も起こしません．以下の点をチェックしてみましょう．
        - returnやprint()，代入操作を忘れていないか．例えば，`x == 3`単体は論理値を返しますが，その結果が何にも使用されないため，無意味な文になってしまいます．式や文について仕様を確認してみましょう．
        - 関数を複数回実行されることを期待した操作を行っていないか．例えば，`print(x) * 3`は`print(x)`の返り値に3を掛けるという操作になってしまいます．
        - タイプミスをしていないか．
        - 代入式（'x = 1'）と間違っていないか．""",
    },
    "W1309": {
        "priority": 2,
        "message": """
        f文字列に対して埋め込みが行われていません．以下の点をチェックしてみましょう．
        - 埋め込みの必要がない文字列でもf文字列を使用していないか．動作に問題はありませんが，不必要な処理を盛り込まないようにすることをお勧めします．
        - {}を入れ忘れていないか．
        - 全角波かっこ｛｝を使用していないか．""",
    },
    "W0603": {
        "priority": 1,
        "message": """
        global宣言を使用しています．動作には問題ありませんが，プログラムの構造を見直し，globalを使わない方法に変更できる場合があります．""",
    },
    "W1404": {
        "priority": 2,
        "message": """
        暗黙的な文字列結合を行っています．以下の点をチェックしてみましょう．
        - 理由なく暗黙的な文字列結合を行っていないか．他のエラーの原因になる可能性があるため，最初から1つの文字列にまとめることをお勧めします．
        - カンマを入れ忘れていないか．""",
    },
    "W0104": {
        "priority": 3,
        "message": """
        無意味な文が存在します．以下の点をチェックしてみましょう．
        - 代入（=）と比較（==）を間違えていないか．
        - 計算結果は変数に代入されているか．""",
    },
    "W0105": {
        "priority": 2,
        "message": """
        文字列のみの文が存在します．print関数の使用や，変数への代入が考えられます．""",
    },
    "W0212": {
        "priority": 2,
        "message": """
        保護されたオブジェクトにアクセスしています．アンダースコア（_）で始まるオブジェクトは外部からアクセスしないことが推奨されています．""",
    },
    "W0622": {
        "priority": 3,
        "message": """
        ビルトインオブジェクトと同名のオブジェクトを定義しています．意図しない動作を引き起こす可能性があるため，オブジェクト名を変更することが推奨されます．""",
    },
    "W2901": {
        "priority": 3,
        "message": """
        ループ変数をループ内で再定義しています．以下の点をチェックしてみましょう．
        - 二重ループを同名の変数を用いてループさせていないか．
        - ループ変数の値をループ内で上書きしようとしていないか．別変数扱いになるため，意図しない動作の原因になります．""",
    },
    "W0621": {
        "priority": 2,
        "message": """
        仮引数と同名の変数を外部で宣言しています．意図しないエラーの原因となるため，変数名を変更することが推奨されます．""",
    },
    "W0404": {
        "priority": 2,
        "message": """
        同じパッケージを複数回インポートしています．""",
    },
    "W0127": {
        "priority": 2,
        "message": """
        変数に自身を代入しようとしています．以下の点をチェックしてみましょう．
        - 「何もしない」を意図していないか．Pythonにおいては`pass`を用いることができます．
        - 条件分岐は工夫できないか．例えば，条件式を否定してifとelseを入れ替えることで，「何もしない」を記述しなくて済む可能性があります．
        - 他の変数と間違えて代入していないか．""",
    },
    "W0717": {
        "priority": 1,
        "message": """
        try文に複数文を記述しています．例外が発生する行を絞るためにも，try文の中身は最小限にすることが推奨されます．""",
    },
    "W0632": {
        "priority": 2,
        "message": """
        アンパックの数を間違えています．正しい記述になっているかチェックしましょう．""",
    },
    "W0631": {
        "priority": 3,
        "message": """
        ループ変数をループの外で使用しています．ループ変数には最後のループの値が残っているため，意図しない挙動を起こす可能性があります．""",
    },
    "W2301": {
        "priority": 1,
        "message": """
        不必要な`...`を使用しています．""",
    },
    "W0107": {
        "priority": 2,
        "message": """
        不必要な`pass`を使用しています．""",
    },
    "W0301": {
        "priority": 2,
        "message": """
        不必要なセミコロンを使用しています．Pythonではセミコロンは不要です．""",
    },
    "W0101": {
        "priority": 3,
        "message": """
        到達できない行が存在します．returnやbreakが正しい位置に存在するかチェックしましょう．""",
    },
    "W0613": {
        "priority": 2,
        "message": """
        未使用の仮引数があります．不要なものは削除しましょう．""",
    },
    "W0611": {
        "priority": 2,
        "message": """
        未使用のインポートがあります．不要なものは削除しましょう．autoflakeにより自動で削除することもできます．""",
    },
    "W0612": {
        "priority": 2,
        "message": """
        未使用の変数があります．不要なものは削除しましょう．autoflakeにより自動で削除することもできます．""",
    },
    "W0614": {
        "priority": 1,
        "message": """
        ワイルドカードインポートで未使用のオブジェクトがあります．autoflakeにより自動で修正することができます．""",
    },
    "W0120": {
        "priority": 2,
        "message": """
        `for(while) ... else ...`構文を使用しています．以下の点をチェックしてみましょう．
        - 単に上記の構文を使用していないか．Pythonでは正式な構文ですが，理解しにくい構文なので使用しないことをお勧めします．
        - elseブロックのインデントがズレていないか．インデントにずれがあると，このエラーが発生する可能性があります．""",
    },
    "W0125": {
        "priority": 2,
        "message": """
        条件式に定数単体が使用されています．以下の点をチェックしてみましょう．
        - `if True`のような記述をしていないか．この場合，条件分岐は不要です．
        - 比較式を書き忘れていないか．例えば，`if x == 2`を意図して`if 2`と記述していないか．""",
    },
    "W0149": {
        "priority": 1,
        "message": """
        while文を使用しています．多くの場合，ループ回数が有限であるfor文に置き換えることができます．""",
    },
    "W0401": {
        "priority": 1,
        "message": """
        ワイルドカードインポート（*）を使用しています．どのオブジェクトがどのモジュールに含まれるか分かりにくくなるため，ワイルドカードの乱用はやめましょう．""",
    },
    ##########
    # Convention
    ##########
    "C1901": {
        "priority": 2,
        "message": """
        空の文字列との比較を行っています．以下の点をチェックしてみましょう．
        - 単に空の文字列との比較を行っていないか．多くの場合，`if x != ''`は，暗黙的な論理値変換を利用して，`if x`に置き換えることができます．
        - 代入演算子（`=`）と比較演算子（`==`）を間違えていないか．""",
    },
    "C2001": {
        "priority": 2,
        "message": """
        0との比較を行っています．`if len(mylist) == 0`のような条件式を記述している場合は，暗黙的な変換を用いて`if x`に置き換えることができます．""",
    },
    "C0201": {
        "priority": 2,
        "message": """
        `dict.keys()`をイテレート（反復）しています．for文などで辞書をループする場合は，`for key in mydict`のように記述することができます．""",
    },
    "C0206": {
        "priority": 2,
        "message": """
        ループ内で辞書にキーアクセスしています．`for key, value in mydict.items()`のようにループさせることで，`value`変数により辞書の値にアクセスすることができます．""",
    },
    "C0200": {
        "priority": 2,
        "message": """
        enumerateの使用を検討しましょう．`for index, value in enumerate(mylist)`のようにループさせることで，インデックスと値の両方にアクセスすることができます．""",
    },
    "C0209": {
        "priority": 2,
        "message": """
        f文字列の使用を検討しましょう．f文字列には以下のような利点があります．
        - シンプルな記述方法で，コードが不必要に長くならない．
        - 型を考慮する必要性が低く，修正時にエラーの原因になりにくい．""",
    },
    "C0415": {
        "priority": 2,
        "message": """
        トップレベル以外の場所（関数内など）でimportが使用されています．何がインポートされているか明確にするために，プログラムの最上位に記述することが推奨されます．""",
    },
    "C0103": {
        "priority": 1,
        "message": """
        命名規則から外れています．動作には問題ありませんが，命名規則を意識すると可読性があがりコードが見やすくなります．""",
    },
    "C0301": {
        "priority": 1,
        "message": """
        1行が長すぎます．可読性が落ちるため，短くなるように記述を工夫するか，適宜改行を用いましょう．Blackなどのオートフォーマッタにより自動で修正を行うこともできます．""",
    },
    "C2201": {
        "priority": 2,
        "message": """
        定数値を比較式の左に配置しています．定数値など比較される方の値は比較式の右に置くことが好ましいとされています．""",
    },
    "C0115": {
        "priority": 1,
        "message": """
        クラスドキュメント（クラスの説明文）を記述していません．クラスの役割を記述しておくと，共同開発などの際に意図が伝わりやすくなります．""",
    },
    "C0116": {
        "priority": 1,
        "message": """
        関数ドキュメント（関数の説明文）を記述していません．関数の役割を記述しておくと，共同開発などの際に意図が伝わりやすくなります．""",
    },
    "C0114": {
        "priority": 1,
        "message": """
        モジュールドキュメント（ファイルの説明文）を記述していません．モジュールの役割を記述しておくと，共同開発などの際に意図が伝わりやすくなります．""",
    },
    "C0321": {
        "priority": 2,
        "message": """
        1行に複数文を記述しています．可読性のためにも，適宜改行しましょう．Blackなどのオートフォーマッタにより自動で修正することもできます．""",
    },
    "C2403": {
        "priority": 3,
        "message": """
        ASCII文字以外を含むモジュールをインポートしています．""",
    },
    "C2401": {
        "priority": 3,
        "message": """
        ASCIIに含まれない文字を文字列やコメント以外で使用しています．以下の点をチェックしてみましょう．
        - 漢字などを変数名に使用している．動作はしますが，混乱に繋がる可能性があるため使用しないことが推奨されます．
        - 文字列が正しく引用符で囲われているか．""",
    },
    "C0325": {
        "priority": 2,
        "message": """
        不要なカッコが含まれています．Blackなどのオートフォーマッタにより自動で修正することもできます．""",
    },
    "C0305": {
        "priority": 1,
        "message": """
        ファイル末尾に不要な空白行がある．Blackなどのオートフォーマッタにより自動で修正することもできます．""",
    },
    "C0303": {
        "priority": 1,
        "message": """
        行末に不要な空白が含まれています．Blackなどのオートフォーマッタにより自動で修正することもできます．""",
    },
    "C0412": {
        "priority": 2,
        "message": """
        インポートがグループ化されていません．isortなどのオートフォーマッタにより自動で修正することもできます．""",
    },
    "C1803": {
        "priority": 2,
        "message": """
        暗黙的な比較を行うことが可能です．例えば，`if mylist == []`のような記述は，`if mylist`に置き換えることができます．""",
    },
    "C1802": {
        "priority": 2,
        "message": """
        `len()`を用いた暗黙的な比較を行っています．例えば，`if len(mylist)`のような記述は，`if mylist`に置き換えることができます．""",
    },
    "C0411": {
        "priority": 1,
        "message": """
        インポートの順番が正しくありません．インポートは，標準ライブラリ，サードパーティのライブラリ（pipでインストールできるもの），ローカルのモジュールの順に記述します．isortなどのオートフォーマッタにより自動で修正することもできます．""",
    },
    "C0413": {
        "priority": 2,
        "message": """
        ファイル最上部以外でインポートが使用されています．何がインポートされているか明確にするためにも，インポートはファイルの最上部で行いましょう．""",
    },
    ##########
    # Refactor
    ##########
    "R1716": {
        "priority": 2,
        "message": """
        チェインによる比較に置き換えることができます．例えば，`1 < x and x < 3`は`1 < x < 3に置き換えられます．`""",
    },
    "R0133": {
        "priority": 2,
        "message": """
        定数同士の比較を行っています．変数との比較とまちがえていないかチェックしましょう．""",
    },
    "R0124": {
        "priority": 2,
        "message": """
        同じオブジェクト同士を比較しています．他のオブジェクトと間違えていないかチェックしましょう．""",
    },
    "R1727": {
        "priority": 2,
        "message": """
        条件式が常に同じ値を取っています．比較式が抜けていないかチェックしましょう．""",
    },
    "R5601": {
        "priority": 2,
        "message": """
        インデントレベルの異なるelifを連続させています．条件分岐がわかりにくくなるため，条件分岐を工夫したり，関数を分割したりして見やすくしましょう．""",
    },
    "R6103": {
        "priority": 1,
        "message": """
        代入式（:=）の使用を検討しましょう．よりシンプルに記述できる場合があります．""",
    },
    "R0402": {
        "priority": 2,
        "message": """
        fromによるインポートを検討しましょう．asを用いてオブジェクト名単体を名付けるのはあまり好ましくありません．""",
    },
    "R1714": {
        "priority": 2,
        "message": """
        inの使用を検討しましょう．よりシンプルに記述できる場合があります．""",
    },
    "R1731": {
        "priority": 2,
        "message": """
        標準関数のmax()の使用を検討しましょう．よりシンプルに記述できる場合があります．""",
    },
    "R1722": {
        "priority": 1,
        "message": """
        exit()が使用されています．exit()は対話型シェルでの利用を想定した関数であるため，sys.exit()を使用することが望ましいとされています．""",
    },
    "R6102": {
        "priority": 1,
        "message": """
        インプレースのリストを用いています．動作には問題ありませんが，一貫性のためにタプルの使用を検討しましょう．""",
    },
    "R5501": {
        "priority": 1,
        "message": """
        else句の内部でさらに条件分岐を行っています．elifの使用を検討しましょう．""",
    },
    "R2044": {
        "priority": 2,
        "message": """
        空白のコメント行が存在します．""",
    },
    "R1710": {
        "priority": 2,
        "message": """
        returnが値を返す場合と返さない場合が混在しています．バグの原因となる可能性があるため，統一することが望ましいです．""",
    },
    "R0123": {
        "priority": 2,
        "message": """
        リテラルとの比較でisを使用しています．予期しない動作につながるため，`==`による比較を用いましょう．""",
    },
    "R1723": {
        "priority": 2,
        "message": """
        if文でbreakするにもかかわらずelse句が存在します．else句を使用せずとも同じ動作をするため，簡略化することができます．""",
    },
    "R1705": {
        "priority": 2,
        "message": """
        if文内でreturnするにもかかわらずelse句が存在します．else句を使用せずとも同じ動作をするため，簡略化することができます．""",
    },
    "R6301": {
        "priority": 1,
        "message": """
        インスタンスメソッドでselfを使用していません．クラスメソッドにすることを考えましょう．""",
    },
    "R1704": {
        "priority": 3,
        "message": """
        関数内で引数と同名の変数を再定義しています．引数が上書きされてしまう可能性があるため，変数名の変更が推奨されます．""",
    },
    "R0204": {
        "priority": 1,
        "message": """
        変数の型が途中で変化しています．バグを減らすためにも，型の変化は最小限に抑えましょう．""",
    },
    "R1726": {
        "priority": 2,
        "message": """
        条件式に無駄な項が存在しています．定数だけの項など常に同じ値を取る項がないかチェックしましょう．""",
    },
    "R1703": {
        "priority": 2,
        "message": """
        return文のみからなるif-else文が存在します．条件式をそのままreturnすることでより簡潔に記述することができます．""",
    },
    "R1260": {
        "priority": 2,
        "message": """
        McCabeによるスコアが高くなっています．条件分岐の数やネストの深さを見直しましょう．""",
    },
    "R0903": {
        "priority": 1,
        "message": """
        クラスのパブリックメソッドが少なすぎます．クラス以外の表現方法で十分な可能性があります．""",
    },
    "R0913": {
        "priority": 1,
        "message": """
        関数の引数が多すぎます．関数を分割したり，タプルやクラスにまとめたりすることを考えてみましょう．""",
    },
    "R0916": {
        "priority": 2,
        "message": """
        論理式の項が多すぎます．論理式を短くしたり，分割することを考えてみましょう．""",
    },
    "R0912": {
        "priority": 2,
        "message": """
        条件分岐が多すぎます．条件式を見直したり，関数を分割したりすることを考えてみましょう．""",
    },
    "R1702": {
        "priority": 2,
        "message": """
        ネスト（if文やfor文などによる字下げ）が深すぎます．条件分岐を工夫したり，関数を分割したりすることを考えてみましょう．""",
    },
    "R0911": {
        "priority": 2,
        "message": """
        関数内のreturnが多すぎます．条件分岐を工夫したり，関数を分割したりすることを考えてみましょう．""",
    },
    "R0915": {
        "priority": 2,
        "message": """
        関数内の文が多すぎます．条件分岐を工夫したり，関数を分割したりすることを考えてみましょう．""",
    },
    "R1707": {
        "priority": 2,
        "message": """
        カッコなしタプルの末尾にカンマを残しています．バグの原因となるため，タプルは明示的にカッコで括ることが推奨されます．""",
    },
    "R1735": {
        "priority": 2,
        "message": r"""
        空の辞書を`dict()`により初期化しています．よりシンプルに`{}`を用いることができます．""",
    },
    "R1734": {
        "priority": 2,
        "message": """
        空のリストを`list()`により初期化しています．よりシンプルに`[]`を用いることができます""",
    },
    "R1711": {
        "priority": 2,
        "message": """
        無意味なreturnが存在します．関数が返す値が特にない場合，returnを記述する必要はありません．""",
    },
}
