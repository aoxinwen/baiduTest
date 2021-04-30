# coding = utf-8

"""
# @Time : 2021/4/8 14:51
# @Author : Axw
# @File : locate_elements_way.py
# @Software: PyCharm
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Locate_elements:
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(executable_path=r'F:\project\baiduTest\driver\chromedriver.exe',chrome_options=option)
    # driver.implicitly_wait(5)  # 隐式等待5s
    timeout = 10  # 显示等待的时间5s

    # 获取url的界面对象
    def get_url(self, URL):
        try:
            self.driver.get(URL)
        except Exception as e:
            print(e)
            print("网页url格式不正确，请使用正确的格式！")

    # 关闭浏览器实例对象
    def close_driver(self):
        self.driver.quit()

    # 通过id定位元素
    def find_by_id(self, ID):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.ID, ID)))

    # 通过name定位元素
    def find_by_name(self, NAME):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.NAME, NAME)))

    # 通过class name定位元素
    def find_by_class(self, CLASS):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.CLASS_NAME, CLASS)))

    # 通过链接text定位元素
    def find_by_link(self, LINK):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.LINK_TEXT, LINK)))

    # 通过链接text模糊定位元素
    def find_by_partial_link(self, Partial_LINK):
        return WebDriverWait(self.driver, self.timeout, 0.5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,
                                                                                                   Partial_LINK)))

    # 通过XPATH定位元素
    def find_by_xpath(self, XPATH):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH, XPATH)))

    # 通用查找方法
    # by: 查找方式
    def find_by(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by, value)))

    # 判断element是否存在
    def is_existence_element(self, by, value):
        try:
            self.find_by(by, value)
            return True
        except NoSuchElementException:
            return False
