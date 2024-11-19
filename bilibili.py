import requests
import re
import json
import os

def craft(title,name):
    cmd = fr"ffmpeg -i {title}.mp4 -i {title}.mp3 -c copy -map 0:v:0 -map 1:a:0 {name}.mp4"
    os.system(cmd)
    os.remove(f"{title}.mp4")
    os.remove(f"{title}.mp3")

def get_video(title,html,headers):
    info_getvideo = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
    json_data_getvideo = json.loads(info_getvideo)
    video_url = json_data_getvideo['data']['dash']['video'][0]['baseUrl']
    audio_url = json_data_getvideo['data']['dash']['audio'][0]['baseUrl']
    video_res = requests.get(video_url, headers=headers)
    audio_res = requests.get(audio_url, headers=headers)
    with open(title + '_.mp4', 'wb') as f:
        f.write(video_res.content)
    with open(title + '_.mp3', 'wb') as f:
        f.write(audio_res.content)

def get_intro(html):
    info_getintro = re.findall("window.__INITIAL_STATE__=(.*?);\(function", html)[0]
    json_data_getintro = json.loads(info_getintro)
    with open('info_getintro.json', 'w', encoding='utf-8') as f:
        json.dump(json_data_getintro, f, ensure_ascii=False)
    author = json_data_getintro['videoData']['owner']['name']
    text = json_data_getintro['videoData']['desc']

    with open("introduce.txt", "w", encoding='utf-8') as f:
        f.write(f"标题：{title}\n作者：{author}\n简介：{text}")


url = "https://www.bilibili.com/video/BV1yUSEYdEc9/"
cookie = ""

headers = {
    "referer":"https://www.bilibili.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "Cookie":cookie,
}

res = requests.get(url, headers=headers)
html = res.text
title = re.findall('title="(.*?)"', html)[0]
title = title.replace(' ', '')

res.encoding = 'utf-8'
with open('test.html', 'w', encoding='utf8') as f:
    f.write(res.text)
get_video(title,html,headers)
craft(title+'_',title)
get_intro(html)
