import pandas as pd
import glob, os, json
from os.path import exists


def check_ids():

    json_dir = 'files'

    json_pattern = os.path.join(json_dir, '*.json')
    file_list = glob.glob(json_pattern)

    iphone_ids = []
    for file in file_list:

        with open (file, 'r', encoding='utf-8') as f:
            iphones = json.load(f)

            for iphone in iphones["ads"]:
                iphone_ids.append(iphone['ad_id'])
    # print(iphone_ids)

    if not exists('iphone_ids.json'):

        with open ('iphone_ids.json', 'w', encoding='utf-8') as f:
            json.dump(iphone_ids, f, indent=4, ensure_ascii=False)

    else:

        with open ('new_iphone_ids.json', 'w', encoding='utf-8') as f:
            json.dump(iphone_ids, f, indent=4, ensure_ascii=False)

    # load json

    with open ('iphone_ids.json', 'r', encoding='utf-8') as f:
        iphones = json.load(f)


    with open ('new_iphone_ids.json', 'r', encoding='utf-8') as f:
        new_iphones = json.load(f)
        

    with open ('iphone_ids', 'w', encoding='utf-8') as f:
        json.dump(new_iphones, f, ensure_ascii=False, indent=4)

    # res = set(iphones).intersection(new_iphones)
    # print(res)

    r = [x for x in new_iphones if x not in iphones]

    print(r)

    with open ('find_iphones.json', 'w', encoding='utf-8') as f:
        json.dump(r,f, ensure_ascii=False, indent=4) 


# check_ids()