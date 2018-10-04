#!user/bin/python
# -*- coding: utf-8 -*-
# Author: mr tang
# Date:   2018-10-04 23:56:20
# Contact: mrtang@nudt.edu.cn 
# Github: trzp
# Last Modified by:   mr tang
# Last Modified time: 2018-10-05 01:32:13

# 该脚本用于抓取长沙各大经销商的起亚K5报价

import urllib
import re
import time
from msvcrt import getch
import datetime

def get_html(url):
    page = urllib.urlopen(url)
    return page.read()

def get_price(url):
    dealer = re.compile(r'<div class="text-main">.*</div>')  #匹配经销商名称字符串
    price = re.compile(r'<span class="price">.*?</span></p>') #匹配价格字符串
    price_v = re.compile(r'[0-9]{1,2}\.{0,1}[0-9]{0,2}') #匹配字符串中的数字

    dealer_str = dealer.findall(get_html(url))[0]
    ind0 = dealer_str.find('</div>')
    dealer_name = dealer_str[23:ind0]

    price_str = price.findall(get_html(url))[0]
    price_num = price_v.findall(price_str)[0]

    return dealer_name,price_num

def main():
    url = ['https://dealer.autohome.com.cn/7266/spec_24058.html?siteid=117#pvareaid=103872',
          'https://dealer.autohome.com.cn/2078448/spec_24058.html?siteid=117#pvareaid=103872',
          'https://dealer.autohome.com.cn/81811/spec_24058.html?siteid=117#pvareaid=103872',
          'https://dealer.autohome.com.cn/2019452/spec_24058.html?siteid=117#pvareaid=103872']

    file = open('price.log','r')
    content = file.read()
    file.close()
    date_r = re.compile(r'date:[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}')
    latest_date = date_r.findall(content)[-1][5:]   #从文件中读取最近的日期
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')

    if latest_date == date_str: return

    file = open('price.log','a')
    print u'今日K5报价'
    file.write('date:%s\n'%date_str)
    for u in url:
        nm,p = get_price(u)
        ps = nm+u': '+p+u'万'
        print ps
        file.write(ps+'\n')
    file.close()

    print ''
    print u'任意键结束'
    getch()


if __name__ == '__main__':
    main()