import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import os
from configuration.webDriver import AppiumConfig
from configuration.utill import capture_screenshot
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


"""
기본 테스트 계정
Standard Account
ID : 01020905304
Password : Kjstar36!!

유일한 관리자 계정
ID : 01000011111
Password : Kjstar36!!
"""

" XPath "
phoneNumberInputBox = "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]"
passwordInputBox = "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]"
" AccessBilityID "
confirm = "확인"
cancel = "취소"
allAgree = "약관 전체 동의"
nextBtn = "다음"
authenticationBtn = "인증요청"
" ClassName "
signUpPhoneNumber = "android.widget.EditText"

class IntroScreen(unittest.TestCase):

    def setUp(self):

        self.driver = AppiumConfig.get_driver()
        self.driver.implicitly_wait(15)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_DQS_T13681(self):
        print("DQS_T13681 로그인/로그아웃 기능 동작 확인")
        try:
            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()

            time.sleep(5)

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            phone_input_box.click()
            self.driver.press_keycode(7) #0
            self.driver.press_keycode(8) #1
            self.driver.press_keycode(7) #0
            self.driver.press_keycode(9) #2
            self.driver.press_keycode(7) #0
            self.driver.press_keycode(16) #9
            self.driver.press_keycode(7) #0
            self.driver.press_keycode(12) #5
            self.driver.press_keycode(10) #3
            self.driver.press_keycode(7) #0
            self.driver.press_keycode(11) #4

            password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()

            time.sleep(10)

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logout_button.click()

            logout_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='로그아웃 하시겠습니까?\n자동로그인 기능이 해제 됩니다.']")
            contentDesc = logout_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "로그아웃 하시겠습니까?\n자동로그인 기능이 해제 됩니다.")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            pass

            print("DQS_T13681 로그인/로그아웃 기능 동작 확인 | Pass")
        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print(f"{self._testMethodName} | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13682(self):
        try:
            print("DQS_T13682 자동 로그인 기능 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            phone_input_box.click()
            phone_input_box.send_keys("01000011111")

            password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()

            time.sleep(5)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상").is_displayed()

            self.driver.quit()

            time.sleep(5)

            options = UiAutomator2Options()
            options.platform_name = 'Android'
            options.device_name = 'R59M906R2SF'
            options.app_package = 'com.suprema.moon'
            options.app_activity = 'com.suprema.moon.MainActivity'
            options.automation_name = 'UiAutomator2'
            options.auto_grant_permissions = True
            options.no_reset = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상").is_displayed()

            pass

            print("DQS_T13682 자동 로그인 기능 동작 확인 | Pass")
        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13682 자동 로그인 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13683(self):
        try:
            print("DQS_T13683 로그인 실패 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            phone_input_box.click()
            phone_input_box.send_keys("01020905305")

            password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
            password_input_box.click()
            password_input_box.send_keys("111111")

            for _ in range(3):

                login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
                login_button.click()

                popUpTest1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.")
                self.assertIsNotNone(popUpTest1, "로그인 실패 팝업이 출력되지 않았습니다.")

                loginFail_msg1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.']")
                contentDesc1 = loginFail_msg1.get_attribute('content-desc')
                print(f"추출한 content-desc 값 : {contentDesc1}")
                self.assertEqual(contentDesc1, "휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.")

                confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirm.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text=\"010 2090 5305\"]/android.widget.ImageView")
            phone_input_box.click()
            phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            phone_input_box.click()
            phone_input_box.send_keys("01020905306")

            password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!@")

            for _ in range(3):

                login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
                login_button.click()

                popUpTest2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.")
                self.assertIsNotNone(popUpTest2, "로그인 실패 팝업이 출력되지 않았습니다.")

                loginFail_msg2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.']")
                contentDesc2 = loginFail_msg2.get_attribute('content-desc')
                print(f"추출한 content-desc 값 : {contentDesc2}")
                self.assertEqual(contentDesc2, "휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.")

                confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
                confirm.click()

            # 해당 계정 로그인 후 로그아웃하여 계정 로그인 실패횟수 초기화
            password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()

            time.sleep(10)

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logout_button.click()

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()
            time.sleep(1)

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            phone_input_box.click()
            phone_input_box.send_keys("01020905305")

            password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()

            time.sleep(5)

            pass
            print("DQS_T13683 로그인 실패 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13683 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13671(self):
        try:
            print("DQS_T13671 공간의 유일한 관리자 회원 탈퇴 시도 시 동작 확인")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            phone_input_box.click()
            phone_input_box.send_keys("01000033333")

            password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

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
            options.device_name = 'R59M906R2SF'
            options.app_package = 'com.suprema.moon'
            options.app_activity = 'com.suprema.moon.MainActivity'
            options.automation_name = 'UiAutomator2'
            options.auto_grant_permissions = True
            options.no_reset = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입만 공간").is_displayed()

            pass

            print("DQS_T13671 공간의 유일한 관리자 회원 탈퇴 시도 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13683 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13677(self):
        try:
            print("DQS_T13677 회원가입 휴대폰 번호 입력 페이지에서 올바르지 않은 번호 입력시 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "만 14세 이상입니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용 약관 동의").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집 및 이용 동의").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리업무 위수탁 계약").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음").is_displayed()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
            isagree = agree.is_enabled()
            self.assertTrue(isagree,"약관 전체 동의 버튼이 활성화되어 있습니다.")

            agree1= self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "만 14세 이상입니다.")
            isagree1 = agree1.is_enabled()
            self.assertTrue(isagree1,"만 14세 이상입니다. 버튼이 활성화되어 있습니다.")

            agree2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이용 약관 동의")
            isagree2 = agree2.is_enabled()
            self.assertTrue(isagree2,"이용 약관 동의 버튼이 활성화되어 있습니다.")

            agree3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 수집 및 이용 동의")
            isagree3 = agree3.is_enabled()
            self.assertTrue(isagree3,"개인정보 수집 및 이용 동의 버튼이 활성화되어 있습니다.")

            agree4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리업무 위수탁 계약")
            isagree4 = agree4.is_enabled()
            self.assertTrue(isagree4,"개인정보 처리업무 위수탁 계약 버튼이 활성화되어 있습니다.")

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

            phoNo.send_keys("123456789")
            #cl5 = phoNo.text
            cl5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 456 789']")
            numtext = cl5.get_attribute('text')
            print(f"추출한 content-desc 값 : {numtext}")
            self.assertEqual("123 456 789", numtext)

            wrongPhoNum = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.']")
            contentDesc = wrongPhoNum.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.")

            next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            next.click()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청").is_displayed()

            pass

            print("DQS_T13677 회원가입 휴대폰 번호 입력 페이지에서 올바르지 않은 번호 입력시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13677 회원가입 휴대폰 번호 입력 페이지에서 올바르지 않은 번호 입력시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13685(self):
        try:
            print("DQS_T13685 회원가입 휴대폰 번호 입력 페이지에서 존재하는 번호 입력 시 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
            agree.click()

            next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next.click()

            phoNo = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            phoNo.click()
            phoNo.send_keys("01020905304")

            authButton = next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            authButton.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미 가입된 번호입니다.").is_displayed()
            phoDeplicate_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='이미 가입된 번호입니다.']")
            contentDesc = phoDeplicate_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "이미 가입된 번호입니다.")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            phoNo = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            assertt = phoNo.text
            self.assertEqual(assertt, "010 2090 5304")

            pass

            print("DQS_T13685 회원가입 휴대폰 번호 입력 페이지에서 존재하는 번호 입력 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13685 회원가입 휴대폰 번호 입력 페이지에서 존재하는 번호 입력 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13718(self):
        try:

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

            pass

            print("DQS_T13718 회원가입 페이지의 약관 동의 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T13718 회원가입 페이지의 약관 동의 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14133(self):
        try:

            print("DQS_T14133 로그인 페이지 휴대폰 번호 인풋 박스 유효성 검사")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            st2.click()
            st2.send_keys("1234567890123450000")
            er = st2.text
            print(er)
            self.assertEqual("123 4567 8901", er)
            st2.clear()

            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            st3.click()
            text_to_input = "ABCDEFG"
            er3 = st3.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er3)
            st3.clear()

            st4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            st4.click()
            text_to_input = "abcdefg"
            er4 = st4.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er4)
            st4.clear()

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            st5.click()
            text_to_input = "가나다라마바사"
            er5 = st5.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er5)
            st5.clear()

            st6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            st6.click()
            text_to_input = "!@#$%^&*()"
            er6 = st6.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er6)
            st6.clear()

            st7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            st7.click()
            st7.send_keys("123456789")
            er7 = st7.text
            print(er7)
            time.sleep(3)
            self.assertEqual("123 456 789", er7)
            st7.clear()

            st8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            st8.click()
            st8.send_keys("01012345678")
            er8 = st8.text
            print(er8)
            self.assertEqual("010 1234 5678", er8)
            st8.clear()

            pass

            print("DQS_T14133 로그인 페이지 휴대폰 번호 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T14133 로그인 페이지 휴대폰 번호 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14134(self):
        try:
            print("DQS_T14134 로그인 페이지 휴대폰 번호 X 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            try:
                self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 1111 2222']/android.widget.ImageView")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            st2.click()
            st2.send_keys("01011112222")

            self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 1111 2222']/android.widget.ImageView").is_displayed()
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 1111 2222']/android.widget.ImageView")
            st3.click()

            st4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            re = st4.text
            print(re)
            self.assertEqual("", re)

            try:
                self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            pass

            print("DQS_T14134 로그인 페이지 휴대폰 번호 X 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T14134 로그인 페이지 휴대폰 번호 X 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14135(self):
        try:
            print("DQS_T14135 로그인 페이지 휴대폰 번호 인풋 박스 Hint 문구 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox).is_displayed()
            st2 = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            st2.click()
            st2.send_keys("1")
            time.sleep(3)

            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1']/android.widget.ImageView")
            st3.click()

            self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]").is_displayed()

            pass

            print("DQS_T14135 로그인 페이지 휴대폰 번호 인풋 박스 Hint 문구 기능 동작 확인 | Pass")
        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T14135 로그인 페이지 휴대폰 번호 인풋 박스 Hint 문구 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14137(self):
        try:
            print("DQS-T14137 로그인 페이지에서 비밀번호만 입력한 경우 로그인 실패 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            st2.click()
            st2.send_keys("Kjstar36!!")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.").is_displayed()
            onlyPass_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.']")
            contentDesc = onlyPass_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.")

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st4.click()

            pass

            print("DQS-T14137 로그인 페이지에서 비밀번호만 입력한 경우 로그인 실패 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14137 로그인 페이지에서 비밀번호만 입력한 경우 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14138(self):
        try:
            print("DQS-T14138 로그인 페이지에서 휴대폰 번호만 입력한 경우 로그인 실패 동작 확인")
            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            st2.click()
            st2.send_keys("01000011111")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.").is_displayed()
            onlyPho_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.']")
            contentDesc = onlyPho_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.")

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st4.click()

            pass

            print("DQS-T14138 로그인 페이지에서 휴대폰 번호만 입력한 경우 로그인 실패 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14138 로그인 페이지에서 휴대폰 번호만 입력한 경우 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14141(self):
        try:
            print("DQS-T14141 로그인 페이지에서 가입되지 않은 휴대폰 번호로 로그인 시도 시 로그인 실패 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, phoneNumberInputBox)
            st2.click()
            st2.send_keys("01045614689")
            #가입되지 않는 폰번호 입력

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.").is_displayed()
            notRegister_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.']")
            contentDesc = notRegister_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.")

            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st4.click()

            pass

            print("DQS-T14141 로그인 페이지에서 가입되지 않은 휴대폰 번호로 로그인 시도 시 로그인 실패 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14141 로그인 페이지에서 가입되지 않은 휴대폰 번호로 로그인 시도 시 로그인 실패 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14142(self):
        try:
            print("DQS-T14142 회원가입 페이지의 휴대폰 번호 인풋 박스 유효성 검사")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, nextBtn)
            st2.click()

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
            st3.click()
            text_to_input = "ABCDEFG"
            er3 = st3.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er3)
            st3.clear()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
            st4.click()
            text_to_input = "abcdefg"
            er4 = st4.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er4)
            st4.clear()

            st5 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
            st5.click()
            text_to_input = "가나다라마바사"
            er5 = st5.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er5)
            st5.clear()

            st6 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
            st6.click()
            text_to_input = "!@#$%^&*()"
            er6 = st6.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er6)
            st6.clear()

            st7 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
            st7.click()
            st7.send_keys("123456789")
            textKey1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 456 789']")
            text1 = textKey1.get_attribute('text')
            print(f"추출한 text 값 : {text1}")
            self.assertEqual("123 456 789", text1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.").is_displayed()
            phoNum1_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.']")
            contentDesc1 = phoNum1_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.")
            st7.clear()

            st8 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
            st8.click()
            st8.send_keys("1234567890123450000")
            textKey2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 4567 8901']")
            text2 = textKey2.get_attribute('text')
            print(f"추출한 text 값 : {text2}")
            self.assertEqual("123 4567 8901", text2)
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청").click()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "필수 입력 사항이 누락되었습니다.").is_displayed()

            phoNum2_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='필수 입력 사항이 누락되었습니다.']")
            contentDesc2 = phoNum2_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "필수 입력 사항이 누락되었습니다.")

            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm).click()
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 4567 8901']/android.widget.ImageView").click()

            st9 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
            st9.click()
            st9.send_keys("01012345678")
            textKey3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 1234 5678']")
            text3 = textKey3.get_attribute('text')
            print(f"추출한 text 값 : {text3}")
            self.assertEqual("010 1234 5678", text3)
            st9.clear()
            pass

            print("DQS-T14142 회원가입 페이지의 휴대폰 번호 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14142 회원가입 페이지의 휴대폰 번호 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14144(self):
        try:

            print("DQS-T14144 회원가입 페이지의 휴대폰 번호 인풋 박스 X버튼 기능 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, nextBtn)
            st2.click()

            try:
                self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 2222 1111']/android.widget.ImageView")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st2 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
            st2.click()
            st2.send_keys("01022221111")

            self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 2222 1111']/android.widget.ImageView").is_displayed()
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 2222 1111']/android.widget.ImageView")
            st3.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
            re = st4.text
            print(re)
            self.assertEqual("", re)

            try:
                self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            pass

            print("DQS-T14144 회원가입 페이지의 휴대폰 번호 인풋 박스 X버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14144 회원가입 페이지의 휴대폰 번호 인풋 박스 X버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14145_T13678(self):
        try:
            print("DQS-T14145 회원가입 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사 || DQS-13678 회원가입 인증번호 입력 페이지에서 올바르지 않은 인증번호 입력 시 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, nextBtn)
            st3.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
            st4.click()
            st4.send_keys("01087561455")

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authenticationBtn)
            st5.click()

            time.sleep(3)

            st6 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st6.click()
            st6.send_keys("ABCDEFG")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증번호는 6자리 숫자입니다.").is_displayed()
            authText_Msg1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증번호는 6자리 숫자입니다.']")
            contentDesc1 = authText_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "인증번호는 6자리 숫자입니다.")
            st11 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            st11.click()
            st6.clear()

            st7 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st7.click()
            st7.send_keys("abcdefg")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증번호는 6자리 숫자입니다.").is_displayed()
            authText_Msg2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증번호는 6자리 숫자입니다.']")
            contentDesc2 = authText_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "인증번호는 6자리 숫자입니다.")
            st11 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            st11.click()
            st7.clear()

            st8 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st8.click()
            st8.send_keys("가나다라마바사")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증번호는 6자리 숫자입니다.").is_displayed()
            authText_Msg3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증번호는 6자리 숫자입니다.']")
            contentDesc3 = authText_Msg3.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc3}")
            self.assertEqual(contentDesc1, "인증번호는 6자리 숫자입니다.")
            st11 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            st11.click()
            st8.clear()

            st9 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st9.click()
            st9.send_keys("!@#$%^&*()")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증번호는 6자리 숫자입니다.").is_displayed()
            authText_Msg4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증번호는 6자리 숫자입니다.']")
            contentDesc4 = authText_Msg4.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc4}")
            self.assertEqual(contentDesc1, "인증번호는 6자리 숫자입니다.")
            st11 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            st11.click()
            st9.clear()

            st10 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st10.click()
            st10.send_keys("123")
            authNum_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증번호는 6자리 숫자입니다.']")
            contentDesc5 = authNum_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc5}")
            self.assertEqual(contentDesc5, "인증번호는 6자리 숫자입니다.")
            st11 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            st11.click()
            st10.clear()

            st12 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st12.click()
            st12.send_keys("9876543210")
            er13 = st12.text
            print(er13)
            self.assertEqual("987654", er13)
            time.sleep(3)
            st12.clear()

            st13 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st13.click()
            st13.send_keys("123456")
            st11 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            st11.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.").is_displayed()
            authError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.']")
            contentDesc6 = authError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc6}")
            self.assertEqual(contentDesc6, "인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.")
            st14 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st14.click()

            pass

            print("DQS-T14145 회원가입 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사 || DQS-13678 회원가입 인증번호 입력 페이지에서 올바르지 않은 인증번호 입력 시 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14145 회원가입 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사 || DQS-13678 회원가입 인증번호 입력 페이지에서 올바르지 않은 인증번호 입력 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14153(self):
        try:
            print("DQS-T14153 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 유효성 검사")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st3.click()
            text_to_input = "ABCDEFG"
            er3 = st3.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er3)
            st3.clear()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st4.click()
            text_to_input = "abcdefg"
            er4 = st4.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er4)
            st4.clear()

            st5 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st5.click()
            text_to_input = "가나다라마바사"
            er5 = st5.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er5)
            st5.clear()

            st6 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st6.click()
            text_to_input = "!@#$%^&*()"
            er6 = st6.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er6)
            st6.clear()

            st7 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st7.click()
            st7.send_keys("123456789")
            #er7 = st7.text
            er7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 456 789']")
            text1 = er7.get_attribute('text')
            print(f"추출한 text 값 : {text1}")
            time.sleep(3)
            self.assertEqual("123 456 789", text1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.").is_displayed()
            wrongPho_Text = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.']")
            contentDesc1 = wrongPho_Text.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.")
            st7.clear()

            st8 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st8.click()
            st8.send_keys("1234567890123450000")
            er8 = st8.text
            print(er8)
            self.assertEqual("123 4567 8901", er8)
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청").click()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "필수 입력 사항이 누락되었습니다.").is_displayed()
            noPass_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='필수 입력 사항이 누락되었습니다.']")
            contentDesc2 = noPass_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "필수 입력 사항이 누락되었습니다.")
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm).click()
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 4567 8901']/android.widget.ImageView").click()

            st9 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st9.click()
            st9.send_keys("01012345678")
            er9 = st9.text
            print(er9)
            self.assertEqual("010 1234 5678", er9)
            st9.clear()

            pass

            print("DQS-T14153 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 유효성 검사 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14153 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14154(self):
        try:
            print("DQS-T14154 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 X 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            try:
                self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 2222 1111']/android.widget.ImageView")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st3.click()
            st3.send_keys("01022221111")

            self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 2222 1111']/android.widget.ImageView").is_displayed()
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010 2222 1111']/android.widget.ImageView")
            st3.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            re = st4.text
            print(re)
            self.assertEqual("", re)

            try:
                self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText/android.widget.ImageView")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            pass

            print("DQS-T14154 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 X 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14154 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 X 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14155(self):
        try:
            print("DQS-T14155 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 Hint 문구 기능 동작 확인")
            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            #stEdit = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").text
            #print(stEdit)
            #self.assertEqual("010부터 휴대폰 번호를 입력해 주세요.", stEdit)

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st3.send_keys("1")

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1']/android.widget.ImageView").is_displayed()
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1']/android.widget.ImageView")
            st3.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            re = st4.text
            print(re)
            self.assertEqual("", re)

            pass

            print("DQS-T14155 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 Hint 문구 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14155 비밀번호 찾기 페이지의 휴대폰 번호 인풋 박스 Hint 문구 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14223(self):
        try:
            print("DQS-T14223 회원가입 휴대폰 번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
            agree.click()

            next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next.click()

            st1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호']/android.view.View/android.widget.ImageView")
            st1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Dev-Server").is_displayed()

            pass

            print("DQS-T14223 회원가입 휴대폰 번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14223 회원가입 휴대폰 번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14224(self):
        try:
            print("DQS-T14224 회원가입 휴대폰 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
            agree.click()

            next = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            next.click()

            st = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st.click()
            st.send_keys("01079461346")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            st1.click()

            time.sleep(3)

            st2 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            st2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")

            pass

            print("DQS-T14224 회원가입 휴대폰 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14224 회원가입 휴대폰 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14222(self):
        try:
            print("DQS-T14222 회원가입 약관 동의 페이지의 뒤로가기 버튼 기능 동작 확인")

            SignUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            SignUp.click()

            st1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            st1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Dev-Server").is_displayed()

            pass

            print("DQS-T14222 회원가입 약관 동의 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14222 회원가입 약관 동의 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14220(self):
        try:
            print("DQS-T14220 비밀번호 찾기 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st2 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st2.click()
            st2.send_keys("01099887766")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            st3.click()
            time.sleep(3)

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
            st4.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호").is_displayed()

            pass

            print("DQS-T14220 비밀번호 찾기 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14220 비밀번호 찾기 인증번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14219(self):
        try:
            print("DQS-T14219 비밀번호 찾기 휴대폰 번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호']/android.view.View/android.widget.ImageView")
            st3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n비밀번호").is_displayed()

            pass

            print("DQS-T14219 비밀번호 찾기 휴대폰 번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14219 비밀번호 찾기 휴대폰 번호 입력 페이지의 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14218(self):
        try:
            print("DQS-T14218 로그인 페이지에서 뒤로가기 버튼 기능 동작 확인")
            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='휴대폰 번호\n비밀번호']/android.view.View[1]/android.widget.ImageView")
            st2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Dev-Server").is_displayed()

            pass

            print("DQS-T14218 로그인 페이지에서 뒤로가기 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14218 로그인 페이지에서 뒤로가기 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14215(self):
        try:
            print("DQS-T14215 회원가입 인증번호 입력 페이지의 인증번호 인풋 박스 Hint 문구 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, nextBtn)
            st3.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
            st4.click()
            st4.send_keys("01078941221")

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authenticationBtn)
            st5.click()

            time.sleep(3)

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st3.send_keys("1")

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1']").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증번호는 6자리 숫자입니다.").is_displayed() #문구 출력 확인

            element_xpath = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증번호는 6자리 숫자입니다.']")
            content_desc = element_xpath.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {content_desc}")
            self.assertEqual(content_desc, "인증번호는 6자리 숫자입니다.")
            st3.clear()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            re = st4.text
            self.assertEqual("", re)

            pass

            print("DQS-T14215 회원가입 인증번호 입력 페이지의 인증번호 인풋 박스 Hint 문구 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14215 회원가입 인증번호 입력 페이지의 인증번호 인풋 박스 Hint 문구 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14161(self):
        try:
            print("DQS_T14161 회원가입 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, nextBtn)
            st3.click()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, signUpPhoneNumber)
            st4.click()
            st4.send_keys("01022548778")

            st5 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authenticationBtn)
            st5.click()

            time.sleep(3)

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st3.send_keys("123456")

            time.sleep(200)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "0분 0초").is_displayed()

            st6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            st6.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+82 01022548778").is_displayed()

            st7 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송")
            st7.click()

            st8 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st8.click()
            st8.send_keys("112233") #123456으로 입력되어짐
            time.sleep(3)

            st6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            st6.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 코드 오류").is_displayed()
            authError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.']")
            contentDesc = authError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.")

            pass

            print("DQS_T14161 회원가입 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T14161 회원가입 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14136(self):
        try:
            print("DQS-T14136 로그인 페이지 비밀번호 인풋 박스 Hint 문구 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            assert self.driver.find_element(AppiumBy.XPATH, passwordInputBox).is_displayed()

            st2 = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            st2.click()
            st2.send_keys("1")

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='•']").is_displayed()

            st3 = self.driver.find_element(AppiumBy.XPATH, passwordInputBox)
            st3.clear()

            assert self.driver.find_element(AppiumBy.XPATH, passwordInputBox).is_displayed()

            pass

            print("DQS-T14136 로그인 페이지 비밀번호 인풋 박스 Hint 문구 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14136 로그인 페이지 비밀번호 인풋 박스 Hint 문구 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14143(self):
        try:
            print("DQS-T14143 회원가입 페이지의 휴대폰 번호 인풋 박스 Hint 문구 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
            st2.click()

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, nextBtn)
            st3.click()

            assert self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").is_displayed()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st4.click()
            st4.send_keys("1")

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1']/android.widget.ImageView").is_displayed()

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1']/android.widget.ImageView")
            st5.click()

            assert self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").is_displayed()

            pass

            print("DQS-T14143 회원가입 페이지의 휴대폰 번호 인풋 박스 Hint 문구 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14143 회원가입 페이지의 휴대폰 번호 인풋 박스 Hint 문구 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14157(self):
        try:
            print("DQS-T14157 비밀번호 찾기 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st2 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st2.click()
            st2.send_keys("01055555555")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            st3.click()
            time.sleep(3)

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st3.click()
            st3.send_keys("ABCDEFG")
            er3 = st3.text
            self.assertEqual("ABCDEF", er3)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증번호는 6자리 숫자입니다.")
            authText_Msg1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증번호는 6자리 숫자입니다.']")
            contentDesc1 = authText_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "인증번호는 6자리 숫자입니다.")
            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            atBtn.click()
            st3.clear()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st4.click()
            st4.send_keys("abcdef")
            er4 = st4.text
            self.assertEqual("abcdef", er4)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증번호는 6자리 숫자입니다.")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증번호는 6자리 숫자입니다.").is_displayed()
            authText_Msg2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증번호는 6자리 숫자입니다.']")
            contentDesc2 = authText_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "인증번호는 6자리 숫자입니다.")
            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            atBtn.click()
            st4.clear()

            st5 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st5.click()
            st5.send_keys("가나다라마바")
            er5 = st5.text
            self.assertEqual("가나다라마바", er5)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증번호는 6자리 숫자입니다.")
            authText_Msg3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증번호는 6자리 숫자입니다.']")
            contentDesc3 = authText_Msg3.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc3}")
            self.assertEqual(contentDesc1, "인증번호는 6자리 숫자입니다.")
            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            atBtn.click()
            st5.clear()

            st6 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st6.click()
            st6.send_keys("!@#$%^&*()")
            er6 = st6.text
            self.assertEqual("!@#$%^", er6)
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증번호는 6자리 숫자입니다.")
            authText_Msg4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증번호는 6자리 숫자입니다.']")
            contentDesc4 = authText_Msg4.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc4}")
            self.assertEqual(contentDesc1, "인증번호는 6자리 숫자입니다.")
            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            atBtn.click()
            st6.clear()

            st7 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st7.click()
            st7.send_keys("123")
            authNum_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증번호는 6자리 숫자입니다.']")
            contentDesc5 = authNum_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc5}")
            self.assertEqual(contentDesc5, "인증번호는 6자리 숫자입니다.")
            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            atBtn.click()
            st7.clear()

            st8 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st8.click()
            st8.send_keys("9876543210")
            er8 = st8.text
            self.assertEqual("987654", er8)
            time.sleep(3)
            st8.clear()

            st9 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st9.click()
            st9.send_keys("123456")
            atBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            atBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.").is_displayed()
            # 회원가입 씬에서 출력된 팝업 문구와 비밀번호 찾기 씬에서 출력되는 팝업 문구가 상이함, 회원가입 씬에서 발생하는 문구로 작성되어 있어서 Fail 발생함, 사양 확정 후 TC보완예정
            authError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.']")
            contentDesc6 = authError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc6}")
            self.assertEqual(contentDesc6, "인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.")
            st10 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            st10.click()

            pass

            print("DQS-T14157 비밀번호 찾기 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사| Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14157 비밀번호 찾기 인증번호 입력 페이지의 인증번호 인풋 박스 유효성 검사 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14158(self):
        try:
            print("DQS-T14158 비밀번호 찾기 인증번호 입력 페이지의 인증번호 인풋 박스 Hint 문구 기능 동작 확인")
            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st2 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st2.click()
            st2.send_keys("01000066666")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            st3.click()
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").is_displayed()

            st4 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st4.click()
            st4.send_keys("1")

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1']").is_displayed()

            st5 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st5.clear()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText").is_displayed()

            pass

            print("DQS-T14158 DQS-T14158 비밀번호 찾기 인증번호 입력 페이지의 인증번호 인풋 박스 Hint 문구 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14158 DQS-T14158 비밀번호 찾기 인증번호 입력 페이지의 인증번호 인풋 박스 Hint 문구 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T14160_T14159(self):
        try:
            print("DQS-T14160 비밀번호 찾기 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인 || DQS_T14159 비밀번호 찾기 인증번호 입력 페이지의 인증번호 재전송 버튼 기능 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st2 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st2.click()
            st2.send_keys("01033333333")

            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            st3.click()
            time.sleep(3)

            st4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st4.send_keys("123456")

            time.sleep(181)
            print("3분 대기중.......................")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "0분 0초").is_displayed()

            st6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            st6.click()

            st7 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "재전송")
            st7.click()

            ID_check = ["2분 29초", "2분 28초", "2분 27초", "2분 26초"]

            element_found = False
            for id in ID_check:
                elements = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, id)
                if len(elements) > 0:
                    element_found = True
                    break

            self.assertTrue(element_found, "None of the specified elements were found")

            st8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st8.click()
            st8.send_keys("")
            time.sleep(1)

            st9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st9.click()
            st9.send_keys("112233")
            time.sleep(3)

            st10 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
            st10.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 코드 오류").is_displayed()
            # 회원가입 씬에서 출력된 팝업 문구와 비밀번호 찾기 씬에서 출력되는 팝업 문구가 상이함, 회원가입 씬에서 발생하는 문구로 작성되어 있어서 Fail 발생함, 사양 확정 후 TC보완예정
            authError_Pop = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.']")
            contentDesc = authError_Pop.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "인증 코드가 일치하지 않습니다. \n다시 입력해 주세요.")

            pass

            print("DQS-T14160 비밀번호 찾기 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인 || DQS_T14159 비밀번호 찾기 인증번호 입력 페이지의 인증번호 재전송 버튼 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T14160 비밀번호 찾기 인증번호 입력 페이지의 인증시간 만료 시 기능 동작 확인 || DQS_T14159 비밀번호 찾기 인증번호 입력 페이지의 인증번호 재전송 버튼 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T13684(self):
        try:
            print("DQS-T13684 비밀번호 찾기 기능 중 가입하지 않은 휴대폰 번호 입력 시 동작 확인")

            st1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            st1.click()

            st2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 찾기")
            st2.click()

            st3 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st3.click()
            st3.send_keys("123456789")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호\n올바른 휴대폰 번호를 입력해 주세요.").is_displayed()

            st4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123 456 789']/android.widget.ImageView")
            st4.click()
            time.sleep(1)

            st5 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st5.click()
            st5.send_keys("11111111111")

            st6 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            st6.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "잘못된 요청").is_displayed()
            wrongPhoneNum_Msg1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='필수 입력 사항이 누락되었습니다.']")
            contentDesc1 = wrongPhoneNum_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "필수 입력 사항이 누락되었습니다.")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()

            st7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='111 1111 1111']/android.widget.ImageView")
            st7.click()
            time.sleep(1)

            st8 = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            st8.click()
            st8.send_keys("01075529810") #회원가입이 안된 전화번호 입력

            st9 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
            st9.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인 정보 오류").is_displayed()
            wrongPhoneNum_Msg2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.']")
            contentDesc2 = wrongPhoneNum_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "휴대폰 번호 혹은 비밀번호를\n다시 확인해 주세요.")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()

            pass

            print("DQS-T13684 비밀번호 찾기 기능 중 가입하지 않은 휴대폰 번호 입력 시 동작 확인| Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS-T13684 비밀번호 찾기 기능 중 가입하지 않은 휴대폰 번호 입력 시 동작 확인 | Failed")
            print(str(e))
            self.fail()

if __name__ == '__main__':
    unittest.main()
