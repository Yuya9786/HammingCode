# HammingCode for 4bits message

### 使い方
`$ python3 hamming_code.py [msg(0 <= msg < 16)]`

### 例（msg = 14）
```
python3 hamming_code.py 14                              
message: 14
↓ encode
encoded message: [1, 1, 1, 0, 0, 1, 0]
↓ transfer
recieved message: [1, 0, 1, 0, 0, 1, 0]
↓ decode s = [0, 1, 1]
decoded message: 14
```

### 説明
encode(): 
メッセージを7ビットのハミング符号に符号化する．
生成には生成行列Gを使用している．

decode():
メッセージと検査行列Hを用いてシンドロームsを計算し，複合化する．

transfer():
メッセージの転送の際のエラーをシミュレートする．一定の確率で7ビットのハミング符号のランダムな1ビットが入れ替わる．
