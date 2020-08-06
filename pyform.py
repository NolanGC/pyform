import time
import re
import requests
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_fields(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    time.sleep(3)
    page = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser').prettify()
    regex = r'entry\.(\d+)'
    fields = re.findall(regex, soup)
    return fields

def submit_form(url, answers):
    fields = get_fields(url)
    submission_url = url.replace('viewform', 'formResponse')
    assert len(fields) == len(answers)
    data = {}
    for i, key in enumerate(fields):
        data['entry.'+key] = answers[i]
    print(data)
    headers = {'Referer':url,
                  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    response = requests.post(submission_url, data=data, headers=headers)
    print(response.status_code, response.reason)

#url = 'https://docs.google.com/forms/d/e/1FAIpQLSdBjsuWd9fT2TH3rZkx_6JLGW1xJpQLj7tppIRPZkj_fYIhAg/viewform?usp=sf_link'
url = 'https://docs.google.com/forms/d/1_rl64smzPM8PHtT7igIj9BwwfHnZbloCCO41OHFoUdY/viewform'
answers = ['nolangclement@gmail.com', 600021071, 'short?', 'Period 3', '12']

#submit_form(url, answers)
#https://docs.google.com/forms/d/e/1FAIpQLSceOjZeNhdQcQSdniYnzax0Q-_no8xrjG18ldWqvLlCpcg 
#https://docs.google.com/forms/d/e/1FAIpQLSdBjsuWd9fT2TH3rZkx_6JLGW1xJpQLj7tppIRPZkj_fYIhAg/viewform?usp=pp_url&entry.1924755413=naAWRpjo@gmail.com&entry.1856435140=Period+2&entry.1040897682=3125123&entry.2142083317=123897&entry.1249098924=123
print(get_questions(url))