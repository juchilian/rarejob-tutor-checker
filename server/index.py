from datetime import datetime, timedelta
from os import error
from decouple import config
from pytz import timezone
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class RarejobBooker:
    def __init__(self, chrome_path, reserve_time_list) -> None:
        self.domain = 'https://www.rarejob.com'
        self.driver = webdriver.Chrome(chrome_path)
        self.driver.implicitly_wait(3)
        self.reserve_time_list = reserve_time_list


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
        # reservation_link_dict = dict()
        # MAX bookmark tutor 100 & tutor numbers per page 15 = 6.7777
        MAX_BOOKMARK_PAGE = 7
        user_max_bookmark_page = MAX_BOOKMARK_PAGE
        tomorrow = datetime.now(timezone('Asia/Tokyo')) + timedelta(days=1)
        tomorrow_str = tomorrow.strftime('%Y/%m/%d')
        # Find all 7:30 button 
        for time_str in self.reserve_time_list:
            for page_num in range(1, user_max_bookmark_page+1):
                page_url = self.domain + '/reservation/bookmark/{}/#page={}'.format(tomorrow_str, page_num)
                self.driver.get(page_url)
                print(page_url)
                time.sleep(1)
                try:
                    self.driver.find_element_by_id('seleneSearchResult')
                except:
                    user_max_bookmark_page = page_num - 1
                    print('現在ブックマークされている講師はいません')
                    break
                time.sleep(2)
                try:
                    reserve_time_link = self.driver.find_element_by_link_text(time_str)
                    print(reserve_time_link)
                    link = reserve_time_link.get_attribute("href")
                    self.driver.get(link)
                    time.sleep(3)
                    self.make_reservation()
                    break
                except:
                    print("time link not found")
                    pass


    def make_reservation(self):
        try:
            # self.driver.find_element_by_css_selector('input[value="予約する"]').click()
            # self.driver.find_element_by_name('yt0').click()
            print('Made reservation')
        except:
            print("Couldn't find reservation button")

    def quit(self):
        self.driver.close()
        self.driver.quit()


# If Yes => click first one => break
# If No => Click '次へ' => If no '次へ' Click '予約可能講師(https://www.rarejob.com/reservation/2021/8/15/#time1=15&time2=15&minAge=20&maxAge=29&searchWordTarget=1&searchWord=TESOL)'


if __name__ == '__main__':
    CHROME_PATH = config('chrome_path')
    reserve_time_list = ["7:30", "8:00", "20:00"]
    rarejob = RarejobBooker(CHROME_PATH, reserve_time_list)
    rarejob.login()
    time.sleep(3)
    rarejob.reserve_from_bookmark()
    time.sleep(3)
    rarejob.quit()






