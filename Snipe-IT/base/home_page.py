from base.base_page import BasePage

#这个好像没用到！
class HomePage(BasePage):
    """
    此类用于继承BasePage类，只继承初始化方法，保证每个页面操作都是同一个对象
    """
    def __init__(self):
        super(BasePage).__init__()
