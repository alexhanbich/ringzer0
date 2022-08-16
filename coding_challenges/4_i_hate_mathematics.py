import requests
import re

def get_message_from_url(url):
    text = requests.get(url).text
    text = re.split('----- BEGIN MESSAGE -----<br />\s+', text)[1]
    return re.split('<br />\s+----- END MESSAGE -----<br />', text)[0]

def get_flag_from_url(url):
    text = requests.get(url).text
    text = text.split('<div class="alert alert-info">')[1]
    return text.split('</div>')[0]

def i_hate_mathematics():
    url_read = 'http://challenges.ringzer0team.com:10032/'
    message = get_message_from_url(url_read)

    # split equation to diff parts
    res_list = message.split()
    a = int(res_list[0])
    b = int(res_list[2], 16)
    c = int(res_list[4], 2)
    # get value for equation
    num = a + b - c

    url_send = 'http://challenges.ringzer0team.com:10032/?r=' + str(num)
    flag = get_flag_from_url(url_send)
    return flag

if __name__ == '__main__':
    print(i_hate_mathematics())