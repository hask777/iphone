import json
import glob
import os
from datetime import date, datetime
import re
from os.path import exists

today = date.today()

def listen_today_iphones():
    global today 

    today_iphone_list = []

    json_dir = 'files'

    json_pattern = os.path.join(json_dir, '*.json')
    file_list = glob.glob(json_pattern)

    # today_iphones_dict = {}


    for file in file_list:

        with open (file, 'r', encoding='utf-8') as f:
            iphones = json.load(f)
            ip_date = re.compile(r"(\d{4}-\d{2}-\d{2}(?=[^0-9]))")

            for iphone in iphones["ads"]:

                date = iphone['list_time']
                new_date = ip_date.search(date)
                new_date = new_date.group(0)

                if new_date == str(today):

                    try:
                        today_iphones_dict = dict(
                            id = iphone['ad_id'],
                            link = iphone['ad_link'],
                            image = iphone['images'][0]['id'],
                            title = iphone['subject'],
                            price = iphone['price_byn'],
                            date = iphone['list_time']
                        )
                    except:
                        continue

                    today_iphone_list.append(today_iphones_dict)

    # print(today_iphone_list)

    if not exists('old_today_iphones.json'):

        with open('old_today_iphones.json', 'w', encoding='utf-8') as f:
            json.dump(today_iphone_list, f, ensure_ascii=False, indent=4)
    else:

        with open('new_today_iphones.json', 'w', encoding='utf-8') as f:
            json.dump(today_iphone_list, f, ensure_ascii=False, indent=4)


      # load json

        with open ('old_today_iphones.json', 'r', encoding='utf-8') as f:
            today_iphones = json.load(f)

        today_iphones_ids = []
        for ip in today_iphones:
            today_iphones_ids.append(ip['id'])

        
        with open ('new_today_iphones.json', 'r', encoding='utf-8') as f:
            new_today_iphones = json.load(f)

        new_today_iphones_ids = []
        for ip in new_today_iphones:
            new_today_iphones_ids.append(ip['id'])

        # Check

        r = [x for x in new_today_iphones if x not in today_iphones]

        if len(r) > 0:
            for iph in r:
                print(iph)
            
            with open ('find_today_iphones.json', 'w', encoding='utf-8') as f:
                 json.dump(r, f, ensure_ascii=False, indent=4)
               
        else:
            print("No new iphones")

        with open('old_today_iphones.json', 'w', encoding='utf-8') as f:
            json.dump(new_today_iphones, f, ensure_ascii=False, indent=4)


        # print("New Iphone")
        

# check_today_iphones()

def get_all_today_iphones():
    
    with open ('new_today_iphones.json', 'r', encoding='utf-8') as f:
        new_today_iphones = json.load(f)

    return new_today_iphones

def get_last_iphones():

    with open ('find_today_iphones.json', 'r', encoding='utf-8') as f:
        last_iphones = json.load(f)

    return last_iphones
