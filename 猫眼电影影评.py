# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 16:54:32 2018

@author: jyz
"""

import json
import requests
import time
import random

#下载一页数据
def get_one_page(url):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None

#解析一页数据
def parse_one_page(html):
    data = json.loads(html)['cmts']
    for item in data:
        yield {
                'comment':item['content'],
                'date':item['time'].split(' ')[0],
                'rate':item['score'],
                'city':item['cityName'],
                'nickname':item['nickName']
                }
        
def save_to_txt():
    for i in range(1,1001):
        url = 'http://m.maoyan.com/mmdb/comments/movie/341516.json?_v_=yes&offset='+str(i)
        html = get_one_page(url)
        print('正在保存第%d页数据'%i)
        for item in parse_one_page(html):
            with open('狄仁杰影评.txt','a', encoding='utf-8') as f:
                f.write(item['date']+',' + item['nickname']+','+item['city']+','\
                +','+str(item['rate'])+','+item['comment']+'\n')
        time.sleep(5+float(random.randint(1,100))/20)

#获取的评论可能有重复，为了最终统计的真实性，需要做去重处理        
        
def delete_repeat(old, new):
    old_file = open(old,'r',encoding='utf-8')
    new_file = open(new, 'w', encoding='utf-8')
    content_list = old_file.readlines()#读取数据集
    content_already_distinct = []
    for line in content_list:
        if line not in content_already_distinct:
            new_file.write(line+'\n')
            content_already_distinct.append(line)
            

if __name__=='__main__':
    save_to_txt()
    delete_repeat(r'狄仁杰影评.txt','狄仁杰影评new.txt')
        