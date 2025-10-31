
from base.event import Event

from base.base_page import BasePage


class SettingIT(BasePage):
    # 页面元素定位
    # settiSO = (By.ID, "settings-sidenav-option")
    # js = "arguments[0].scrollIntoView();"
    # timeout = 8 #WebDriverWait的最长超时时长
    # poll_frequency = 0.5 #WebDriverWait的检测的间隔时间
    # latent_waiting = 2#隐性等待时间
    # setting_list = (By.XPATH, '//*[@id="setting-list"]/section[1]/div/div/h1/ul/li[4]')
    # TabCF = "Custom Fields"

    def do_login(self,user=Event.value_user,passwd=Event.value_passwd):
        # pass
        """
        登录页面输入框，输入用户名和密码
        :param user: 用户名
        :param passwd: 密码
        :return:
        """
        Event.event_login(self,user,passwd)


    # 页面动作
    def setting_all_it(self,Tab):
        """
        进入setting页面
        :param Tab: 页签的名字
        :return:
        """
        return Event.EVT_setting_all_it(self,Tab)



if __name__=="__main__":
    setting_test = SettingIT()
    setting_test.do_login()
    setting_test.setting_all_it(Event.TabCF_Evt)