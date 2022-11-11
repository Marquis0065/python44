import pkg_resources
import requests
from lxml import etree
header = {
    "cookie": "thw=xx; enc=0sUB1hLKhdD788maSPpmzT2cP0ZCsUE51len1gL4RH%2F%2F%2BIb6ctBmGOXA3S40SHjSN6FeG9k42NzTKVPtTqIAdA%3D%3D; cna=Bu/9GDLkbjYCATonWqTYOraI; lgc=fzh006591; tracknick=fzh006591; t=22496aabaff9b69c17cee1d550ae8a5d; useNativeIM=false; cookie2=1b3d887f4eb6695388532cdf59bc80d7; _tb_token_=ee1d0e3547365; _samesite_flag_=true; sgcookie=E10034n98dsyG3ooJ%2F0Nj22glFFTmrOAa9hPlfjpU23dbzFUfvdAUTuxh2pmIqMxFR7DUNJESdYKVFGDU16eiiv1RGOlnBMFVb6Ctl%2B5z47RZvkxJ2fJt%2F%2Fx%2F%2BwWIhJ%2BtGlY; unb=1796498309; uc3=nk2=BcpGEWvCWe8R&lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dCvjXgo3%2FzT3Uwa4Q%3D&id2=UoYXKpACTubCqw%3D%3D; csg=a6f30fc2; cancelledSubSites=empty; cookie17=UoYXKpACTubCqw%3D%3D; dnk=fzh006591; skt=168762f82f9a9cd0; existShop=MTY2ODEzNTE3Mw%3D%3D; uc4=nk4=0%40B0ZrTucqfFsgOn7wC1xyQUhODcA%3D&id4=0%40UO6eyxLgj6dXQAOLXx3%2B1Vj197On; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=194; _nk_=fzh006591; cookie1=AVBfkvm9OgX4OdxDgCK2L0e5sxr5hhuMU9xE5srjP4Y%3D; mt=ci=74_1; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _m_h5_tk=35c043e7c2cb9f5a85608a33da4c529b_1668153408876; _m_h5_tk_enc=79268835f5eae132812305265f35eab5; xlly_s=1; uc1=cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie15=URm48syIIVrSKA%3D%3D&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie14=UoeyBrrjbGvQNA%3D%3D&pas=0&existShop=false; JSESSIONID=9D15AE8E4975465F21C776AAE8CE292E; tfstk=cP3NBFgH9FLaQOlvey4qzcM9Dt4OZg3mPHPYjKqEFKsPiSEGi4BYtTCmLYCFnlf..; l=eBx_3A0Ijw93oO2BBOfZourza77OSIRviuPzaNbMiOCPO11p5pmdW6rCsZ89C3hVh6LkR3lps7xvBeYBqImBfdW22j-la_kmn; isg=BHd3GAhP2CPzf1-1uaqawJNyBmvBPEueVNf73ckkl8ateJe60Q3T7mxaW9gmuCMW"

}
url = 'https://s.taobao.com/search?q=%E4%B8%8A%E7%BD%91%E6%9C%AC&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306'
response = requests.get(url,headers=header)
print(response.status_code)
tree = etree.HTML(response.text)
print(tree)
result = tree.xpath('//strong/text()',encodings='utf8')
print(result)
