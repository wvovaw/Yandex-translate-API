from urllib.request import urlopen, Request
from urllib.parse import quote
import re

AUTHKEY = 'GIVE IT HERE: https://translate.yandex.com/developers/keys'
HOST = 'https://translate.yandex.net/api/v1.5/tr/translate'


def main():
    original_text = quote(input())
    target_lang = 'en'
    translated_text = translate(original_text, target_lang)
    print('====[Yandex Translate: to ' + target_lang + ']==================')
    print(translated_text)
    print('===============================================')


def translate(origin_text, target_lang):
    query = HOST + '?key=' + AUTHKEY + '&text=' + origin_text  + '&lang=' + target_lang + '&format=plain'
    try:
        request = Request(query)
    except:
        print('ERROR: Bad query: ' + query)
        return None
    try:
        response = urlopen(request)
    except:
        print('ERROR: Bad request')
        return None
    xml = response.read()
    response.close()
    xml = xml.decode('utf-8')
    match = re.compile('<text>(.*?)</text>').search(str(xml))
    if match:
        translated_text = match.group(1)
        return translated_text
    else:
        return None

if __name__ == "__main__":
    main()