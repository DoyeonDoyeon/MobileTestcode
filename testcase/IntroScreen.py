import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction


class IntroScreen(unittest.TestCase):

    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'R39M30571MZ'
        options.app_package = 'com.suprema.moon'
        options.app_activity = 'com.suprema.moon.MainActivity'
        options.automation_name = 'UiAutomator2'
        options.auto_grant_permissions = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_DQS_T13681(self):
        print("DQS_T13681 로그인/로그아웃 기능 동작 확인")
        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()

        phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
        phone_input_box.click()
        self.driver.press_keycode(7)
        self.driver.press_keycode(8)
        self.driver.press_keycode(7)
        self.driver.press_keycode(16)
        self.driver.press_keycode(7)
        self.driver.press_keycode(11)
        self.driver.press_keycode(16)
        self.driver.press_keycode(14)
        self.driver.press_keycode(15)
        self.driver.press_keycode(11)
        self.driver.press_keycode(14)

        password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
        password_input_box.click()
        password_input_box.send_keys("Rlaehdus100!")

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()

        time.sleep(10)

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
        logout_button.click()

        confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
        confirm.click()

    def test_DQS_T13682(self):
        print("DQS_T13682 자동 로그인 기능 동작 확인")

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()

        phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
        phone_input_box.click()
        phone_input_box.send_keys("01090497847")

        password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
        password_input_box.click()
        password_input_box.send_keys("Rlaehdus100!")

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()

        time.sleep(5)

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개발서버").is_displayed()

        self.driver.quit()

        time.sleep(5)

        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'R39M30571MZ'
        options.app_package = 'com.suprema.moon'
        options.app_activity = 'com.suprema.moon.MainActivity'
        options.automation_name = 'UiAutomator2'
        options.auto_grant_permissions = True
        options.no_reset = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

        time.sleep(3)

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개발서버").is_displayed()

    def test_DQS_T13683(self):
        print("DQS_T13683 로그인 실패 동작 확인")

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()

        phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
        phone_input_box.click()
        phone_input_box.send_keys("01090497847")

        password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
        password_input_box.click()
        password_input_box.send_keys("111111")

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()



if __name__ == '__main__':
    unittest.main()
