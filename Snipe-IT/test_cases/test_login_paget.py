# -*- coding:utf-8 -*-
import pytest


from po.login_page import LoginSnipeit

class TestLoginSnipeit():

    # 测试用例之前的准备工作
    def setup(self):
        # 获取项目地址
        self.lg = LoginSnipeit()
        # self.lg.get(self.lg.url)
        # 初始化数据
        self.real0 = self.lg.real_Success
        self.real1 = self.lg.real_FCSuccess
        self.expe0 = self.lg.expected_Success
        self.expe1 = self.lg.expected_Success_content
        self.Ereal0 = self.lg.real_Error
        self.Ereal1 = self.lg.real_FCError
        self.Eexpe0 = self.lg.expected_Error
        self.Eexpe1 = self.lg.expected_Error_content

    def test01_login(self):
        """
        用例1：使用默认用户名密码
        :return:
        """
        self.lg.do_login()
        #断言
        real_content = self.lg.result_comparison(self.real0,self.real1,self.expe0,self.expe1)
        # print(real_content,self.expe2 )
        assert self.expe0 in real_content[0] and self.expe1 in real_content[1]

    def test02_login(self,user='',passwd=''):
        """
        用例2：使用空的用户名密码
        :return:
        """
        self.lg.do_login(user,passwd)
        #断言
        real_content = self.lg.result_comparison(self.Ereal0,self.Ereal1,self.Eexpe0,self.Eexpe1)
        # print(real_content, self.Eexpe2)
        assert self.Eexpe0 in real_content[0] and self.Eexpe1 in real_content[1]

    # 测试用例之后的扫尾工作
    def teardown(self) -> None:
        self.lg.close()
        self.lg.quit()


if __name__=="__main__":
    pytest.main(['-vs'])
    # TL =TestLoginSnipeit()
    # TL.setup()
    # TL.test01_login()
    # TL.teardown()
    # TL.setup()
    # TL.test02_login()
    # TL.teardown()
