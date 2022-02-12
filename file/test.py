import requests

API_LINK = "https://api.telegram.org/bot5167627424:AAFGOxsZa3YH4egdKF2FjDBsrsbh37rhqRs"

updates = requests.get(API_LINK + "/getUpdates?offset=-1").json()

print(updates)

#get a meassage
message = updates['result'][0]['message']
chat_id = message['from']['id']
text = message['text']

sent_message = requests.get(API_LINK + f'/sendMessage?chat_id={chat_id}&text= Мой id {chat_id}')