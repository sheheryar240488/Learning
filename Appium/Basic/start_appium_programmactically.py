import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


"""#import appium service class
from appium.webdriver.appium_service import AppiumService


#create appium servise class object
appium_service = AppiumService()
appium_service.start()

# Call start method by using appium service
#appium_service.start()

# Check if the server started successfully
if appium_service.is_running:
    print("Appium server started successfully!")
else:
    print("Failed to start Appium server.")
"""
# Create desired caps
desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "platformVersion": "10.0",
    "deviceName": "emulator-5554",
    "app": "/Users/sheheryarshah/Downloads/Android_Demo_App.apk"

}
"""desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel5'
desired_caps['app'] = ('/Users/sheheryarshah/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
"""
# Create the driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# Interact with your app
button = driver.find_element_by_accessibility_id("Btn1")
button.click()

# Close the driver
time.sleep(5)
driver.quit()

"""

#step 5 call stop method by using the appium service
# Check if the server stopped successfully
appium_service.stop()
if not appium_service.is_running:
    print("Appium server stopped successfully!")
else:
    print("Failed to stop Appium server.")
"""