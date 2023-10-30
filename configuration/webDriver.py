from appium import webdriver


desired_cap = {
    "appium:deviceName": "R39M30571MZ",
    "platformName": "Android",
    "appium:appPackage": "com.suprema.moon",
    "appium:appActivity": "com.suprema.moon.MainActivity"
}

def mainApp():
    wd = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    wd.implicitly_wait(10)
    return  wd
