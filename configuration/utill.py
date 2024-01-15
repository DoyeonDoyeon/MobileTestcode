from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
import os
from datetime import datetime
import re
import subprocess
from selenium.webdriver import ActionChains


def swipe_until_element_found(driver, xpath, max_swipes=10):
    """
    주어진 XPath의 요소를 찾을 때까지 화면을 아래로 스와이프합니다.

    :param driver: Appium WebDriver 인스턴스
    :param xpath: 찾고자 하는 요소의 XPath
    :param max_swipes: 최대 스와이프 시도 횟수
    :return: 요소를 찾으면 True, 찾지 못하면 False 반환
    """
    for _ in range(max_swipes):
        try:
            element = driver.find_element(AppiumBy.XPATH, xpath)
            if element.is_displayed():
                return True
        except:
            # 요소가 없으면 스와이프를 수행합니다.
            swipe_up(driver)

    return False

def swipe_up(driver):
    """
    화면을 아래에서 위로 스와이프합니다.

    :param driver: Appium WebDriver 인스턴스
    """
    window_size = driver.get_window_size()
    start_x = window_size['width'] // 2
    start_y = window_size['height'] * 3 // 4
    end_x = start_x
    end_y = window_size['height'] // 4

    action = TouchAction(driver)
    action.press(x=start_x, y=start_y).wait(700).move_to(x=end_x, y=end_y).release().perform()


def capture_screenshot(driver, test_name):
    """
    실패한 화면의 스크린샷을 캡처하고 저장합니다.

    :param driver: Appium WebDriver 인스턴스
    :param test_name: 테스트 케이스의 이름
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_folder = os.path.join(os.getcwd(), "screenshots")
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)
    screenshot_file = os.path.join(screenshot_folder, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot saved to {screenshot_file}")

def extract_verification_code(driver, phone_number):
    """
    SMS 메시지에서 인증번호를 추출합니다.

    :param driver: Appium WebDriver 인스턴스
    :param phone_number: SMS를 보낸 전화번호
    :return: 추출된 인증번호
    """
    # adb 명령어를 사용하여 최근 SMS 메시지를 가져옵니다.
    command = f"adb shell dumpsys sms --phone {phone_number}"
    result = subprocess.check_output(command, shell=True).decode('utf-8')

    # 정규 표현식을 사용하여 6자리 인증번호를 찾습니다.
    match = re.search(r'(\d{6})', result)
    if match:
        return match.group(1)
    else:
        raise Exception("Verification code not found in SMS")

def swipe(self, start_x, start_y, end_x, end_y):
    actions = ActionChains(self.driver)
    actions.move_to_location(start_x, start_y)
    actions.click_and_hold()
    actions.move_by_offset(end_x - start_x, end_y - start_y)
    actions.release()
    actions.perform()
