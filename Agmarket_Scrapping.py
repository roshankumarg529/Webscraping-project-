#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import required module
import time
from selenium import webdriver
# Import Select class
from selenium.webdriver.support.ui import Select
# Using chrome driver

commodity = "Potato" # val=24
State = "Uttar Pradesh"
District = "Agra"
# Market = all
Date = "01-Jan-2020"
To = "31-Dec-2020"

driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://agmarknet.gov.in/")
print("Connecting....")
time.sleep(5)
# Select commodity
selectCommodity = Select(driver.find_element_by_xpath('//*[@id="ddlCommodity"]'))
selectCommodity.select_by_value('24')
time.sleep(5)

#Select State
selectState = Select(driver.find_element_by_xpath('//*[@id="ddlState"]'))
selectState.select_by_value('UP')
time.sleep(5)

#Select District
selectDistrict = Select(driver.find_element_by_xpath('//*[@id="ddlDistrict"]'))
selectDistrict.select_by_value('1')
time.sleep(5)

selectMarket = driver.find_element_by_xpath('//*[@id="ddlMarket"]') 

options = [x for x in selectMarket.find_elements_by_tag_name("option")]
opt_list = []
for element in options:
    opt_list.append(element.get_attribute("value"))
    
opt_list = opt_list[1:]


for val in opt_list:
    selectMarket = Select(driver.find_element_by_xpath('//*[@id="ddlMarket"]'))
    selectMarket.select_by_value(val)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="txtDate"]').clear()
    driver.find_element_by_xpath('//*[@id="txtDate"]').send_keys(Date)
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="txtDateTo"]').clear()
    driver.find_element_by_xpath('//*[@id="txtDateTo"]').send_keys(To)
    time.sleep(3)
    
    driver.find_element_by_xpath('//*[@id="btnGo"]').click()
    time.sleep(10)
    
    driver.find_element_by_xpath('//*[@id="cphBody_ButtonExcel"]').click()
    
    
# driver.find_element_by_xpath('//*[@id="btnGo"]').click()
    

