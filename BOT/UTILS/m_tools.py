import requests
import json


def get_search_reverse_image():
    params = {
        'api_key': 'CA4CD3500FE8469A9678E7D111EFC872',
        'engine': 'google',
        'search_type': 'reverse_image_search',
        'image_url': 'https://storage.yandexcloud.net/sol/FILES/IMAGES/p1.jpg',
        'hl': 'en',
        'time_period': 'last_year',
        'device': 'desktop',
        'sort_by': 'relevance',
        'page': '1',
        'max_page': '1',
        'output': 'json'
    }

    api_result = requests.get('https://api.serpwow.com/search', params)

    result = json.dumps(api_result.json())

    print(result)

    visual = result["visual_matches"][0]['link']

    print(visual)

    pagination = result["pagination"]["pages"][0]["other_pages"][0]["link"]

    print(pagination)


def get_search(query='sex'):
    params = {
        'api_key': 'CA4CD3500FE8469A9678E7D111EFC872',
        'engine': 'yandex',
        'q': query,
        'yandex_language': 'ru',
        'yandex_location': '1',
        'page': '1',
        'max_page': '1',
        'output': 'json'
    }

    # make the http GET request to SerpWow
    api_result = requests.get('https://api.serpwow.com/search', params)

    # print the JSON response from SerpWow
    return json.dumps(api_result.json())

get_search()
