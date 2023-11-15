import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import os
from selenium.webdriver.common.action_chains import ActionChains

"""
기본 테스트 계정
Standard Account
ID : 01090497847
Password : Rlaehdus100!

유일한 관리자 계정
ID : 010311111111
Password : Rlaehdus100!



"""



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

        print("DQS_T13681 로그인/로그아웃 기능 동작 확인 | Pass")

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
        print("DQS_T13682 자동 로그인 기능 동작 확인 | Pass")

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

        for _ in range(10):

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()

            pupUpTest = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호 또는 비밀번호가 일치하지 않습니다.")
            self.assertIsNotNone(pupUpTest,"로그인 실패 팝업이 출력되지 않았습니다.")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

        print("DQS_T13683 로그인 실패 동작 확인 | Pass")

    def test_DQS_T13671(self):
        print("DQS_T13671 공간의 유일한 관리자 회원 탈퇴 시도 시 동작 확인")

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()

        phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
        phone_input_box.click()
        phone_input_box.send_keys("010311111111")

        password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
        password_input_box.click()
        password_input_box.send_keys("Rlaehdus100!")

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()
        time.sleep(5)

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
        csct.click()

        leavMB = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.widget.ImageView[3]")
        leavMB.click()

        start_x = 114
        start_y = 1998

        end_x = 982
        end_y = 1998

        actions = ActionChains(self.driver)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)  # 100ms 대기
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지원 하지 않음").is_displayed()
        confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
        confirm.click()

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

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e222").is_displayed()

        print("DQS_T13671 공간의 유일한 관리자 회원 탈퇴 시도 시 동작 확인 | Pass")

    def test_DQS_T13677(self):
        print("DQS_T13677 회원가입 휴대폰 번호 입력 페이지에서 올바르지 않은 번호 입력시 동작 확인")

        SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
        SignUp.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용 약관 동의 (필수)").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집 및 이용 동의 (필수)").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음").is_displayed()

        agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
        isagree = agree.is_enabled()
        self.assertTrue(isagree,"약관 전체 동의 버튼이 활성화되어 있습니다.")

        agree1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용 약관 동의 (필수)")
        isagree1 = agree1.is_enabled()
        self.assertTrue(isagree1,"이용 약관 동의 (필수) 버튼이 활성화되어 있습니다.")

        agree2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집 및 이용 동의 (필수)")
        isagree2 = agree2.is_enabled()
        self.assertTrue(isagree2,"개인정보 수집 및 이용 동의 (필수) 버튼이 활성화되어 있습니다.")

        next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
        isnext = next.is_enabled()
        self.assertTrue(isnext, "다음 버튼이 활성화되어 있습니다.")

        agree.click()

        self.assertTrue(isnext, "다음 버튼이 비활성화 되어 있습니다.")
        next.click()

        authButton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
        isauthButton = authButton.is_enabled()
        self.assertTrue(isauthButton, "인증요청 버튼이 활성화 되어 있습니다.")

        phoNo = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        phoNo.click()

        text_to_input = "~!@#$%^&*("
        os.system(f"adb shell input text '{text_to_input}'")
        cl1 = phoNo.text
        self.assertEqual("", cl1)

        text_to_input1 = "가나다라마바사아"
        os.system(f"adb shell input text '{text_to_input1}'")
        cl2 = phoNo.text
        self.assertEqual("", cl2)

        text_to_input2 = "ABCDEFGH"
        os.system(f"adb shell input text '{text_to_input2}'")
        cl3 = phoNo.text
        self.assertEqual("", cl3)

        text_to_input3 = "abcdefgh"
        os.system(f"adb shell input text '{text_to_input3}'")
        cl4 = phoNo.text
        self.assertEqual("", cl4)

        text_to_input4 = "123456789"
        os.system(f"adb shell input text '{text_to_input4}'")
        cl5 = phoNo.text
        self.assertEqual("123 456 789", cl5)

        next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
        next.click()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청").is_displayed()

        print("DQS_T13677 회원가입 휴대폰 번호 입력 페이지에서 올바르지 않은 번호 입력시 동작 확인 | Pass")

    def test_DQS_T13685(self):
        print("DQS_T13685 회원가입 휴대폰 번호 입력 페이지에서 존재하는 번호 입력 시 동작 확인")

        SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
        SignUp.click()

        agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
        agree.click()

        next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
        next.click()

        phoNo = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        phoNo.click()
        phoNo.send_keys("01090497847")

        authButton = next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
        authButton.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미 가입된 번호입니다.").is_displayed()

        confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
        confirm.click()

        phoNo = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        assertt = phoNo.text
        self.assertEqual(assertt, "010 9049 7847")

        print("DQS_T13685 회원가입 휴대폰 번호 입력 페이지에서 존재하는 번호 입력 시 동작 확인 | Pass")
    def test_DQS_T13718(self):
        print("DQS_T13718 회원가입 페이지의 약관 동의 기능 동작 확인")

        SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
        SignUp.click()

        agree1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[4]")
        agree1.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용약관")

        lead = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
        lead.click()

        agree2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[6]")
        agree2.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보")

        lead = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
        lead.click()

        agree1Bt = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용 약관 동의 (필수)")
        agree1Bt.click()

        next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
        next.click()

        agree1Bt = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용 약관 동의 (필수)")
        agree1Bt.click()

        next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
        next.click()

        agree2Bt = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집 및 이용 동의 (필수)")
        agree2Bt.click()

        next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
        next.click()

        agree2Bt = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집 및 이용 동의 (필수)")
        agree2Bt.click()

        next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
        next.click()

        agreeBt = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
        agreeBt.click()

        agreeBt = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
        agreeBt.click()

        next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
        next.click()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음").is_displayed()

        print("DQS_T13718 회원가입 페이지의 약관 동의 기능 동작 확인 | Pass")

if __name__ == '__main__':
    unittest.main()
