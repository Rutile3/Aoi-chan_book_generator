"""
url_pattern1 = "http://ncode.syosetu.com/n2634dg/"#小説家になろう
url_pattern2 = "https://syosetu.org/novel/114636/"#ハーメルン
"""

target_url = input()

if "ncode.syosetu.com" in target_url:
    print("小説家になろう")
elif "syosetu.org" in target_url:
    print("ハーメルン") 

url = target_url + str(1) + "/"
print(url)