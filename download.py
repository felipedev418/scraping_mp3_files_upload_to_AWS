import time
import os
import requests
from DrissionPage import ChromiumPage, ChromiumOptions
import sys

API_KEY = 'defb6b2014788f056e07360864c2bbf5'
SITE_KEY = '6LdGXiUTAAAAAE7dvTaYFXusCmXMP4re9HKIztYj'
PAGE_URL = 'https://app.inquirly.com/new_admin/adminpage.php'

def solve_captcha(site_key, page_url, api_key):
    url = "http://2captcha.com/in.php"
    params = {
        'key': api_key,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': page_url,
        'json': 1
    }

    response = requests.post(url, params=params)
    result = response.json()

    if result['status'] == 1:
        captcha_id = result['request']

        while True:
            time.sleep(5)
            result = requests.get(f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}&json=1").json()
            if result['status'] == 1:
                return result['request']
            elif result['request'] != 'CAPCHA_NOT_READY':
                raise Exception(f"Error solving captcha: {result['request']}")
    else:
        raise Exception(f"Error submitting captcha: {result['request']}")

def signin(page, download_url):
    if page.ele("xpath://input[@id='userID']"):
        page.ele("xpath://input[@id='userID']").input("majeem")
        time.sleep(1)
        print(1)
        page.ele("xpath://input[@id='userPsswd']").input("kfgr),D*_W41Ql")
        print(2)
        captcha_solution = solve_captcha(SITE_KEY, PAGE_URL, API_KEY)
        print(f"Captcha solution: {captcha_solution}")
        page.run_js(f"document.getElementById('g-recaptcha-response').innerHTML = '{captcha_solution}';")
        page.run_js(f"document.getElementById('g-recaptcha-response').value = '{captcha_solution}';")
        page.ele("xpath://button[@type='submit']").click()
        print(3)
        time.sleep(5)
    page.get(download_url)
    time.sleep(3)

    page.get('https://us-west-2.console.aws.amazon.com/s3/buckets/inq-audits?region=us-west-2&bucketType=general&tab=objects')
    time.sleep(3)

    if page.ele("xpath://input[@id='username']"):
        page.ele("xpath://input[@id='username']").input("stormdev0418")
        time.sleep(1)
        page.ele("xpath://input[@id='account']").input("majeem")
        time.sleep(1)
        print(1)
        page.ele("xpath://input[@id='password']").input("v(H45'")
        print(2)
        page.ele("xpath://div[@id='input_signin_button']").click()
        time.sleep(5)
    page.get('https://us-west-2.console.aws.amazon.com/s3/upload/inq-audits?region=us-west-2&bucketType=general')
    time.sleep(3)

    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    file_name = "RE1c1e44a42d7fac1ab67938efc1abde0b.mp3"
    upload_file = os.path.abspath(os.path.join(download_folder, file_name))
    
    page.ele("xpath://input[@data-testid='upload-file-table__file-input']").input(upload_file)
    time.sleep(3)
    page.ele("xpath://button[@data-testid='upload-configuration__submit']").click()
    print('\a' * 6)

def main(download_url):
    page = ChromiumPage()
    page.get('https://app.inquirly.com/new_admin/adminpage.php')
    signin(page, download_url)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide a download URL")
