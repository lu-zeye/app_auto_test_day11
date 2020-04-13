import allure


class Test(object):
    """自定义测试类"""

    # 添加测试步骤
    # 1代语法
    # @allure.step(title="测试步骤001")

    # 2代语法
    @allure.MASTER_HELPER.step(title='测试步骤001')
    def test_func1(self):
        print('测试方法')
