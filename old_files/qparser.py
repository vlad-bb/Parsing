# from selenium import webdriver


# def main():
#     driver = webdriver.Chrome(executable_path='https://selenoid.to-3d.com/status')
#     driver.get('https://www.gauthmath.com/solution/i1130273393/A-motor-boat-takes4hours-to-travel-128-miles-going'
#                '-upstream-The-return-trip-take')
#     answer = driver.find_element_by_xpath('/html/head/meta[1]').get_attribute('content')

#     return answer
#
#
# from selenium import webdriver
# from bs4 import BeautifulSoup
#
#
# def main():
#     chromedriver = 'https://selenoid.to-3d.com'
#     options = webdriver.ChromeOptions()
#     options.add_argument('headless')
#     browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
#     browser.get(
#         'https://www.gauthmath.com/solution/i1130273393/A-motor-boat-takes4hours-to-travel-128-miles-going-upstream-The-return-trip-take')
#     requiredHtml = browser.page_source
#     soup = BeautifulSoup(requiredHtml, 'html5lib')
#     meta = soup.find('content')


from selenium import webdriver
import time
import uuid
capabilities = {"browserName": "chrome", "version": "102"}


class Gauthmath(Search):
    def get_driver(self):
        return webdriver.Remote(command_executor="https://selenoid.to-3d.com/wd/hub",
                                desired_capabilities=capabilities)

    def get(self, id: str, url: str, entity=None) -> dict:
        driver = self.get_driver()
        driver.get(url)
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,700)", "")
        element = driver.find_elements_by_xpath("//button[text()='Get the Gauthmath App']")
        element[1].click()
        try:
            driver.find_element_by_css_selector("i[class*='index-module__icon-modal-close']").click()
        except:
            pass
        time.sleep(3)
        elements = driver.find_elements_by_css_selector("div[class*='index-module__expression']")
        filename = "/screens/" + uuid.uuid4().__str__() + ".png"
        elements[2].screenshot("static/dist" + filename)
        return {"screenshot": filename, "text": elements[2].text}


gauthmath = Gauthmath()
result = gauthmath.get("123", "https://www.gauthmath.com/solution/1723069356421125/12-In-1973-a-dozen-eggs-cost-0-78-Twenty-years-later-the-price-increased-to-0-85")
print(result)


# if __name__ == '__main__':
    # main()
