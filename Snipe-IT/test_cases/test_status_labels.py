import pytest

from po.status_labels import StatusLabels


class TestStatusLabels:

    def setup(self) -> None:
        self.ST = StatusLabels()
        self.ST.do_login()
        self.ST.setting_all_it()

    def test05_status_labels_add(self):
        # 新增输入框中有很多要校验的地方，暂时先如此
        self.ST.status_labels_add(1)

    def test06_status_labels_delete(self):
        self.ST.status_labels_delete("StatusLabels_XxyWym2025-10-24 21:34:35")

    def tearDown(self) -> None:
        self.ST.close()
        self.ST.quit()

if __name__=="__main__":
    TSL = TestStatusLabels()
    TSL.setup()
    TSL.test05_status_labels_add()
    TSL.test06_status_labels_delete()
    # pytest.main(['-vs'])