import requests
import re
import json
import os

def craft(path,title,name):
    cmd = fr"ffmpeg -i {title}.mp4 -i {title}.mp3 -c copy -map 0:v:0 -map 1:a:0 {name}.mp4"
    os.system(cmd)
    os.remove(f"{title}.mp4")
    os.remove(f"{title}.mp3")

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
url = "https://www.bilibili.com/video/BV12dSfYVEac/"
video_url = "https://xy112x46x159x110xy.mcdn.bilivideo.cn:8082/v1/resource/26570523548-1-100143.m4s?agrr=1&build=0&buvid=E76C8913-BD3D-3212-3F66-EC53467860EF08459infoc&bvc=vod&bw=186014&deadline=1731920705&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv2&logo=A0020000&mcdnid=50012909&mid=330470790&nbs=1&nettype=0&og=cos&oi=1882394254&orderid=0%2C3&os=mcdn&platform=pc&sign=6e0e62&traceid=trqonRlArLVwHN_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform%2Cog&upsig=ff8a7ecc39990f25a26e0b3803ee7606"
audio_url = "https://xy115x56x242x26xy.mcdn.bilivideo.cn:8082/v1/resource/26570523548-1-30280.m4s?agrr=1&build=0&buvid=E76C8913-BD3D-3212-3F66-EC53467860EF08459infoc&bvc=vod&bw=25227&deadline=1731920705&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv2&logo=A0020000&mcdnid=50012909&mid=330470790&nbs=1&nettype=0&og=hw&oi=1882394254&orderid=0%2C3&os=mcdn&platform=pc&sign=592c8e&traceid=tryGxsfKIfCYfN_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform%2Cog&upsig=e0ef1a0fbe563c31fe966ce068af1463"

cookie = "buvid_fp_plain=undefined; header_theme_version=CLOSE; enable_web_push=DISABLE; DedeUserID=330470790; DedeUserID__ckMd5=d2a0b21a3196a7b8; FEED_LIVE_VERSION=V8; buvid4=DA4D3B36-9172-44EE-24C9-383313CA36DF16052-023071020-z9dbFvbIYFFDGvD%2Be2S1Qw%3D%3D; is-2022-channel=1; buvid3=E76C8913-BD3D-3212-3F66-EC53467860EF08459infoc; b_nut=1720540108; _uuid=B36F44BF-25DB-14B7-1068B-71063D3D61086E45118infoc; hit-dyn-v2=1; rpdid=|(J|)Y~~|JJ|0J'u~kJll~~~R; LIVE_BUVID=AUTO1517235652907577; fingerprint=8fd80b7f922a13877f694e8577d4d706; buvid_fp=8fd80b7f922a13877f694e8577d4d706; CURRENT_QUALITY=116; CURRENT_FNVAL=4048; SESSDATA=b24271bd%2C1747297977%2C267da%2Ab2CjD1ztxdHPW83RqCJw_A00-CNoBb0N9DHGsOz0pwj6xDXAqgfq9ZawIWIA5WMXZZC64SVlY3QW5qazI1b2JsYTlDem80UGFJM1Zpak5Nelh2MEZHRUdHTFpsbWphY1N0ZW9RUUI1aUVxSkpxOW9BdU5ENXFuTUh6ZHlkQnllV19ZOWN3YjRwT2t3IIEC; bili_jct=c09e731680c720017a02df0d7f436c6d; sid=5di1c10u; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzIwNzg1NDYsImlhdCI6MTczMTgxOTI4NiwicGx0IjotMX0.xyzDbydCzpdGjuM4bA3vno_ylUg8VIkojGmuShHhnOw; bili_ticket_expires=1732078486; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; home_feed_column=5; browser_resolution=1994-1060; PVID=2; bp_t_offset_330470790=1000993981472964608; bsource=search_bing; b_lsid=B1036DA57_1933E15FF5F"

headers = {
    "referer":"https://www.bilibili.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Cookie":cookie,
}

res = requests.get(url, headers=headers)
html = res.text
title = re.findall('title="(.*?)"', html)[0]
title = title.replace(' ','')
print(title)

info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
json_data = json.loads(info)
print(json_data)
video_url = json_data['data']['dash']['video'][0]['baseUrl']
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
print(video_url)
print(audio_url)

video_res = requests.get(video_url, headers=headers)
audio_res = requests.get(audio_url, headers=headers)

with open(title+'_.mp4', 'wb') as f:
    f.write(video_res.content)
with open(title+'_.mp3', 'wb') as f:
    f.write(audio_res.content)
res.encoding = 'utf-8'
with open('test.html', 'w', encoding='utf8') as f:
    f.write(res.text)
craft(current_dir,title+'_',title)
