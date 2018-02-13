import requests
from bs4 import BeautifulSoup

print("台本化するurlを入力してください。")
#target_url = input()
target_url = "http://ncode.syosetu.com/n2634dg/1/"#デバッグ用

print("話数を入力して下さい")
#story_number = int(input())
story_number = 238#デバッグ用


html = requests.get(target_url)             #HTMLの取得
soup = BeautifulSoup(html.content, 'lxml')  #要素を抽出（texでなくcontent）
text = soup.find("div", {"id": "novel_honbun"})
print(text.text)

f = open("台本.txt", 'w') # 書き込みモードで開く
f.write(text.text) # 引数の文字列をファイルに書き込む
f.close() # ファイルを閉じる