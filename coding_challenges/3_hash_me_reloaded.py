from inspect import getfile
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

def string_to_chunks(str, n):
    chunks = [str[i:i+n] for i in range(0, len(str), n)]
    return chunks

def hash_me_reloaded():
    url_read = 'http://challenges.ringzer0team.com:10014/'
    message = get_message_from_url(url_read)

    # split message to chunks of 8
    chunks = string_to_chunks(message, 8)

    # convert each chunk to byte_array
    b_arr = bytearray(b'')
    for chunk in chunks:
        b_arr.append(int(chunk, 2))

    # hash 
    hash = hashlib.sha512(b_arr).hexdigest()

    url_send = 'http://challenges.ringzer0team.com:10014/?r=' + hash
    flag = get_flag_from_url(url_send)
    return flag

if __name__ == '__main__':
    print(hash_me_reloaded())