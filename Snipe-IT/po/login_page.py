import pytest
from selenium.webdriver.common.by import By
from base.event import Event

from base.base_page import BasePage

#第二层:po页面层
class LoginSnipeit(BasePage):
    # 页面元素定位
    #成功的断言
    real_Success = (By.XPATH, '//strong[contains(text(),"Success: ")]')#返回Success定位
    real_FCSuccess = (By.XPATH, '//*[@id="success-notification"]/div')#返回Success后的内容定位
    expected_Success = ("Success")#返回Success
    expected_Success_content = ("恭喜，登陆成功。") ##返回Success后的内容，只有这个值是不同的
    #失败的断言
    real_Error = (By.XPATH, '//strong[contains(text(),"错误:")]')#返回Error定位
    real_FCError = (By.XPATH, '//*[@id="error-notification"]/div')#返回FCError后的内容定位
    expected_Error = ("错误")#返回Success
    expected_Error_content = ("请检查下面的表单以了解错误") ##返回Success后的内容，只有这个值是不同的


    # 页面动作，# 想把和用户登录这个分离，因为其他页面也用登录，那么就要将这个是实例化，可这个driver实例化后和其他页面的实例化并不是同一个

    def do_login(self,user=Event.value_user,passwd=Event.value_passwd):
        # pass
        """
        登录页面输入框，输入用户名和密码
        :param user: 用户名
        :param passwd: 密码
        :return:
        """
        Event.event_login(self,user,passwd)

    def dismiss_login(self):
        """退出登录"""
        pass

    def fogot_passwd(self):
        """
        忘记密码
        """
        pass

    def browser_do(self):
        """浏览器的箭头退出或加载按钮"""
        pass

if __name__=="__main__":
    lg =  LoginSnipeit()
    lg.do_login()
















