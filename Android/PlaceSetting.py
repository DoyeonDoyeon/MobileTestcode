#import datetime
import os
import time
import unittest
#from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#from appium.options.android import UiAutomator2Options
from selenium.common import NoSuchElementException
#from selenium.webdriver.common.action_chains import ActionChains
#from configuration.utill import capture_screenshot
from configuration.webDriver import AppiumConfig
#from configuration.utill import swipe_until_element_found, swipe_up, capture_screenshot, extract_verification_code
from configuration.utill import capture_screenshot

checkFalse = "false"
checkTrue = "true"


class AlramMenu(unittest.TestCase):

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

    def test_DQS_T15894(self):
        try:
            print("DQS_T15894 [출입보안] 공간 설정에 알람 설정 UI 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            #출입문 이벤트 출력 확인 - 기본값 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 이벤트").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카카오 QR인증 성공시 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 성공시 알람']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카카오 QR인증 실패시 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 실패시 알람']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "네이버 QR인증 성공시 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 성공시 알람']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "네이버 QR인증 실패시 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 실패시 알람']/android.widget.Switch").is_displayed()

            #시스템 이벤트 출력 확인 - 기본값 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시스템 이벤트").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "문열림 알람(Tamper)").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='문열림 알람(Tamper)']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "강제 문열림 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='강제 문열림 알람']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "장시간 문열림 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='장시간 문열림 알람']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "미허가 인증수단 시도 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='미허가 인증수단 시도 알람']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 장애 상태 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문 장애 상태 알람']/android.widget.Switch").is_displayed()

            pass
            print("DQS_T15894 [출입보안] 공간 설정에 알람 설정 UI 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15894 [출입보안] 공간 설정에 알람 설정 UI 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15895(self):
        try:
            print("DQS_T15895 [영상보안] 공간 설정에 알람 설정 UI 확인")

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상")
            place.click()
            time.sleep(5)

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            #출입문 이벤트 출력 확인 - 기본값 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 이벤트").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카카오 QR인증 성공시 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 성공시 알람']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카카오 QR인증 실패시 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 실패시 알람']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "네이버 QR인증 성공시 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 성공시 알람']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "네이버 QR인증 실패시 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 실패시 알람']/android.widget.Switch").is_displayed()

            #시스템 이벤트 출력 확인 - 기본값 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시스템 이벤트").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "문열림 알람(Tamper)").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='문열림 알람(Tamper)']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "강제 문열림 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='강제 문열림 알람']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "장시간 문열림 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='장시간 문열림 알람']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "미허가 인증수단 시도 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='미허가 인증수단 시도 알람']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 장애 상태 알람").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문 장애 상태 알람']/android.widget.Switch").is_displayed()

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            #영상 감시 이벤트 출력 확인 - 기본값 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "움직임 감지").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='움직임 감지']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시야각 가림").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='시야각 가림']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "IoT 접점 센서").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='IoT 접점 센서']/android.widget.Switch").is_displayed()

            #영상 이벤트 순서 오류 출력 확인 - 기본값 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 이벤트 순서 오류").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내부 오류").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='내부 오류']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "연결 해제").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연결 해제']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "디스크 공간 없음").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='디스크 공간 없음']/android.widget.Switch").is_displayed()

            #IoT 이벤트 순서 오류 출력 확인 - 기본값 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "IoT 이벤트 순서 오류").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "센서 분리").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='센서 분리']/android.widget.Switch").is_displayed()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "배터리 얼마남지 않음").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='배터리 얼마남지 않음']/android.widget.Switch").is_displayed()

            pass
            print("DQS_T15895 [영상보안] 공간 설정에 알람 설정 UI 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15895 [영상보안] 공간 설정에 알람 설정 UI 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15896(self):
        try:
            print("DQS_T15896 출입 통제에 출입문 이벤트 알람 설정 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            #카카오 QR인증 성공시 알람 이벤트만 설정
            acKakaoFail = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 실패시 알람']/android.widget.Switch")
            acKakaoFail.click()
            time.sleep(2)

            acNaverSuccess = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 성공시 알람']/android.widget.Switch")
            acNaverSuccess.click()
            time.sleep(2)

            acNaverFail = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 실패시 알람']/android.widget.Switch")
            acNaverFail.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 성공시 알람']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkTrue

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 실패시 알람']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkFalse

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 성공시 알람']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkFalse

            check4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 실패시 알람']/android.widget.Switch")
            is_checked_str4 = check4.get_attribute('checked')
            print(is_checked_str4)
            assert is_checked_str4 == checkFalse

            #네이버 QR인증 성공시 알람 이벤트만 설정
            acKakaoSucess = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 성공시 알람']/android.widget.Switch")
            acKakaoSucess.click()
            time.sleep(2)

            acNaverSuccess = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 성공시 알람']/android.widget.Switch")
            acNaverSuccess.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 성공시 알람']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkFalse

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 실패시 알람']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkFalse

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 성공시 알람']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkTrue

            check4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 실패시 알람']/android.widget.Switch")
            is_checked_str4 = check4.get_attribute('checked')
            print(is_checked_str4)
            assert is_checked_str4 == checkFalse

            #카카오 QR인증 실패시 알람 이벤트만 설정
            acNaverSuccess = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 성공시 알람']/android.widget.Switch")
            acNaverSuccess.click()
            time.sleep(2)

            acKakaoFail = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 실패시 알람']/android.widget.Switch")
            acKakaoFail.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 성공시 알람']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkFalse

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 실패시 알람']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkTrue

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 성공시 알람']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkFalse

            check4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 실패시 알람']/android.widget.Switch")
            is_checked_str4 = check4.get_attribute('checked')
            print(is_checked_str4)
            assert is_checked_str4 == checkFalse

            #네이버 QR인증 실패시 알람 이벤트만 설정
            acKakaoFail = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 실패시 알람']/android.widget.Switch")
            acKakaoFail.click()
            time.sleep(2)

            acNaverFail = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 실패시 알람']/android.widget.Switch")
            acNaverFail.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 성공시 알람']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkFalse

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='카카오 QR인증 실패시 알람']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkFalse

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 성공시 알람']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkFalse

            check4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='네이버 QR인증 실패시 알람']/android.widget.Switch")
            is_checked_str4 = check4.get_attribute('checked')
            print(is_checked_str4)
            assert is_checked_str4 == checkTrue

            pass
            print("DQS_T15896 출입 통제에 출입문 이벤트 알람 설정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15896 출입 통제에 출입문 이벤트 알람 설정 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15897(self):
        try:
            print("DQS_T15897 출입 통제에 시스템 이벤트 알람 설정 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            #문열림 알람(Tamper) 이벤트만 설정
            forceDoor = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='강제 문열림 알람']/android.widget.Switch")
            forceDoor.click()
            time.sleep(2)

            longTimeDoor = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='장시간 문열림 알람']/android.widget.Switch")
            longTimeDoor.click()
            time.sleep(2)

            unAuth = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='미허가 인증수단 시도 알람']/android.widget.Switch")
            unAuth.click()
            time.sleep(2)

            doorFail = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문 장애 상태 알람']/android.widget.Switch")
            doorFail.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='문열림 알람(Tamper)']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkTrue

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='강제 문열림 알람']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkFalse

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='장시간 문열림 알람']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkFalse

            check4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='미허가 인증수단 시도 알람']/android.widget.Switch")
            is_checked_str4 = check4.get_attribute('checked')
            print(is_checked_str4)
            assert is_checked_str4 == checkFalse

            check5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문 장애 상태 알람']/android.widget.Switch")
            is_checked_str5 = check5.get_attribute('checked')
            print(is_checked_str5)
            assert is_checked_str5 == checkFalse

            #강제 문열림 알람 이벤트만 설정
            forceDoor = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='강제 문열림 알람']/android.widget.Switch")
            forceDoor.click()
            time.sleep(2)

            tamperDoor = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='문열림 알람(Tamper)']/android.widget.Switch")
            tamperDoor.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='문열림 알람(Tamper)']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkFalse

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='강제 문열림 알람']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkTrue

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='장시간 문열림 알람']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkFalse

            check4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='미허가 인증수단 시도 알람']/android.widget.Switch")
            is_checked_str4 = check4.get_attribute('checked')
            print(is_checked_str4)
            assert is_checked_str4 == checkFalse

            check5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문 장애 상태 알람']/android.widget.Switch")
            is_checked_str5 = check5.get_attribute('checked')
            print(is_checked_str5)
            assert is_checked_str5 == checkFalse

            #장시간 문열림 알람 이벤트만 설정
            forceDoor = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='강제 문열림 알람']/android.widget.Switch")
            forceDoor.click()
            time.sleep(2)

            longTimeDoor = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='장시간 문열림 알람']/android.widget.Switch")
            longTimeDoor.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='문열림 알람(Tamper)']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkFalse

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='강제 문열림 알람']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkFalse

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='장시간 문열림 알람']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkTrue

            check4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='미허가 인증수단 시도 알람']/android.widget.Switch")
            is_checked_str4 = check4.get_attribute('checked')
            print(is_checked_str4)
            assert is_checked_str4 == checkFalse

            check5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문 장애 상태 알람']/android.widget.Switch")
            is_checked_str5 = check5.get_attribute('checked')
            print(is_checked_str5)
            assert is_checked_str5 == checkFalse

            # 미허가 인증 수단 시도 알람 이벤트만 설정
            longTimeDoor = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='장시간 문열림 알람']/android.widget.Switch")
            longTimeDoor.click()
            time.sleep(2)

            unAuth = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='미허가 인증수단 시도 알람']/android.widget.Switch")
            unAuth.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='문열림 알람(Tamper)']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkFalse

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='강제 문열림 알람']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkFalse

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='장시간 문열림 알람']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkFalse

            check4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='미허가 인증수단 시도 알람']/android.widget.Switch")
            is_checked_str4 = check4.get_attribute('checked')
            print(is_checked_str4)
            assert is_checked_str4 == checkTrue

            check5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문 장애 상태 알람']/android.widget.Switch")
            is_checked_str5 = check5.get_attribute('checked')
            print(is_checked_str5)
            assert is_checked_str5 == checkFalse

            # 출입문 장애 상태 알람 이벤트만 설정
            unAuth = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='미허가 인증수단 시도 알람']/android.widget.Switch")
            unAuth.click()
            time.sleep(2)

            doorFail = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문 장애 상태 알람']/android.widget.Switch")
            doorFail.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            acMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 통제")
            acMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='문열림 알람(Tamper)']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkFalse

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='강제 문열림 알람']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkFalse

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='장시간 문열림 알람']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkFalse

            check4 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='미허가 인증수단 시도 알람']/android.widget.Switch")
            is_checked_str4 = check4.get_attribute('checked')
            print(is_checked_str4)
            assert is_checked_str4 == checkFalse

            check5 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문 장애 상태 알람']/android.widget.Switch")
            is_checked_str5 = check5.get_attribute('checked')
            print(is_checked_str5)
            assert is_checked_str5 == checkTrue

            pass
            print("DQS_T15897 출입 통제에 시스템 이벤트 알람 설정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15897 출입 통제에 시스템 이벤트 알람 설정 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15898(self):
        try:
            print("DQS_T15898 영상 감시에 영상 이벤트 알람 설정 동작 확인")

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상")
            place.click()
            time.sleep(5)

            self.driver.tap([(786, 649)])
            #비디오 공간 진입
            time.sleep(5)

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            #움직임 감지 이벤트만 설정
            tempering = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='시야각 가림']/android.widget.Switch")
            tempering.click()
            time.sleep(2)

            iotSenser = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='IoT 접점 센서']/android.widget.Switch")
            iotSenser.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='움직임 감지']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkTrue

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='시야각 가림']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkFalse

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='IoT 접점 센서']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkFalse

            #시야각 가림 이벤트만 설정
            motionDe = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='움직임 감지']/android.widget.Switch")
            motionDe.click()
            time.sleep(2)

            tempering = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='시야각 가림']/android.widget.Switch")
            tempering.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='움직임 감지']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkFalse

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='시야각 가림']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkTrue

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='IoT 접점 센서']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkFalse

            #IoT 접점 센서 이벤트만 설정
            tempering = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='시야각 가림']/android.widget.Switch")
            tempering.click()
            time.sleep(2)

            iotSenser = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='IoT 접점 센서']/android.widget.Switch")
            iotSenser.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='움직임 감지']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkFalse

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='시야각 가림']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkFalse

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='IoT 접점 센서']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkTrue

            pass
            print("DQS_T15898 영상 감시에 영상 이벤트 알람 설정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15898 영상 감시에 영상 이벤트 알람 설정 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15899(self):
        try:
            print("DQS_T15899 영상 감시에 영상 이벤트 순서 오류 알람 설정 동작 확인")

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상")
            place.click()
            time.sleep(5)

            self.driver.tap([(786, 649)])
            #비디오 공간 진입
            time.sleep(5)

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            #내부 오류 이벤트만 설정
            disconnect = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연결 해제']/android.widget.Switch")
            disconnect.click()
            time.sleep(2)

            fullDisk = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='디스크 공간 없음']/android.widget.Switch")
            fullDisk.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='내부 오류']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkTrue

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연결 해제']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkFalse

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='디스크 공간 없음']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkFalse

            #연결 해제 이벤트만 설정
            localErr = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='내부 오류']/android.widget.Switch")
            localErr.click()
            time.sleep(2)

            disconnect = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연결 해제']/android.widget.Switch")
            disconnect.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='내부 오류']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkFalse

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연결 해제']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkTrue

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='디스크 공간 없음']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkFalse

            #디스크 공간 없음 이벤트만 설정
            disconnect = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연결 해제']/android.widget.Switch")
            disconnect.click()
            time.sleep(2)

            fullDisk = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='디스크 공간 없음']/android.widget.Switch")
            fullDisk.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='내부 오류']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkFalse

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='연결 해제']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkFalse

            check3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='디스크 공간 없음']/android.widget.Switch")
            is_checked_str3 = check3.get_attribute('checked')
            print(is_checked_str3)
            assert is_checked_str3 == checkTrue

            pass
            print("DQS_T15899 영상 감시에 영상 이벤트 순서 오류 알람 설정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15899 영상 감시에 영상 이벤트 순서 오류 알람 설정 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15900(self):
        try:
            print("DQS_T15900 영상 감시에 IoT 이벤트 순서 오류 알람 설정 동작 확인")

            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "멤버쉽관리_초대 100명 이상")
            place.click()
            time.sleep(5)

            self.driver.tap([(786, 649)])
            #비디오 공간 진입
            time.sleep(5)

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            #센서 분리 이벤트만 설정
            lowBattery = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='배터리 얼마남지 않음']/android.widget.Switch")
            lowBattery.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='센서 분리']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkTrue

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='배터리 얼마남지 않음']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkFalse

            #배터리 얼마남지 않음 이벤트만 설정
            senserDis = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='센서 분리']/android.widget.Switch")
            senserDis.click()
            time.sleep(2)

            lowBattery = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='배터리 얼마남지 않음']/android.widget.Switch")
            lowBattery.click()
            time.sleep(2)

            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            videoMenu = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "영상 감시")
            videoMenu.click()

            check1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='센서 분리']/android.widget.Switch")
            is_checked_str1 = check1.get_attribute('checked')
            print(is_checked_str1)
            assert is_checked_str1 == checkFalse

            check2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='배터리 얼마남지 않음']/android.widget.Switch")
            is_checked_str2 = check2.get_attribute('checked')
            print(is_checked_str2)
            assert is_checked_str2 == checkTrue

            pass
            print("DQS_T15900 영상 감시에 IoT 이벤트 순서 오류 알람 설정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15900 영상 감시에 IoT 이벤트 순서 오류 알람 설정 동작 확인 | Failed")
            print(str(e))
            self.fail()

class adminMenu(unittest.TestCase):

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

    def test_DQS_T15901(self):
        try:
            print("DQS_T15901 관리자 초대 메뉴 UI 출력 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            # 관리자 초대 메뉴 UI 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주소록").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 리스트").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정").is_displayed()

            #멤버쉽 관리_초대 100명 이상 공간에 임의 초대된 계정 확인
            #01000011111 계정 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1테스트").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "#010****1111").is_displayed()

            #01020905304 계정 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "#010****5304").is_displayed()

            pass
            print("DQS_T15901 관리자 초대 메뉴 UI 출력 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15901 관리자 초대 메뉴 UI 출력 확인| Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15902(self):
        try:
            print("DQS_T15902 관리자 초대에 직접 입력 메뉴 UI 출력 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            # 직접 입력 UI 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 받는 사람").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+82").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리 방침 안내").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기").is_displayed()

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력").is_displayed() #버튼 비활성화 확인 - 직접입력 화면 유지 확인

            # 지역 코드 확인
            countryNum = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+82")
            countryNum.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지역 코드").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()

            start_x1 = 539
            start_y1 = 223
            end_x1 = 539
            end_y1 = 932
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)

            personalData = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리 방침 안내")
            personalData.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 기능 개인 정보 처리 방침 안내").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 기능 사용시 개인 정보의 보관 및 삭제 등 법규에 따른 관리 책임은 고객(이하 관리자)에게 있습니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대에 응하지 않은 사용자 정보의 보관 및 삭제는 관리자가 진행해야 합니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "따라서 관리자는 사용자 개인의 요청이 있을 경우 혹은 해당 개인 정보가 더 이상 필요치 않을 경우 삭제를 진행해야 하며 외부에 노출되지 않도록 관리 해야 합니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()

            pass
            print("DQS_T15902 관리자 초대에 직접 입력 메뉴 UI 출력 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15902 관리자 초대에 직접 입력 메뉴 UI 출력 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15903(self):
        try:
            print("DQS_T15903 관리자 초대에 직접 입력 설정 Validation 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            # 지역 코드 유효성 체크
            countryNum = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+82")
            countryNum.click()

            st1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st1.click()
            st1.send_keys("123456")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st1.clear()

            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st2.click()
            st2.send_keys("Korea")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st2.clear()

            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st3.click()
            st3.send_keys("!@#$")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st3.clear()

            st4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st4.click()
            st4.send_keys("가나다")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st4.clear()

            st5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st5.click()
            st5.send_keys("+81")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st5.clear()

            st6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st6.click()
            st6.send_keys("ㄷ")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st6.clear()

            st7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st7.click()
            st7.send_keys("ㅇ")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "지역코드가 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            st7.clear()

            st8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st8.click()
            st8.send_keys("대한")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "대한민국\n+82").is_displayed()

            st8.clear()

            st9 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st9.click()
            st9.send_keys("일")
            searchBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            searchBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81").is_displayed()

            seleteCountry = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81")
            seleteCountry.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+81").is_displayed()

            #전화번호 유효성 체크
            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput1.click()
            text_to_input = "ABCDEFG"
            er1 = phoneInput1.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er1)
            phoneInput1.clear()

            phoneInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput2.click()
            text_to_input = "abcdefg"
            er2 = phoneInput2.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er2)
            phoneInput2.clear()

            phoneInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput3.click()
            text_to_input = "가나다라마바사"
            er3 = phoneInput3.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er3)
            phoneInput3.clear()

            phoneInput4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput4.click()
            text_to_input = "!@#$%^&*()"
            er4 = phoneInput4.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er4)
            phoneInput4.clear()

            phoneInput5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput5.click()
            phoneInput5.send_keys("012345678")
            time.sleep(1)

            # 초대하기 버튼 클릭 - 비활성화 확인(초대 동작 되지 않고 현재 화면 출력 확인)
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력").is_displayed()

            phoneInput5.clear()
            time.sleep(1)

            phoneInput6 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput6.click()
            phoneInput6.send_keys("012345678901234567890123456789")
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='01234567890123456789']").is_displayed()

            # 초대하기 버튼 클릭 - 비활성화 확인(초대 동작 되지 않고 현재 화면 출력 확인)
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력").is_displayed()

            phoneInput6.clear()
            time.sleep(1)

            phoneInput7 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput7.click()
            phoneInput7.send_keys("012345678901")
            time.sleep(1)

            # 초대하기 버튼 클릭 - 비활성화 확인(초대 동작 되지 않고 현재 화면 출력 확인)
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력").is_displayed()

            phoneInput7.clear()
            time.sleep(1)

            phoneInput8 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput8.click()
            phoneInput8.send_keys("01023235454")
            time.sleep(1)

            # 초대하기 버튼 클릭 - 활성화 확인(초대 동작 확인 및 리스트 '회원가입 전' 출력 확인)
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입 전").is_displayed()

            #초대한 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            pass
            print("DQS_T15903 관리자 초대에 직접 입력 설정 Validation 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15903 관리자 초대에 직접 입력 설정 Validation 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15904(self):
        try:
            print("DQS_T15904 직접 입력으로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            #관리자 초대
            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput1.click()
            phoneInput1.send_keys("01000099999")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #최초 회원가입 시 '회원가입 전'으로 출력 되지만 회원가입 후 확인하는 케이스를 진행할 수 없어 이미 가입된 관리자로 테스트 진행함
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_main").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "#010****9999").is_displayed()

            #테스트한 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            pass
            print("DQS_T15904 직접 입력으로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15904 직접 입력으로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15905(self):
        try:
            print("DQS_T15905 직접 입력으로 다수의 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            #관리자 초대
            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput1.click()
            phoneInput1.send_keys("01000088888")
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            countryNum1 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@content-desc='+82'])[2]")
            countryNum1.click()

            seleteJapan1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81")
            seleteJapan1.click()

            phoneInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.EditText[2]")
            phoneInput2.click()
            phoneInput2.send_keys("01023235455")
            time.sleep(1)

            deleteAdmin = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.ImageView[3]")
            deleteAdmin.click()
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            countryNum2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@content-desc='+82'])[2]")
            countryNum2.click()

            seleteJapan2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81")
            seleteJapan2.click()

            phoneInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.EditText[2]")
            phoneInput3.click()
            phoneInput3.send_keys("01023235455")
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            countryNum3 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@content-desc='+82'])[2]")
            countryNum3.click()

            seleteJapan3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "일본\n+81")
            seleteJapan3.click()

            phoneInput4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[3]")
            phoneInput4.click()
            phoneInput4.send_keys("01023235456")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #최초 회원가입 시 '회원가입 전'으로 출력 되지만 회원가입 후 확인하는 케이스를 진행할 수 없어 이미 가입된 관리자로 테스트 진행함
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_sub").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "#010****8888").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='회원가입 전'])[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='회원가입 전'])[2]").is_displayed()

            #회원가입 전 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            adminDelete2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[4]") #4번째 등록된 관리자 삭제
            adminDelete2.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            adminDelete3 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete3.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            pass
            print("DQS_T15905 직접 입력으로 다수의 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15905 직접 입력으로 다수의 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15906(self):
        try:
            print("DQS_T15906 관리자 초대에 주소록 메뉴 UI 출력 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            seleteAdress = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주소록")
            seleteAdress.click()

            # 주소록 UI 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주소록").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 받는 사람").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리 방침 안내").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기").is_displayed()

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주소록").is_displayed() #버튼 비활성화 확인 - 주소록 화면 유지 확인

            personalData = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "개인정보 처리 방침 안내")
            personalData.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 기능 개인 정보 처리 방침 안내").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대 기능 사용시 개인 정보의 보관 및 삭제 등 법규에 따른 관리 책임은 고객(이하 관리자)에게 있습니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대에 응하지 않은 사용자 정보의 보관 및 삭제는 관리자가 진행해야 합니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "따라서 관리자는 사용자 개인의 요청이 있을 경우 혹은 해당 개인 정보가 더 이상 필요치 않을 경우 삭제를 진행해야 하며 외부에 노출되지 않도록 관리 해야 합니다.").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            pass
            print("DQS_T15906 관리자 초대에 주소록 메뉴 UI 출력 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15906 관리자 초대에 주소록 메뉴 UI 출력 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15907(self):
        try:
            print("DQS_T15907 주소록으로 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            seleteAdress = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주소록")
            seleteAdress.click()

            #관리자 초대
            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()
            time.sleep(1)

            seleteAdmin1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_admin1")
            seleteAdmin1.click()
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #최초 회원가입 시 '회원가입 전'으로 출력 되지만 회원가입 후 확인하는 케이스를 진행할 수 없어 이미 가입된 관리자로 테스트 진행함
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_주소록1").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "#010****0001").is_displayed()

            #테스트한 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            pass
            print("DQS_T15907 주소록으로 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15907 주소록으로 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15908(self):
        try:
            print("DQS_T15908 주소록으로 다수의 관리자 초대 동작 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            seleteAdress = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "주소록")
            seleteAdress.click()

            #관리자 초대
            addBtn1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn1.click()
            time.sleep(1)

            seleteAdmin1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_admin1")
            seleteAdmin1.click()
            time.sleep(1)

            addBtn2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn2.click()
            time.sleep(1)

            seleteAdmin2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_admin2")
            seleteAdmin2.click()
            time.sleep(1)

            #2번째 관리자 삭제
            deleteAdmin = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.ImageView[4]")
            deleteAdmin.click()

            addBtn2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn2.click()
            time.sleep(1)

            seleteAdmin3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_admin3")
            seleteAdmin3.click()
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #최초 회원가입 시 '회원가입 전'으로 출력 되지만 회원가입 후 확인하는 케이스를 진행할 수 없어 이미 가입된 관리자로 테스트 진행함
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_주소록1").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "#010****0001").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입 전").is_displayed()

            #테스트한 관리자 삭제
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete1.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            pass
            print("DQS_T15908 주소록으로 다수의 관리자 초대 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15908 주소록으로 다수의 관리자 초대 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15909(self):
        try:
            print("DQS_T15909 메인 관리자 계정 접속된 경우 초대된 관리자 수정 기능 확인")

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]").is_displayed()

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            #관리자 초대
            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput1.click()
            phoneInput1.send_keys("01000099999")
            time.sleep(1)

            addBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            addBtn.click()

            phoneInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대 받는 사람']/android.view.View[1]/android.widget.EditText[2]")
            phoneInput2.click()
            phoneInput2.send_keys("01000088888")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(3)

            #메인 관리자 권한 이관 동작
            permission = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='권한 이관'])[2]")
            permission.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "권한 이행").is_displayed()
            permission_Msg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "메인 관리자 권한을 변경 하시겠습니까?")
            contentDesc1 = permission_Msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "메인 관리자 권한을 변경 하시겠습니까?")

            cancelBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancelBtn.click()

            permission = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='권한 이관'])[1]")
            permission.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.widget.ImageView[9]").is_displayed()

            # 메인 관리자 삭제
            adminDelete1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내보내기").is_displayed()
            delete_Msg1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "해당 관리자를 공간에서 내보내시겠습니까?")
            contentDesc2 = delete_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "해당 관리자를 공간에서 내보내시겠습니까?")

            cancelBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancelBtn.click()

            adminDelete2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete2.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            # 서브 관리자 삭제
            adminDelete3 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete3.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내보내기").is_displayed()
            delete_Msg2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "해당 관리자를 공간에서 내보내시겠습니까?")
            contentDesc3 = delete_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc3}")
            self.assertEqual(contentDesc3, "해당 관리자를 공간에서 내보내시겠습니까?")

            cancelBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancelBtn.click()

            adminDelete2 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[3]") #3번째 등록된 관리자 삭제
            adminDelete2.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[1]").is_displayed()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기").is_displayed()
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "나가기 버튼 및 삭제 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            pass
            print("DQS_T15909 메인 관리자 계정 접속된 경우 초대된 관리자 수정 기능 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15909 메인 관리자 계정 접속된 경우 초대된 관리자 수정 기능 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15910(self):
        try:
            print("DQS_T15910 서브 관리자 계정 접속된 경우 초대된 관리자 수정 기능 확인")

            leadbutton = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
            leadbutton.click()

            logout_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그아웃")
            logout_button.click()

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()

            phone_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
            phone_input_box.click()
            phone_input_box.send_keys("01000022222")

            password_input_box = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
            password_input_box.click()
            password_input_box.send_keys("Kjstar36!!")

            login_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "로그인")
            login_button.click()
            time.sleep(7)

            spaceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "공간 설정")
            spaceSetting.click()
            time.sleep(1)

            adminInvite = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "관리자 초대")
            adminInvite.click()

            # 나가기 버튼 출력 확인 / 삭제 버튼 미출력 확인
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기").is_displayed()

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[1]").is_displayed()
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]").is_displayed()
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "삭제 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            manualInput = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "직접 입력")
            manualInput.click()

            #관리자 초대
            phoneInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            phoneInput.click()
            phoneInput.send_keys("01000088888")
            time.sleep(1)

            # 초대하기 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()
            time.sleep(2)

            #서브 관리자 삭제 동작
            adminDelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제") #본인 계정외 서브 관리자만 삭제버튼 출력
            adminDelete.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "내보내기").is_displayed()
            delete_Msg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "해당 관리자를 공간에서 내보내시겠습니까?")
            contentDesc = delete_Msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "해당 관리자를 공간에서 내보내시겠습니까?")

            cancelBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancelBtn.click()

            adminDelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제") #본인 계정외 서브 관리자만 삭제버튼 출력
            adminDelete.click()

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(3)

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "나가기")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "나가기 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            pass
            print("DQS_T15910 서브 관리자 계정 접속된 경우 초대된 관리자 수정 기능 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15910 서브 관리자 계정 접속된 경우 초대된 관리자 수정 기능 확인 | Failed")
            print(str(e))
            self.fail()

if __name__ == '__main__':
    unittest.main()

