from selenium import webdriver



def main():
    driver = webdriver.Chrome(executable_path='/Users/user/Documents/GitHub/Parsing/chromedriver')
    driver.get('https://www.gauthmath.com/solution/i1130273393/A-motor-boat-takes4hours-to-travel-128-miles-going-upstream-The-return-trip-take')
    answer = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/main/div[2]/div[5]/div/div/p[2]').text
    return  answer

if __name__ == '__main__':
    main()
