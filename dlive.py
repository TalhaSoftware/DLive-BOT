# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 10:45:52 2021

@author: TalhaSoftware
"""

import requests
from bs4 import BeautifulSoup
import re 
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import random



url = "https://dlive.tv/xxx"

with open('emails.txt') as f: emails = f.readlines()

for i in range(1):
    options = Options()
    options.headless = True
    browser = webdriver.Firefox()
    email = random.choice(emails)
    emails.remove(email)
    emails = ''.join(emails)
    with open('emails.txt', 'w') as f:
        f.write(emails)
    email, email_password = email.strip().split(':')
    
    browser.get(url)
    # time.sleep(2)
    try:
        browser.find_element_by_class_name("sign-in-button").click()
    except:
        try:
            browser.find_element_by_css_selector("#genius > div.application--wrap > div:nth-child(1) > nav > div > div.navbar-items-right.flex-all-center > div.text-xs-right > div > div:nth-child(1) > div.sign-register-buttons.flex-align-center > div.d-btn.border-radius-3.text-14-medium.no-select.flex-all-center.text-nowrap.position-relative.marginl-4.btnC.clickable > div").click()
        except:
            pass
    try:
        userarea = browser.find_element_by_css_selector(".v-form > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
        userarea.send_keys(email)
    except:
        userarea = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[102]/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div[1]/form/div[1]/div/div/div/div/input")
        userarea.send_keys(email)
    try:
        passwordarea = browser.find_element_by_css_selector("#genius > div.v-dialog__content.v-dialog__content--active > div > div > div.flex-auto > div:nth-child(2) > div > div > div:nth-child(1) > div > div:nth-child(1) > div.flex-all-center.flex-column > form > div:nth-child(2) > div > div > div > div > input[type=password]")
        passwordarea.send_keys(email_password)
    except:
        passwordarea = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[104]/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div[1]/form/div[2]/div/div/div/div/input")
        passwordarea.send_keys(email_password)
    try:
        girisyap = browser.find_element_by_css_selector("#genius > div.v-dialog__content.v-dialog__content--active > div > div > div.flex-auto > div:nth-child(2) > div > div > div:nth-child(1) > div > div:nth-child(1) > div.flex-all-center.flex-column > form > div.d-btn.border-radius-3.text-14-medium.no-select.flex-all-center.text-nowrap.position-relative.width-100.border-radius-5.btnC.clickable > div")
        girisyap.click()
    except:
        girisyap = browser.find_element_by_xpath('//*[@id="genius"]/div[36]/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div[1]/form/div[3]/div')
        girisyap.click()
    
    
    
    time.sleep(1)
    takip= browser.find_element_by_css_selector(".channel-header-right > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")
    try:
        yazi = takip.text
        print(yazi)
        if(yazi == "Takip et"):
            takip.click()
            print("Takip ediliyor")
           
    except:
        pass
    # time.sleep(2)
    msg = "Sorry For Text Message :)"
    try:
        browser.find_element_by_css_selector('.textarea > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > textarea:nth-child(1)').send_keys(msg+ Keys.ENTER)
        browser.find_element_by_css_selector("#chatroom > div.v-stream-chatroom-input.paddingt-3.paddingb-4.paddinglr-4.bordert-grey.position-relative > div:nth-child(2) > div.flex-justify-end.paddingt-3 > div.d-btn.border-radius-3.text-14-medium.no-select.flex-all-center.text-nowrap.position-relative.text-12-medium.marginl-3.btnC.clickable > div").click()
        
    except:
        try:
            browser.find_element_by_xpath('//*[@id="chatroom"]/div[3]/div[2]/div[1]/div[1]/div/div/div/div/textarea').send_keys(msg+ Keys.ENTER)
            browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[50]/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div').click()
        except:
           try:
               browser.find_element_by_xpath('//*[@id="chatroom"]/div[3]/div[2]/div[1]/div[1]/div/div/div/div/textarea').send_keys(msg+ Keys.ENTER)
               browser.find_element_by_xpath('//*[@id="chatroom"]/div[3]/div[2]/div[1]/div[1]/div/div/div/div/textarea').send_keys(Keys.ENTER)
               browser.find_element_by_xpath('//*[@id="chatroom"]/div[3]/div[2]/div[1]/div[1]/div/div/div/div/textarea').send_keys(Keys.ENTER)
               browser.find_element_by_xpath('//*[@id="chatroom"]/div[3]/div[2]/div[1]/div[1]/div/div/div/div/textarea').send_keys(Keys.ENTER)
           except:
               pass
    print("Mesaj Gönderildi "+email)
    time.sleep(2)
    browser.close()
    
