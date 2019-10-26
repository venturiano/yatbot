import json
import requests


def send_text(bot_token, chat_id, text):
    """Send text message to a chat

    :param bot_token (string): the bot's api token
    :param chat_id (string): the receiver's chat id
    :param text (string): the text of the message

    :return: None
    """

    url = 'https://api.telegram.org/bot'+bot_token+'/sendMessage';
    files = {}
    data = {'chat_id' : chat_id, 'text' : text}
    r= requests.post(url, files=files, data=data)
    #print(r.status_code, r.reason, r.content)


def send_image(bot_token, chat_id, image_path, caption=None):
    """Send text message to a chat

    :param bot_token (string): the bot's api token
    :param chat_id (string): the receiver's chat id
    :param image_path (string): absolute path of image
    :param 

    :return: None
    """
    url = 'https://api.telegram.org/bot'+bot_token+'/sendPhoto';
    files = {'photo': open(image_path, 'rb')}
    data = {'chat_id' : chat_id}
    if caption:
        data['caption'] = caption
    r= requests.post(url, files=files, data=data)
    #print(r.status_code, r.reason, r.content)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def getUpdates(bot_api_token,offset=None):
    url = 'https://api.telegram.org/bot'+bot_api_token+'/getUpdates?timeout=100';
    if offset:
        url += '&offset='+str(offset)
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    if update_ids!=[]:
        return max(update_ids)
    else:
        return 0
