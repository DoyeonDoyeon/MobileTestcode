#import datetime
#import os
import time
import unittest
#from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
#from selenium.webdriver.common.action_chains import ActionChains
from configuration.utill import capture_screenshot
from configuration.webDriver import AppiumConfig


'Xpath'
leadBtn = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView"


class SideMenu(unittest.TestCase):

    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()

        phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
        phone_input_box.click()
        phone_input_box.send_keys("01020905304")

        password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
        password_input_box.click()
        password_input_box.send_keys("Kjstar36!!")

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()
        time.sleep(7)

        place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상")
        place.click()
        time.sleep(5)

        self.driver.tap([(786, 649)])
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_DQS_T13730(self):
        try:
            print("DQS_T13730 Side Menu 기본UI 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃").is_displayed()

            print("DQS_T13730 Side Menu 기본UI 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13730 Side Menu 기본UI 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13731(self):
        try:
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

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13731 방해 금지 시간 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13732(self):
        try:
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

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13732 방해 금지 시간 설정 불가 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13733(self):
        try:
            print("DQS_T13733 고객센터 기본 UI 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            csct.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "안녕하세요.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "슈프리마 CLUe 서비스 고객센터 입니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "무엇을 도와드릴까요?").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "운영시간 09:00 ~ 17:00").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "(주말, 공휴일 제외)").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화 상담 1660-4507").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "정보 및 회원탈퇴").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "버전정보").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용약관").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원탈퇴").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "라이센스").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "오픈 소스").is_displayed()

            print("DQS_T13733 고객센터 기본 UI 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13734(self):
        try:
            print("DQS_T13734 고객센터 전화상담 기능 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            csct.click()

            call = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화 상담 1660-4507")
            call.click()

            #assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "숫자 입력 영역").is_displayed()

            #self.driver.press_keycode(4)

            #assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화 상담 1660-4507").is_displayed()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.samsung.android.dialer:id/digits']").is_displayed()
            #테스트폰마다 전화 화면이 다를 수 있어 전화화면에 찾는 element가 있다면 pass로 수정
            print("DQS_T13734 고객센터 전화상담 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14226(self):
        try:
            print("DQS-T14226 설정 페이지에서 뒤로가기 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃").is_displayed()

            print("DQS-T14226 설정 페이지에서 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14227(self):
        try:
            print("DQS-T14227 내 계정 페이지의 뒤로가기 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃").is_displayed()

            print("DQS-T14227 내 계정 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14228(self):
        try:
            print("DQS-T14228 고객센터 페이지의 뒤로가기 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃").is_displayed()

            print("DQS-T14228 고객센터 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13735(self):
        try:
            print("DQS_T13735 고객센터 페이지의 이용약관 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            csct.click()

            cl1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.widget.ImageView[1]")
            cl1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용약관").is_displayed()
            time.sleep(2)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='슈프리마 ']").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@text=' '])[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='서비스 ']").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@text=' '])[2]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='이용약관 ']").is_displayed()


            prev = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            prev.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()

            print("DQS_T13735 고객센터 페이지의 이용약관 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13736(self):
        try:
            print("DQS_T13736 고객센터 페이지의 개인정보 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            csct = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터")
            csct.click()

            cl1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.widget.ImageView[2]")
            cl1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보").is_displayed()
            time.sleep(2)

            prev = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            prev.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()


            print("DQS_T13736 고객센터 페이지의 개인정보 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13737(self):
        try:
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

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "설정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "고객센터").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃").is_displayed()

            print("DQS_T13737 고객센터 페이지의 개인정보 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14102(self):
        try:
            print("DQS_T14102 프로필 이름 변경 불가 케이스 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            prifile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304")
            prifile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            nameIPB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            nameIPB.click()
            nameIPB.send_keys("kjjung")

            time.sleep(1)

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            isconfirm = confirm.get_attribute("checked") == 'true'
            print(isconfirm)
            self.assertFalse(isconfirm)

            isnameIPB = nameIPB.text
            print(isnameIPB)

            self.assertEqual(isnameIPB, "kjjung")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()


        print("DQS_T14102 프로필 이름 변경 불가 케이스 동작 확인 | Pass")

    def test_DQS_T14009(self):
        try:
            print("DQS_T14009 프로필 정보 변경 취소 시 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            prifile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304")
            prifile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            nameIPB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            nameIPB.click()
            nameIPB.send_keys("test user123")
            time.sleep(3)

            cancel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancel.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung").is_displayed()

            print("DQS_T14009 프로필 정보 변경 취소 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13738(self):
        try:
            print("DQS_T13738 프로필 이름 변경 기능 동작 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            prifile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung\n#01020905304")
            prifile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            nameIPB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            nameIPB.click()
            nameIPB.send_keys("e2e_test1")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_test1").is_displayed()

            #기존 상태로 복구 동작
            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            nameIPB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            nameIPB.click()
            nameIPB.send_keys("kjjung")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung").is_displayed()

            print("DQS_T13738 프로필 이름 변경 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

class AC(unittest.TestCase):
    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()

        phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
        phone_input_box.click()
        phone_input_box.send_keys("01020905304")

        password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
        password_input_box.click()
        password_input_box.send_keys("Kjstar36!!")

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()
        time.sleep(7)

        place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상")
        place.click()
        time.sleep(5)

        self.driver.tap([(786, 649)])
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_DQS_T14017(self):
        try:
            print("DQS_T14017 출입문 없는 케이스 동작 확인")

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
            place.click()
            time.sleep(5)

            self.driver.tap([(789, 1299)])

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문\n장치 없음\n출입문이 없습니다.']/android.widget.ImageView[3]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문\n장치 없음\n출입문이 없습니다.']/android.widget.ImageView[2]").is_displayed()

            el1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문\n장치 없음\n출입문이 없습니다.']/android.view.View[4]/android.widget.ImageView[2]")
            el1.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문\n장치 없음\n출입문이 없습니다.']/android.widget.ImageView[3]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문\n장치 없음\n출입문이 없습니다.']/android.widget.ImageView[2]").is_displayed()

            print("DQS_T14017 출입문 없는 케이스 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14018(self):
        try:
            print("DQS_T14018 출입문 수동 잠금 기능 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            door.click()

            manuallock = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[2]")
            manuallock.click()

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 잠금'])[2]").is_displayed()

            self.driver.tap([(550, 747)])
            self.driver.tap([(540, 2031)])

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 닫힘'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 닫힘").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Fail")

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 잠금 시작'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 잠금 시작").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Fail")


            backbtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            backbtn.click()

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n수동 잠금\nDoor1_BS3")
            door.click()

            manuallock = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[2]")
            manuallock.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금").is_displayed()

            self.driver.tap([(550, 747)])
            self.driver.tap([(540, 2031)])

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 닫힘'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 닫힘").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Fail")

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 잠금 시작'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 잠금 시작").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Fail")

            print("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14019(self):
        try:
            print("DQS_T14019 출입문 일시 열림 기능 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            door.click()

            opendoor = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[3]")
            opendoor.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림").is_displayed()

            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금").is_displayed()

            time.sleep(1)

            self.driver.tap([(550, 747)])
            self.driver.tap([(540, 2031)])

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 닫힘'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 닫힘").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Fail")

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='잠금 해제'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금 해제").is_displayed()
                except NoSuchElementException:
                    self.fail("DQS_T14018 출입문 수동 잠금 기능 동작 확인 | Fail")

            print("DQS_T14019 출입문 일시 열림 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14020(self):
        try:
            print("DQS_T14020 출입문명 변경 기능 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            door.click()

            setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            setting.click()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Test_1")

            dnIBtext = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIBtext)

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            #backPress = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            #backPress.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nTest_1").is_displayed()
            door1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nTest_1")
            door1.click()

            setting1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_1")
            setting1.click()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Door1_BS3")

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            #backPress = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            #backPress.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3").is_displayed()

            print("DQS_T14020 출입문명 변경 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14021(self):
        try:
            print("DQS_T14021 출입문 수동 열림 기능 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            door.click()

            manualOpen = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[4]")
            manualOpen.click()

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 열림'])[2]").is_displayed()

            self.driver.tap([(550, 747)])
            self.driver.tap([(540, 2031)])

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 열림 시작'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 열림 시작").is_displayed()
                except NoSuchElementException:
                    try:
                        assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 열림 시작'])[2]").is_displayed()
                    except NoSuchElementException:
                        self.fail("Fail")

            backbtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            backbtn.click()

            door2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n수동 열림\nDoor1_BS3")
            door2.click()

            manualOpen = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[4]")
            manualOpen.click()

            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금").is_displayed()

            self.driver.tap([(550, 747)])
            self.driver.tap([(540, 2031)])

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 모드 해제'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 모드 해제").is_displayed()
                except NoSuchElementException:
                    self.fail("Fail")

            time.sleep(2)

            print("DQS_T14021 출입문 수동 열림 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14022(self):
        try:
            print("DQS_T14022 출입문 Grid 리스트에서 스와이프 시 기능 동작 확인")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3").is_displayed()

            start_x = 274
            start_y = 1600
            end_x = 848
            end_y = 1600
            self.driver.swipe(start_x, start_y, end_x, end_y)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3").is_displayed()

            start_x1 = 848
            start_y1 = 1600
            end_x1 = 274
            end_y1 = 1600

            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor2_N2").is_displayed()

            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor2_N2").is_displayed()

            self.driver.swipe(start_x, start_y, end_x, end_y)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3").is_displayed()

            print("DQS_T14022 출입문 Grid 리스트에서 스와이프 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    '''def test_DQS_T14023(self):
        try:
            print("DQS_T14023 출입문 연결 끊김 시 동작 확인")
            print("더미 장치가 없어 Test수행 불가능함")

            start_x1 = 848
            start_y1 = 1600
            end_x1 = 274
            end_y1 = 1600
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            time.sleep(1)
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n수동 잠금\ne2e_연결끊김테스트").is_displayed()

            disabledoor = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n수동 잠금\ne2e_연결끊김테스트")
            disabledoor.click()

            manuaLock = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[2]")
            manuaLock.click()

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 잠금'])[2]").is_displayed()

            doorOpen = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[3]")
            doorOpen.click()

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 잠금'])[2]").is_displayed()

            manualOpen = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[4]")
            manualOpen.click()

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 잠금'])[2]").is_displayed()

            setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_연결끊김테스트")
            setting.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_연결끊김테스트").is_displayed()

            print("DQS_T14023 출입문 연결 끊김 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()'''

    '''def test_DQS_T14024_T14087(self):
        try:
            print("DQS_T14024 출입문 스케쥴 열림 설정 시 동작 확인 || DQS-T14087 출입문 스케줄 열림 설정 해제 시 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음")
            st3.click()

            #Schedule 추가 등록
            addSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addSchedule.click()

            scheduleName = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName.click()
            scheduleName.send_keys("E2E_Schedule_add1")

            nxt_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nxt_Btn.click()

            monSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]")
            monSchedule.click()
            time.sleep(1)

            self.driver.tap([(801, 1687)])
            max_swipes = 20
            start_x = 729
            start_y = 1693
            end_x = 729
            end_y = 1693+80

            for _ in  range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "23시 정각")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x, start_y, end_x, end_y)
                else:
                    raise NoSuchElementException("찾을 수 없습니다.")

            self.driver.tap([(801, 1687)])
            max_swipes = 20
            start_x1 = 868
            start_y1 = 1696
            end_x1 = 868
            end_y1 = 1696+80

            for _ in  range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "59분")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
                else:
                    raise NoSuchElementException("찾을 수 없습니다.")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            tueSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[3]")
            tueSchedule.click()

            wedSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[5]")
            wedSchedule.click()

            thuSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[7]")
            thuSchedule.click()

            friSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[9]")
            friSchedule.click()

            satSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[11]")
            satSchedule.click()

            sunSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[13]")
            sunSchedule.click()

            creatSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "생성")
            creatSchedule.click()
            time.sleep(3)

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule_add1")
            st4.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nE2E_Schedule_add1").is_displayed()

            self.driver.tap([(60, 160)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n스케줄 열림\nDoor1_BS3").is_displayed()

            self.driver.tap([(540, 2031)])

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 열림 시작'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림 시작").is_displayed()
                except NoSuchElementException:
                    try:
                        assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 열림 시작'])[2]").is_displayed()
                    except NoSuchElementException:
                        self.fail("Fail")

            self.driver.tap([(60, 160)])

          #- TODO 하기 테스트 항목은 스케쥴 열림 상태에서 이슈로 인하여 모니터링 -> Place Main View 진입시 이전 Door 가 출력되지 않아 임시로 변경해 놓은 상태
          #- TODO 그러하여 임의로 기존 Test Door 로 돌려 놓았으며 나중에 정상 시나리오로 변경 해야함.

            print("하기 테스트 항목은 스케쥴 열림 상태에서 이슈로 인하여 모니터링 -> Place Main View 진입시 이전 Door 가 출력되지 않아 임시로 변경해 놓은 상태\n그러하여 임의로 기존 Test Door 로 돌려 놓았으며 나중에 정상 시나리오로 변경 해야함")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n스케줄 열림\nDoor1_BS3").is_displayed()
            re = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n스케줄 열림\nDoor1_BS3")
            re.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nE2E_Schedule_add1")
            st3.click()

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
            st4.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음").is_displayed()

            self.driver.tap([(60, 160)])
            time.sleep(1)

            self.driver.tap([(540, 2031)])
            time.sleep(2)

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 열림 종료'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림 종료").is_displayed()
                except NoSuchElementException:
                    try:
                        assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 열림 종료'])[2]").is_displayed()
                    except NoSuchElementException:
                        self.fail("Fail")

            self.driver.tap([(60, 160)])

            #등록된 Schdeule(E2E_Schedule_add1) 삭제
            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음")
            st3.click()

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='E2E_Schedule_add1']/android.widget.ImageView[2]")
            st5.click()

            delSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            delSchedule.click()
            time.sleep(1)

            pass

            print("DQS_T14024 출입문 스케쥴 열림 설정 시 동작 확인 || DQS-T14087 출입문 스케줄 열림 설정 해제 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14025_T14088(self):
        try:
            print("DQS_T14025 출입문 스케쥴 잠금 설정 시 동작 확인 || DQS-T14088 출입문 스케줄 잠금 설정 해제 시 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\n없음")
            st3.click()

            #Schedule 추가 등록
            addSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addSchedule.click()

            scheduleName = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName.click()
            scheduleName.send_keys("E2E_Schedule_add2")

            nxt_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nxt_Btn.click()

            monSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]")
            monSchedule.click()
            time.sleep(1)

            self.driver.tap([(801, 1687)])
            max_swipes = 20
            start_x = 729
            start_y = 1693
            end_x = 729
            end_y = 1693+80

            for _ in  range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "23시 정각")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x, start_y, end_x, end_y)
                else:
                    raise NoSuchElementException("찾을 수 없습니다.")

            self.driver.tap([(801, 1687)])
            max_swipes = 20
            start_x1 = 868
            start_y1 = 1696
            end_x1 = 868
            end_y1 = 1696+80

            for _ in  range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "59분")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
                else:
                    raise NoSuchElementException("찾을 수 없습니다.")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            tueSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[3]")
            tueSchedule.click()

            wedSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[5]")
            wedSchedule.click()

            thuSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[7]")
            thuSchedule.click()

            friSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[9]")
            friSchedule.click()

            satSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[11]")
            satSchedule.click()

            sunSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[13]")
            sunSchedule.click()

            creatSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "생성")
            creatSchedule.click()
            time.sleep(3)

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule_add2")
            st4.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\nE2E_Schedule_add2").is_displayed()

            self.driver.tap([(60, 180)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n스케줄 잠금\nDoor1_BS3").is_displayed()

            self.driver.tap([(540, 2031)])
            time.sleep(2)

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 잠금 시작'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금 시작").is_displayed()
                except NoSuchElementException:
                    try:
                        assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 잠금 시작'])[2]").is_displayed()
                    except NoSuchElementException:
                        self.fail("Fail")

            self.driver.tap([(60, 160)])

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n스케줄 잠금\nDoor1_BS3")
            st5.click()

            st6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            st6.click()

            st7 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\nE2E_Schedule_add2")
            st7.click()

            st8 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
            st8.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\n없음").is_displayed()
            self.driver.tap([(60, 160)])
            time.sleep(1)

            self.driver.tap([(540, 2031)])
            time.sleep(2)

            try:
                assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 잠금 종료'])[1]").is_displayed()
            except NoSuchElementException:
                try:
                    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금 종료").is_displayed()
                except NoSuchElementException:
                    try:
                        assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='스케줄 잠금 종료'])[2]").is_displayed()
                    except NoSuchElementException:
                        self.fail("Fail")

            self.driver.tap([(60, 160)])

            # 등록된 Schdeule(E2E_Schedule_add2) 삭제
            st9 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n스케줄 잠금\nDoor1_BS3")
            st9.click()

            st10 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            st10.click()

            st11 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\n없음")
            st11.click()

            st12 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='E2E_Schedule_add2']/android.widget.ImageView[2]")
            st12.click()

            delete_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            delete_Btn.click()
            time.sleep(3)

            self.driver.tap([(60, 160)])

            self.driver.tap([(60, 160)])

            pass
            print("DQS_T14025 출입문 스케쥴 잠금 설정 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()'''

    def test_DQS_T14077(self):
        try:
            print("DQS_T14077 출입문 모드 변경시 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[2]")
            st2.click()

            time.sleep(1)

            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[4]")
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 제어").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "현재 모드를 해제 하시겠습니까?").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소").is_displayed()

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            st4.click()

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수동 잠금'])[2]").is_displayed()

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[4]")
            st5.click()

            st6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            st6.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금").is_displayed()

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[4]")
            st5.click()

            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[2]")
            st2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 제어").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "현재 모드를 해제 하시겠습니까?").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소").is_displayed()

            st6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            st6.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금").is_displayed()

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[4]")
            st5.click()

            time.sleep(1)

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[3]")
            st5.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 제어").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "현재 모드를 해제 하시겠습니까?").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소").is_displayed()

            st6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            st6.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금").is_displayed()

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[2]")
            st5.click()

            time.sleep(1)

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ImageView[3]")
            st5.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 제어").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "현재 모드를 해제 하시겠습니까?").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소").is_displayed()

            st6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            st6.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금").is_displayed()

            print("DQS_T14077 출입문 모드 변경시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14083(self):
        try:
            print("DQS_T14083 출입문 Grid 리스트 에서 출입문 선택 시 동작 확인")

            st1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[4]/android.widget.ImageView[2]")
            st1.click()

            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door2_N2\n잠금  ").is_displayed()

            print("DQS_T14083 출입문 Grid 리스트 에서 출입문 선택 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14084(self):
        try:
            print("DQS-T14084 출입문 리스트 변경 버튼 기능 동작 확인")

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[4]")
            st2.click()

            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door2_N2\n잠금  ").is_displayed()
            #assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_연결끊김테스트\n잠금 | 수동 잠금").is_displayed()

            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[4]")
            st3.click()

            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3").is_displayed()

            print("DQS-T14084 출입문 리스트 변경 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14085(self):
        try:
            print("DQS-T14085 출입문 리스트 뷰에서 출입문 선택 시 기능 동작 확인")

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[4]")
            st2.click()

            time.sleep(1)

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3\n잠금  ")
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3").is_displayed()

            self.driver.tap([(601, 767)])

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door2_N2\n잠금  ")
            st4.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door2_N2").is_displayed()

            self.driver.tap([(601, 767)])
            time.sleep(1)

            #st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_연결끊김테스트\n잠금 | 수동 잠금")
            #st5.click()

            #assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_연결끊김테스트").is_displayed()

            #self.driver.tap([(601, 767)])
            #time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[4]")
            st2.click()

            print("DQS-T14085 출입문 리스트 뷰에서 출입문 선택 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    '''def test_DQS_T14086(self):
        try:
            print("DQS-T14086 출입문 리스트 뷰 스와이프 시 기능 동작 확인")
            print("장치 4개이상 있어야 케이스 진행할 수 있음 - 현재 환경 2대여서 테스트 불가")

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[4]")
            st2.click()

            max_swipes = 20
            start_x = 503
            start_y = 1804
            end_x = 503
            end_y = 1804-100

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1_e2e_연결끊김테스트\n잠금  ")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x, start_y, end_x, end_y)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")

            time.sleep(3)

            max_swipes = 20
            start_x = 503
            start_y = 1804-100
            end_x = 503
            end_y = 1804

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3\n잠금  ")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x, start_y, end_x, end_y)
            else:
                raise NoSuchElementException("찾을 수 없습니다.")


            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[4]")
            st2.click()

            pass

            print("DQS-T14086 출입문 리스트 뷰 스와이프 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()'''

    def test_DQS_T14164(self):
        try:
            print("DQS-T14164 출입문 스케줄 열림/잠금 스케줄 이 중복되는 시간의 스케줄 설정 시도 시 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            st1.click()

            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            st2.click()

            time.sleep(1)

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음")
            st3.click()

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            st4.click()

            time.sleep(5)

            scheduleOpen = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='스케줄 열림\n없음']")
            contentDesc = scheduleOpen.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            expected_text = "스케줄 열림\n없음"

            # 스케줄 설정 후 설정된 스케줄명이 바로 갱신되지 않아서 뒤에 실행되는 케이스들이 fail되어 조건문 작성
            if contentDesc == expected_text:
                print("스케줄 열림에 설정한 E2E_Schedule가 출력되지 않음 - Test Fail임")
                #뒤로가기 클릭
                self.driver.tap([(54, 158)])
                time.sleep(1)

                place1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
                place1.click()
                time.sleep(5)

                self.driver.tap([(268, 591)])
                time.sleep(3)

                place2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상")
                place2.click()
                time.sleep(5)

                self.driver.tap([(786, 649)])
                time.sleep(5)

                st10 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n스케줄 열림\nDoor1_BS3")
                st10.click()
                time.sleep(1)

                st11 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
                st11.click()
                time.sleep(1)
            else:
                print("스케줄 열림에 설정한 E2E_Schedule 이 출력됨")


            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\n없음")
            st5.click()

            time.sleep(1)

            st6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            st6.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지원 하지 않음").is_displayed()

            st7 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            st7.click()

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            st8 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\nE2E_Schedule")
            st8.click()

            st9 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
            st9.click()

            time.sleep(5)

            pass

            print("DQS-T14164 출입문 스케줄 열림/잠금 스케줄 이 중복되는 시간의 스케줄 설정 시도 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14209(self):
        try:
            print("DQS-T14209 출입문 설정 페이지의 뒤로가기 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            st1.click()

            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            st2.click()

            self.driver.tap([(60, 190)])

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3").is_displayed()

            print("DQS-T14209 출입문 설정 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14210(self):
        try:
            print("DQS-T14210 출입문 설정 페이지의 출입문명 인풋 박스 유효성 검사")
            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            door.click()

            setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            setting.click()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Ab")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "Ab")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("12")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "12")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("가나")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "가나")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("- _")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "- _")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("!@#$%^&*()")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "!@#$%^&*()")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.").is_displayed()
            specialText1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='공백,-,_, 외의 특수문자는 사용할 수 없습니다.']")
            contentDesc = specialText1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Ab1")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "Ab1")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Ab가")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "Ab가")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Ab - _")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "Ab - _")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Ab!")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.").is_displayed()
            specialText2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='공백,-,_, 외의 특수문자는 사용할 수 없습니다.']")
            contentDesc = specialText2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "Ab!")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("1가")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "1가")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("1 - _")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "1 - _")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("가 - _")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "가 - _")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("가!@#$%^&*()")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.").is_displayed()
            specialText3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='공백,-,_, 외의 특수문자는 사용할 수 없습니다.']")
            contentDesc = specialText3.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "가!@#$%^&*()")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012345678901234567890123456789012345678901234567890123456")

            try:
                errormsg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.")
                raise AssertionError(f"Fail : 에러 메시지 출력, '공백,-,_, 외의 특수문자는 사용할 수 없습니다.'")
            except NoSuchElementException:
                print(f"pass : 에러 메시지 출력하지 않음")


            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1,"<<<<<이 친구는 기획이 이상하여 64자 넘어갔을때 잘못된 문구가 출력 되어 나중에 테스트 하시는분은 PES 기획에 문구 수정 요청하세요 ! ")
            self.assertEqual(dnIB1, "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012345678901234567890123456789012345678901234567890123456")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            print("DQS-T14210 출입문 설정 페이지의 출입문명 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14230(self):
        try:
            print("DQS-T14230 스케줄 잠금 시간 목록 페이지의 뒤로가기 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            st1.click()

            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            st2.click()

            time.sleep(1)

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\n없음")
            st3.click()

            self.driver.tap([(60, 190)])

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문").is_displayed()

            print("DQS-T14230 스케줄 잠금 시간 목록 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14229(self):
        try:
            print("DQS-T14229 스케줄 열림 시간 목록 페이지의 뒤로가기 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            st1.click()

            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            st2.click()

            time.sleep(1)

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음")
            st3.click()

            self.driver.tap([(60, 190)])

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문").is_displayed()

            print("DQS-T14229 스케줄 열림 시간 목록 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14211(self):
        try:
            print("DQS-T14211 출입문 설정 페이지의 출입문명 인풋 박스 X 버튼 기능 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
            door.click()

            setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
            setting.click()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("1")

            can = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1']/android.widget.ImageView")
            can.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText").is_displayed()

            print("DQS-T14211 출입문 설정 페이지의 출입문명 인풋 박스 X 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

class Video(unittest.TestCase):
    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()

        phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
        phone_input_box.click()
        phone_input_box.send_keys("01020905304")

        password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
        password_input_box.click()
        password_input_box.send_keys("Kjstar36!!")

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()
        time.sleep(7)

        place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상")
        place.click()
        time.sleep(5)

        self.driver.tap([(786, 649)])
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_DQS_T14028(self):
        try:
            print("DQS-T14028 비디오 최대화/최소화 버튼 기능 동작 확인")

            #최대화(가로모드) 버튼 클릭
            self.driver.tap([(1010, 1132)])
            time.sleep(3)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "전체화면 전환안됨, 출입문 출력됨"
            except NoSuchElementException:
                pass

            # 최소화 버튼 클릭
            self.driver.tap([(67, 2054)])
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")

            pass
            print("DQS-T14028 비디오 최대화/최소화 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14029(self):
        try:
            print("DQS-T14029 비디오명 변경 기능 동작 확인")

            self.driver.tap([(1013, 498)])

            st1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st1.click()
            st1.send_keys("Test1")

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            st2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "변경이 완료 되었습니다.").is_displayed()
            camNameModify = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='변경이 완료 되었습니다.']")
            contentDesc = camNameModify.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "변경이 완료 되었습니다.")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            st3.click()

            self.driver.tap([(549, 2073)])
            time.sleep(3)

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "14 개 필터 선택")
            st4.click()
            # 멀티 NVR환경 구성 때문에 초기값 14개 필터로 출력됨

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라\n2")
            st5.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1").is_displayed()
            time.sleep(3)

            self.driver.tap([(69, 174)])
            time.sleep(1)

            self.driver.tap([(69, 174)])
            time.sleep(3)

            self.driver.tap([(1013, 498)])

            st1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st1.click()
            st1.send_keys("CAM-1")

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            st2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "변경이 완료 되었습니다.")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            st3.click()
            time.sleep(1)

            #최대화에서 카메라 이름 변경
            self.driver.tap([(1016, 1136)])
            time.sleep(2)

            self.driver.tap([(1011, 2049)])
            time.sleep(2)

            st1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st1.click()
            st1.send_keys("Test2")

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            st2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "변경이 완료 되었습니다.").is_displayed()
            camNameModify = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='변경이 완료 되었습니다.']")
            contentDesc = camNameModify.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "변경이 완료 되었습니다.")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            st3.click()
            time.sleep(0.5)

            self.driver.tap([(81, 2049)])
            time.sleep(1)

            self.driver.tap([(549, 2073)])
            time.sleep(3)

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "14 개 필터 선택")
            st4.click()
            # 멀티 NVR환경 구성 때문에 초기값 14개 필터로 출력됨

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라\n2")
            st5.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2").is_displayed()
            time.sleep(3)

            self.driver.tap([(69, 174)])
            time.sleep(1)

            self.driver.tap([(69, 174)])
            time.sleep(3)

            self.driver.tap([(1013, 498)])

            st1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st1.click()
            st1.send_keys("CAM-1")

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            st2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "변경이 완료 되었습니다.")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            st3.click()

            print("DQS-T14029 비디오명 변경 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14030_T14027(self):
        try:
            print("DQS-T14030 비디오 멀티뷰에서 특정 비디오 선택 시 동작 확인 || DQS-T14027 비디오 뷰 변경 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[3]")
            st1.click()
            time.sleep(1)

            self.driver.tap([(178, 614)])
            time.sleep(1)

            #선택한 채널이름 추출할 수 없어서 1ch 변경 후 설정 버튼 클릭 시 이동하는지 확인
            self.driver.tap([(1013, 498)])
            time.sleep(1)

            self.driver.tap([(51, 156)])
            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[3]")
            st2.click()
            time.sleep(1)

            self.driver.tap([(776, 625)])
            time.sleep(1)

            #선택한 채널이름 추출할 수 없어서 1ch 변경 후 최대화 되는지 확인
            self.driver.tap([(1018, 1134)])
            time.sleep(1)

            self.driver.tap([(65, 2057)])
            time.sleep(1)

            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[3]")
            st3.click()
            time.sleep(1)

            self.driver.tap([(183, 1002)])
            time.sleep(1)

            #선택한 채널이름 추출할 수 없어서 1ch 변경 후 설정 버튼 클릭 시 이동하는지 확인
            self.driver.tap([(1013, 498)])
            time.sleep(1)

            self.driver.tap([(51, 156)])
            time.sleep(1)

            st4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[3]")
            st4.click()
            time.sleep(1)

            self.driver.tap([(781, 991)])
            time.sleep(1)

            #선택한 채널이름 추출할 수 없어서 1ch 변경 후 최대화 확인
            self.driver.tap([(1018, 1134)])
            time.sleep(1)

            self.driver.tap([(65, 2057)])
            time.sleep(1)

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[3]")
            st5.click()
            time.sleep(1)

            print("DQS-T14030 비디오 멀티뷰에서 특정 비디오 선택 시 동작 확인 || DQS-T14027 비디오 뷰 변경 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13557(self):
        try:
            print("DQS-T13557 양방향 통화 중 카메라 화면 전환 시 동작 확인")

            #양방향 톻화버튼 선택
            self.driver.tap([(913, 1128)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스피커 방송").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '누르고 말하세요.\n말하는 중에는 들리지 않습니다.').is_displayed()

            touch_action = TouchAction(self.driver)
            x = 550
            y = 1696
            touch_action.long_press(x=x, y=y, duration=3000).release().perform()

            #양방향 통화 종료 - 비디오 임의 위치 클릭
            self.driver.tap([(479, 796)])
            time.sleep(1)

            #2번 > 3번 ch 이동
            for _ in range(2):
                start_x1 = 846
                start_y1 = 819
                end_x1 = 246
                end_y1 = 819
                self.driver.swipe(start_x1, start_y1, end_x1, end_y1)

            #양방향 톻화버튼 선택
            self.driver.tap([(913, 1128)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스피커 방송").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '누르고 말하세요.\n말하는 중에는 들리지 않습니다.').is_displayed()

            #양방향 통화 종료 - 비디오 임의 위치 클릭
            self.driver.tap([(479, 796)])
            time.sleep(1)

            #3번 > 1번 ch 이동
            for _ in range(2):
                start_x2 = 246
                start_y2 = 819
                end_x2 = 846
                end_y2 = 819
                self.driver.swipe(start_x2, start_y2, end_x2, end_y2)

            pass
            print("DQS-T13557 양방향 통화 중 카메라 화면 전환 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13558(self):
        try:
            print("DQS-T13558 양방향 통화 상태에서 전체 화면(가로 모드) 전환 시 동작 확인")

            #양방향 톻화버튼 선택
            self.driver.tap([(913, 1128)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스피커 방송").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '누르고 말하세요.\n말하는 중에는 들리지 않습니다.').is_displayed()

            touch_action = TouchAction(self.driver)
            x = 550
            y = 1696
            touch_action.long_press(x=x, y=y, duration=3000).release().perform()

            #양방향 통화 종료 - 비디오 임의 위치 클릭
            self.driver.tap([(479, 796)])
            time.sleep(1)

            #전체 화면(가로 모드) 버튼 클릭
            self.driver.tap([(1010, 1132)])
            time.sleep(3)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "전체화면 전환안됨, 출입문 출력됨"
            except NoSuchElementException:
                pass

            # 최소화 버튼 클릭
            self.driver.tap([(67, 2054)])
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")

            pass
            print("DQS-T13558 양방향 통화 상태에서 전체 화면(가로 모드) 전환 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13559(self):
        try:
            print("DQS-T13559 양방향 통화 종료 기능 동작 확인")

            #양방향 톻화버튼 선택
            self.driver.tap([(913, 1128)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스피커 방송").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '누르고 말하세요.\n말하는 중에는 들리지 않습니다.').is_displayed()

            touch_action = TouchAction(self.driver)
            x = 550
            y = 1696
            touch_action.long_press(x=x, y=y, duration=3000).release().perform()

            #양방향 통화 종료 - 스와이프 동작
            start_x1 = 550
            start_y1 = 1360
            end_x1 = 550
            end_y1 = 1560
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            #양방향 통화 종료 확인
            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nDoor1_BS3")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "전체화면 전환안됨, 출입문 출력됨"
            except NoSuchElementException:
                pass

            pass
            print("DQS-T13559 양방향 통화 종료 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13561(self):
        try:
            print("DQS-T13561 양방향 통화 기능이 없는 카메라 싱글뷰에서 양방향 통화 버튼 확인")

            #1번 > 2번 ch 이동 - 2번 ch 양방향 통화 기는 없는 카메라
            start_x1 = 846
            start_y1 = 819
            end_x1 = 246
            end_y1 = 819
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)

            #양방향 톻화버튼 선택
            self.driver.tap([(913, 1128)])
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스피커 방송")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "스피커 방송 출력되는지 확인"
            except NoSuchElementException:
                pass

            pass
            print("DQS-T13561 양방향 통화 기능이 없는 카메라 싱글뷰에서 양방향 통화 버튼 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

class EventSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(10)

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()

        phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
        phone_input_box.click()
        phone_input_box.send_keys("01020905304")

        password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
        password_input_box.click()
        password_input_box.send_keys("Kjstar36!!")

        login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
        login_button.click()
        time.sleep(7)

    def tearDown(self):
        self.driver.quit()

    def test_DQS_T13627(self):
        try:
            print("DQS-T13627 [출입보안][워크스페이스 변경] 동일한 타입으로 변경 시 동작 확인")

            #하단 이력 조회 선택
            self.driver.tap([(362, 2081)])
            time.sleep(2)

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 - 출입 인증 선택 해제
            self.driver.tap([(1016, 380)])
            time.sleep(1)

            acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
            acEvent.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "5 개 필터 선택").is_displayed()
            #6개로 출력됨 - issue

            #워크 스페이지 변경 - 출입보안(공간이름 : Test 공간2)

            self.driver.tap([(175, 294)])
            time.sleep(5)

            self.driver.tap([(277, 1823)])
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test 공간2").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "6 개 필터 선택").is_displayed()

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 - 출입 인증 선택 해제
            self.driver.tap([(1016, 380)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            #place변경(공간이름 : 멤버쉽관리_초대 100명 이상)
            self.driver.tap([(140, 291)])
            time.sleep(5)

            self.driver.tap([(271, 622)])
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "5 개 필터 선택").is_displayed()

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 - 출입 인증 선택
            self.driver.tap([(1016, 380)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            #이력 필터 기존 설정 복구
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 - 출입 인증 선택
            self.driver.tap([(1016, 380)])
            time.sleep(1)

            acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
            acEvent.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            pass
            print("DQS-T13627 [출입보안][워크스페이스 변경] 동일한 타입으로 변경 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13628(self):
        try:
            print("DQS-T13628 [영상보안][워크스페이스 변경] 동일한 타입으로 변경 시 동작 확인")

            #영상보안 공간 이동
            self.driver.tap([(215, 331)])
            time.sleep(5)

            self.driver.tap([(786, 609)])
            time.sleep(5)

            #하단 이력 조회 선택
            self.driver.tap([(362, 2081)])
            time.sleep(2)

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 - 출입 인증 선택 해제
            self.driver.tap([(1016, 490)])
            time.sleep(1)

            acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
            acEvent.click()

            self.driver.tap([(1016, 490)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()

            #영상 이벤트 - 움직임 감지 선택 해제
            self.driver.tap([(1016, 600)])
            time.sleep(1)

            veEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "움직임 감지")
            veEvent.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n3").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "14 개 필터 선택").is_displayed()
            #14개로 출력됨 - issue

            #워크 스페이지 변경 - 영상보안(공간이름 : Test 공간)

            self.driver.tap([(175, 291)])
            time.sleep(5)

            self.driver.tap([(797, 1209)])
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test 공간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "12 개 필터 선택").is_displayed()
            #12개 필터 출력됨(issue) - 10개로 출력되어야 함

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 - 출입 인증 선택 해제
            self.driver.tap([(1016, 490)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()

            self.driver.tap([(1016, 490)])
            time.sleep(1)

            self.driver.tap([(1016, 600)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n4").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            #place변경(공간이름 : 비디오 공간)
            self.driver.tap([(140, 291)])
            time.sleep(5)

            self.driver.tap([(794, 606)])
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "12 개 필터 선택").is_displayed()

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 - 출입 인증 선택
            self.driver.tap([(1016, 500)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()

            self.driver.tap([(1016, 500)])
            time.sleep(1)

            self.driver.tap([(1016, 600)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n3").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            #이력 필터 기존 설정 복구
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 - 출입 인증 선택
            self.driver.tap([(1016, 500)])
            time.sleep(1)

            acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
            acEvent.click()

            self.driver.tap([(1016, 500)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()

            self.driver.tap([(1016, 600)])
            time.sleep(1)

            veEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "움직임 감지")
            veEvent.click()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            pass
            print("DQS-T13628 [영상보안][워크스페이스 변경] 동일한 타입으로 변경 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13629(self):
        try:
            print("DQS-T13629 [워크스페이스 변경] 비디오 워크스페이스로 변경 시 동작 확인")

            #하단 이력 조회 선택
            self.driver.tap([(362, 2081)])
            time.sleep(2)

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 - 출입 인증 선택 해제
            self.driver.tap([(1016, 380)])
            time.sleep(1)

            acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
            acEvent.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "5 개 필터 선택").is_displayed()
            #6개로 출력됨 - issue

            #워크 스페이지 변경 - 영상보안(공간이름 : 비디오 공간)

            self.driver.tap([(140, 291)])
            time.sleep(5)

            self.driver.tap([(794, 606)])
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "14 개 필터 선택").is_displayed()
            #10 개 필터로 출력됨 -issue

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 선택
            self.driver.tap([(1020, 501)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()

            #영상 이벤트 선택
            self.driver.tap([(1020, 600)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n4").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            #place변경(공간이름 : 멤버쉽관리_초대 100명 이상)
            self.driver.tap([(140, 291)])
            time.sleep(5)

            self.driver.tap([(271, 622)])
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "5 개 필터 선택").is_displayed()

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 - 출입 인증 선택
            self.driver.tap([(1016, 380)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            #이력 필터 기존 설정 복구
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 - 출입 인증 선택
            self.driver.tap([(1016, 380)])
            time.sleep(1)

            acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
            acEvent.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            pass
            print("DQS-T13629 [워크스페이스 변경] 비디오 워크스페이스로 변경 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13630(self):
        try:
            print("DQS-T13630 [워크스페이스 변경] 출입문 워크스페이스로 변경 시 동작 확인")

            #영상보안 공간 이동
            self.driver.tap([(215, 331)])
            time.sleep(5)

            self.driver.tap([(786, 609)])
            time.sleep(5)

            #하단 이력 조회 선택
            self.driver.tap([(362, 2081)])
            time.sleep(2)

            #워크 스페이지 변경 - 출입보안(공간이름 : QA 무인매장)
            self.driver.tap([(170, 286)])
            time.sleep(5)

            self.driver.tap([(295, 1190)])
            time.sleep(3)

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 - 출입 인증 선택 해제
            self.driver.tap([(1020, 394)])
            time.sleep(1)

            acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
            acEvent.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "6 개 필터 선택").is_displayed()
            #6개로 출력됨 - issue

            #워크 스페이지 변경 - 영상보안(공간이름 : 비디오 공간)

            self.driver.tap([(140, 291)])
            time.sleep(5)

            self.driver.tap([(794, 606)])
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "10 개 필터 선택").is_displayed()
            #10 개 필터로 출력됨 -issue

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입 이벤트 선택
            self.driver.tap([(1020, 501)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()

            #영상 이벤트 선택
            self.driver.tap([(1020, 600)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n4").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            #place변경(공간이름 : 공간이름 : QA 무인매장)
            self.driver.tap([(170, 286)])
            time.sleep(5)

            self.driver.tap([(295, 1190)])
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이력조회").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "QA 무인매장").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "5 개 필터 선택").is_displayed()

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n5").is_displayed()

            #출입 이벤트 - 출입 인증 선택
            self.driver.tap([(1020, 394)])
            time.sleep(1)

            acEvent = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증")
            acEvent.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            pass
            print("DQS-T13630 [워크스페이스 변경] 출입문 워크스페이스로 변경 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13637(self):
        try:
            print("DQS-T13637 [출입보안] 이력조회 필터의 기본값 확인")

            #출입보안 공간 이동 - QA 무인매장
            self.driver.tap([(215, 331)])
            time.sleep(5)

            self.driver.tap([(268, 1208)])
            time.sleep(5)

            #하단 이력 조회 선택
            self.driver.tap([(362, 2081)])
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "7 개 필터 선택").is_displayed()

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입문 확인
            self.driver.tap([(1016, 282)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "무인 문11").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문\n1").is_displayed()

            self.driver.tap([(1016, 282)])
            time.sleep(1)

            #출입 이벤트 확인
            self.driver.tap([(1016, 389)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 제어").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 제어").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도어락 잠금").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "퇴실 입력").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "문열림 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()

            pass
            print("DQS-T13637 [출입보안] 이력조회 필터의 기본값 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13638(self):
        try:
            print("DQS-T13638 [영상보안] 이력조회 필터의 기본값 확인")

            #영상보안 공간 이동 - 비디오 공간
            self.driver.tap([(215, 331)])
            time.sleep(5)

            self.driver.tap([(794, 606)])
            time.sleep(3)

            #하단 이력 조회 선택
            self.driver.tap([(362, 2081)])
            time.sleep(2)

            #출입문, 카메라 등록 환경에서 따하 필터 갯수가 다를 수 있음
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "14 개 필터 선택").is_displayed()

            #핕터 선택
            self.driver.tap([(1002, 291)])
            time.sleep(1)

            #출입문 확인
            self.driver.tap([(1016, 282)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door2_N2").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문\n2").is_displayed()


            self.driver.tap([(1016, 282)])
            time.sleep(1)

            #카메라 확인
            self.driver.tap([(1016, 389)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CAM-1").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CAM-2").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CAM-3").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CAM-4").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CAM-5").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CAM-6").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라\n2").is_displayed()

            self.driver.tap([(1016, 389)])
            time.sleep(1)

            #출입 이벤트 확인
            self.driver.tap([(1016, 500)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 인증").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수동 제어").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 제어").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도어락 잠금").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "퇴실 입력").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "문열림 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 이벤트\n6").is_displayed()

            self.driver.tap([(1016, 500)])
            time.sleep(1)

            #영상 이벤트 확인
            self.driver.tap([(1016, 600)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "움직임 감지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시야각 가림").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "IoT 접점 센서").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사람 감지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트\n4").is_displayed()

            pass
            print("DQS-T13638 [영상보안] 이력조회 필터의 기본값 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13652(self):
        try:
            print("DQS-T13652 [출입보안] 이력조회 기간의 검색 범위 초과 설정 시(8일 이상) 동작 확인")

            #하단 이력 조회 선택
            self.driver.tap([(362, 2081)])
            time.sleep(3)

            #조회 기간 선택
            self.driver.tap([(1016, 546)])
            time.sleep(1)

            #이전 달 이동
            self.driver.tap([(63, 483)])
            time.sleep(1)

            #3번째 주 월요일 선택
            self.driver.tap([(233, 926)])
            time.sleep(1)

            #4번째 주 월요일 선택
            self.driver.tap([(233, 1029)])
            time.sleep(1)

            #확인 버튼 클릭 후 팝업 출력 확인
            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "검색 범위 초과").is_displayed()
            searchError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='최대 검색 범위는 7일 입니다.']")
            contentDesc = searchError_Pop.get_attribute('content-desc')
            print(f"추츨한 content-desc 값 : {contentDesc}")

            #팝업 확인 버튼 클릭
            confirmPop_Btn = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.Button[@content-desc='확인'])[2]")
            confirmPop_Btn.click()

            cancle_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancle_Btn.click()

            pass
            print("DQS-T13652 [출입보안] 이력조회 기간의 검색 범위 초과 설정 시(8일 이상) 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13653(self):
        try:
            print("DQS-T13653 [영상보안] 이력조회 기간의 검색 범위 초과 설정 시(8일 이상) 동작 확인")

            #영상보안 공간 이동 - 비디오 공간
            self.driver.tap([(215, 331)])
            time.sleep(5)

            self.driver.tap([(794, 606)])
            time.sleep(3)

            #하단 이력 조회 선택
            self.driver.tap([(362, 2081)])
            time.sleep(4)

            #조회 기간 선택
            self.driver.tap([(1016, 546)])
            time.sleep(1)

            #이전 달 이동
            self.driver.tap([(63, 483)])
            time.sleep(1)

            #2번째 주 월요일 선택
            self.driver.tap([(233, 823)])
            time.sleep(1)

            #3번째 주 월요일 선택
            self.driver.tap([(233, 931)])
            time.sleep(1)

            #확인 버튼 클릭 후 팝업 출력 확인
            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "검색 범위 초과").is_displayed()
            searchError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='최대 검색 범위는 7일 입니다.']")
            contentDesc = searchError_Pop.get_attribute('content-desc')
            print(f"추츨한 content-desc 값 : {contentDesc}")

            #팝업 확인 버튼 클릭
            confirmPop_Btn = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.Button[@content-desc='확인'])[2]")
            confirmPop_Btn.click()

            cancle_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancle_Btn.click()

            pass
            print("DQS-T13653 [영상보안] 이력조회 기간의 검색 범위 초과 설정 시(8일 이상) 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()





if __name__ == '__main__':
    unittest.main()


