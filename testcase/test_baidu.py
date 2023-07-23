import requests
import allure

def test_baidu():
    with allure.step( "访问京东" ):
        res = requests.get( "https://www.jd.com/" )
        res.status_code == 200
