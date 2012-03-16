# -*- coding: UTF-8 -*-

import datetime
import urllib
# import webbrowser

# webbrowser.open("http://whois.ename.net/dingdongquan.com", 0)
# webbrowser.open("mailto:chatme@263.net")

urls = [
        #'http://www.dingdongquan.com', \
        #'http://www.dingdongquan.com/pregnant', 'http://www.dingdongquan.com/baby', \
        #'http://www.dingdongquan.com/young', 'http://www.dingdongquan.com/children', \
        #'http://www.dingdongquan.com/diet', 'http://www.dingdongquan.com/mall', \
        #'http://www.dingdongquan.com/she-he', 'http://www.dingdongquan.com/health', \
        #'http://www.dingdongquan.com/elder', 'http://www.dingdongquan.com/fashion', \
        'http://whois.ename.net/dingdongquan.com', 'http://www.myip.cn/dingdongquan.com', \

        #'http://www.ouds.biz', 'http://www.gaiding.com', \
        'http://whois.ename.net/gaiding.com', 'http://www.myip.cn/gaiding.com', \
        'http://whois.ename.net/ouds.biz', 'http://www.myip.cn/ouds.biz', \

        #'http://www.ThinkerUnion.com', 'http://www.mmxxt.com', \
        'http://whois.ename.net/ThinkerUnion.com', 'http://www.myip.cn/ThinkerUnion.com', \
        'http://whois.ename.net/mmxxt.com', 'http://www.myip.cn/mmxxt.com', \

        #'http://www.ThinkerUnion.net', 'http://www.ThinkerUnion.org', \
        'http://whois.ename.net/ThinkerUnion.net', 'http://www.myip.cn/ThinkerUnion.net', \
        'http://whois.ename.net/ThinkerUnion.org', 'http://www.myip.cn/ThinkerUnion.org', \

        #'http://www.Ganzu.com', 'http://www.Ouds.cn', \
        'http://whois.ename.net/Ganzu.com', 'http://www.myip.cn/Ganzu.com', \
        'http://whois.ename.net/Ouds.cn', 'http://www.myip.cn/Ouds.cn', \

        #'http://www.SimpleLang.org', 'http://www.Simple-Lang.org', \
        'http://whois.ename.net/SimpleLang.org', 'http://www.myip.cn/SimpleLang.org', \
        'http://whois.ename.net/Simple-Lang.org', 'http://www.myip.cn/Simple-Lang.org', \

        #'http://www.Simple-Lang.com', 'http://www.Simple-Language.com', \
        'http://whois.ename.net/Simple-Lang.com', 'http://www.myip.cn/Simple-Lang.com', \
        'http://whois.ename.net/Simple-Language.com', 'http://www.myip.cn/Simple-Language.com', \

        #'http://www.Simple-Language.org', 'http://www.Ouds.net', \
        'http://whois.ename.net/Simple-Language.org', 'http://www.myip.cn/Simple-Language.org', \
        'http://whois.ename.net/Ouds.net', 'http://www.myip.cn/Ouds.net', \

        #'http://www.Ouds.us', 'http://www.Ouds.me', \
        'http://whois.ename.net/Ouds.us', 'http://www.myip.cn/Ouds.us', \
        'http://whois.ename.net/Ouds.me', 'http://www.myip.cn/Ouds.me', \
        
        #'http://www.LoSpring.com', 'http://www.Thinker.cc', \
        'http://whois.ename.net/LoSpring.com', 'http://www.myip.cn/LoSpring.com', \
        'http://whois.ename.net/Thinker.cc', 'http://www.myip.cn/Thinker.cc'
        ]

for url in urls:
    page_url = urllib.urlopen(url)
    page_html = page_url.read()
    page_url.close()
    
    domain = url.replace('/', '_').split('.')
    f = file('E:/spider/' + \
             domain[1] + '_' + domain[2] + '_' + \
             str(datetime.datetime.now().month) + '_' + \
             str(datetime.datetime.now().day) + '_' + \
             str(datetime.datetime.now().hour) + '_' + \
             str(datetime.datetime.now().minute) + '_' + \
             str(datetime.datetime.now().second) + '_' + \
             str(datetime.datetime.now().microsecond) + \
             '.html', 'w')
    f.write(page_html)
    f.close()
    
    print str(urls.index(url) + 1) + '.', url + ' -----> has completed !'
    


