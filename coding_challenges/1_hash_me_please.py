import requests
import re
import hashlib

def get_message_from_url(url):
    text = requests.get(url).text
    text = re.split('----- BEGIN MESSAGE -----<br />\s+', text)[1]
    return re.split('<br />\s+----- END MESSAGE -----<br />', text)[0]

def get_flag_from_url(url):
    text = requests.get(url).text
    text = text.split('<div class="alert alert-info">')[1]
    return text.split('</div>')[0]

def hash_me_please():
    url_read = 'http://challenges.ringzer0team.com:10013/'
    message = get_message_from_url(url_read)

    # hashing
    hash = hashlib.sha512(message.encode('utf-8')).hexdigest()

    url_send = 'http://challenges.ringzer0team.com:10013/?r=' + hash
    flag = get_flag_from_url(url_send)
    return flag

if __name__ == '__main__':
    print(hash_me_please())