import allure


class Test(object):
    """自定义测试类"""

    # 添加测试步骤
    # 1代语法
    # @pytest.allure.severity(Severity)
    # 级别调用
    # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)

    # 2代语法
    """
    级别分布
    BLOCKER = 阻碍
    CRITICAL = 严重
    NORMAL = 正常
    MINOR = 次要
    TRIVIAL = 不重要
    """
    # @allure.MASTER_HELPER.severity(级别)
    # 级别调用
    # @allure.MASTER_HELPER.severity(allure.MASTER_HELPER.severity_level.CRITICAL)
    # def test_func3(self):
    #     print('测试方法')

    # 添加严重级别(扩展)
    # 变量字母全部大写的变量名称为常量
    BLOCKER = allure.MASTER_HELPER.severity_level.BLOCKER
    CRITICAL = allure.MASTER_HELPER.severity_level.CRITICAL
    NORMAL = allure.MASTER_HELPER.severity_level.NORMAL
    MINOR = allure.MASTER_HELPER.severity_level.MINOR
    TRIVIAL = allure.MASTER_HELPER.severity_level.TRIVIAL

    @allure.MASTER_HELPER.severity(BLOCKER)
    def test_func1(self):
        print('测试方法1')

    @allure.MASTER_HELPER.severity(CRITICAL)
    def test_func2(self):
        print('测试方法2')

    @allure.MASTER_HELPER.severity(NORMAL)
    def test_func3(self):
        print('测试方法3')

    @allure.MASTER_HELPER.severity(MINOR)
    def test_func4(self):
        print('测试方法4')

    @allure.MASTER_HELPER.severity(TRIVIAL)
    def test_func5(self):
        print('测试方法5')
