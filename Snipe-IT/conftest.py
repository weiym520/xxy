# conftest.py
import pytest
from selenium import webdriver

from base.event import Event as EV
from base.home_page import HomePage

#这个好像没用到！
@pytest.fixture(scope="class")
def login():
    global driver
    driver = HomePage()
    EV.event_login(EV.value_user,EV.value_passwd)#用的是basebage的driver，没用HomePage的，那这个作用是什么呢
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def open_homepage():
    global driver
    print("1111111111111111111111111111")
    driver = HomePage()
    print("2222222222222222222222222")
    driver.getURL(EV.url)
    print("3333333333333333333333")
    yield driver
    driver.quit()


