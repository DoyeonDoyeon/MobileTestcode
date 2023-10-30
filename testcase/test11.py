from appium import webdriver
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = 'R39M30571MZ'
options.app_package = 'com.suprema.moon'
options.app_activity = 'com.suprema.moon.MainActivity'
options.automation_name = 'UiAutomator2'

# Appium 서버에 연결하고 드라이버 인스턴스를 생성합니다.
driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)

el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="로그인")
el4.click()
el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
el5.click()
el5.send_keys("01090497847")
el6 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
el6.click()
el6.send_keys("Rlaehdus100!")
el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="로그인")
el7.click()
el8 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView")
el8.click()
el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="로그아웃")
el9.click()
el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="확인")
el10.click()
els1 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.Button[@content-desc=\"로그인\"]")
el11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="로그인")
el11.click()
els2 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")
els3 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[2]")
els4 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"휴대폰 번호\n비밀번호\"]/android.widget.EditText[1]")

driver.quit()
