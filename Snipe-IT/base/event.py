from selenium.webdriver.common.by import By


class Event:
    url = "http://192.168.181.12/"
    Evt_user = (By.ID,"username") #用户名字输入框定位
    Evt_password = (By.ID, "password")#密码输入框定位
    Evt_submit = (By.ID, "submit") #提交按钮
    value_user = ("nimi") #用户名字
    value_passwd = ("admin@123")#密码
    Evt_timeout = 5 #WebDriverWait的最长超时时长
    Evt_poll_frequency = 0.5 #WebDriverWait的检测的间隔时间

    settiSO_Evt= (By.ID, "settings-sidenav-option")
    js_Evt = "arguments[0].scrollIntoView();"
    latent_waiting_Evt = 2#隐性等待时间
    setting_list_Evt = (By.XPATH, '//*[@id="setting-list"]/section[1]/div/div/h1/ul/li[4]')
    breadcrumb_item  = (By.XPATH, '//li[@class="breadcrumb-item active"]')
    TabCF_Evt = "Custom Fields"


    @staticmethod
    # @allure.step('登录')
    def event_login(self,user=value_user, passwde=value_passwd):
        try:
            self.getURL(Event.url)
            # 输入用户名，显示等待
            self.wait_for_element(Event.Evt_timeout,Event.Evt_poll_frequency,Event.Evt_user).send_keys(user)
            # self.send_keys_to(user, Event.Evt_user)
            #输入密码
            self.send_keys_to(passwde,Event.Evt_password)
            #点击提交
            self.click_on(Event.Evt_submit)
        except Exception as e:
            print(f'登录异常，为，{e}')
            raise e

    # 页面动作
    @staticmethod
    def EVT_setting_all_it(self,Tab):
        """
        进入setting页面
        :param Tab: 页签的名字，如Custom Fields、Status Labels、Asset Models、Categories  等
        :return:
        """
        #隐式等待
        self.wait(Event.latent_waiting_Evt)
        # 把浏览器放到最大
        self.max_window()
        #滚动条
        above = self.finBY(Event.settiSO_Evt)
        self.script(Event.js_Evt,above)
        # 鼠标悬浮到SETTING
        self.action_chains_base(above)
        #页签的名字，如：Custom Fields、Status Labels、Asset Models、Categories  等
        self.wait_for_element(Event.Evt_timeout,Event.Evt_poll_frequency,(By.LINK_TEXT,Tab)).click()
        # 这个是分别进入页签的页面后获取左上角的文本
        # res = self.get_text(Event.setting_list_Evt)
        res = self.get_text(Event.breadcrumb_item)
        if Tab in res:
            print(f"{Tab}登录成功！")
        else:
            print("页面加载失败",Tab,res)
        return res