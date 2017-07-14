#coding:utf-8
import requests
import re
from lxml import etree

headers = {
    'connection': "keep-alive",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'referer':'http://uems.sysu.edu.cn/jwxt/',
    'cache-control': "no-cache"
}
session=requests.session()

def get_youku(url,session):
    response=session.get(url,headers=headers)
    html=response.content.decode('utf-8','ignore')
    video_url=selector.xpath("//input[@id='link2' and @class='form_input form_input_s']/@value")
    print video_url
    


def get_iqiyi(url,session):
    response=session.get(url,headers=headers)
    html=response.content.decode('utf-8','ignore')
    param=dict(re.findall("param\['(\w+)'\] = \"(\w*)\"",html))
    id=re.search('/([\w_]+)\.html',url).group(1)
    video_url="http://player.video.qiyi.com/%s/0/0/%s.swf-albumId=%s-tvId=%s-isPurchase=0-cnId=%s"%(param['vid'],id,param['albumId'],param['tvid'],param['channelID'])
    return video_url

def get_qq(url,session):
    response=session.get(url,headers=headers)
    html=response.content.decode('utf-8','ignore')
    vid=re.search('\"vid\":\"(\w+)\"',html).group(1)
    video_url="https://imgcache.qq.com/tencentvideo_v1/playerv3/TPout.swf?max_age=86400&v=20161117&vid=%s&auto=0"%vid
    return video_url    
    
def get_sohu(url,session):#edge 搜pub_catecode
    response=session.get(url,headers=headers)
    html=response.content.decode('utf-8','ignore')
    param=dict(re.findall('var (\w+)=\"(\d*)\";',html))
    if param['osubcid']=='':
        param['osubcid']=0
    video_url="http://share.vrs.sohu.com/%s/v.swf&topBar=1&autoplay=false&plid=%s&pub_catecode=%s&from=page"%(param['vid'],param['playlistId'],param['osubcid'])
    return video_url 
#get_youku('http://v.youku.com/v_show/id_XMjg3MDYwNzg1Ng==.html',session)
#print get_iqiyi('http://www.iqiyi.com/v_19rr700mq0.html',session)
#print get_qq('https://v.qq.com/x/cover/dhzimk1qzznf301/z0024iqj5u3.html',session)
print get_sohu('http://tv.sohu.com/20160706/n457968543.shtml?fid=65&pvid=4d4db6d26aa0a4ec',session)