import datetime
import os
import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.common import NoSuchElementException

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
        password_input_box.send_keys("Wjdrnrwls100!")

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

    def test_DQS_T13730(self):
        try:
            print("DQS_T13730 Side Menu 기본UI 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "정국진\n#01020905304").is_displayed()
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
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화 상담 1522-4507").is_displayed()
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

            call = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화 상담 1522-4507")
            call.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "숫자 입력 영역").is_displayed()

            self.driver.press_keycode(4)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "전화 상담 1522-4507").is_displayed()

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

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_1\n#01090497847")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.XPATH, leadBtn)
            st3.click()

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

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2").is_displayed()

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

            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@resource-id='pf1']/android.view.View").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용약관").is_displayed()

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

            prev = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            prev.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보").is_displayed()

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

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "오픈 소스").is_displayed()

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

            prifile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_1\n#01020905304")
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

            prifile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_1\n#01020905304")
            prifile.click()

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            nameIPB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            nameIPB.send_keys("123123123")

            cancel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancel.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_1").is_displayed()

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

            prifile = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_1\n#01020905304")
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
        password_input_box.send_keys("Wjdrnrwls100!")

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

    def test_DQS_T14017(self):
        try:
            print("DQS_T14017 출입문 없는 케이스 동작 확인")

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "app_e2e_test")
            place.click()
            time.sleep(10)

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

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
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

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n수동 잠금\n도연 책상 xs2")
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

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
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

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
            door.click()

            setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2")
            setting.click()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("Test_1")

            dnIBtext = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIBtext)

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            backPress = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            backPress.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nTest_1")
            door1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\nTest_1")
            door1.click()

            setting1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_1")
            setting1.click()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("도연 책상 xs2")

            edit = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            edit.click()

            backPress = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            backPress.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")

            print("DQS_T14020 출입문명 변경 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14021(self):
        try:
            print("DQS_T14021 출입문 수동 열림 기능 동작 확인")

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
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
                    self.fail("Fail")

            backbtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            backbtn.click()

            door2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n수동 열림\n도연 책상 xs2")
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

            print("DQS_T14021 출입문 수동 열림 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14022(self):
        try:
            print("DQS_T14022 출입문 Grid 리스트에서 스와이프 시 기능 동작 확인")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2").is_displayed()

            start_x = 274
            start_y = 1600
            end_x = 848
            end_y = 1600
            self.driver.swipe(start_x, start_y, end_x, end_y)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2").is_displayed()

            start_x1 = 848
            start_y1 = 1600
            end_x1 = 274
            end_y1 = 1600

            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 bs3").is_displayed()

            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n수동 잠금\ne2e_연결끊김테스트").is_displayed()

            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n1_e2e_연결끊김테스트").is_displayed()

            self.driver.swipe(start_x, start_y, end_x, end_y)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n수동 잠금\ne2e_연결끊김테스트").is_displayed()

            self.driver.swipe(start_x, start_y, end_x, end_y)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 bs3").is_displayed()

            self.driver.swipe(start_x, start_y, end_x, end_y)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2").is_displayed()

            print("DQS_T14022 출입문 Grid 리스트에서 스와이프 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14023(self):
        try:
            print("DQS_T14023 출입문 연결 끊김 시 동작 확인")

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
            self.fail()

    def test_DQS_T14024(self):
        try:
            print("DQS_T14024 출입문 스케쥴 열림 설정 시 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음")
            st3.click()

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e스케쥴")
            st4.click()

            time.sleep(1)
            self.driver.tap([(60, 180)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\ne2e스케쥴").is_displayed()

            self.driver.tap([(60, 180)])

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n스케줄 열림\n도연 책상 xs2").is_displayed()

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

            self.driver.tap([(60, 180)])

          #- TODO 하기 테스트 항목은 스케쥴 열림 상태에서 이슈로 인하여 모니터링 -> Place Main View 진입시 이전 Door 가 출력되지 않아 임시로 변경해 놓은 상태
          #- TODO 그러하여 임의로 기존 Test Door 로 돌려 놓았으며 나중에 정상 시나리오로 변경 해야함.

            print("하기 테스트 항목은 스케쥴 열림 상태에서 이슈로 인하여 모니터링 -> Place Main View 진입시 이전 Door 가 출력되지 않아 임시로 변경해 놓은 상태\n그러하여 임의로 기존 Test Door 로 돌려 놓았으며 나중에 정상 시나리오로 변경 해야함")

            start_x1 = 274
            start_y1 = 1600
            end_x1 = 848
            end_y1 = 1600
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)


            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n스케줄 열림\n도연 책상 xs2").is_displayed()
            re = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "열림\n스케줄 열림\n도연 책상 xs2")
            re.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\ne2e스케쥴")
            st3.click()

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
            st4.click()


            print("DQS_T14024 출입문 스케쥴 열림 설정 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14025(self):
        try:
            print("DQS_T14025 출입문 스케쥴 잠금 설정 시 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\n없음")
            st3.click()

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e스케쥴")
            st4.click()

            time.sleep(1)
            self.driver.tap([(60, 180)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\ne2e스케쥴").is_displayed()

            self.driver.tap([(60, 180)])

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n스케줄 잠금\n도연 책상 xs2").is_displayed()

            self.driver.tap([(540, 2031)])

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

            self.driver.tap([(60, 180)])
            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n스케줄 잠금\n도연 책상 xs2")
            st5.click()

            st6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2")
            st6.click()

            st7 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\ne2e스케쥴")
            st7.click()

            st8 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음")
            st8.click()

            print("DQS_T14025 출입문 스케쥴 잠금 설정 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14077(self):
        try:
            print("DQS_T14077 출입문 스케쥴 잠금 설정 시 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
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

            print("DQS_T14077 출입문 스케쥴 잠금 설정 시 동작 확인 | Pass")

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

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 bs3\n잠금  ").is_displayed()

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

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 bs3\n잠금  ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_연결끊김테스트\n잠금 | 수동 잠금").is_displayed()

            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[4]")
            st3.click()

            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2").is_displayed()

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

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2\n잠금  ")
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2").is_displayed()

            self.driver.tap([(601, 767)])

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 bs3\n잠금  ")
            st4.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 bs3").is_displayed()

            self.driver.tap([(601, 767)])
            time.sleep(1)

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_연결끊김테스트\n잠금 | 수동 잠금")
            st5.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_연결끊김테스트").is_displayed()

            self.driver.tap([(601, 767)])
            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[4]")
            st2.click()

            print("DQS-T14085 출입문 리스트 뷰에서 출입문 선택 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14086(self):
        try:
            print("DQS-T14086 출입문 리스트 뷰 스와이프 시 기능 동작 확인")

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
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2\n잠금  ")
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
            self.fail()

    def test_DQS_T14164(self):
        try:
            print("DQS-T14164 출입문 스케줄 열림/잠금 스케줄 이 중복되는 시간의 스케줄 설정 시도 시 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
            st1.click()

            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2")
            st2.click()

            time.sleep(1)

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\n없음")
            st3.click()

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e스케쥴")
            st4.click()

            time.sleep(5)

            self.driver.tap([(60, 190)])

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 잠금\n없음")
            st5.click()

            time.sleep(1)

            st6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e스케쥴")
            st6.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지원 하지 않음")

            st7 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            st7.click()

            self.driver.tap([(60, 190)])

            st8 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "스케줄 열림\ne2e스케쥴")
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

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
            st1.click()

            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2")
            st2.click()

            self.driver.tap([(60, 190)])

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2").is_displayed()

            print("DQS-T14209 출입문 설정 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14210(self):
        try:
            print("DQS-T14210 출입문 설정 페이지의 출입문명 인풋 박스 유효성 검사")
            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
            door.click()

            setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2")
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

            dnIB1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            print(dnIB1)
            self.assertEqual(dnIB1, "가!@#$%^&*()")

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.clear()

            dnIB = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            dnIB.click()
            dnIB.send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012345678901234567890123456789012345678901234567890123456")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공백,-,_, 외의 특수문자는 사용할 수 없습니다.").is_displayed()

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

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
            st1.click()

            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2")
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

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
            st1.click()

            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2")
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

            door = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잠금\n도연 책상 xs2")
            door.click()

            setting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "도연 책상 xs2")
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

    def test_DQS_T14028(self):
        try:
            print("DQS-T14028 비디오 최대화/최소화 버튼 기능 동작 확인")

            self.driver.tap([(1010, 1117)])
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "app_e2e_test").is_displayed()

            self.driver.tap([(67, 1997)])
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정").is_displayed()

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

            self.driver.tap([(1010, 529)])

            st1 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st1.click()
            st1.send_keys("Test1")

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            st2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "변경이 완료 되었습니다.")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            st3.click()

            self.driver.tap([(540, 2039)])
            time.sleep(3)

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "30 개 필터 선택")
            st4.click()

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라\n16")
            st5.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1")
            time.sleep(3)

            self.driver.tap([(69, 174)])
            time.sleep(1)

            self.driver.tap([(69, 174)])
            time.sleep(3)

            self.driver.tap([(1010, 529)])

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

    def test_DQS_T14030(self):
        try:
            print("DQS-T14030 비디오 멀티뷰에서 특정 비디오 선택 시 동작 확인")

            st1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[3]")
            st1.click()
            time.sleep(1)

            self.driver.tap([(256, 657)])
            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[3]")
            st2.click()
            time.sleep(1)

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "3")
            st3.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "3").is_displayed()

            st4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[3]")
            st4.click()

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CAM-4")
            st5.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CAM-4").is_displayed()


            print("DQS-T14030 비디오 멀티뷰에서 특정 비디오 선택 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14027(self):
        try:
            print("DQS-T14027 비디오 뷰 변경 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[3]")
            st1.click()
            time.sleep(1)

            self.driver.tap([(256, 657)])
            time.sleep(1)

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[3]")
            st2.click()
            time.sleep(1)

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "3")
            st3.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "3").is_displayed()

            st4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.view.View[3]")
            st4.click()

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CAM-4")
            st5.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CAM-4").is_displayed()

            print("DQS-T14027 비디오 뷰 변경 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

if __name__ == '__main__':
    unittest.main()


