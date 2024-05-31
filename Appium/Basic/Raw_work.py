import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService

# Start Appium Server Programmatically using AppiumService
appium_service = AppiumService()
appium_service.start()
print("Appium server started successfully!")
time.sleep(5)  # Give some time for the server to start

# Create desired capabilities for the game
desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '10',
    'deviceName': 'Pixel5',
    'app': '/Users/sheheryarshah/Downloads/Android_Demo_App.apk',
    'appPackage': 'com.code2lead.kwad',
    'appActivity': 'com.code2lead.kwad.MainActivity'
}

# Create Appium options and load desired capabilities
options = AppiumOptions().load_capabilities(desired_caps)

# Create WebDriver object to control the game
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)

# Action on the game
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

# Close the WebDriver
driver.quit()

# Stop the Appium server
appium_service.stop()
print("Appium server stopped successfully!")