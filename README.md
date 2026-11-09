## 概要
Recurtion (https://recursionist.io/) のカリキュラムが変更されたため、再度自分でFile Manipulator Programを作ってみました。<br>
前回作ったものはこちら: https://github.com/HikaruCS/File_Manipulator_Program

## コマンド
このプログラムには、以下の4つのコマンドを打つことで、ファイル操作を行うことができます。<br>
1: reverse — 中身を逆順にして書き出す<br>
書き方:
```
python3 file_manipulator.py reverse <inputpath> <outputpath>
```
具体例:
```
$ python3 file_manipulator.py reverse hello.txt reversed.txt
$ cat reversed.txt
dlroW olleH
```
2: copy — ファイルを複製する<br>
書き方:
```
python3 file_manipulator.py copy <inputpath> <outputpath>
```
具体例:
```
$ python3 file_manipulator.py copy hello.txt copied.txt
$ cat copied.txt
Hello World
```
3: duplicate-contents — 中身を n 回繰り返す<br>
書き方:
```
python3 file_manipulator.py duplicate-contents <inputpath> <n>
```
具体例:
```
$ python3 file_manipulator.py duplicate-contents hello.txt 3
$ cat hello.txt
Hello WorldHello WorldHello World
```
4: replace-string — 文字列を一括置換する (inputpath中のneedleをすべてnewstringに置き換える)<br>
書き方:
```
python3 file_manipulator.py replace-string <inputpath> <needle> <newstring>
```
具体例:
```
$ python3 file_manipulator.py replace-string copied.txt World Python
$ cat copied.txt
Hello Python
```

## 注意
- 今回はストレッチ課題をスキップしています。なので、不正な入力をした場合にはプログラムが突然止まる場合があります。

## もし今後改善版を作る場合...
- コード内に重複箇所がいくつかあるので、それを一つにまとめたい。
- バリデーションを含むストレッチ課題を実装する。