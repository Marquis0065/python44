import urllib.request
#下载网页、文件、视频
# urllib.request.urlretrieve('http://www.baidu.com','baidu.html')
url_video = 'https://vd2.bdstatic.com/mda-kc1r7dfwd2rmv6j5/v1-cae/sc/mda-kc1r7dfwd2rmv6j5.mp4?v_from_s=hkapp-haokan-hna&auth_key=1667793096-0-0-0eebf108ff1d3a77e7e598d925db401e&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=1296074103&vid=15076718898606000219&abtest=104959_1&klogid=1296074103'
url = 'https://img0.baidu.com/it/u=3375911127,635571288&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=889'
urllib.request.urlretrieve(url_video,'eee.mp4')