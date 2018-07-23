import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from time import sleep



class Moments():
    def __init__(self):
        """
        初始化
        """

        # 平台
        PLATFORM = 'Android'

        # 设备名称
        DEVICE_NAME = 'PRA_AL00'

        # APP路径
        APP = os.path.abspath('.') + '/weixin.apk'

        # APP包名
        APP_PACKAGE = 'com.tencent.mm'

        # 入口类名
        APP_ACTIVITY = '.ui.LauncherUI'

        # Appium地址
        DRIVER_SERVER = 'http://localhost:4723/wd/hub'
        # 等待元素加载时间
        TIMEOUT = 300

        # 滑动点
        FLICK_START_X = 300
        FLICK_START_Y = 300
        FLICK_DISTANCE = 700

        # 滑动间隔
        SCROLL_SLEEP_TIME = 1

        # 驱动配置
        self.desired_caps = {
            'platformName': PLATFORM,
            'deviceName': DEVICE_NAME,
            'appPackage': APP_PACKAGE,
            'appActivity': APP_ACTIVITY
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def login(self):
        """
        登录微信
        :return:
        """

        print('login...')
        # 授权
        button1 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
        button1.click()
        button2 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
        button2.click()
        # 登录按钮
        sleep(3)
        TouchAction(self.driver).tap(x=295, y=1641).perform()
        # 手机输入
        phone = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/hz')))
        phone.set_text('13513513510')
        # 下一步
        next = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/alr')))
        next.click()
        # 密码
        password = self.wait.until(
            EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/hz')))
        password.set_text('qq1412029')
        # 提交
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/alr')))
        submit.click()
        # 不关联通讯录
        button3 = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/an2')))
        button3.click()

    def qq_login(self):
        print('qq_login...')
        # 授权
        button1 = self.wait.until(
            EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
        button1.click()
        button2 = self.wait.until(
            EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
        button2.click()
        # 登录按钮
        sleep(3)
        TouchAction(self.driver).tap(x=295, y=1641).perform()
        button3 = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/c1t')))
        button3.click()
        # 输入qq
        phone = self.wait.until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText")))
        phone.set_text('12345678')
        # 密码
        password = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")))
        password.set_text('mima123456')
        # 提交
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/c1u')))
        submit.click()
        # 不关联通讯录
        button4 = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/an2')))
        button4.click()

    def enter(self):
        print('enter...')

        # 等加载数据
        self.wait.until(EC.invisibility_of_element_located((By.ID, 'com.tencent.mm:id/xx')))
        # 点击通讯录
        button1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.FrameLayout[@content-desc=\"当前所在页面,与wxid_4s00v48dt1e422的聊天\"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView")))
        button1.click()
        # 点公众号
        sleep(3)
        TouchAction(self.driver).tap(x=266, y=764).perform()
        # 点第一个公众号
        sleep(3)
        TouchAction(self.driver).tap(x=450, y=387).perform()
        # 点右上角小人头
        button2 = self.wait.until(EC.element_to_be_clickable((By.ID, '聊天信息')))
        button2.click()
        # 拉到底下
        sleep(3)
        TouchAction(self.driver).press(x=680, y=1633).move_to(x=751, y=421).release().perform()
        # 点全部信息
        button3 = self.wait.until(EC.element_to_be_clickable((By.ID, 'com.tencent.mm:id/aom')))
        button3.click()

        # 点击第一个文章
        while True:
            sleep(5)
            print('--------')
            TouchAction(self.driver).tap(x=540, y=1325).perform()
            sleep(1)
            TouchAction(self.driver).tap(x=540, y=1383).perform()
            sleep(1)
            TouchAction(self.driver).tap(x=540, y=1383).perform()
            title = ''
            read_num = ''
            like_num = ''

            title_item = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'activity-name')))
            for i in title_item:
                try:
                    title = i.get_attribute('text')
                except :
                    pass

            read_item = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'readNum3')))
            for i in read_item:
                try:
                    read_num = i.get_attribute('text')
                except:
                    pass

            like_item = self.wait.until(EC.presence_of_all_elements_located((By.ID, 'likeNum3')))
            for i in like_item:
                try:
                    like_num = i.get_attribute('text')
                except:
                    pass

            print(title)
            print(read_num)
            print(like_num)
            self.driver.back()
            sleep(5)
            self.driver.swipe(582, 1567, 569, 1199)

    def main(self):
        """
        入口
        :return:
        """
        # 登录
        # self.login()
        self.qq_login()
        # 进入公众号
        self.enter()



if __name__ == '__main__':
    moments = Moments()
    moments.main()
