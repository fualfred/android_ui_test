# android_ui_test
pytest+allure+appium基于OP设计模式的android端测试框架

框架分层结构结构如下：
![image](https://user-images.githubusercontent.com/21330243/126063395-5e36897c-0e73-40a9-80b0-e8a6791d6c9d.png)

common：日志工具、装饰器、yaml解释工具类等
log：日志文件夹
page：页面类对象，包含base_page、main_page等
pageYaml：放置页面对象yaml解析文件，主要用来解析类中的各种方法，单独独立于yaml保存，实现测试步骤驱动
report：生成的allure报告
result:存放allure报告的json文件，生成报告需要用到
screenshot_tmp:运行中的截图文件夹
test_data:yaml文件保存的测试数据，实现测试数据驱动
testcases:测试用例脚本
pytest.ini:pytest的全局配置文件
run_all_tests.py:全部测试用例执行入口

效果如下：
1.测试步骤驱动：
![image](https://user-images.githubusercontent.com/21330243/126063645-fd7f3954-746a-4efc-adf3-bd8c0a1b14b5.png)
对应的pageObject文件里面对于不同的方法
2.测试数据驱动：
![image](https://user-images.githubusercontent.com/21330243/126063660-5739b95d-c058-44ff-bcea-a00f0bac00e8.png)
对于不同的测试脚本，针对不同的测试方法
3.运行后，allure报告效果如下：
![image](https://user-images.githubusercontent.com/21330243/126063709-8d5c893e-7c6d-4074-9917-7d60d061d3f4.png)
