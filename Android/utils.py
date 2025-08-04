import re
import time
import requests
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import os
from configuration.webDriver import AppiumConfig
from configuration.utill import capture_screenshot
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


" XPath "
phoneNumberInputBox = "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]"
passwordInputBox = "//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]"
emailInputBox = "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[1]"
emailPasswordInputBox = "//android.widget.ImageView[@content-desc=\"이메일 주소\n비밀번호\"]/android.widget.EditText[2]"
lead = "//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView"

" AccessBilityID "
login = "로그인"
logout = "로그아웃"
confirm = "확인"
cancel = "취소"
allAgree = "약관 전체 동의"
next = "다음"
authRequest = "인증요청"
authComplete = "인증완료"
mobileLogin = "모바일로 로그인"
emailLogin = "이메일로 로그인"

" ClassName "
signUpInput = "android.widget.EditText"
widgetImage = "android.widget.ImageView"

class utils(unittest.TestCase):

    def authCode(self):
        self.driver.press_keycode(3)
        # 홈화면
        time.sleep(1)

        if "outlook" not in self.driver.current_package:
            print("앱이 종료되어 다시 실행")
            self.driver.activate_app("com.microsoft.office.outlook")

        for _ in range(3):  # 새로고침
            start_x1 = 573
            start_y1 = 291
            end_x1 = 573
            end_y1 = 559
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            time.sleep(3)

        self.driver.tap([(497, 358)])
        time.sleep(2)

        MAX_RETRIES = 7
        WAIT_TIME = 3
        retries = 0

        while retries < MAX_RETRIES:
            elements = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")
            count = len(elements)

            if count >= 16:
                print(f"요소 {count}개 찾음. 모든 요소의 텍스트값 추출 시작")
                break

            print(f"현재 요소 {count}개 찾음. 16개 이상 찾을 때까지 재시도 중...({retries + 1}/{MAX_RETRIES}")
            time.sleep(WAIT_TIME)
            retries += 1
        else:
            print("최대 시도 횟수를 초과하였습니다. 요소를 충분히 찾지 못하였습니다.")

            self.driver.press_keycode(3)
            # 홈화면
            time.sleep(1)

            outlook_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Outlook")
            outlook_button.click()
            time.sleep(1)

        elements2 = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")

        if len(elements2) >= 15:
            text_value = elements2[14].get_attribute("text")
            print("인증번호:", text_value)
        else:
            print("인증번호 없음")

        officeBack = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "닫기")
        officeBack.click()
        time.sleep(1)

        self.driver.press_keycode(3)
        # 홈화면
        time.sleep(1)

        clue_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe")
        clue_button.click()
        time.sleep(0.5)

        auth_input_box = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
        auth_input_box.click()
        auth_input_box.send_keys(text_value)

    def authCode_mobile(self):
        self.driver.press_keycode(3)
        #홈화면
        time.sleep(1)

        teamsApp_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Teams")
        teamsApp_button.click()

        for _ in range(2): #새로고침
            start_x1 = 573
            start_y1 = 291
            end_x1 = 573
            end_y1 = 559
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            time.sleep(1)

        chSelete = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.microsoft.teams:id/textView' and @text='채널']")
        chSelete.click()

        mobileAuthCh = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.microsoft.teams:id/teams_channel_text' and @text='CLUe 인증 코드 수신채널']")
        mobileAuthCh.click()
        time.sleep(2)

        elements = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@content-desc]")

        for i, el in enumerate(elements, start=1):
            text_value1 = el.get_attribute("text")
            print(f"요소 {i}의 텍스트 값: {text_value1}")

        if len(elements) >= 4:
            fourth_element = elements[3]
            content_desc = fourth_element.get_attribute("content-desc")
            print(f"4번쨰 요소의 content-desc 값: {content_desc}")

            num_value = content_desc[25:31]
            print(f"추출한 값: {num_value}")

        else:
            print("요소가 4개 미만이라 content-desc를 추출할 수 없음.")

        teamsBack = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "뒤로")
        teamsBack.click()
        time.sleep(0.3)

        chSelete2 = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.microsoft.teams:id/textView' and @text='채널']")
        chSelete2.click()
        time.sleep(0.1)

        self.driver.press_keycode(3)
        #홈화면
        time.sleep(1)

        clue_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe")
        clue_button.click()
        time.sleep(0.5)

        auth_input_box = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
        auth_input_box.click()
        auth_input_box.send_keys(num_value)

    # def email_Token(self):
    #     url1 = "https://api.moon.supremainc.com/stage/v1/accounts/login/email"
    #     headers1 = {
    #         "Content-Type": "application/json"
    #     }
    #     body1 = {
    #         "email": "kjjung+pga@suprema.co.kr",
    #         "password": "Kjstar36!!",
    #         "authDeviceType": "WEB_BROWSER"
    #     }
    #     response1 = requests.post(url1, headers=headers1, json=body1)
    #     print("Status Code:", response1.status_code)
    #     try:
    #         print("Response JSON:", response1.json())
    #     except Exception:
    #         print("Response Text:", response1.text)
    #
    #     self.driver.press_keycode(3)
    #     # 홈화면
    #     time.sleep(1)
    #
    #     if "outlook" not in self.driver.current_package:
    #         print("앱이 종료되어 다시 실행")
    #         self.driver.activate_app("com.microsoft.office.outlook")
    #
    #     for _ in range(3):  # 새로고침
    #         start_x1 = 573
    #         start_y1 = 291
    #         end_x1 = 573
    #         end_y1 = 559
    #         self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
    #         time.sleep(3)
    #
    #     self.driver.tap([(497, 358)])
    #     time.sleep(2)
    #
    #     MAX_RETRIES = 10
    #     WAIT_TIME = 3
    #     retries = 0
    #
    #     while retries < MAX_RETRIES:
    #         elements = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")
    #         count = len(elements)
    #
    #         if count >= 16:
    #             print(f"요소 {count}개 찾음. 모든 요소의 텍스트값 추출 시작")
    #             break
    #
    #         print(f"현재 요소 {count}개 찾음. 16개 이상 찾을 때까지 재시도 중...({retries + 1}/{MAX_RETRIES}")
    #         time.sleep(WAIT_TIME)
    #
    #         self.driver.press_keycode(3)
    #         # 홈화면
    #         time.sleep(1)
    #
    #         outlook_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Outlook")
    #         outlook_button.click()
    #         time.sleep(1)
    #
    #     elements2 = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")
    #
    #     if len(elements2) >= 15:
    #         text_value = elements2[14].get_attribute("text")
    #         print("인증번호:", text_value)
    #     else:
    #         print("인증번호 없음")
    #
    #     officeBack = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "닫기")
    #     officeBack.click()
    #     time.sleep(1)
    #
    #     url2 = "https://api.moon.supremainc.com/stage/v1/accounts/login/two-factor"
    #     headers2 = {
    #       "Content-Type": "application/json"
    #     }
    #     body2 = {
    #         "email": "kjjung+pga@suprema.co.kr",
    #         "twoFactor": text_value,
    #         "authDeviceType": "WEB_BROWSER"
    #     }
    #     response2 = requests.post(url2, headers=headers2, json=body2)
    #     if response2.status_code == 200:
    #         data = response2.json().get("data", {})
    #         access_token = data.get("accessToken")
    #         refresh_token = data.get("refreshToken")
    #         print("Access Token:", access_token)
    #         print("Refresh Token:", refresh_token)

    def placeInviteEmail(self):
        url1 = "https://api.moon.supremainc.com/stage/v1/accounts/login/email"
        headers1 = {
            "Content-Type": "application/json"
        }
        body1 = {
            "email": "kjjung+pga@suprema.co.kr",
            "password": "Kjstar36!!",
            "authDeviceType": "WEB_BROWSER"
        }
        response1 = requests.post(url1, headers=headers1, json=body1)
        print("Status Code:", response1.status_code)
        try:
            print("Response JSON:", response1.json())
        except Exception:
            print("Response Text:", response1.text)

        self.driver.press_keycode(3)
        # 홈화면
        time.sleep(1)

        if "outlook" not in self.driver.current_package:
            print("앱이 종료되어 다시 실행")
            self.driver.activate_app("com.microsoft.office.outlook")

        for _ in range(3):  # 새로고침
            start_x1 = 573
            start_y1 = 291
            end_x1 = 573
            end_y1 = 559
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            time.sleep(3)

        self.driver.tap([(497, 358)])
        time.sleep(2)

        MAX_RETRIES = 7
        WAIT_TIME = 3
        retries = 0

        while retries < MAX_RETRIES:
            elements = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")
            count = len(elements)

            if count >= 16:
                print(f"요소 {count}개 찾음. 모든 요소의 텍스트값 추출 시작")
                time.sleep(0.1)
                break

            print(f"현재 요소 {count}개 찾음. 16개 이상 찾을 때까지 재시도 중...({retries + 1}/{MAX_RETRIES}")
            time.sleep(WAIT_TIME)
            retries += 1
        else:
            print("최대 시도 횟수를 초과하였습니다. 요소를 충분히 찾지 못하였습니다.")

        self.driver.press_keycode(3)
            # 홈화면
        time.sleep(1)

        outlook_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Outlook")
        outlook_button.click()
        time.sleep(1)

        elements2 = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")

        if len(elements2) >= 15:
            text_value = elements2[14].get_attribute("text")
            print("인증번호:", text_value)
        else:
            print("인증번호 없음")

        officeBack = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "닫기")
        officeBack.click()
        time.sleep(1)

        url2 = "https://api.moon.supremainc.com/stage/v1/accounts/login/two-factor"
        headers2 = {
            "Content-Type": "application/json"
        }
        body2 = {
            "email": "kjjung+pga@suprema.co.kr",
            "twoFactor": text_value,
            "authDeviceType": "WEB_BROWSER"
        }
        response2 = requests.post(url2, headers=headers2, json=body2)
        if response2.status_code == 200:
            data = response2.json().get("data", {})
            access_token = data.get("accessToken")
            refresh_token = data.get("refreshToken")
            print("Access Token:", access_token)
            print("Refresh Token:", refresh_token)

        url = "https://api.moon.supremainc.com/stage/v1/places/27/invite-email"
            # 현재 공간 그룹에서 발급된 API Key로 동작이 안되어 SO계정 로그인 후 해당 토큰으로 임시로 넣어둠, 테스트 할때 마다 토근 입력해야 됨
        #token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0dGMiOiJhYyIsImR0YyI6IndiIiwiZXhwIjoxNzUzNDE3Mjk3LCJyaWMiOjE3OCwiaWF0IjoxNzUzNDEzNjk3fQ.ALhZ53j8gSvmKPFLeL5oS4d3WuIAM7bBIZgo_4DaZfA"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        body = {
            "invitees": [
                {
                    "email": "kjjung+pp1001@suprema.co.kr",
                    "role": "MASTER"
                }
            ]
        }
        response = requests.post(url, headers=headers, json=body)
        print("Status Code:", response.status_code)
        try:
            print("Response JSON:", response.json())
        except Exception:
            print("Response Text:", response.text)

        self.driver.press_keycode(3)
        # 홈화면
        time.sleep(0.5)

        clue_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe")
        clue_button.click()
        time.sleep(0.5)

    def placeInvitePhone(self):
        url1 = "https://api.moon.supremainc.com/stage/v1/accounts/login/email"
        headers1 = {
            "Content-Type": "application/json"
        }
        body1 = {
            "email": "kjjung+pga@suprema.co.kr",
            "password": "Kjstar36!!",
            "authDeviceType": "WEB_BROWSER"
        }
        response1 = requests.post(url1, headers=headers1, json=body1)
        print("Status Code:", response1.status_code)
        try:
            print("Response JSON:", response1.json())
        except Exception:
            print("Response Text:", response1.text)

        self.driver.press_keycode(3)
        # 홈화면
        time.sleep(1)

        if "outlook" not in self.driver.current_package:
            print("앱이 종료되어 다시 실행")
            self.driver.activate_app("com.microsoft.office.outlook")

        for _ in range(3):  # 새로고침
            start_x1 = 573
            start_y1 = 291
            end_x1 = 573
            end_y1 = 559
            self.driver.swipe(start_x1, start_y1, end_x1, end_y1)
            time.sleep(3)

        self.driver.tap([(497, 358)])
        time.sleep(2)

        MAX_RETRIES = 7
        WAIT_TIME = 3
        retries = 0

        while retries < MAX_RETRIES:
            elements = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")
            count = len(elements)

            if count >= 16:
                print(f"요소 {count}개 찾음. 모든 요소의 텍스트값 추출 시작")
                break

            print(f"현재 요소 {count}개 찾음. 16개 이상 찾을 때까지 재시도 중...({retries + 1}/{MAX_RETRIES}")
            time.sleep(WAIT_TIME)
            retries += 1
        else:
            print("최대 시도 횟수를 초과하였습니다. 요소를 충분히 찾지 못하였습니다.")

            self.driver.press_keycode(3)
            # 홈화면
            time.sleep(1)

            outlook_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Outlook")
            outlook_button.click()
            time.sleep(1)

        elements2 = self.driver.find_elements(AppiumBy.XPATH, "//android.view.View[@text][1]")

        if len(elements2) >= 15:
            text_value = elements2[14].get_attribute("text")
            print("인증번호:", text_value)
        else:
            print("인증번호 없음")

        officeBack = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "닫기")
        officeBack.click()
        time.sleep(1)

        url2 = "https://api.moon.supremainc.com/stage/v1/accounts/login/two-factor"
        headers2 = {
            "Content-Type": "application/json"
        }
        body2 = {
            "email": "kjjung+pga@suprema.co.kr",
            "twoFactor": text_value,
            "authDeviceType": "WEB_BROWSER"
        }
        response2 = requests.post(url2, headers=headers2, json=body2)
        if response2.status_code == 200:
            data = response2.json().get("data", {})
            access_token = data.get("accessToken")
            refresh_token = data.get("refreshToken")
            print("Access Token:", access_token)
            print("Refresh Token:", refresh_token)

        url = "https://api.moon.supremainc.com/stage/v1/places/27/invite-phone"
        # 현재 공간 그룹에서 발급된 API Key로 동작이 안되어 SO계정 로그인 후 해당 토큰으로 임시로 넣어둠, 테스트 할때 마다 토근 입력해야 됨
        #token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0dGMiOiJhYyIsImR0YyI6IndiIiwiZXhwIjoxNzUzNDE3Mjk3LCJyaWMiOjE3OCwiaWF0IjoxNzUzNDEzNjk3fQ.ALhZ53j8gSvmKPFLeL5oS4d3WuIAM7bBIZgo_4DaZfA"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        body = {
            "invitees": [
                {
                    "countryCode": "kr",
                    "phone": "01010010001",
                    "role": "MASTER"
                }
            ]
        }
        response = requests.post(url, headers=headers, json=body)
        print("Status Code:", response.status_code)
        try:
            print("Response JSON:", response.json())
        except Exception:
            print("Response Text:", response.text)

        self.driver.press_keycode(3)
        # 홈화면
        time.sleep(0.5)

        clue_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe")
        clue_button.click()
        time.sleep(0.5)

        self.driver.press_keycode(3)
        # 홈화면
        time.sleep(0.5)

        clue_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Suprema CLUe")
        clue_button.click()
        time.sleep(0.5)

    def signUpEmail(self):
        signUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
        signUp.click()

        agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, allAgree)
        agree.click()

        nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, next)
        nextBtn.click()

        emailInput = self.driver.find_element(AppiumBy.CLASS_NAME, signUpInput)
        emailInput.click()
        emailInput.send_keys("kjjung+pp1001@suprema.co.kr")


        self.driver.hide_keyboard()

        authBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authRequest)
        authBtn.click()
        time.sleep(0.1)

        utils.authCode(self)

        authComBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, authComplete)
        authComBtn.click()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이메일 주소").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "kjjung+pp1001@suprema.co.kr").is_displayed()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름").is_displayed()
        nameInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
        nameInput.click()
        nameInput.send_keys("Test singUP")

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호").is_displayed()
        passwordInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[2]")
        passwordInput.click()
        passwordInput.send_keys("Kjstar36!!")

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재입력").is_displayed()
        rePasswordInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[3]")
        rePasswordInput.click()
        rePasswordInput.send_keys("Kjstar36!!")

        self.driver.hide_keyboard()

        startBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시작하기")
        startBtn.click()


    def signUpMobile(self):
        signUp = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "회원가입")
        signUp.click()

        agree = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "약관 전체 동의")
        agree.click()

        nextBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "다음")
        nextBtn.click()

        mobileSel = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "모바일")
        mobileSel.click()

        mobileInput = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        mobileInput.click()
        mobileInput.send_keys("01010010001")

        authRequest = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증요청")
        authRequest.click()

        utils.authCode_mobile(self)

        self.driver.hide_keyboard()

        authApply = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "인증완료")
        authApply.click()

        time.sleep(0.1)

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "휴대폰 번호").is_displayed()
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "010 1001 0001").is_displayed()

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "이름").is_displayed()
        nameInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[1]")
        nameInput.click()
        nameInput.send_keys("Test SingUP")

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호").is_displayed()
        passwordInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[2]")
        passwordInput.click()
        passwordInput.send_keys("Kjstar36!!")

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "비밀번호 재입력").is_displayed()
        rePasswordInput = self.driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[3]")
        rePasswordInput.click()
        rePasswordInput.send_keys("Kjstar36!!")

        self.driver.hide_keyboard()

        startBtn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "시작하기")
        startBtn.click()















