from selenium import webdriver



def main():
    driver = webdriver.Chrome(executable_path='https://selenoid.to-3d.com/status')
    driver.get('https://www.gauthmath.com/solution/i1130273393/A-motor-boat-takes4hours-to-travel-128-miles-going-upstream-The-return-trip-take')
    answer = driver.find_element_by_class_name('in102').text
    return  answer

if __name__ == '__main__':
    main()
