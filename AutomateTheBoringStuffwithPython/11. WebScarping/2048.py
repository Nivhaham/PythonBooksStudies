import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

# This code will play the 2048 game in a random manner.

def main():
    driver = webdriver.Chrome()
    driver.get("https://play2048.co/")

    for i in range(1000):
        key = random.randint(1, 4)
        if key == 1:
            driver.switch_to.active_element.send_keys(Keys.ARROW_UP)
        elif key == 2:
            driver.switch_to.active_element.send_keys(Keys.ARROW_RIGHT)
        elif key == 3:
            driver.switch_to.active_element.send_keys(Keys.ARROW_DOWN)
        else:
            driver.switch_to.active_element.send_keys(Keys.LEFT)
        time.sleep(0.1)

if __name__ == '__main__':
    main()