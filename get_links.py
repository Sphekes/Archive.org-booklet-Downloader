from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pyshadow.main import Shadow

import re
from pyvirtualdisplay import Display



def get_links(url):
    
    display = Display(visible=0, size=(800, 600))
    display.start()
    
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 0)
    driver = webdriver.Firefox(profile)
    driver.get(url)

    shadow = Shadow(driver)
    elem = shadow.find_element("button.click-for-photos")
    elem.click()

    # el_title = shadow.find_element("span.breaker-breaker")
    # title = el_title.text

    el_num = shadow.find_element(".BRcurrentpage")
    num_pages = int(re.findall('\d+', el_num.text)[1])

    el_link = shadow.find_element("div.BRpagecontainer:nth-child(1) > img:nth-child(1)")
    link = el_link.get_attribute("src").replace('&scale=4&rotate=0','')
    links = [link.replace('0000', str(i).zfill(4)) for i in range(num_pages)]

    driver.close()
    return links