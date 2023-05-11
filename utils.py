import requests
from bs4 import BeautifulSoup
import json

def get_inline_keyboard():
    keyboard = [
        [{
            'text': "Все айфоны за сегодня", 
            'callback_data': '1'
        }],
         [{
            'text': "Новые айфоны", 
            'callback_data': '2'        
        }]
    ]

    return keyboard

def get_back_keyboard():
    keyboard = [
        [{
            'text': "Назад?", 
            'callback_data': 'Back'
        }],
    ]

    return keyboard

