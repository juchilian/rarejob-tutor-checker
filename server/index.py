from datetime import datetime, timedelta
import logging
from os import error
from decouple import config
from pytz import timezone
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


class RarejobBooker:
    def __init__(self, chrome_path, reserve_time_list) -> None:
        self.domain = 'https://www.rarejob.com'
        self.driver = webdriver.Chrome(chrome_path)
        self.driver.implicitly_wait(3)
        self.reserve_time_list = reserve_time_list
        self.reservation_link_dict = self.make_reserve_time_dict()
        self.has_reserved = False


    def login(self):
        self.driver.get(self.domain + '/account/login/')
        MY_EMAIL = config('email')
        MY_PASSWORD = config('password')
        email_field = self.driver.find_element_by_id('RJ_LoginForm_email')
        email_field.clear()
        email_field.send_keys(MY_EMAIL)
        password_field = self.driver.find_element_by_id('RJ_LoginForm_password')
        password_field.clear()
        password_field.send_keys(MY_PASSWORD)
        password_field.send_keys(Keys.RETURN)


    def reserve_from_bookmark(self):
        if self.has_reserved:
            return
        
        tomorrow_str = self.get_tommorow_str()
        MAX_BOOKMARK_PAGE = 7
        for page_num in range(1, MAX_BOOKMARK_PAGE + 1):
            page_url = self.domain + '/reservation/bookmark/{}/#page={}'.format(tomorrow_str, page_num)
            self.driver.get(page_url)
            logging.info('Successfully visited', page_url)
            # print(page_url)
            time.sleep(1)
            if self.check_terminate():
                reservation_url, valid = self.get_best_url()
                if valid:
                    self.make_reservation(reservation_url)                
                break
            for time_str in self.reserve_time_list:
                reserve_time_elements = self.driver.find_elements_by_link_text(time_str)
                print(len(reserve_time_elements), 'lessons found at', time_str, 'on page', page_num)
                for link in reserve_time_elements:
                    url = link.get_attribute("href")
                    self.reservation_link_dict[time_str].append(url)
    
    def reserve_from_available(self):
        if self.has_reserved:
            return
        time_parameter_dict = dict({'6:30': 13, '7:00': 14, '7:30': 15, '8:00': 16, '8:30': 17, '9:00': 18, '9:30': 19, '10:00': 20, '10:30': 21, '11:00': 22, '11:30': 23, '12:00': 24, '12:30': 25, '13:00': 26, '13:30': 27, '14:00': 28, '14:30': 29, '15:00': 30, '15:30': 31, '16:00': 32, '16:30': 33, '17:00': 34, '17:30': 35, '18:00': 36, '18:30': 37, '19:00': 38, '19:30': 39, '20:00': 40, '20:30': 41, '21:00': 42, '21:30': 43, '22:00': 44, '22:30': 45, '23:00': 46,  '23:30': 47, '24:00': 48, '24:30': 49,})
        tomorrow_str = self.get_tommorow_str()
        time_parameter = time_parameter_dict[self.reserve_time_list[0]]
        search_url = self.domain + '/reservation/{}/#time1={}&time2={}&searchWordTarget=1'.format(tomorrow_str, time_parameter, time_parameter)
        self.driver.get(search_url)
        print(search_url)
        logging.info('Successfully visited', search_url)
        time.sleep(2)
        reservation_url = self.driver.find_element_by_partial_link_text(self.reserve_time_list[0]).get_attribute("href")
        self.make_reservation(reservation_url)


    def get_best_url(self):
        for time in self.reserve_time_list:
            links = self.reservation_link_dict[time]
            if len(links):
                return links[0], True
        return '', False

    def make_reserve_time_dict(self):
        reserve_dict = dict()
        for time_str in self.reserve_time_list:
            reserve_dict[time_str] = []
        return reserve_dict

    def get_tommorow_str(self):
        tomorrow = datetime.now(timezone('Asia/Tokyo')) + timedelta(days=1)
        tomorrow_str = tomorrow.strftime('%Y/%m/%d')
        return tomorrow_str

    def check_terminate(self):
        try:
            self.driver.find_element_by_id('seleneSearchResult')
            return False
        except:
            return True

    def make_reservation(self, reservation_url):
        self.driver.get(reservation_url)
        time.sleep(2)
        try:
            # self.driver.find_element_by_css_selector('input[value="予約する"]').click()
            print('Made reservation')
        except:
            print("Couldn't find reservation button")

    def quit(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    CHROME_PATH = config('chrome_path')
    reserve_time_list = ["7:30", "8:00"]
    rarejob = RarejobBooker(CHROME_PATH, reserve_time_list)
    rarejob.login()
    time.sleep(3)
    # rarejob.reserve_from_bookmark()
    time.sleep(3)
    rarejob.reserve_from_available()
    time.sleep(3)
    rarejob.quit()






