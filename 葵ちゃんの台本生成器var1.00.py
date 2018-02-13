import requests
from bs4 import BeautifulSoup

print("台本化するurlを入力してください。")
target_url = input()
print("話数を入力して下さい")
story_number = int(input())

file = open("台本.txt", "w") # 書き込みモードで開く
i = 1
while i<=story_number:#for i in range(story_number):#forでやるとなぜか上手くいかない
    print(str(i)+"話読み込み開始", end='    ')
    url = target_url + str(i) + "/"             
    html = requests.get(url)                        #HTMLの取得
    soup = BeautifulSoup(html.content, "lxml")      #要素を抽出（texでなくcontent）
    text = soup.find("div", {"id": "novel_honbun"}) #台本にしたい部分を抽出（idとかを変えれるようにしたらほかのサイトでも使えそう）
    file.write(text.text)                           #引数の文字列をファイルに書き込む
    print(str(i)+"話読み込み終了")
    i += 1
file.close()

print("全て読み込みました")
print("何かキーを押すと終了します")
input()
