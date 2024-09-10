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

'Xpath'
NameInputBox = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText[1]"
phoneInputBox = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText[2]"
confirm = "확인"
cancel = "취소"
modify = "수정"
invite = "초대"
delete = "삭제"
allAgree = "약관 전체 동의"
nextBtn = "다음"
authenticationBtn = "인증요청"
" ClassName "
signUpPhoneNumber = "android.widget.EditText"

def backBtn(self):
    #뒤로가기 후 사용자 상세 재 진입
    self.driver.tap([(54, 152)])
    time.sleep(1)


class UserMenu(unittest.TestCase):

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
        #비디오 공간 진입
        time.sleep(5)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_DQS_T7196(self):
     try:
        print("DQS_T7196 사용자 목록 UI 구조 확인")

        #등록된 사용자가 없는 공간 진입 - Test 공간
        place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
        place.click()
        time.sleep(5)

        self.driver.tap([(796, 1204)])
        time.sleep(2)

        self.driver.tap([(967, 2084)])
        #사용자 초대 버튼 클릭
        time.sleep(1)

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 목록").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 리스트").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록순").is_displayed()
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[3]").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정").is_displayed()

        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[4]").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대된 사용자가 없습니다.").is_displayed()
        assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='초대하기']").is_displayed()

        inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
        inviteBtn.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 방식").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증 모드 선택").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 인식").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지문 인식").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "RF 카드").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호").is_displayed()

        pass
        print("DQS_T7196 사용자 목록 UI 구조 확인 | Pass")

     except Exception as e:
        capture_screenshot(self.driver, self._testMethodName)
        print("DQS_T7196 사용자 목록 UI 구조 확인 | Failed")
        print(str(e))
        self.fail()

    def test_DQS_T7649(self):
        try:
            print("DQS_T7649 사용자 출입문 권한 설정 기능 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            #출입문 수정 버튼 클릭
            self.driver.tap([(963, 1319)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='출입문'])[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='출입문'])[2]").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모든 출입문").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door2_N2").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모든 출입문은 해당 공간에 추가 혹은 삭제되는 모든 출입문 권한을 자동 반영 합니다.").is_displayed()

            #1번째 리스트에 있는 출입문 x버튼 클릭
            doorDelete = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]")
            doorDelete.click()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door1_BS3")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "장치 삭제했는데 남아있음을 확인"
            except NoSuchElementException:
                pass

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door2_N2").is_displayed()

            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, modify)
            modify_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n#01001010101\n출입기간\n지정된 출입문\n카카오QR\n네이버QR")
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입기간\n수정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입문 권한\n수정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Door2_N2").is_displayed()

            #전체 출입문 복구
            self.driver.tap([(963, 1319)])
            time.sleep(1)

            alldoor = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모든 출입문")
            alldoor.click()

            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, modify)
            modify_Btn.click()
            time.sleep(1)

            pass
            print("DQS_T7649 사용자 출입문 권한 설정 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T7649 사용자 출입문 권한 설정 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12217(self):
        try:
            print("DQS_T12217 사용자 출입 기간 요일별 설정 시 기능 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            #출입기간 수정 버튼 클릭
            self.driver.tap([(959, 702)])
            time.sleep(1)

            #요일별 클릭
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음").is_displayed()
            daySetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySetting.click()

            #Schedule 설정
            scheduleSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            scheduleSelete.click()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirm_Btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\nE2E_Schedule").is_displayed()

            #수정 버튼 클릭
            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, modify)
            modify_Btn.click()
            time.sleep(2)

            #뒤로가기 후 사용자 상세 재 진입
            self.driver.tap([(54, 152)])
            time.sleep(1)

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            #출입기간 수정 버튼 클릭
            self.driver.tap([(959, 702)])
            time.sleep(1)

            #요일별 클릭
            daySetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\nE2E_Schedule")
            daySetting.click()
            time.sleep(1)

            #Schedule 설정
            scheduleSelete1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "근무시간1")
            scheduleSelete1.click()

            # 기존 설정된 Schdeuld 재 선택
            scheduleSelete2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "E2E_Schedule")
            scheduleSelete2.click()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirm_Btn.click()

            #수정 버튼 클릭 - 버튼 비활성화를 확인하지 못하여 클릭 후 페이지 유지 동작으로 작성
            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, modify)
            modify_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='출입 기간'])[1]").is_displayed()

            #요일별 - 제한 없음으로 복구
            org1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "제한없음")
            org1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음").is_displayed()

            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, modify)
            modify_Btn.click()
            time.sleep(2)

            pass
            print("DQS_T12217 사용자 출입 기간 요일별 설정 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12217 사용자 출입 기간 요일별 설정 시 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12218(self):
        try:
            print("DQS_T12218 사용자 출입문 전체 삭제 시 기능 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            #출입문 수정 버튼 클릭
            self.driver.tap([(963, 1319)])
            time.sleep(1)

            #출입문 2번 삭제
            doorDelete2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[4]")
            doorDelete2.click()

            #출입문 1번 삭제
            doorDelete1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]")
            doorDelete1.click()

            #수정 버튼 클릭 - 버튼 비활성화를 확인하지 못하여 클릭 후 페이지 유지 동작으로 작성
            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, modify)
            modify_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='출입문'])[1]").is_displayed()

            #뒤로가기 버튼 클릭하여 사용자 초대 화면 진입
            for _ in range(2):
                self.driver.tap([(54, 158)])
                time.sleep(1)

            # 신규 사용자 초대 후 출입문 모두 삭제 동작 확인 케이스
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 휴대폰 번호(QR)로 사용자 초대
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
            qrSetting.click()

            st1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            st1.click()
            st1.send_keys("Test_QR2")

            # 폰번호 입력
            st2 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            st2.click()
            st2.send_keys("01099990002")

            # 다음 버튼 클릭
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()

            #출입문 1번 삭제
            doorDelete2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문\nDoor1_BS3\nDoor2_N2\n모든 출입문은 해당 공간에 추가 혹은 삭제되는 모든 출입문 권한을 자동 반영 합니다.']/android.widget.ImageView[2]")
            doorDelete2.click()

            #출입문 2번 삭제
            doorDelete1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='출입문\nDoor2_N2']/android.widget.ImageView[2]")
            doorDelete1.click()

            #초대 버튼 - 버튼 비활성화를 확인하지 못하여 클릭 후 페이지 유지 동작으로 작성
            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, invite)
            st3.click()
            time.sleep(1)

            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 권한").is_displayed()

            pass
            print("DQS_T12218 사용자 출입문 전체 삭제 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12218 사용자 출입문 전체 삭제 시 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12231(self):
        try:
            print("DQS_T12231 동일한 이름 및 휴대폰번호로 사용자 초대 시 실패 케이스 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            #사용자 초대화면 진입
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 휴대폰 번호(QR)로 사용자 초대
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
            qrSetting.click()

            # 기등록된 사용자의 동일한 이름 입력
            st1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            st1.click()
            st1.send_keys("e2e_Test1")

            # 기등록된 사용자의 폰번호 입력
            st2 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            st2.click()
            st2.send_keys("01001010101")

            # 다음 버튼 클릭
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()

            #초대 버튼
            st3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, invite)
            st3.click()
            time.sleep(1)

            # 동일 사용자 팝업 출력 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록 오류").is_displayed()
            duplicationuser_msg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미 등록된 동일 휴대폰 번호가 있습니다.")
            contentDesc = duplicationuser_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "이미 등록된 동일 휴대폰 번호가 있습니다.")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirm_Btn.click()

            # 다음 버튼 클릭
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()

            #초대 버튼 - 팝업 출력되어 확인버튼 클릭 후 다시 초대 버튼 클릭 시 폰번호없이 초대되는 현상 발생함
            st4 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, invite)
            st4.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록 오류").is_displayed()

            pass
            print("DQS_T12231 동일한 이름 및 휴대폰번호로 사용자 초대 시 실패 케이스 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12231 동일한 이름 및 휴대폰번호로 사용자 초대 시 실패 케이스 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12236(self):
        try:
            print("DQS_T12236 사용자 요일별 스케줄 추가 및 삭제 기능 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            #Test1 사용자 선택
            user1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='e2e_Test1\n출입기간'])[1]")
            user1.click()
            time.sleep(1)

            #출입기간 수정 버튼 선택
            self.driver.tap([(953, 702)])
            time.sleep(1)

            #스케줄 추가
            daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySchedule.click()

            addSchedule1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
            addSchedule1.click()

            scheduleName1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName1.click()
            scheduleName1.send_keys("Test_Schedule1")

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

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "23시 정각")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x, start_y, end_x, end_y)
                else:
                    raise NoSuchElementException("찾을 수 없습니다.")

            self.driver.tap([(868, 1696)])
            max_swipes = 20
            start_x1 = 868
            start_y1 = 1696
            end_x1 = 868
            end_y1 = 1696+80

            for _ in range(max_swipes):
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

            creatSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "생성")
            creatSchedule.click()
            time.sleep(2)

            #스케줄 추가 - 모든 요일 설정
            addSchedule1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
            addSchedule1.click()

            scheduleName1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName1.click()
            scheduleName1.send_keys("Test_Schedule2")

            nxt_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nxt_Btn.click()

            monSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]")
            monSchedule.click()
            time.sleep(1)

            self.driver.tap([(801, 1687)])
            max_swipes = 20
            start_x2 = 729
            start_y2 = 1693
            end_x2 = 729
            end_y2 = 1693+80

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "23시 정각")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x2, start_y2, end_x2, end_y2)
                else:
                    raise NoSuchElementException("찾을 수 없습니다.")

            self.driver.tap([(868, 1696)])
            max_swipes = 20
            start_x3 = 868
            start_y3 = 1696
            end_x3 = 868
            end_y3 = 1696+80

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "59분")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x3, start_y3, end_x3, end_y3)
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
            time.sleep(2)

            #Test_Schedule2 설정
            seleteSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Test_Schedule2']/android.widget.ImageView[1]")
            seleteSchedule.click()

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()
            time.sleep(1)

            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modify_Btn.click()
            time.sleep(1)

            #뒤로가기 후 사용자 상세 재 진입
            backBtn(self)

            userSelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "e2e_Test1\n출입기간")
            userSelete.click()
            time.sleep(1)

            # 출입기간 수정 버튼
            self.driver.tap([(953, 702)])
            time.sleep(1)

            daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\nTest_Schedule2")
            daySchedule.click()

            #Test_Schedule1 삭제
            seleteSchedule1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Test_Schedule1']/android.widget.ImageView[2]")
            seleteSchedule1.click()

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='월'])[2]").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "오전").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "0:00 ~ ").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "오후").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "11:59").is_displayed()

            deleteSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            deleteSchedule.click()
            time.sleep(3)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Schedule1")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "삭제한 스케줄이 있는지 확인"
            except NoSuchElementException:
                pass

            #Test_Schedule2 삭제 - 예외처리 확인
            seleteSchedule2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Test_Schedule2']/android.widget.ImageView[2]")
            seleteSchedule2.click()

            deleteSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            deleteSchedule.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "서버 내부 에러").is_displayed()
            serverErr_msg = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='서버 에러 발생 \n다시 시도해주세요.']")
            contentDesc = serverErr_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "서버 에러 발생 \n다시 시도해주세요.")

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()

            #요일별 - 제한없음 설정(원복)
            self.driver.tap([(54, 148)])
            time.sleep(1)

            cancel_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancel_Btn.click()

            intSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "제한없음")
            intSetting.click()

            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modify_Btn.click()

            pass
            print("DQS_T12236 사용자 요일별 스케줄 추가 및 삭제 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12236 사용자 요일별 스케줄 추가 및 삭제 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12238(self):
        try:
            print("DQS_T12238 사용자 요일별 스케줄 설정 회면에서 뒤로가기 및 취소 버튼 선택 시 기능 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            #Test1 사용자 선택
            user1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='e2e_Test1\n출입기간'])[1]")
            user1.click()
            time.sleep(1)

            # 출입기간 수정 버튼 클릭
            self.driver.tap([(953, 702)])
            time.sleep(1)

            #스케줄 추가 클릭 후 뒤로가기 버튼 클릭
            daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySchedule.click()

            addSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
            addSchedule.click()

            #뒤로가기 버튼 클릭
            self.driver.tap([(54, 148)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기").is_displayed()

            #스케줄 설정화면에서 뒤로가기 버튼 클릭
            addSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
            addSchedule.click()

            scheduleName1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName1.click()
            scheduleName1.send_keys("Test_Schedule3")

            nxt_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nxt_Btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Schedule3").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "생성").is_displayed()

            #뒤로가기 버튼 클릭
            self.driver.tap([(54, 148)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기").is_displayed()

            #스케줄 설정화면에서 취소 버튼 클릭
            addSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
            addSchedule.click()

            scheduleName1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName1.click()
            scheduleName1.send_keys("Test_Schedule3")

            nxt_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nxt_Btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Schedule3").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "생성").is_displayed()

            #취소 버튼 클릭
            cancel_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancel_Btn.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기").is_displayed()

            pass
            print("DQS_T12238 사용자 요일별 스케줄 설정 회면에서 뒤로가기 및 취소 버튼 선택 시 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12238 사용자 요일별 스케줄 설정 회면에서 뒤로가기 및 취소 버튼 선택 시 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12239_T12617(self):
        try:
            print("DQS_T12239 사용자 요일별 스케줄 일정 변경 시 기능 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            #Test1 사용자 선택
            user1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='e2e_Test1\n출입기간'])[1]")
            user1.click()
            time.sleep(1)

            #출입기간 수정 버튼 선택
            self.driver.tap([(953, 702)])
            time.sleep(1)

            #스케줄 편집 - 수요일 시간 변경
            daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySchedule.click()

            seleteSchedule1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='E2E_Schedule']/android.widget.ImageView[2]")
            seleteSchedule1.click()
            time.sleep(1)

            #수요일 시간변경전 기존값 확인
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수'])[2]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오전'])[3]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='0:00 ~ '])[3]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오후'])[3]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='11:59'])[3]").is_displayed()

            wedModify = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[6]")
            wedModify.click()

            self.driver.tap([(282, 1700)])
            max_swipes = 20
            start_x = 210
            start_y = 1696
            end_x = 210
            end_y = 1696-90

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1시 정각")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x, start_y, end_x, end_y)
                else:
                    raise NoSuchElementException("찾을 수 없습니다.")

            self.driver.tap([(796, 1696)])
            max_swipes = 20
            start_x1 = 729
            start_y1 = 1696
            end_x1 = 729
            end_y1 = 1696+80

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "22시 정각")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
                else:
                    raise NoSuchElementException("찾을 수 없습니다.")

            self.driver.tap([(796, 1696)])
            max_swipes = 20
            start_x2 = 873
            start_y2 = 1691
            end_x2 = 873
            end_y2 = 1691-90

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.SeekBar[@content-desc='0분'])[2]")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x2, start_y2, end_x2, end_y2)
                else:
                    raise NoSuchElementException("찾을 수 없습니다.")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            #변경된 값 확인
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수'])[2]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오전'])[3]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='1:00 ~ '])").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오후'])[3]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='10:00'])").is_displayed()

            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modify_Btn.click()
            time.sleep(2)

            #스케줄 변경 후 뒤로가기 버튼 클릭 동작 확인 - 수요일 시간 삭제 후 뒤로가기 버튼 클릭
            seleteSchedule1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='E2E_Schedule']/android.widget.ImageView[2]")
            seleteSchedule1.click()
            time.sleep(1)

            wedSchedule1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[6]")
            wedSchedule1.click()
            time.sleep(1)

            wedDelete = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            wedDelete.click()

            backBtn(self)

            seleteSchedule1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='E2E_Schedule']/android.widget.ImageView[2]")
            seleteSchedule1.click()
            time.sleep(1)

            #변경된 값 있는지 확인
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='수'])[2]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오전'])[3]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='1:00 ~ '])").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오후'])[3]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='10:00'])").is_displayed()

            #스케줄 삭제 - 목요일에 등록된 스케줄 삭제
            thuDelete = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[8]")
            thuDelete.click()

            delete_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '삭제')
            delete_Btn.click()

            #삭제된 값 확인
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='목'])[2]").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "없음").is_displayed()

            time.sleep(1)

            print("DQS-T12617 사용자 요일별 스케줄 설정 시 시간 복사 기능 동작 확인")
            wedSchedule2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[5]")
            wedSchedule2.click()

            thuSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[7]")
            thuSchedule.click()

            friSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[9]")
            friSchedule.click()

            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modify_Btn.click()
            time.sleep(2)

            #변경된 값 확인
            seleteSchedule1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='E2E_Schedule']/android.widget.ImageView[2]")
            seleteSchedule1.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오전'])[3]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='0:00 ~ '])[3]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오후'])[3]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='11:59'])[3]").is_displayed()

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오전'])[4]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='0:00 ~ '])[4]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오후'])[4]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='11:59'])[4]").is_displayed()

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오전'])[5]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='0:00 ~ '])[5]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오후'])[5]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='11:59'])[5]").is_displayed()

            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modify_Btn.click()
            time.sleep(2)

            cancelBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "취소")
            cancelBtn.click()

            pass
            print("DQS_T12239 사용자 요일별 스케줄 일정 변경 시 기능 동작 확인 || DQS-T12617 사용자 요일별 스케줄 설정 시 시간 복사 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12239 사용자 요일별 스케줄 일정 변경 시 기능 동작 확인 || DQS-T12617 사용자 요일별 스케줄 설정 시 시간 복사 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12618(self):
        try:
            print("DQS_T12618 사용자 요일별 스케줄 설정 시 익일 기능 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            #Test1 사용자 선택
            user1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='e2e_Test1\n출입기간'])[1]")
            user1.click()
            time.sleep(1)

            #출입기간 수정
            self.driver.tap([(953, 702)])
            time.sleep(1)

            daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySchedule.click()

            #스케줄 - 추가하기 버튼 클릭
            addSchedule1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
            addSchedule1.click()

            scheduleName = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName.click()
            scheduleName.send_keys("next_Schedule")

            nxt_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nxt_Btn.click()

            monSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]")
            monSchedule.click()
            time.sleep(1)

            self.driver.tap([(282, 1700)])
            max_swipes = 20
            start_x = 210
            start_y = 1776
            end_x = 210
            end_y = 1776-100

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "4시 정각")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x, start_y, end_x, end_y)
                else:
                    raise NoSuchElementException("찾을 수 없습니다.")

            self.driver.tap([(796, 1696)])
            max_swipes = 20
            start_x1 = 729
            start_y1 = 1696
            end_x1 = 729
            end_y1 = 1696+80

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "23시 정각")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
                else:
                    raise NoSuchElementException("찾을 수 없습니다.")

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "익일").is_displayed()
            nxtDay = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView")
            nxtDay.click()
            time.sleep(1)

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            #익일 설정된 값 확인
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='월'])[2]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='오전'])").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='4:00 ~ '])").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='익일 오후'])").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='11:00'])").is_displayed()

            creatSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "생성")
            creatSchedule.click()
            time.sleep(2)

            #생성된 스케줄 설정
            nxtSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='next_Schedule']/android.widget.ImageView[1]")
            nxtSchedule.click()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\nnext_Schedule")

            # 수정 버튼 클릭
            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modify_Btn.click()
            time.sleep(2)

            #출입기간 수정 버튼 클릭 - 설정되어 있는지 재확인
            backBtn(self) #뒤로가기

            user1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='e2e_Test1\n출입기간'])[1]")
            user1.click()
            time.sleep(1)
            #사용자 선택

            self.driver.tap([(953, 702)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\nnext_Schedule")

            #스케줄 삭제 - 원복
            noSchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "제한없음")
            noSchedule.click()

            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modify_Btn.click()
            time.sleep(2)

            backBtn(self) #뒤로가기

            user1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='e2e_Test1\n출입기간'])[1]")
            user1.click()
            time.sleep(1)
            #사용자 선택

            self.driver.tap([(953, 702)])
            time.sleep(1)

            daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySchedule.click()

            nxtSchedule_Selete = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='next_Schedule']/android.widget.ImageView[2]")
            nxtSchedule_Selete.click()

            nxtSchedule_Del = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제")
            nxtSchedule_Del.click()

            pass
            print("DQS_T12618 사용자 요일별 스케줄 설정 시 익일 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12618 사용자 요일별 스케줄 설정 시 익일 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12619(self):
        try:
            print("DQS_T12619 사용자 요일별 스케줄 설정 시 시간 설정 오류 케이스 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            #Test1 사용자 선택
            user1 = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='e2e_Test1\n출입기간'])[1]")
            user1.click()
            time.sleep(1)

            #출입기간 수정
            self.driver.tap([(953, 702)])
            time.sleep(1)

            daySchedule = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "요일별\n제한없음")
            daySchedule.click()

            #스케줄 - 추가하기 버튼 클릭
            addSchedule1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가하기")
            addSchedule1.click()

            scheduleName = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            scheduleName.click()
            scheduleName.send_keys("next_Schedule")

            nxt_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nxt_Btn.click()

            monSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]")
            monSchedule.click()
            time.sleep(1)

            self.driver.tap([(282, 1700)])
            max_swipes = 20
            start_x = 210
            start_y = 1776
            end_x = 210
            end_y = 1776-80

            for _ in range(max_swipes):
                try:
                    element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1시 정각")
                    if element.is_displayed():
                        break
                except NoSuchElementException:
                    self.driver.swipe(start_x, start_y, end_x, end_y)
                else:
                    raise NoSuchElementException("찾을 수 없습니다.")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            #시간 설정 오류 팝업 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시간 설정 오류").is_displayed()
            timeError_Pop1 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='시작 시간이 종료 시간 보다 늦거나\n다른 요일 시간과 중복이 있습니다.']")
            contentDesc = timeError_Pop1.get_attribute('content-desc')
            print(f"추츨한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "시작 시간이 종료 시간 보다 늦거나\n다른 요일 시간과 중복이 있습니다.")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            #스케줄 설정여부 확인 - 없음으로 출력
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='없음'])[1]").is_displayed()

            #월 복사 버튼 클릭 - 시간 설정 오류 팝업 확인
            monSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[1]")
            monSchedule.click()

            #시간 설정 오류 팝업 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시간 설정 오류").is_displayed()
            timeError_Pop2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='시작 시간이 종료 시간 보다 늦거나\n다른 요일 시간과 중복이 있습니다.']")
            contentDesc = timeError_Pop2.get_attribute('content-desc')
            print(f"추츨한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "시작 시간이 종료 시간 보다 늦거나\n다른 요일 시간과 중복이 있습니다.")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            #화 복사 버튼 클릭 - 시간 설정 오류 팝업 확인
            tueSchedule = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[3]")
            tueSchedule.click()

            #시간 설정 오류 팝업 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시간 설정 오류").is_displayed()
            timeError_Pop2 = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='시작 시간이 종료 시간 보다 늦거나\n다른 요일 시간과 중복이 있습니다.']")
            contentDesc = timeError_Pop2.get_attribute('content-desc')
            print(f"추츨한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "시작 시간이 종료 시간 보다 늦거나\n다른 요일 시간과 중복이 있습니다.")

            confirm = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirm.click()

            pass
            print("DQS_T12619 사용자 요일별 스케줄 설정 시 시간 설정 오류 케이스 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12619 사용자 요일별 스케줄 설정 시 시간 설정 오류 케이스 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15911(self):
        try:
            print("DQS_T15911 고객사  관리, 무인매장, 멤버쉽 관리 공간별 사용자 편집 아이콘 출력 및 동작 확인")

            #멤버쉽 관리 공간에 사용자 초대 버튼 출력 확인
            assert self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.widget.ImageView[3]").is_displayed()

            self.driver.tap([(967, 2084)])
            #멤버쉽 관리 공간 - 사용자 초대 버튼 클릭
            time.sleep(1)

            #사용자 목록 화면 출력 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 목록").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 리스트").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정").is_displayed()

            #뒤로가기 버튼 클릭
            self.driver.tap([(54, 148)])
            time.sleep(1)

            #무인매장 공간 진입
            self.driver.tap([(255, 255)])
            time.sleep(3)

            self.driver.tap([(264, 1204)])
            time.sleep(3)

            #사용자 초대 버튼 출력 여부 확인
            try:
                self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.widget.ImageView[3]")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "사용자 초대 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            #고객사 확인 공간 진입
            self.driver.tap([(255, 336)])
            time.sleep(3)

            self.driver.tap([(792, 1794)])
            time.sleep(3)

            #사용자 초대 버튼 출력 여부 확인
            try:
                self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='영상\n실시간\n출입문']/android.widget.ImageView[3]")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "사용자 초대 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            print("DQS_T15911 고객사  관리, 무인매장, 멤버쉽 관리 공간별 사용자 편집 아이콘 출력 및 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15911 고객사  관리, 무인매장, 멤버쉽 관리 공간별 사용자 편집 아이콘 출력 및 동작 확인 | Failed")
            print(str(e))
            self.fail()

class User_Credential(unittest.TestCase):

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
        #비디오 공간 진입
        time.sleep(5)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_DQS_T15912(self):
        try:
            print("DQS_T15912 휴대폰 번호 인증방식 설정 시 Validation 체크 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 휴대폰 번호(QR) 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
            qrSetting.click()

            #이름 입력 - 한글 31자 입력 시도
            userInput1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput1.click()
            userInput1.send_keys("가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차카")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차']").is_displayed()
            userInput1.clear()

            #이름 입력 - 영어 31자 입력 시도
            userInput2 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput2.click()
            userInput2.send_keys("abcdefghijabcdefghijabcdefghijk")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcdefghijabcdefghijabcdefghij']").is_displayed()
            userInput2.clear()

            #이름 입력 - 일어 31자 입력 시도
            userInput3 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput3.click()
            userInput3.send_keys("ユーザー名入力テストユーザー名入力テストユーザー名入力テストです")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ユーザー名入力テストユーザー名入力テストユーザー名入力テスト']").is_displayed()
            userInput3.clear()

            #이름 입력 - 숫자 31자 입력 시도
            userInput4 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput4.click()
            userInput4.send_keys("1234567890123456789012345678901")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123456789012345678901234567890']").is_displayed()
            userInput4.clear()

            #이름 입력 - 특수문자 입력 시도
            userInput5 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput5.click()
            userInput5.send_keys("~!@#$%^&")
            time.sleep(1)

            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput1.click()
            phoneInput1.send_keys("01099990099")
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인(출입권한 화면으로 이동하지 않고 현재 화면 출력 확인)
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름 및 휴대폰 번호").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='~!@#$%^&']").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='01099990099']").is_displayed()

            userInput5 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput5.click()
            userInput5.clear()
            time.sleep(1)

            userInput6 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput6.click()
            userInput6.send_keys("Test_QR1")

            phoneInput1 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput1.click()
            phoneInput1.clear()
            time.sleep(1)

            phoneInput2 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput2.click()
            text_to_input = "ABCDEFG"
            er1 = phoneInput2.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er1)
            phoneInput2.clear()

            phoneInput3 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput3.click()
            text_to_input = "abcdefg"
            er2 = phoneInput3.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er2)
            phoneInput3.clear()

            phoneInput4 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput4.click()
            text_to_input = "가나다라마바사"
            er3 = phoneInput4.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er3)
            phoneInput4.clear()

            phoneInput5 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput5.click()
            text_to_input = "!@#$%^&*()"
            er4 = phoneInput5.text
            os.system(f"adb shell input text '{text_to_input}'")
            self.assertEqual("", er4)
            phoneInput5.clear()

            phoneInput6 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput6.click()
            phoneInput6.send_keys("0123456789012345678901")
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인(출입권한 화면으로 이동하지 않고 현재 화면 출력 확인)
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름 및 휴대폰 번호").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Test_QR1']").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='01234567890123456789']").is_displayed()

            phoneInput6.clear()
            time.sleep(1)

            phoneInput7 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput7.click()
            phoneInput7.send_keys("010123456")
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인(출입권한 화면으로 이동하지 않고 현재 화면 출력 확인)
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름 및 휴대폰 번호").is_displayed()
            phoneInput7.clear()
            time.sleep(1)

            phoneInput7 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput7.click()
            phoneInput7.send_keys("01012345678")
            time.sleep(1)

            # 다음 버튼 클릭 - 활성화 확인(출입권한 화면으로 이동 확인)
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 권한").is_displayed()

            pass
            print("DQS_T15912 휴대폰 번호 인증방식 설정 시 Validation 체크 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15912 휴대폰 번호 인증방식 설정 시 Validation 체크 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T7650_T7977(self):
        try:
            print("DQS_T7650 사용자 초대 성공 케이스 동작 확인(인증방식 : QR)")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 휴대폰 번호(QR) 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
            qrSetting.click()

            #이름 입력
            userInput = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput.click()
            userInput.send_keys("Add QR_Test")

            phoneInput = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            phoneInput.click()
            phoneInput.send_keys("01099990001")

            # 다음 버튼 클릭 - 출입 권한 UI 확인
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()

            #초대 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, invite)
            inviteBtn.click()
            time.sleep(3)

            #뒤로가기 버튼 클릭
            self.driver.tap([(54, 148)])
            time.sleep(1)

            print("DQS_T7977 사용자 삭제 기능 동작 확인")
            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            modify_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, modify)
            modify_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "삭제").is_displayed()

            #사용자 삭제 버튼 클릭
            delete_Btn = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]")
            delete_Btn.click()

            #사용자 제외 팝업 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 제외").is_displayed()
            userDelete_msg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "해당 사용자를 이 공간에서 제외하시겠습니까?")
            contentDesc = userDelete_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "해당 사용자를 이 공간에서 제외하시겠습니까?")

            #사용자 제외 팝업 취소 버튼 클릭
            cancle_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, cancel)
            cancle_Btn.click()
            time.sleep(1)

            #사용자 삭제 버튼 클릭
            delete_Btn = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]")
            delete_Btn.click()

            #사용자 제외 팝업 확인 버튼 클릭
            confirm_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirm_Btn.click()
            time.sleep(1)

            #사용자 리스트에 초대된 사용자 없음 확인
            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add QR_Test")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "삭제된 사용자 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            # 확인 버튼 클릭하여 수정버튼 변경 확인
            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirm_Btn.click()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정").is_displayed()

            pass
            print("DQS_T7977 사용자 삭제 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T7977 사용자 삭제 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T12237(self):
        try:
            print("DQS_T12237 사용자 다중 초대 성공 케이스 동작 확인(인증방식 : QR)")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 휴대폰 번호(QR) 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
            qrSetting.click()

            #사용자1 정보 입력
            user1_1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            user1_1.click()
            user1_1.send_keys("Test1")

            user1_2 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            user1_2.click()
            user1_2.send_keys("01088880001")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자2 정보 입력
            user2_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText[3]")
            user2_1.click()
            user2_1.send_keys("Test2")

            user2_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[4]")
            user2_2.click()
            user2_2.send_keys("01088880002")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자3 정보 입력
            user3_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText[5]")
            user3_1.click()
            user3_1.send_keys("Test3")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            user3_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText[6]")
            user3_2.click()
            user3_2.send_keys("01088880003")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자4 정보 입력
            user4_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[7]")
            user4_1.click()
            user4_1.send_keys("Test4")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            user4_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[8]")
            user4_2.click()
            user4_2.send_keys("01088880004")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자5 정보 입력
            user5_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[9]")
            user5_1.click()
            user5_1.send_keys("Test5")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            user5_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[8]")
            user5_2.click()
            user5_2.send_keys("01088880005")


            # 다음 버튼 클릭 - 출입 권한 UI 확인
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()

            #초대 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, invite)
            inviteBtn.click()
            time.sleep(3)

            #벌크초대 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 권한").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1 01088880001").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2 01088880002").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3 01088880003").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4 01088880004").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5 01088880005").is_displayed()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirm_Btn.click()

            #사용자 리스트 - 초대 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간").is_displayed()

            pass
            print("DQS_T12237 사용자 다중 초대 성공 케이스 동작 확인(인증방식 : QR) | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T12237 사용자 다중 초대 성공 케이스 동작 확인(인증방식 : QR) | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15938(self):
        try:
            print("DQS_T15938 사용자 다중 초대시 중복 사용자 실패 케이스 동작 확인(인증방식 : QR)")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 휴대폰 번호(QR) 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호")
            qrSetting.click()

            #사용자1 정보 입력
            user1_1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            user1_1.click()
            user1_1.send_keys("홍길동")

            user1_2 = self.driver.find_element(AppiumBy.XPATH, phoneInputBox)
            user1_2.click()
            user1_2.send_keys("01088880006")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)


            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자2 정보 입력
            user2_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText[3]")
            user2_1.click()
            user2_1.send_keys("Test2")

            user2_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[4]")
            user2_2.click()
            user2_2.send_keys("01088880002")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자3 정보 입력
            user3_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText[5]")
            user3_1.click()
            user3_1.send_keys("Test3")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            user3_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText[6]")
            user3_2.click()
            user3_2.send_keys("01088880003")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)


            #사용자4 정보 입력
            user4_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[7]")
            user4_1.click()
            user4_1.send_keys("아무개")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            user4_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[8]")
            user4_2.click()
            user4_2.send_keys("01088880007")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자5 정보 입력
            user5_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[9]")
            user5_1.click()
            user5_1.send_keys("1a-_-")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            user5_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[8]")
            user5_2.click()
            user5_2.send_keys("01088880008")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            # 추가 버튼 클릭
            add_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "추가")
            add_btn.click()
            time.sleep(1)

            #사용자5 정보 입력
            user6_1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[9]")
            user6_1.click()
            user6_1.send_keys("Test1")

            #키보드 닫기
            self.driver.tap([(846, 2286)])
            time.sleep(1)

            user5_2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[8]")
            user5_2.click()
            user5_2.send_keys("01088880009")

            # 다음 버튼 클릭 - 출입 권한 UI 확인
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()

            #초대 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, invite)
            inviteBtn.click()
            time.sleep(5)

            #벌크초대 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "출입 권한").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동 01088880006").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2 01088880002").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3 01088880003").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동 01088880006").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개 01088880007").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_- 01088880008").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1 01088880009").is_displayed()

            # 동일 사용자 팝업 출력 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록 오류").is_displayed()
            duplicationuser_msg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미 등록된 동일 휴대폰 번호가 있습니다.")
            contentDesc = duplicationuser_msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc}")
            self.assertEqual(contentDesc, "이미 등록된 동일 휴대폰 번호가 있습니다.")

            confirm_Btn2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.Button[@content-desc='확인'])[2]")
            confirm_Btn2.click()

            confirm_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, confirm)
            confirm_Btn.click()
            # 등록 오류 팝업이 발생하지 않거나 무한로딩 발생되는 현상 있어 Test 실패됨(CLUEQ-147)

            #사용자 리스트 - 초대 확인
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]").is_displayed()

            pass
            print("DQS_T15938 사용자 다중 초대시 중복 사용자 실패 케이스 동작 확인(인증방식 : QR) | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15938 사용자 다중 초대시 중복 사용자 실패 케이스 동작 확인(인증방식 : QR) | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T7198(self):
        try:
            print("DQS_T7198 사용자 조회 화면에서의 기능 동작 확인") #사용자 리스트의 element가 변경될 수 있음

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            userSearch = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView[3]")
            userSearch.click()

            # 사용자 조회 UI 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 조회").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 리스트").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록순").is_displayed()

            st1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st1.click()
            st1.send_keys("010")

            search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
            search_Btn.click()
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "사용자리스트 출력 확인"
            except NoSuchElementException:
                pass

            # X버튼 클릭 후 조회버튼 클릭
            inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='010']/android.widget.ImageView")
            inputDelete_Btn.click()

            search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
            search_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간").is_displayed()

            for _ in range(2):
                start_x1 = 501
                start_y1 = 2040
                end_x1 = 501
                end_y1 = 716
                self.driver.swipe(start_x1, start_y1, end_x1, end_y1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간").is_displayed()

            #Test1 입력 후 조회 동작
            st2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st2.click()
            st2.send_keys("Test1")

            search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
            search_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]").is_displayed()

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            # X버튼 클릭 후 조회버튼 클릭
            inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Test1']/android.widget.ImageView")
            inputDelete_Btn.click()

            #test1 입력 후 조회 동작
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st3.click()
            st3.send_keys("test1")

            search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
            search_Btn.click()
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            # X버튼 클릭 후 조회버튼 클릭
            inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='test1']/android.widget.ImageView")
            inputDelete_Btn.click()

            #TEST1 입력 후 조회 동작
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st3.click()
            st3.send_keys("TEST1")

            search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
            search_Btn.click()
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            # X버튼 클릭 후 조회버튼 클릭
            inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='TEST1']/android.widget.ImageView")
            inputDelete_Btn.click()

            #Te 입력 후 조회 동작
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st3.click()
            st3.send_keys("Te")

            search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
            search_Btn.click()
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            # X버튼 클릭 후 조회버튼 클릭
            inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Te']/android.widget.ImageView")
            inputDelete_Btn.click()

            #홍길동 입력 후 조회 동작
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st3.click()
            st3.send_keys("홍길동")

            search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
            search_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간").is_displayed()

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            # X버튼 클릭 후 조회버튼 클릭
            inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='홍길동']/android.widget.ImageView")
            inputDelete_Btn.click()

            #홍 입력 후 조회 동작
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st3.click()
            st3.send_keys("홍")

            search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
            search_Btn.click()
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            # X버튼 클릭 후 조회버튼 클릭
            inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='홍']/android.widget.ImageView")
            inputDelete_Btn.click()

            #1a-_- 입력 후 조회 동작
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st3.click()
            st3.send_keys("1a-_-")

            search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
            search_Btn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간").is_displayed()

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            # X버튼 클릭 후 조회버튼 클릭
            inputDelete_Btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='1a-_-']/android.widget.ImageView")
            inputDelete_Btn.click()

            #1a-_ 입력 후 조회 동작
            st3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            st3.click()
            st3.send_keys("1a-_")

            search_Btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "조회")
            search_Btn.click()
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간")
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간")
                self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[2]")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "인풋 필드에 텍스트가 없는데 X 버튼 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            #뒤로가기 버튼 쿨릭 후 사용자 목록 UI 확인
            self.driver.tap([(54, 166)])
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 목록").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기").is_displayed()

            #사용자 리스트 - 초대 확인
            assert self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='Test1\n출입기간'])[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test2\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test3\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test4\n출입기간").is_displayed()

            for _ in range(2):
                start_x1 = 501
                start_y1 = 2040
                end_x1 = 501
                end_y1 = 716
                self.driver.swipe(start_x1, start_y1, end_x1, end_y1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test5\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "홍길동\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "아무개\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1a-_-\n출입기간").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test1\n출입기간").is_displayed()

            print("다중 사용자 삭제 - e2e_Test1만 빼고 삭제되어야 함, e2e_Test1 하위에 user 삭제이며, 순서가 상이할 경우 fail 발생")
            #뒤로가기 클릭
            self.driver.tap([(54, 158)])
            time.sleep(1)

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            userDelete = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]")

            for _ in range(9):
                userDelete = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]")
                userDelete.click()
                time.sleep(0.5)

                confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
                confirmBtn.click()
                time.sleep(0.5)
            pass
            print("DQS_T7198 사용자 조회 화면에서의 기능 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T7198 사용자 조회 화면에서의 기능 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15913(self):
        try:
            print("DQS_T15913 얼굴 인증방식 설정 시 Validation 체크 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 얼굴 인식 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 인식")
            qrSetting.click()

            #이름 입력 - 한글 31자 입력 시도
            userInput1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput1.click()
            userInput1.send_keys("가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차카")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차']").is_displayed()
            userInput1.clear()

            #이름 입력 - 영어 31자 입력 시도
            userInput2 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput2.click()
            userInput2.send_keys("abcdefghijabcdefghijabcdefghijk")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcdefghijabcdefghijabcdefghij']").is_displayed()
            userInput2.clear()

            #이름 입력 - 일어 31자 입력 시도
            userInput3 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput3.click()
            userInput3.send_keys("ユーザー名入力テストユーザー名入力テストユーザー名入力テストです")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ユーザー名入力テストユーザー名入力テストユーザー名入力テスト']").is_displayed()
            userInput3.clear()

            #이름 입력 - 숫자 31자 입력 시도
            userInput4 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput4.click()
            userInput4.send_keys("1234567890123456789012345678901")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123456789012345678901234567890']").is_displayed()
            userInput4.clear()

            #이름 입력 - 특수문자 입력 시도
            userInput5 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput5.click()
            userInput5.send_keys("~!@#$%^&")
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인(출입권한 화면으로 이동하지 않고 현재 화면 출력 확인)
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름 및 얼굴").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='~!@#$%^&']").is_displayed()

            pass
            print("DQS_T15913 얼굴 인증방식 설정 시 Validation 체크 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15913 얼굴 인증방식 설정 시 Validation 체크 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15917(self):
        try:
            print("DQS_T15917 사용자 초대 성공 케이스 동작 확인[인증방식 : 얼굴 / 갤러리(이미지) 선택]")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 얼굴 인식 선택
            faceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 인식")
            faceSetting.click()

            #이름 입력
            userInput1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput1.click()
            userInput1.send_keys("Test_Face1")
            time.sleep(1)

            text_output = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Test_Face1']")
            text = text_output.get_attribute('text')
            print(f"추출한 text 값 : {text}")
            self.assertEqual(text, "Test_Face1")

            seleteFace2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")
            seleteFace2.click()
            time.sleep(1)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지")
                # 요소가 존재한다면, 여기서 예외가 발생하지 않으므로 테스트 실패
                assert False, "이미지 팝업 출력됨 확인 필요"
            except NoSuchElementException:
                pass

            seleteFace1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 1")
            seleteFace1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc1 = image_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo1 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[2]")
            photo1.click()
            time.sleep(1)

            seleteFace2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")
            seleteFace2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc2 = image_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[3]")
            photo2.click()
            time.sleep(1)

            deletePhoto = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.widget.ImageView[2]")
            deletePhoto.click()
            time.sleep(1)

            seleteFace2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")
            seleteFace2.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[4]")
            photo2.click()
            time.sleep(1)

            # 다음 버튼 클릭
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
            inviteBtn.click()
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Face1\n출입기간").is_displayed()

            userClick = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Face1\n출입기간")
            userClick.click()
            time.sleep(2)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Face1\n출입기간\n모든 출입문\n얼굴").is_displayed()

            faceClick = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Test_Face1\n출입기간\n모든 출입문\n얼굴']/android.widget.ImageView[2]")
            faceClick.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.widget.ImageView[1]")
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]/android.widget.ImageView[1]")

            # Test_Face1 사용자 삭제
            for _ in range(2):

                self.driver.tap([(72, 162)])
                time.sleep(0.5)

            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            deleteUser = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]")
            deleteUser.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 제외")
            delete_Msg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "해당 사용자를 이 공간에서 제외하시겠습니까?")
            contentDesc3 = delete_Msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc3}")
            self.assertEqual(contentDesc3, "해당 사용자를 이 공간에서 제외하시겠습니까?")

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            pass
            print("DQS_T15917 사용자 초대 성공 케이스 동작 확인[인증방식 : 얼굴 / 갤러리(이미지) 선택] | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15917 사용자 초대 성공 케이스 동작 확인[인증방식 : 얼굴 / 갤러리(이미지) 선택] | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T16914(self):
        try:
            print("DQS_T16914 사용자 초대 실패 케이스 동작 확인[인증방식 : 얼굴]")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 얼굴 인식 선택
            faceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 인식")
            faceSetting.click()

            #이름 입력
            userInput1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput1.click()
            userInput1.send_keys("Test_Face2")
            time.sleep(1)

            seleteFace1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 1")
            seleteFace1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc1 = image_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo1 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[1]")
            photo1.click()
            time.sleep(1)

            # 다음 버튼 클릭
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            # 초대 버튼 클릭 - 팝업 발생 확인
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
            inviteBtn.click()
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 등록 실패").is_displayed()
            faceFail_Msg1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴의 회전 각도가 기준치를 초과하였습니다.")
            contentDesc1 = faceFail_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "얼굴의 회전 각도가 기준치를 초과하였습니다.")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            photoReclick1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ImageView[1]")
            photoReclick1.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[7]")
            photo2.click()
            time.sleep(1)

            # 다음 버튼 클릭
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            # 초대 버튼 클릭 - 팝업 발생 확인
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
            inviteBtn.click()
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 등록 오류").is_displayed()
            faceFail_Msg2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사진에서 얼굴을 찾을 수 없습니다.")
            contentDesc2 = faceFail_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "사진에서 얼굴을 찾을 수 없습니다.")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            photoReclick2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ImageView[1]")
            photoReclick2.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo3 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[4]")
            photo3.click()
            time.sleep(1)

            # 다음 버튼 클릭
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            # 초대 버튼 클릭
            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
            inviteBtn.click()
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Face2\n출입기간").is_displayed()

            userClick = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Face2\n출입기간")
            userClick.click()
            time.sleep(2)

            faceClick = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Test_Face2\n출입기간\n모든 출입문\n얼굴']/android.widget.ImageView[2]")
            faceClick.click()
            time.sleep(1)

            photoReclick3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.widget.ImageView[1]")
            photoReclick3.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo4 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[7]")
            photo4.click()
            time.sleep(1)

            # 수정 버튼 클릭 - 팝업 발생 확인
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 등록 오류").is_displayed()
            faceFail_Msg2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사진에서 얼굴을 찾을 수 없습니다.")
            contentDesc2 = faceFail_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "사진에서 얼굴을 찾을 수 없습니다.")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            photoReclick4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.widget.ImageView[1]")
            photoReclick4.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo5 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[1]")
            photo5.click()
            time.sleep(1)

            # 수정 버튼 클릭 - 팝업 발생 확인
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 등록 실패").is_displayed()
            faceFail_Msg1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴의 회전 각도가 기준치를 초과하였습니다.")
            contentDesc1 = faceFail_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "얼굴의 회전 각도가 기준치를 초과하였습니다.")

            confirmBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "확인")
            confirmBtn.click()
            time.sleep(1)

            # Test_Face2 사용자 삭제
            for _ in range(2):

                self.driver.tap([(72, 162)])
                time.sleep(0.5)

            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            deleteUser = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]")
            deleteUser.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 제외")

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            pass
            print("DQS_T16914 사용자 초대 실패 케이스 동작 확인[인증방식 : 얼굴] | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T16914 사용자 초대 실패 케이스 동작 확인[인증방식 : 얼굴] | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15918(self):
        try:
            print("DQS_T15918 얼굴 인증 방식 수정 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 얼굴 인식 선택
            faceSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "얼굴 인식")
            faceSetting.click()

            #이름 입력
            userInput1 = self.driver.find_element(AppiumBy.XPATH, NameInputBox)
            userInput1.click()
            userInput1.send_keys("Test_Face3")
            time.sleep(1)

            seleteFace1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 1")
            seleteFace1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc1 = image_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo1 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[2]")
            photo1.click()
            time.sleep(1)

            # 다음 버튼 클릭
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대")
            inviteBtn.click()
            time.sleep(3)

            userClick = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Test_Face3\n출입기간")
            userClick.click()
            time.sleep(2)

            faceClick = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Test_Face3\n출입기간\n모든 출입문\n얼굴']/android.widget.ImageView[2]")
            faceClick.click()
            time.sleep(1)

            photoReclick1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.widget.ImageView[1]")
            photoReclick1.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc2 = image_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[2]")
            photo2.click()
            time.sleep(1)

            photoReclick2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.widget.ImageView[1]")
            photoReclick2.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카메라").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리").is_displayed()
            image_Msg2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이미지를 가져올 방법을 선택해주세요.")
            contentDesc2 = image_Msg2.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc2}")
            self.assertEqual(contentDesc2, "이미지를 가져올 방법을 선택해주세요.")

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo3 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[2]")
            photo3.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사진 등록 실패")
            faceFail_Msg1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동일한 사진은 등록할 수 없습니다.")
            contentDesc1 = faceFail_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "동일한 사진은 등록할 수 없습니다.")

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            seleteFace2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")
            seleteFace2.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리")
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo4 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[2]")
            photo4.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사진 등록 실패")
            faceFail_Msg1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "동일한 사진은 등록할 수 없습니다.")
            contentDesc1 = faceFail_Msg1.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc1}")
            self.assertEqual(contentDesc1, "동일한 사진은 등록할 수 없습니다.")

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            seleteFace3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")
            seleteFace3.click()

            seletePhoto = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "갤러리") #TC에는 사진촬영으로 작성되어 있지만 E2E 수행 할 수 없어 갤러리로 사진 선택 케이스로 작성함
            seletePhoto.click()

            aosPhoto1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.google.android.documentsui:id/apps_group']/android.widget.LinearLayout[2]")
            aosPhoto1.click()

            aosPhoto2 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id='com.sec.android.gallery3d:id/smart_album_image'])[3]")
            aosPhoto2.click()

            photo5 = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.FrameLayout[@resource-id='com.sec.android.gallery3d:id/deco_view_layout'])[3]")
            photo5.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.widget.ImageView[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[3]/android.widget.ImageView[1]").is_displayed()
            time.sleep(1)

            deletePhoto = self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.widget.ImageView[2]")
            deletePhoto.click()

            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.widget.ImageView[1]").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+얼굴 2")

            # 하단 수정 버튼 클릭
            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()
            time.sleep(3)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 상세").is_displayed()

            # Test_Face3 사용자 삭제
            self.driver.tap([(72, 162)])
            time.sleep(0.5)

            modifyBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "수정")
            modifyBtn.click()

            deleteUser = self.driver.find_element(AppiumBy.XPATH, "(//android.view.View[@content-desc='삭제'])[2]")
            deleteUser.click()

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "사용자 제외")
            delete_Msg = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "해당 사용자를 이 공간에서 제외하시겠습니까?")
            contentDesc3 = delete_Msg.get_attribute('content-desc')
            print(f"추출한 content-desc 값 : {contentDesc3}")
            self.assertEqual(contentDesc3, "해당 사용자를 이 공간에서 제외하시겠습니까?")

            confirmBtn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='확인']")
            confirmBtn.click()
            time.sleep(1)

            pass
            print("DQS_T15918 얼굴 인증 방식 수정 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15918 얼굴 인증 방식 수정 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15915(self):
        try:
            print("DQS_T15915 카드 인증방식 설정 시 Validation 체크 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 지문 인식 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "RF 카드")
            qrSetting.click()

            #이름 입력 - 한글 31자 입력 시도
            userInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput1.click()
            userInput1.send_keys("가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차카")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차']").is_displayed()
            userInput1.clear()

            #이름 입력 - 영어 31자 입력 시도
            userInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput2.click()
            userInput2.send_keys("abcdefghijabcdefghijabcdefghijk")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcdefghijabcdefghijabcdefghij']").is_displayed()
            userInput2.clear()

            #이름 입력 - 일어 31자 입력 시도
            userInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput3.click()
            userInput3.send_keys("ユーザー名入力テストユーザー名入力テストユーザー名入力テストです")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ユーザー名入力テストユーザー名入力テストユーザー名入力テスト']").is_displayed()
            userInput3.clear()

            #이름 입력 - 숫자 31자 입력 시도
            userInput4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput4.click()
            userInput4.send_keys("1234567890123456789012345678901")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123456789012345678901234567890']").is_displayed()
            userInput4.clear()

            #이름 입력 - 특수문자 입력 시도
            userInput5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput5.click()
            userInput5.send_keys("~!@#$%^&")
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인(출입권한 화면으로 이동하지 않고 현재 화면 출력 확인)
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름 및 카드").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='~!@#$%^&']").is_displayed()

            pass
            print("DQS_T15915 카드 인증방식 설정 시 Validation 체크 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15915 카드 인증방식 설정 시 Validation 체크 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15932(self):
        try:
            print("DQS_T15932 사용자 초대에서 카드 스캔 시 등록 가능한 장치가 없는 경우 동작 확인")

            # 카드 스캔 장치가 없는 공간으로 이동
            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
            place.click()
            time.sleep(5)

            self.driver.tap([(273, 600)])
            time.sleep(3)

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 지문 인식 선택
            cardSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "RF 카드")
            cardSetting.click()

            # +카드 1 클릭
            card1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+ 카드 1")
            card1.click()
            time.sleep(1)

            # 등록가능 장치 없음 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "카드 스캔").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록 가능한 장치가 없습니다.").is_displayed()

            pass
            print("사용자 초대에서 카드 스캔 시 등록 가능한 장치가 없는 경우 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("사용자 초대에서 카드 스캔 시 등록 가능한 장치가 없는 경우 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15933(self):
        try:
            print("DQS_T15933 사용자 초대에서 카드 스캔 타임아웃이 지난 경우 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 지문 인식 선택
            cardSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "RF 카드")
            cardSetting.click()

            #이름 입력
            userInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput.click()
            userInput.send_keys("Test_Card1_e2e")
            time.sleep(1)

            # +카드 1 클릭
            finger1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+ 카드 1")
            finger1.click()
            time.sleep(1)

            # 지문 등록장치 선택
            deviceFinger = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BLN2_OA_538761744")
            deviceFinger.click()
            time.sleep(22)

            # 스캔 타임 아웃 동작 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "첫번째 카드 입력\n스캔 가능 시간을 초과하였습니다.\n다시 시도해 주세요.\n카드 스캔 남은시간\n00:00")

            pass
            print("DQS_T15933 사용자 초대에서 카드 스캔 타임아웃이 지난 경우 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15933 사용자 초대에서 카드 스캔 타임아웃이 지난 경우 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15914(self):
        try:
            print("DQS_T15914 지문 인증방식 설정 시 Validation 체크 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 지문 인식 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지문 인식")
            qrSetting.click()

            #이름 입력 - 한글 31자 입력 시도
            userInput1 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput1.click()
            userInput1.send_keys("가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차카")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='가나다라마바사아자차가나다라마바사아자차가나다라마바사아자차']").is_displayed()
            userInput1.clear()

            #이름 입력 - 영어 31자 입력 시도
            userInput2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput2.click()
            userInput2.send_keys("abcdefghijabcdefghijabcdefghijk")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='abcdefghijabcdefghijabcdefghij']").is_displayed()
            userInput2.clear()

            #이름 입력 - 일어 31자 입력 시도
            userInput3 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput3.click()
            userInput3.send_keys("ユーザー名入力テストユーザー名入力テストユーザー名入力テストです")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='ユーザー名入力テストユーザー名入力テストユーザー名入力テスト']").is_displayed()
            userInput3.clear()

            #이름 입력 - 숫자 31자 입력 시도
            userInput4 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput4.click()
            userInput4.send_keys("1234567890123456789012345678901")
            time.sleep(1)
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='123456789012345678901234567890']").is_displayed()
            userInput4.clear()

            #이름 입력 - 특수문자 입력 시도
            userInput5 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput5.click()
            userInput5.send_keys("~!@#$%^&")
            time.sleep(1)

            # 다음 버튼 클릭 - 비활성화 확인(출입권한 화면으로 이동하지 않고 현재 화면 출력 확인)
            nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
            nextBtn.click()
            time.sleep(1)

            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름 및 지문").is_displayed()
            assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='~!@#$%^&']").is_displayed()

            pass
            print("DQS_T15914 지문 인증방식 설정 시 Validation 체크 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15914 지문 인증방식 설정 시 Validation 체크 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15922(self):
        try:
            print("DQS_T15922 사용자 초대에서 지문 스캔 시 등록 가능한 장치가 없는 경우 동작 확인")

            #지문 스캔 장치가 없는 공간으로 이동
            place = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비디오 공간")
            place.click()
            time.sleep(5)

            self.driver.tap([(273, 600)])
            time.sleep(3)

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 지문 인식 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지문 인식")
            qrSetting.click()

            # +지문 1 클릭
            finger1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+ 지문 1")
            finger1.click()
            time.sleep(1)

            # 등록가능 장치 없음 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지문 스캔").is_displayed()
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "등록 가능한 장치가 없습니다.").is_displayed()

            pass
            print("사용자 초대에서 지문 스캔 시 등록 가능한 장치가 없는 경우 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("사용자 초대에서 지문 스캔 시 등록 가능한 장치가 없는 경우 동작 확인 | Failed")
            print(str(e))
            self.fail()

    def test_DQS_T15924(self):
        try:
            print("DQS_T15924 사용자 초대에서 지문 스캔 타임아웃이 지난 경우 동작 확인")

            self.driver.tap([(967, 2084)])
            #사용자 초대 버튼 클릭
            time.sleep(1)

            inviteBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "초대하기")
            inviteBtn.click()

            # 인증 수단 - 지문 인식 선택
            qrSetting = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "지문 인식")
            qrSetting.click()

            #이름 입력
            userInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText")
            userInput.click()
            userInput.send_keys("Test_Finger1_e2e")
            time.sleep(1)

            # +지문 1 클릭
            finger1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "+ 지문 1")
            finger1.click()
            time.sleep(1)

            # 지문 등록장치 선택
            deviceFinger = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BLN2_OA_538761744")
            deviceFinger.click()
            time.sleep(22)

            # 스캔 타임 아웃 동작 확인
            assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "첫번째 지문 입력\n스캔 가능 시간을 초과하였습니다.\n다시 시도해 주세요.\n지문 스캔 남은시간\n00:00")

            pass
            print("DQS_T15924 사용자 초대에서 지문 스캔 타임아웃이 지난 경우 동작 확인 | Pass")

        except Exception as e:
            capture_screenshot(self.driver, self._testMethodName)
            print("DQS_T15924 사용자 초대에서 지문 스캔 타임아웃이 지난 경우 동작 확인 | Failed")
            print(str(e))
            self.fail()

if __name__ == '__main__':
    unittest.main()
