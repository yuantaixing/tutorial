import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
}
login_url = "https://accounts.douban.com/j/mobile/login/basic"
session = requests.Session()


def login():
    data = {
        "name": "13135767989",
        "password": "4833123yuan",
        "remember": "false"
    }
    session.post(login_url, data=data, headers=headers)


def get_profile():
    profile_url = "https://www.douban.com/people/141952954/"
    response = session.get(url=profile_url, headers=headers)
    print(response.text)


def edit_profile():
    edit_url = "https://www.douban.com/j/people/141952954/edit_intro"
    data = {
        "intro": "hello",
        "ck": "jA2J"
    }
    session.post(url=edit_url, data=data, headers=headers)


if __name__ == '__main__':
    login()
