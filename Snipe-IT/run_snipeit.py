#步骤1： 通过Pytest生成测试报告数据文件，这里带有--alluredir参数 ，生成的数据文件目录为allure-result中
import os

import pytest


# pytest.main(['./test_cases','-sv','--alluredir','allure-result'])

pytest.main(['-sv','--alluredir','allure-result'])
# 步骤2 ： 通过allure 读取数据源生成测试报告
#解释：
#allure-result : 生成的json数据文件目录
#-o allure-report : 生成的allure报告目录
#-c : 生成之前清除目录
# cmd = "allure generate allure-result -o allure-report -c"
cmd = "allure generate allure-result -o allure-report -c"
os.system(cmd)
# if __name__ == "__main__":
#     pytest.main([
#         "-v",           # 详细输出模式
#         "-s",           # 显示print输出
#         "--html=./report/report.html",  # 生成HTML报告
#         "--junitxml=./report/report.xml"  # 生成JUnit格式报告
#     ])
