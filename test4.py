# coding: UTF-8
 
# 書き込む文字列
str = "カシオペア"
 
f = open('text.txt', 'w') # 書き込みモードで開く
f.write(str) # 引数の文字列をファイルに書き込む
f.close() # ファイルを閉じる