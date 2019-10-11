# 取扱説明書

1.python 3.7.4をインストール
- やり方はググるとでてくる
- pathを通すのを忘れないこと！！！！！！

2.ターミナル(windowsならコマンドプロンプト)で

```
pip install pytz
```

と入力し、datatimeライブラリを入れる

3.走るときにターミナルに

```
python run.py
```

と入力し、以下ファン数をどんどん入力

例)

```
200
170
230
230
・
・
・
```

4.最後に0を入力すると時間、ファン数、平均獲得ファン数などが「status.txtに出力されます！！」

注)60秒以上実行しないと

```
Traceback (most recent call last):
  File "run.py", line 33, in <module>
    zisoku = (total // minute) * 60
ZeroDivisionError: integer division or modulo by zero
```

多分こんな感じのエラー出ると思うのでテストの際は1分以上図ってから入力するとよさそうです
