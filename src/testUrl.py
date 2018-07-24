#获取CSDN博客中的排名并自动邮件通知
from time import sleep
import requests
from bs4 import BeautifulSoup

def get_nums(blogs_des):
    split_str = blogs_des.split('-')[1].strip()
    return split_str


def get_blog_ranks(url):
    # url = self.url_fmt %(self.id,self.id)
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    fangwenList = soup.select("dd[title]")
    fangwen = fangwenList[0].text
    return fangwen
    # lis = soup.findAll('div')
    #
    # for item in lis:
    #     if 'sidebar_scorerank' == item.get('id'):
    #         li_lists = item.findAll('li')
    #
    #         for li_item in li_lists:
    #             if u'积分' in li_item.text:
    #                 self.score = get_nums(li_item.text)
    #             elif u'排名' in li_item.text:
    #                 self.rank = get_nums(li_item.text)
    #             else:
    #                 print('Error')
    #     continue

print(get_blog_ranks("https://blog.csdn.net/tianjing222"))


def __init__(self,id):
    self.gap_seconds = 60*30

def monitor_score_rank(self):
    while True:
        self.get_blog_ranks()
        if self.score != self.his_score:
            print("排名发生变化了")

        sleep(self.gap_seconds)