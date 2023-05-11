import requests
from bs4 import BeautifulSoup
import json
from utils import get_inline_keyboard, get_back_keyboard
from env import *
import time
from today import get_all_today_iphones, get_last_iphones

arr = []
main_dict = {}

def get_updates():
    url = base_url+'getUpdates'
    getUp = requests.get(url).json()
    print(getUp)

    try:
        update = getUp['result'][-2]['update_id']
    except:
        return

    params = {
        'offset': update + 1
    }

    url = base_url+'getUpdates?'
    getUp = requests.get(url, params=params).json()

    try:
        if getUp['result'][0]['callback_query'] is not None:
            update = getUp['result'][0]  
    except:
        update = None


    try:
        start_keyboard()
    except:
        return
    
    try:
        if getUp['result'][0]['callback_query']['data'] == '1':
            get_all(update)
            start_keyboard()
        else:
            # getUp['result'][0]['callback_query']['data'] == '1':
            listen_iphones(update)
    except:
        return

    
    
def start_keyboard():
    # update = update['update_id']
    send_message_url = base_url+'sendMessage?'

    params = {
                        'chat_id':'5650732610',
                        'text': 'Начать поиск',
                        'reply_markup': json.dumps({
                        'inline_keyboard': get_inline_keyboard(),
                        # 'resize_keyboard': True 
        })
    }

    send_buttons = requests.get(send_message_url, params=params).json()

    
def get_all(update):
    print('work')
    print(update)

    iphones = get_all_today_iphones()

    try:

        for iphone in iphones:
            id_ = iphone['id']
            link = iphone['link']
            image = iphone['image']
            title = iphone['title']
            price = iphone['price']
            date = iphone['date']
        
            # update = update['update_id']
            send_message_url = base_url+'sendMessage?'

            params = {
                            'chat_id':'5650732610',
                            'text': f'{title}\n{link}\n{price}\nhttps://yams.kufar.by/api/v1/kufar-ads/images/88/{id_}.jpg\n{date}',
                        }
                
            send_items = requests.get(send_message_url, params=params).json()

            
    except:
        
        return
    

def listen_iphones(update):
    print('listen')

    last_iphones = get_last_iphones()

    try:

        for iphone in last_iphones:
            id_ = iphone['id']
            link = iphone['link']
            image = iphone['image']
            title = iphone['title']
            price = iphone['price']
            date = iphone['date']
        
            # update = update['update_id']
            send_message_url = base_url+'sendMessage?'

            params = {
                            'chat_id':'5650732610',
                            'text': f'{title}\n{link}\n{price}\nhttps://yams.kufar.by/api/v1/kufar-ads/images/88/{id_}.jpg\n{date}',
                        }
                
            send_items = requests.get(send_message_url, params=params).json()

            
    except:   
        return





def main():
    get_updates()

while True:
    if __name__ == '__main__':
        main()
        time.sleep(3)