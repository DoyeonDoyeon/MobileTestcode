import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class PlaceMainView(unittest.TestCase):

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

        self.driver.tap([(786, 649)])
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    def swipe(self, start_x, start_y, end_x, end_y):
        actions = ActionChains(self.driver)
        actions.move_to_location(start_x, start_y)
        actions.click_and_hold()
        actions.move_by_offset(end_x - start_x, end_y - start_y)
        actions.release()
        actions.perform()


    def test_DQS_T13730(self):
        print("DQS_T13730 Side Menu 기본UI 확인")

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_1\n#01090497847").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃").is_displayed()

        print("DQS_T13730 Side Menu 기본UI 확인 | Pass")

    def test_DQS_T13731(self):
        print("DQS_T13731 방해 금지 시간 기능 동작 확인")

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정")
        setting.click()

        notouch = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "방해 금지 시간")
        notouch.click()

        notouch_button = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Switch")
        is_toggle_on = notouch_button.get_attribute("checked") == 'true'
        print(is_toggle_on)
        self.assertFalse(is_toggle_on)
        notouch_button.click()


        notouch_button = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Switch")
        is_toggle_on = notouch_button.get_attribute("checked") == 'true'
        print(is_toggle_on)
        self.assertTrue(is_toggle_on)

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시작 시간\n 오전 00 : 00").is_displayed()

        self.driver.tap([(840, 574)])
        max_swipes = 20
        start_x = 685
        start_y = 1707
        end_x = 685
        end_y = 1707+85

        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "11시 정각")
                if element.is_displayed():
                    break
            except NoSuchElementException:
                self.driver.swipe(start_x, start_y, end_x, end_y)
        else:
            raise NoSuchElementException("찾을 수 없습니다.")

            # assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "11시 정각").is_displayed()

        max_swipes = 60
        start_x1 = 797
        start_y1 = 1707
        end_x1 = 797
        end_y1 = 1707+85

        time.sleep(1)

        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "59분")
                if element.is_displayed():
                    break
            except NoSuchElementException:
                self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
        else:
            raise NoSuchElementException("찾을 수 없습니다.")

            # assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "59분").is_displayed()

        max_swipes = 60
        start_x3 = 926
        start_y3 = 1707
        end_x3 = 926
        end_y3 = 1707+85

        time.sleep(1)

        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "오후")
                if element.is_displayed():
                    break
            except NoSuchElementException:
                self.driver.swipe(start_x3, start_y3, end_x3, end_y3)
        else:
            raise NoSuchElementException("찾을 수 없습니다.")


        confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
        confirm.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시작 시간\n 오전 00 : 00")
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "종료 시간\n 오후 11 : 59")


        print("DQS_T13731 방해 금지 시간 기능 동작 확인 | Pass")

    def test_DQS_T13732(self):
        print("DQS_T13732 방해 금지 시간 설정 불가 동작 확인")

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정")
        setting.click()

        notouch = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "방해 금지 시간")
        notouch.click()

        notouch_button = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Switch")
        is_toggle_on = notouch_button.get_attribute("checked") == 'true'
        self.assertFalse(is_toggle_on)
        notouch_button.click()

        notouch_button = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Switch")
        is_toggle_on = notouch_button.get_attribute("checked") == 'true'
        self.assertTrue(is_toggle_on)

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시작 시간\n 오전 00 : 00").is_displayed()

        self.driver.tap([(840, 574)])
        max_swipes = 60
        start_x = 391
        start_y = 1707
        end_x = 391
        end_y = 1707-85

        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "오후")
                if element.is_displayed():
                    break
            except NoSuchElementException:
                self.driver.swipe(start_x, start_y, end_x, end_y)
        else:
            raise NoSuchElementException("찾을 수 없습니다.")

        max_swipes = 60
        start_x1 = 686
        start_y1 = 1706
        end_x1 = 686
        end_y1 = 1706+85

        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "11시 정각")
                if element.is_displayed():
                    break
            except NoSuchElementException:
                self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
        else:
            raise NoSuchElementException("찾을 수 없습니다.")

        max_swipes = 60
        start_x2 = 926
        start_y2 = 1707
        end_x2 = 926
        end_y2 = 1707+85

        time.sleep(1)

        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "오전")
                if element.is_displayed():
                    break
            except NoSuchElementException:
                self.driver.swipe(start_x2, start_y2, end_x2, end_y2)
        else:
            raise NoSuchElementException("찾을 수 없습니다.")

        confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
        is_toggle_on = confirm.get_attribute("checked") == 'true'
        print(is_toggle_on)
        self.assertFalse(is_toggle_on)
        confirm.click()

        print("DQS_T13732 방해 금지 시간 설정 불가 동작 확인 | Pass")

    def test_DQS_T13733(self):
        print("DQS_T13733 고객센터 기본 UI 확인")

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
        csct.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "안녕하세요.").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "슈프리마 문 서비스 고객센터 입니다.").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "무엇을 도와드릴까요?").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "운영시간 09:00 ~ 17:00").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "(주말, 공휴일 제외)").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화상담 1522-4507").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "정보 및 회원탈퇴").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "버전정보").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용약관").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원탈퇴").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "라이센스").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "오픈 소스").is_displayed()

        print("DQS_T13733 고객센터 기본 UI 확인 | Pass")

    def test_DQS_T13734(self):
        print("DQS_T13734 고객센터 전화상담 기능 동작 확인")

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
        csct.click()

        call = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화상담 1522-4507")
        call.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "숫자 입력 영역").is_displayed()

        self.driver.press_keycode(4)

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화상담 1522-4507").is_displayed()

        print("DQS_T13734 고객센터 전화상담 기능 동작 확인 | Pass")

    def test_DQS_T13735(self):
        print("DQS_T13735 고객센터 페이지의 이용약관 동작 확인")

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
        csct.click()

        cl1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.widget.ImageView[1]")
        cl1.click()

        assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@resource-id='pf1']/android.view.View").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용약관").is_displayed()

        prev = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
        prev.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()

        print("DQS_T13735 고객센터 페이지의 이용약관 동작 확인 | Pass")

    def test_DQS_T13736(self):
        print("DQS_T13736 고객센터 페이지의 개인정보 동작 확인")

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
        csct.click()

        cl1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.widget.ImageView[2]")
        cl1.click()

        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='개인정보 수집ㆍ이용 동의서']").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보").is_displayed()

        prev = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
        prev.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보").is_displayed()

        print("DQS_T13736 고객센터 페이지의 개인정보 동작 확인 | Pass")

    def test_DQS_T13737(self):
        print("DQS_T13737 고객센터 페이지의 오픈 소스 동작 확인")

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
        csct.click()

        cl1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.widget.ImageView[4]")
        cl1.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "오픈 소스").is_displayed()

        prev = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
        prev.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "오픈 소스").is_displayed()

        print("DQS_T13737 고객센터 페이지의 개인정보 동작 확인 | Pass")

    def test_DQS_T14102(self):
        print("DQS_T14102 프로필 이름 변경 불가 케이스 동작 확인")

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        prifile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_1\n#01090497847")
        prifile.click()

        edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
        edit.click()

        nameIPB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        nameIPB.click()
        nameIPB.send_keys("e2e_1")

        time.sleep(1)

        confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
        isconfirm = confirm.get_attribute("checked") == 'true'
        print(isconfirm)
        self.assertFalse(isconfirm)

        isnameIPB = nameIPB.text
        print(isnameIPB)

        self.assertEqual(isnameIPB, "e2e_1")

        confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
        confirm.click()



        print("DQS_T14102 프로필 이름 변경 불가 케이스 동작 확인 | Pass")

    def test_DQS_T14009(self):
        print("DQS_T14009 프로필 정보 변경 취소 시 동작 확인")

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        prifile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_1\n#01090497847")
        prifile.click()

        edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
        edit.click()

        nameIPB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        nameIPB.send_keys("123123123")

        cancel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
        cancel.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_1").is_displayed()

        print("DQS_T14009 프로필 정보 변경 취소 시 동작 확인 | Pass")

    def test_DQS_T13738(self):
        print("DQS_T13738 프로필 이름 변경 기능 동작 확인")

        leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
        leadbutton.click()

        prifile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_1\n#01090497847")
        prifile.click()

        edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
        edit.click()

        nameIPB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        nameIPB.click()
        nameIPB.send_keys("e2e_2")

        confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
        confirm.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_2").is_displayed()

        edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
        edit.click()

        nameIPB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        nameIPB.click()
        nameIPB.send_keys("e2e_1")

        confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
        confirm.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_1").is_displayed()



        print("DQS_T13738 프로필 이름 변경 기능 동작 확인 | Pass")

if __name__ == '__main__':
    unittest.main()


