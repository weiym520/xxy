# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from base.event import Event



class CustomFields(BasePage):

    # 页面动作
    ele_webui = (By.XPATH, '//*[@id="webui"]/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/button[1]/i')
    ele_strftime = "%Y-%m-%d %H:%M:%S"
    new_CUS_name = "CustomFields_XxyWym0001"
    ele_CUS_name = (By.ID, "name")
    ele_submit = (By.ID,"submit_button")
    ele_suce = (By.XPATH,'//strong[contains(text(),"Success: ")]')
    ele_suceFLLY = (By.XPATH,'//*[@id="success-notification"]/div')
    success_content = "Success"
    successFLLY_content = "Fieldset created successfully."
    Tab = "Custom Fields"
    latent_waiting = 2  # 隐性等待时间


    # 登录
    def do_login(self,user=Event.value_user,passwd=Event.value_passwd):
        # pass
        """
        登录页面输入框，输入用户名和密码
        :param user: 用户名
        :param passwd: 密码
        :return:
        """
        Event.event_login(self,user,passwd)

    #就点击setting下的页签
    def setting_all_it(self,Tab):
        """
        进入setting页面
        :param Tab: 页签的名字
        :return:
        """
        return Event.EVT_setting_all_it(self,Tab)



    def custom_fields_add(self):
        tt_name =CustomFields.set_name(self,CustomFields.new_CUS_name)
        #点击+号
        self.wait(CustomFields.latent_waiting)
        # 输入用户名，显示等待
        self.wait_for_element(Event.Evt_timeout, Event.Evt_poll_frequency, CustomFields.ele_webui).click()
        self.send_keys_to(tt_name,CustomFields.ele_CUS_name)
        #点save
        self.click_on(CustomFields.ele_submit)
        # 获取页面的文字：
        self.res =  self.result_comparison(CustomFields.ele_suce, CustomFields.ele_suceFLLY, CustomFields.success_content, CustomFields.successFLLY_content)
        return self.res

if __name__=="__main__":
    CF = CustomFields()
    CF.do_login()
    CF.setting_all_it(CF.Tab)
    CF.custom_fields_add()




