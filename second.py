import requests
from bs4 import BeautifulSoup
import fake_useragent
import time
import json
from datetime import datetime
from itertools import count

class Func():
    def __init__(self):
        self.c = 0
    def __call__(self):
        self.c += 1
        return self.c  
counter = Func()

def get_links(text):
    
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url=f"https://hh.ru/search/vacancy?text={text}&salary=&area=1&ored_clusters=true&enable_snippets=true&page=1",
        headers={"user-agent":ua.random}
    )
    if data.status_code != 200:
        return
    soup = BeautifulSoup(data.content,"lxml")
    try:
        page_count = int(soup.find("div",attrs={"class":"pager"}).find_all("span",recursive=False)[-1].find("a").find("span").text)
    except:
        return
    for page in range(page_count):
        try:
            data = requests.get(
                url=f"https://hh.ru/search/vacancy?text={text}&salary=&area=1&ored_clusters=true&enable_snippets=true&page={page}",
                headers={"user-agent":ua.random}
            )
            if data.status_code != 200:
                continue
            soup = BeautifulSoup(data.content, "lxml")
            for a in soup.find_all("a",attrs={"class":"serp-item__title"}):
                yield f"{a.attrs['href'].split('?')[0]}"
        except Exception as e:
            print(f"{e}")
            time.sleep(1)
def get_vacancy(link):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url = link, 
        headers={"user-agent":ua.random}
    )
    if data.status_code !=200:
        return
    soup = BeautifulSoup(data.content,"lxml")
    try:
        name = soup.find(attrs={"class":"vacancy-title"}).text.replace("з/п не указана","")
    except:
            name = ""
    try:
        url = link
    except:
            link = ""
    try:
        tags = [tag.text for tag in soup.find(attrs={"class":"bloko-tag-list"}).find_all(attrs={"class":"bloko-tag__section_text"})]
    except:
            tags = []
    try:
        time = str(datetime.now())
    except:
            time = ""
    try:
        count = counter()
    except:
            count = ""        

    resume = {
        "count":count,
        "name":name,
        "time":time,
        "url":url,
        "tags":tags
     }
    return resume

if __name__ == "__main__":

    data = []
    for a in get_links("Специалист по технической защите информации"):
        data.append(get_vacancy(a))
        time.sleep(0.001)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data,f,indent=4,ensure_ascii = False)
    

    # for a in get_links("python"):
    #     print(a)
    # for a in get_links("python"):
    #     print(get_resume(a))
    #     time.sleep(1)