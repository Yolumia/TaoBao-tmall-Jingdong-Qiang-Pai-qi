#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket
import paho.mqtt.client as mqtt
import wmi
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
import datetime
import time
# import ntplib
import base64
import clipboard
from os import path




def on_message_callback(client, userdata, message):
    print(message.topic + " " + ":" + str(message.payload))
    print("输入时间的格式：2020-09-30 08:00:00 000000\n")
    # times = input()
    with open('time.txt', encoding='utf-8') as file_obj:
        contents = file_obj.read()
        print(contents.rstrip())
    # times = "2020-09-30 20:00:00 000000"
    times = contents
    login()
    buy(times)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("times")


def link():
    client = mqtt.Client('601305005')
    client.connect("183.230.40.39", 6002, 60)
    client.username_pw_set('332255', 'qpq023')
    client.on_connect = on_connect
    mac = "" + get_mac_address()
    client.publish("times", mac, 1)
    # client.subscribe('times')
    client.on_message = on_message_callback
    client.loop_forever()


def get_mac_address():
    import uuid
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return mac


def login():
    driver.get("https://www.jd.com")
    time.sleep(5)
    if driver.find_element_by_link_text("你好，请登录"):
        driver.find_element_by_link_text("你好，请登录").click()
        print("请在30秒内完成扫码")
        time.sleep(30)
        driver.get("https://cart.jd.com/cart.action")
    time.sleep(5)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    print("程序正在运行")
    print("设定时间："+buytime)
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > buytime:
            try:
                #driver.get("https://cart.jd.com/cart.action")
                #if driver.find_element_by_id('toggle-checkboxes_down'):
                #   driver.find_element_by_id('toggle-checkboxes_down').click()
                driver.get("https://trade.jd.com/shopping/order/getOrderInfo.action")#https://trade.jd.com/shopping/order/getOrderInfo.action
                #currentPageUrl = driver.current_url
                #print ("当前页为" + currentPageUrl)
                try:
                    if driver.find_element_by_id('order-submit'):
                            driver.find_element_by_id('order-submit').click()
                            time.sleep(30)
                    elif driver.find_element_by_xpath("/html/body/div[15]/div/div[10]/div[7]/div/div[2]/div[1]/button[1]"):
                        driver.find_element_by_xpath( "/html/body/div[15]/div/div[10]/div[7]/div/div[2]/div[1]/button[1]").click()
                        time.sleep(30)
                except:
                    #time.sleep(0.1)
                    #print(now)
                    pass
            except:
                #time.sleep(0.1)
                #print(now)
                pass
        pass
        #print(now)
        #time.sleep(0.1)



if __name__ == "__main__":
    with open('time.txt', encoding='utf-8') as file_obj:
        contents = file_obj.read()
        print("读取设定时间成功：" + contents.rstrip())
        # times = "2020-06-20 20:00:00 000000"
    times = contents


    print("设定时间=" + times)
   
    deadline = "2023-06-01 08:00:00.000000"

    chrome_options = webdriver.ChromeOptions()
    #prefs = {"profile.managed_default_content_settings.images": 2}
    #chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.jd.com")
    driver.maximize_window()

    # c = ntplib.NTPClient()
    # response = c.request('ntp1.aliyun.com')
    # ts = response.tx_time
    # _date = time.strftime('%Y-%m-%d', time.localtime(ts))
    # _time = time.strftime('%X', time.localtime(ts))
    # os.system('date {} && time {}'.format(_date, _time))
    # print("输入时间的格式：2020-09-06 08:00:00 000000\n")
    # times = input()

    if True:
        now2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now2 > times:
            while True:
                print("设定时间早于当前时间，请重新设定时间！请至少设定3分钟之后。")
                time.sleep(1)
        print("当前设置为JD模式")
        login()
        buy(times)
    


