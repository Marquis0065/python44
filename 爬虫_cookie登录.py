import urllib.request
import urllib.parse
import urllib.error
url = 'https://mail.sohu.com/fe/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'Cookie': 'gidinf=x099980109ee134259577ec70000d777cc8a0728cdb0; SUV=2104292204552OXB; IPLOC=CN4406; cityIpLocation=124.240.85.101; __bid_n=18447747de53f877fb4207; clt=1667811414; cld=20221107165654; reqtype=pc; a=123; t=1667811462195; jv=8276bff5592e33936d5f06b0133e7eb6-fwd7FX2W1667811427723; ppinf=2|1667811428|1669021028|bG9naW5pZDowOnx1c2VyaWQ6MTg6ZnpoMDA2NTkxQHNvaHUuY29tfHNlcnZpY2V1c2U6MzA6MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwfGNydDoxMDoyMDIyLTExLTA3fGVtdDoxOjB8YXBwaWQ6NjoxMDEzMDV8dHJ1c3Q6MToxfHBhcnRuZXJpZDoxOjB8cmVsYXRpb246MDp8dXVpZDo5OnUxOTgyMjUxMHx1aWQ6OTp1MTk4MjI1MTB8dW5pcW5hbWU6MDp8; pprdig=wrCA2OsFFPlJKt46PwlNP6TlD-ZdAj1KjomwrLQPDuAJYElIHxgq0kEIPfuf6xSZIWu1SeETQhOijYJEZt-0gujQ5r7UxF_NAzPE2L7K6KZbF6SUZaIZurByrVGr_zSWC-FU-a8keXSk_tRzguT9S2RioRTuHy4zwKwyIiFvSVg; ppmdig=166781142800000042548edf759bdfeaf4538d6934e5e876; mailinfo=fzh006591@sohu.com:fzh006591@sohu.com:ae541a0dd8390274de122a42db099b65; lt_ui=DofCrt4XxkvH+PeNVb11vEvq3KPtqTlQ4r2U4De4HNKyGo76aZT8rPLORd2otCI45jZ81TiohWy6qGBEzXGRbadhCuRrgera5CuPqqvn8MMMhrWTyKL5OX9JQV+cx7Q1k6308xpVnFVlNZxDRNBxPyl7ZcF/pWnNxqeZJg9W7hsNlTKBNXQjLEziLAxUAzQZDlrtfCZXePLoXep7ZsIvCktdtEfr0wOtG/hg5n26Lkg='
}
request = urllib.request.Request(url= url ,headers=header)
response = urllib.request.urlopen(request)
content = response.read().decode('utf8')
print(content)
with open('sohu.html','w',encoding='utf8') as fp:
    fp.write(content)