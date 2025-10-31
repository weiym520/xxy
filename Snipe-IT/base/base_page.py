from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.select import Select

#第一层:BasePage基础层
class BasePage():

    # 构造方法:在生成对象时自动调用的方法
    def __init__(self):
        # # 打开谷歌浏览器
        self.driver = webdriver.Chrome()

    def finBY(self,args):
        """
        封装定位元素(所有的定位全走这里)
        :param args: 定位元素，如：By.ID,"username"
        :return:
        """
        return self.driver.find_element(*args)

    def getURL(self,URl):
        self.driver.get(URl)

    def get_text(self,args):
        """
        获取页面文本
        :param args: 定位元素，如：By.ID,"username"
        :return:
        """
        return self.finBY(args).text

    def click_on(self,args):
        """
        点击
        :param args: 定位元素，如：By.ID,"username"
        :return:
        """
        return self.finBY(args).click()

    def send_keys_to(self,content,args):
        """
        输入框输入内容
        :param args: 定位元素，如：By.ID,"username"
        :return:
        """
        return self.finBY(args).send_keys(content)

    def wait(self,time):
        return self.driver.implicitly_wait(time)

    def wait_for_element(self,timeout,poll_frequency,args):
        """
        显示等待，调用的是visibility_of_element_located的并判断元素是否可见
        :param timeout:WebDriverWait的最长超时时长
        :param poll_frequency:WebDriverWait的检测的间隔时间
        :param args:定位元素，如：By.ID,"username"
        :return:针对元素的等待返回值
        """
        try:
            # print(args)
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_any_elements_located((args)))
            element = self.finBY(args)
            return element
        except Exception as e:
            print(f"Element with ID {args} did not appear within {timeout} seconds")
            raise e

    def quit(self):
        """
        退出浏览器
        :return:
        """
        self.driver.quit()

    def close(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.close()

    def max_window(self):
        """
        放大浏览器
        :return:
        """
        self.driver.maximize_window()

    def result_comparison(self,ele_Prompt,ele_Scontent,expect_Prompt,expect_Scontent):
        """
        :param Prompt:文字Success
        :param Scontent: Success成功后面的文字
        :param ele_Prompt: 对Success的元素定位,预期的字段
        :param ele_Scontent: 对 Success成功后面的文字定位,预期的字段
        :return:
        """
        # 断言,获取Success:
        real_Prompt = self.get_text(ele_Prompt)
        #获取Fieldset created successfully.
        real_FCSuccess = self.get_text(ele_Scontent)
        if (expect_Prompt in real_Prompt) and (expect_Scontent in real_FCSuccess):
            # print(expected_Scontent)
            return (real_Prompt,real_FCSuccess)

    def script(self,js,above):
        """
        滚动条
        :param js: javascript代码
        :param above:已经定位的元素，如：above = self.finBY(args)
        :return:
        """
        self.driver.execute_script(js, above)

    def action_chains_base(self,above,click=''):
        """
         鼠标悬浮到SETTING，也相当于滚动条滚动到此元素所在的页面
        :param above: 已经定位的元素，如：above = self.finBY(args)
        :param click: 不仅是悬浮鼠标，还要判断是否进行点击
        :return:
        """
        if click =="click":
            # 悬浮并点击
            ActionChains(self.driver).move_to_element(above).click(above).perform()
        else:
            # 只悬浮
            ActionChains(self.driver).move_to_element(above).perform()


    def set_name(self,pre_name):
        """
        :param pre_name: 名字的前缀如CustomFields_XxyWym0001"
        :return: 返回加了时间后缀的名字
        """
        # 格式化本地时间
        formatted_time = time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime())
        # print("格式化后的本地时间:", formatted_time)
        # #输入信息
        name_customfields = pre_name+str(formatted_time)
        return name_customfields

    def select_base(self,type,value,args):
        """
        下拉框的选择
        :param type: 选择下拉框的类型选输入的数据有：index，value，text
        :param value: 若type是index,则输入的value是int,若type是value,则输入的value是选value,若type是text,则输入的value是选text,
        :param args: 下拉框的元素定位
        :return:
        """
        # Select下拉框
        if type == "index":
            Select(self.finBY(args)).select_by_index(value)
        elif type == "value":
            Select(self.finBY(args)).select_by_value(value)
        else:
            Select(self.finBY(args)).select_by_visible_text(value)

    def isElementexit(self,args):
        """
        通过捕获NoSuchElementException异常来判断元素是否存在。如果找不到元素，则会抛出异常。
        :param driver1: 哈哈哈，我竟然不知道怎么解释，就百度详细看看-->
            1、driver是什么？
                答：driver是你通过selenium驱动的浏览器的对象，driver的属性就是浏览器的属性；即driver==浏览器（可以这样理解）
            2、driver能做什么？
               答：你想想你的浏览器能做什么？打开网址、放大缩小、全屏、切换标签页（窗口）…等等。
        :param by:  By.ID、By.XPATH、By.CLASS_NAME等等..
        :param value: 元素
        :return:bool值
        """
        try:
            self.finBY(args)
        except NoSuchElementException:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True