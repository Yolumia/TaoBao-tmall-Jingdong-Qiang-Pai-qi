#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket
import paho.mqtt.client as mqtt
import wmi
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import time
import ntplib
import base64
import clipboard
from os import path



#d = path.dirname(__file__)
#abspath = path.abspath(d)
#chromedriver = abspath + "\chromedriver.exe"
#os.environ["webdriver.chrome.driver"] = chromedriver
#driver = webdriver.Chrome(chromedriver)

def on_message_callback(client, userdata, message):
 
    print(message.topic+" " + ":" + str(message.payload))
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
    print("Connected with result code "+str(rc))
    client.subscribe("times")
 
def link():
    client = mqtt.Client('601305005')
    client.connect("183.230.40.39", 6002, 60)
    client.username_pw_set('332255', 'qpq023')
    client.on_connect = on_connect
    mac= ""+get_mac_address()
    client.publish("times", mac, 1)
    # client.subscribe('times')
    client.on_message = on_message_callback
    client.loop_forever()

def get_mac_address():
    import uuid
    node = uuid.getnode()
    mac = uuid.UUID(int = node).hex[-12:]
    return mac

def login():
    #driver.get("https://www.taobao.com")
    time.sleep(5)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
        print("请在30秒内完成扫码")
        time.sleep(30)
        driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(5)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S.%f'))

def buy(buytime):
    print("抢购程序正在运行中！")
    print("设定时间"+buytime)
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > buytime:
            try:
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                    #currentPageUrl = driver.current_url
                    #print ("当前页为"+currentPageUrl)
                    while True:
                        try:
                            if driver.find_element_by_xpath('//*[@title="提交订单"]'):
                                driver.find_element_by_xpath('//*[@title="提交订单"]').click()
                                break  # 提交订单后退出循环
                            elif driver.find_element_by_xpath("//*[@id='submitOrderPC_1']/div/a[2]"):
                                driver.find_element_by_xpath("//*[@id='submitOrderPC_1']/div/a[2]").click()
                                break  # 提交订单后退出循环
                            elif driver.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a[2]'):
                                driver.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a[2]').click()
                                break  # 提交订单后退出循环
                            elif driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/div[1]/div/div[9]/div/div/a[2]"):
                                driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/div[1]/div/div[9]/div/div/a[2]").click()
                                break  # 提交订单后退出循环
                            elif driver.find_element_by_link_text('提交订单'):
                                driver.find_element_by_link_text('提交订单').click()
                                break  # 提交订单后退出循环
                            #time.sleep(0.1)
                            pass
                            print('成功提交订单')
                            break  # 提交订单后退出循环
                        except:
                            print('提交订单失败，正在重新提交')
                    while True:
                        print ("如果抢购成功，请手动输入密码" )
            except:
                #time.sleep(0.1)
                #print(now)
                pass
        #print(now)
        #print("设定时间"+buytime)
        #time.sleep(0.1)
        pass


if __name__ == "__main__":
    with open('time.txt', encoding='utf-8') as file_obj:
        contents = file_obj.read()
        print("读取设定时间成功：" + contents.rstrip())
        # times = "2020-06-20 20:00:00 000000"
    times = contents
    
    print ("设定时间=" + times)
   
    # print("本机序列号1=" + mac)
    # print("本机序列号2=" + board_id2)
    deadline = "2023-01-01 08:00:00.000000"
   

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.taobao.com")
    driver.maximize_window()

    #c = ntplib.NTPClient()
    #response = c.request('ntp1.aliyun.com')
    #ts = response.tx_time
    #_date = time.strftime('%Y-%m-%d', time.localtime(ts))
    #_time = time.strftime('%X', time.localtime(ts))
    #os.system('date {} && time {}'.format(_date, _time))
    #print("输入时间的格式：2020-09-06 08:00:00.000000\n")
    # times = input()

    if True:
        now2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now2 > times:
            while True:
                print("设定时间早于当前时间，请重新设定时间！请至少设定3分钟之后。")
                time.sleep(1)
        print("当前设置为淘宝天猫模式")
        login()
        buy(times)
   
