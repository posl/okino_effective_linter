# eflint
Python初学者のコード改善のためのリンター．
初学者のエラー傾向を元にしたPylintの提案メッセージの追加と，lib2to3の機能を用いた提案コードへの変換機能を持つ．

## インストール
```
pip install git+https://github.com/posl/okino_effective_linter.git
```

## 実行例
```
eflint sample.py
```
標準入力から受け取る場合は，
```
echo print('Hello') | eflint --stdin
```

## 出力内容
現状，全ての出力はJSON形式で行われる．
|パラメータ名|内容|
|---|---|
|lineStart|検出部分の開始行|
|columnStart|検出部分の開始列|
|lineEnd|検出部分の終了行|
|columnEnd|検出部分の終了列|
|code|提案の識別子|
|message|提案メッセージ|
|severity|重要度*(1)|
|priority|優先度*(1)|
|source|検出を行ったツール名（現在はeflintのみ）|
|correctable|変換コードを提供しているか否か|
|docsUrl|提案内容のPylintドキュメントのURL|
|inlineFix|変換コードの内容．内容は下記|

inlineFix
|パラメータ名|内容|
|---|---|
|replacement|変換コード|
|start|変換部分の開始列（column）と開始行（line）|
|end|変換部分の終了列（column）と終了列（line）|


*(1): 重要度はPylintの分類（Error, Warning等）を元にして定義された値で，優先度は初学者への提案の優先度を分析結果を元に定義した値．

