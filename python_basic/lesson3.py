import requests


def request_get_test1():
    response = requests.get('http://www.baidu.com')
    print(response.status_code)  # 打印状态码
    print(response.url)  # 打印请求url
    print(response.headers)  # 打印头信息
    print(response.cookies)  # 打印cookie信息
    print(response.text)  # 以文本形式打印网页源码
    print(response.content)  # 以字节流形式打印
    pass


def request_get_test2():
    pass


def request_session_test():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"
    }
    login_url = "https://accounts.douban.com/j/mobile/login/basic"
    "ck=&=13135767689&password=4833123&=false&ticket="
    data = {
        "name": "131357679559",
        "password": "48331212af1uan",
        "remember": "false"
    }
    session = requests.Session()
    response = session.post(login_url, data=data, headers=headers)
    print(response.text)
    mine_url = "https://www.douban.com/people/141952954/"
    response = session.get(url=mine_url, headers=headers)
    edit_url = "https://www.douban.com/j/people/141952954/edit_intro"
    data = {
        "intro": "hello",
        "ck": "jA2J"
    }
    session.post(url=edit_url, data=data, headers=headers)
    pass


if __name__ == '__main__':
    """"""
    # request_get_test1()
    request_session_test()
