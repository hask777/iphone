import requests
import json
from bs4 import BeautifulSoup as bs
from sqlalchemy.orm import Session
from models import Phone
from database import engine


import pandas as pd
import glob, os, json


json_dir = 'files'

json_pattern = os.path.join(json_dir, '*.json')
file_list = glob.glob(json_pattern)

# print(file_list)

for file in file_list:

    # print(file)

    with open (file, 'r', encoding='utf-8') as f:
        iphones = json.load(f)

        # print(iphones)

        for iphone in iphones["ads"]:

            with Session(engine) as session:

                try:
                    iphone = Phone(
                        add_id=iphone['ad_id'],
                        add_link=iphone['ad_link'],
                        title=iphone['subject'],
                        image=iphone['images'][0]['id'],
                        price=iphone['price_byn'],
                    )
                except:
                    continue
                            

            session.add_all([iphone])
            session.commit()



# for file in file_list:
#     # print(file)
#     dfs = []
#     for file in file_list:
#         with open(file, 'r', encoding='utf-8') as f:
#             json_data = pd.json_normalize(json.loads(f.read()))
#             json_data['site'] = file.rsplit("/", 1)[-1]
#         dfs.append(json_data)
#     df = pd.concat(dfs)
#     df.reset_index(drop=True, inplace=True)
#     total = df.to_json('totals.json')

#     with open ('totals.json', 'r', encoding='utf-8') as f:
#         iphones = json.load(f)

#     with open ('iphones.json', 'w', encoding='utf-8') as f:
#         phones = json.dump(iphones['ads'], f, indent=4, ensure_ascii=False)

#     with open ('iphones.json', 'r', encoding='utf-8') as f:
#         phones = json.load(f)

#         # print(phones["0"])

#         # with Session(engine) as session:

#         for iphone in phones:
#             for item in iphone:
#                 print(item)
                # try:
                #     phone = Phone(
                #         add_id=iphone['ad_id'],
                #         add_link=iphone['ad_link'],
                #         title=iphone['subject'],
                #         price=iphone['price_byn'],
                #     )
                # except:
                #     continue
                    

                # session.add_all([phone])
                # session.commit()



