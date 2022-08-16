import itertools
import requests
import re
import hashlib

def get_hash_from_url(url):
    text = requests.get(url).text
    text = re.split('----- BEGIN HASH -----<br />\s+', text)[1]
    return re.split('<br />\s+----- END HASH -----<br />', text)[0]

def get_salt_from_url(url):
    text = requests.get(url).text
    text = re.split('----- BEGIN SALT -----<br />\s+', text)[1]
    return re.split('<br />\s+----- END SALT -----<br />', text)[0]

def get_flag_from_url(url):
    text = requests.get(url).text
    text = text.split('<div class="alert alert-info">')[1]
    return text.split('</div>')[0]

def hash_breaker():
    url = 'http://challenges.ringzer0team.com:10057/'
    hash = get_hash_from_url(url)
    salt = get_salt_from_url(url)
    print(hash)
    print(salt)
    # len(hash) == 40, so most likely a sha-1 hash
    # online decrypt shows that the message is a digit
    for i in itertools.count(0):
        print(hash)
        print(hashlib.sha1(str(i).encode('utf-8')+salt.encode('utf-8')).hexdigest())
        if hash == hashlib.sha1(str(i).encode('utf-8')+salt.encode('utf-8')).hexdigest():
            break
    message = str(i)
    url_send = 'http://challenges.ringzer0team.com:10056/?r=' + message
    flag = get_flag_from_url(url_send)
    return flag



if __name__ == '__main__':
    print(hash_breaker())