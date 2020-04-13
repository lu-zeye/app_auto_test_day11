import allure


class Test(object):
    """自定义测试类"""

    # 添加测试步骤
    # 1代语法
    # allure.attach('描述', '我是测试步骤001的描述~~~')

    # 2代语法
    # 注意：该方法需要在测试方法内部进行调用
    def test_func2(self):
        allure.MASTER_HELPER.attach('登录', '1.输入用户名 2.输入密码 3.输入验证码 4.点击登录按钮')
        print('测试方法')
