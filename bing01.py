from urllib.request import urlopen
import urllib.parse
import urllib.request
import requests,  re
from lxml import etree

'''
html = requests.get('https://bing.ioliu.cn/?p=2')
print(html.text)
#print(type(html.text))
#print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
item = re.findall(r'<div class="description"><h3>(.*?)<\/h3>',str(html.text))

print(item)
'''

def get_one_page(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        print(type(response))
        img(response)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def img(response):
    regx = r'src[\S]*\.jpg'
    print(response.text)
    pattern = re.compile(regx)
    get_img = re.findall(pattern, repr(response))
    num = 1
    for img in get_img:
        with open('%s.jpg' %num,'wb') as fp:
            print('\n进入图片下载模块\n')
            fp.write(image)
            num +=1
            print('正在下载第%s张图片'%num)
    return

#拉取图片的文字故事
def parse_one_page(html):
    item = re.findall(r'<div class="description"><h3>(.*?)<\/h3>', html)
    return item

def main():
    url = 'https://bing.ioliu.cn/'
    html = get_one_page(url)
    parse_one_page(html)
'''以下为打印模块
    for item1 in parse_one_page(html):
        print(item1)
'''

main()
