# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from Database_connect import MysqlOperation
from base.base_page import BasePage
from base.event import Event
import random


class StatusLabels(BasePage):
    # 页面元素定位
    setting_list = (By.XPATH, '//*[@id="setting-list"]/section[1]/div/div/h1/ul/li[2]')
    SLTab = "Status Labels"
    ele_webui_SL = (By.XPATH, '//*[@id="webui"]/div/div[1]/div/div/div[1]/div[1]/div[1]/button[1]/i')
    ele_SL_name = (By.ID, "name")
    latent_waiting = 2  # 隐性等待时间
    ele_SL_ceateFrom = (By.XPATH, '//*[@id="create-form"]/div/div/div/div/div[2]/div/span')
    ele_Select_name = (By.NAME, 'statuslabel_types')
    ele_SLcreate_form = (By.XPATH, '//*[@id="create-form"]/div/div/div/div/div[2]/label')
    ele_SL_color = (By.ID, 'color')
    ele_SL_notes = (By.ID,'notes')
    content_notes ="selenium的下拉选择框。"
    ele_SL_show_in_nav = (By.ID, 'show_in_nav')
    ele_SL_default_label = (By.ID, 'default_label')
    ele_SL_submit = (By.ID, 'submit_button')
    ele_SLsuce = (By.XPATH,  '//strong[contains(text(),"Success: ")]')
    ele_SLsuceFLLY = (By.XPATH, '//*[@id="success-notification"]/div')
    success_SLcontent = "Success"
    successFLLY_SLcontent = "Status Label created successfully."
    ele_dataConfirmOKSL = (By.ID, 'dataConfirmOK')
    ele_delete_Success = (By.XPATH, '//strong[contains(text(),"Success: ")]')
    ele_delete_SuccessFLY = (By.XPATH, '//*[@id="success-notification"]/div')
    content_successe_SL = "Success"
    content_successeFLY_SL = "The Status Label was deleted successfully."
    ele_SLSearch_webui = (By.XPATH, '//*[@id="webui"]/div/div[1]/div/div/div[1]/div[1]/div[2]/div/input')

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
    def setting_all_it(self):
        """
        进入setting页面
        :param Tab: 页签的名字
        :return:
        """
        return Event.EVT_setting_all_it(self,StatusLabels.SLTab)

    def status_labels_add(self,Number):
        """
        :param Number: 增加的数据条数
        :return:
        """
        testSL = self.get_text(StatusLabels.setting_list)
        # 保持在当前页面
        if StatusLabels.SLTab in testSL:
            while Number:
                #点击+号新增
                #显示等待
                self.wait_for_element(Event.Evt_timeout, Event.Evt_poll_frequency, StatusLabels.ele_webui_SL).click()
                #Create New，name
                name_statuslabels = StatusLabels.set_name(self, StatusLabels.SLTab)
                self.send_keys_to(name_statuslabels,StatusLabels.ele_SL_name)
                # 点击Status Type的倒三角型
                self.wait(StatusLabels.latent_waiting)
                # 显示等待
                self.wait_for_element(Event.Evt_timeout, Event.Evt_poll_frequency, StatusLabels.ele_SL_ceateFrom).click()
                # Select下拉框
                num = random.randrange(5)
                self.select_base('index', num, StatusLabels.ele_Select_name)
                # 点击“Select Status Type”的文字将下拉框收起
                self.click_on(StatusLabels.ele_SLcreate_form)
                # 点击“Chart Color”的框。没有输入内容，保留默认
                self.click_on(StatusLabels.ele_SL_color)
                #点击“notes”，输入文字
                self.send_keys_to(StatusLabels.content_notes,StatusLabels.ele_SL_notes)
                # 点击勾选框Show in side nav
                self.click_on(StatusLabels.ele_SL_show_in_nav)
                # 点击勾选框Default Label
                self.click_on(StatusLabels.ele_SL_default_label)
                # 点击save保存按钮
                self.click_on(StatusLabels.ele_SL_submit)

                # 断言
                # 断言数据库校验
                res_name_statuslabels = MysqlOperation().select_mysql("status_labels",name_statuslabels)
                if name_statuslabels == res_name_statuslabels:
                    print("Status Labels 添加成功！")
                # 界面断言校验
                self.res = self.result_comparison(StatusLabels.ele_SLsuce, StatusLabels.ele_SLsuceFLLY,
                                                  StatusLabels.success_SLcontent, StatusLabels.successFLLY_SLcontent)
                Number -= 1
                return self.res


    def status_labels_delete(self,name):
        """
        :param name:  Status Labels页面中要删除的一条数据中的name列中的某个值的名字
        :return:
        """
        #判断元素是否存在当前页面上，即判断元素是否被删除了或不在当前页面
        res_ele_exit = self.isElementexit((By.PARTIAL_LINK_TEXT, name))
        if res_ele_exit:
            # 数据存在当前页面
            #执行在当前页中删除数据，而不使用分页或者是查询的方式先查出数据再进行删除。这是测试要点之一
            #用鼠标的方式滚动滚动条
            ele = self.finBY((By.PARTIAL_LINK_TEXT, name))
            self.action_chains_base(ele)
            #隐式等待
            self.wait(2)
            # 点击元素的删除按钮
            _item = self.finBY((By.XPATH, "//a[contains(@data-content,'"+name+"')]/i"))
            self.action_chains_base(_item,"click")
            # 点击弹框的yes按钮
            self.click_on(StatusLabels.ele_dataConfirmOKSL)
            # 界面断言校验返回值
            self.res = self.result_comparison(StatusLabels.ele_delete_Success, StatusLabels.ele_delete_SuccessFLY,
                                              StatusLabels.content_successe_SL, StatusLabels.content_successeFLY_SL)
        else:
            # 数据不存在当前页面，则进行搜索
            #在输入框中查询数据，定位输入框，并输入元素进行查询
            self.send_keys_to(name,StatusLabels.ele_SLSearch_webui)
            # 按下回车键
            self.send_keys_to(Keys.ENTER,StatusLabels.ele_SLSearch_webui)
            # 判断元素是否存在当前页面上，即判断元素是否被删除了或不在当前页面
            res_ele_exit_search = self.isElementexit((By.PARTIAL_LINK_TEXT, name))
            # 隐式等待
            if res_ele_exit_search:
                #搜索后发现数据存在！则继续删除数据！以下的代码有重复的地方，后续优化！
                # 点击元素的删除按钮
                # 隐式等待
                self.wait(2)
                # 点击元素的删除按钮
                _item = self.finBY((By.XPATH, "//a[contains(@data-content,'" + name + "')]/i"))
                self.action_chains_base(_item,"click")
                # 点击弹框的yes按钮
                self.click_on(StatusLabels.ele_dataConfirmOKSL)
                # 界面断言校验返回值
                self.res = self.result_comparison(StatusLabels.ele_delete_Success, StatusLabels.ele_delete_SuccessFLY,
                                                  StatusLabels.content_successe_SL, StatusLabels.content_successeFLY_SL)
            else:
                print("数据经过搜索查询后，依然不存在，请查看要删除的数据是否正确！")


if __name__=="__main__":
    # pytest.main()
    StatusLabels_test = StatusLabels()
    StatusLabels_test.do_login()
    StatusLabels_test.setting_all_it()
    StatusLabels_test.status_labels_add(1)
    # 这个数据已经被删除
    # StatusLabels_test.status_labels_delete('StatusLabels_XxyWym2025-10-24 21:38:55')
    # 这个数据还存在
    StatusLabels_test.status_labels_delete('Status Labels2025-10-28 23:52:36')




