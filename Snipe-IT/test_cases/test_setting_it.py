import pytest

from po.setting_IT import SettingIT


class TestSettinIT:

    # 测试用例之前的准备工作
    def setup(self) -> None:
        self.SIT = SettingIT()
        self.SIT.do_login()

    def test03_setting_it(self, Tab="Custom Fields"):
        """
        点击setting下不同的页签
        :param Tab:
        :return:
        """
        res = self.SIT.setting_all_it(Tab)
        assert Tab in res

    # 测试用例之后的扫尾工作
    def teardown(self) -> None:
        self.SIT.close()
        self.SIT.quit()

if __name__=="__main__":
    pytest.main()
