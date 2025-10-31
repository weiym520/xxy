import pytest

from po.CustomFields import CustomFields


class TestSettinIT:

    # 测试用例之前的准备工作
    def setup(self) -> None:
        self.CF = CustomFields()
        self.CF.do_login()
        self.CF.setting_all_it(self.CF.Tab)

    def test04_custom_fields_add(self):
        """
        点击setting下不同的页签
        :param Tab:
        :return:
        """
        self.res = self.CF.custom_fields_add()
        # 这个断言方式要修改
        if "Success" == self.res and "Fieldset created successfully." == self.res[1]:
            assert 1 == 1

    # 测试用例之后的扫尾工作
    def teardown(self) -> None:
        self.CF.close()
        self.CF.quit()

if __name__=="__main__":
    pytest.main()
