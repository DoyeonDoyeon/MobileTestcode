import json
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

class AppiumConfig:
    @staticmethod
    def get_driver():
        # 현재 스크립트의 디렉토리 경로를 얻음
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # 상대 경로를 사용하여 capability.json 파일의 전체 경로를 구성
        config_path = os.path.join(current_dir, 'capability.json')

        with open(config_path) as config_file:
            config = json.load(config_file)

        options = UiAutomator2Options()
        for key, value in config.items():
            setattr(options, key, value)

        return webdriver.Remote("http://localhost:4723/wd/hub", options=options)
