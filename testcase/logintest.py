import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
#from appium.webdriver.common.touch_action import TouchAction


class LoginLogout(unittest.TestCase):

#-TODO- setUp 부분 다른 폴더로 이동하여 함수화 하고 Setup 에는 다른 프리컨디션 입력 예정

    def setUp(self):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.device_name = 'R3CXB0MKLGP'
        options.app_package = 'com.suprema.moon'
        options.app_activity = 'com.suprema.moon.MainActivity'
        options.automation_name = 'UiAutomator2'
        options.auto_grant_permissions = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_loginandlogout(self):
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
    def test_callingUI(self):
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

        place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개발서버")
        place.click()

        time.sleep(5)

        self.driver.tap([(791,1251)])

        time.sleep(5)

        self.driver.tap([(913,1116)])

        time.sleep(10)

        calling1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
        calling1.click()

    def test_DQST7650(self):
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

        time.sleep(10)

        place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개발서버")
        place.click()

        time.sleep(10)

        self.driver.tap([(786,649)])

        time.sleep(5)

        placesetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
        placesetting.click()

        inveteuser = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 초대")
        inveteuser.click()

        invite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
        invite.click()

        face = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 인식")
        phonenumber = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")

        self.assertIsNotNone(face)
        print("얼굴 인식 Test Pass")
        self.assertIsNotNone(phonenumber)
        print("휴대폰 번호 Test Pass")

        phonenumber.click()

        nameInputBox = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText[1]")
        nameInputBox.click()

        nameInputBox.send_keys("-")

        invetephonenumber = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010']")

        self.assertEqual(invetephonenumber.text, "010", "010이 InputBox 에 Hint 문구로 출력 되지 않았습니다 Test fail")
        print("010 출력 Test Pass")

        invetephonenumber.click()
        invetephonenumber.send_keys("70708080")

        next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
        next.click()

        nolimitedperiod = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "제한없음")
        nolimitedperiod_enable = nolimitedperiod.is_enabled()

        self.assertTrue(nolimitedperiod_enable, "제한 없음 버튼이 선택 되어 있지 않습니다 확인이 필요 합니다")

        alldoorsetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모든 출입문")
        alldoorsetting_enable = alldoorsetting.is_enabled()

        self.assertTrue(alldoorsetting_enable, "모든 출입문 버튼이 선택 되어 있지 않습니다 확인이 필요 합니다")

        invitebutton = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
        invitebutton.click()

        sort = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록순")
        sort.click()

        createuser = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "-\n#01070708080\n출입기간")

        createuser.click()

        backbtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        backbtn.click()

        useredit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
        useredit.click()

        deleteuser = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[1]")
        deleteuser.click()

        confirmuserdel = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
        confirmuserdel.click()

        print("DQS-T7650 사용자 초대 성공 케이스 동작 확인 | Pass")
        print("DQS-T7977 사용자 삭제 기능 동작 확인 | Pass")
    def test_DQS12219(self):
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

        print("로그인 성공")

        time.sleep(10)

        place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개발서버")
        place.click()

        time.sleep(10)

        self.driver.tap([(786, 649)])

        print("e2etest공간 진입 성공")

        time.sleep(5)

        placesetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
        placesetting.click()

        inveteuser = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 초대")
        inveteuser.click()

        testuser = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "_Test\n#01022222222\n출입기간")
        testuser.click()

        time.sleep(3)

        """
        유저 상세 정보에 필요한 정보들이 있는지 확인하는 코드
        """
        assertion = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "2Test\n#01022222222\n출입기간\n모든 출입문\n카카오QR\n네이버QR")
        self.assertIsNotNone(assertion)

        time.sleep(1)

        print("DQS-T12219 사용자 상세 정보 기능 동작 확인 Test | Pass")


if __name__ == '__main__':
    unittest.main()
