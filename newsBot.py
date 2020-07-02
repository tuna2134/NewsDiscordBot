from pygooglenews import GoogleNews
import json
import requests
import time


import config

url =  config.WEBHOOK_URL 

gn = GoogleNews('pt','BR')
gn.BASE_URL = gn.BASE_URL+"?hl={}&gl={}".format(gn.lang,gn.country)

top = gn.top_news()

for key, value in top.items():
    print(key)

top10 = top['entries'][:10]

for el in top10:
    data = {}  
    data["username"] = "News Bot"
    data["content"] = el.link
    result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
    time.sleep(5)






# news_link=top['entries'][1]
# print(len(top['entries']))

#print(news_link.title)
#print(news_link.url)
#print(news_link.link)

# url =  config.WEBHOOK_URL #"<your url>" #webhook url, from here: https://i.imgur.com/aT3AThK.png

# data = {}
# # #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
# data["content"] = news_link.link
# data["username"] = "News Bot"


# result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

# try:
#     result.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     print(err)
# else:
#     print("Payload delivered successfully, code {}.".format(result.status_code))
