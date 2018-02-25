import requests
from bs4 import BeautifulSoup

while True:
    print("台本化するurlを入力してください。")
    target_url = input()
    if "syosetu.org" in target_url:     #ハーメルン
        selector_name = "honbun"
        url_end_str = ".html"
        break
    elif "syosetu.com" in target_url:   #小説家になろう
        selector_name = "novel_honbun"
        url_end_str = "/"
        break
    else:
        print("対応していないページです\n")

while True:
    try:
        print("話数を入力して下さい")
        story_number = int(input())
        break
    except ValueError:
        print("自然数を入力してください\n")

file = open("台本.txt", "w")
for i in range(1, story_number):
    print(str(i)+"話読み込み開始", end='    ')
    url = target_url + str(i) +  url_end_str           
    html = requests.get(url)                        #HTMLの取得
    soup = BeautifulSoup(html.content, "lxml")      #要素を抽出（texでなくcontent）
    text = soup.find("div", {"id": selector_name})  #台本にしたい部分を抽出（idとかを変えれるようにしたらほかのサイトでも使えそう）
    file.write(text.text)                           #引数の文字列をファイルに書き込む
    print(str(i)+"話読み込み終了")
file.close()

print("全て読み込みました")
print("何かキーを押すと終了します")
input()
