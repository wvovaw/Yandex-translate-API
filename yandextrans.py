from urllib.request import urlopen, Request
from urllib.parse import quote
import re

AUTHKEY = 'trnsl.1.1.20191202T210131Z.0efaaf74a79b747b.66acfde631d5a271bca8f55e333f0f42e668fdc7'
HOST = 'https://translate.yandex.net/api/v1.5/tr/translate'
lang = 'ru'
tranlate_to = 'en-ru'
text_format = 'plain'


def translate(text):
    query = HOST + '?key=' + AUTHKEY + '&text=' + text  + '&lang=' + lang + '&format=' + text_format
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
        print('==[Yandex Translate: ' + tranlate_to + ']====================')
        print(translated_text)
        print('===============================================')
        return translated_text
    else:
        return None


def main():
    original_text = quote(input())
    translated_text = translate(original_text)
    print(translated_text)


if __name__ == "__main__":
    main()