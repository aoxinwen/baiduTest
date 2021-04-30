# coding = utf-8

"""
# @Time : 2021/4/7 20:07 
# @Author : Axw
# @File : test_HomePage.py
# @Software: PyCharm
"""
import pytest
import sys
from selenium.webdriver.common.by import By
sys.path.append("..")
from common.pages import locate_elements_way, homepage


class Test_Home_page(locate_elements_way.Locate_elements, homepage.Homepage):
    def setup_class(self):
        self.get_url(self, self.link)

    def teardown_class(self):
        self.close_driver(self)

    def test_Click_news(self):
        if self.is_existence_element(By.LINK_TEXT, self.news_href):
            self.find_by_link(self.news_href).click()
            handles = self.driver.window_handles
            self.driver.switch_to_window(handles[-1])
            assert self.is_existence_element(By.PARTIAL_LINK_TEXT, '音乐')
            self.driver.close()
            self.driver.switch_to_window(handles[0])
        else:
            assert False

    def test_search(self):
        if self.is_existence_element(By.ID, self.input_id):
            self.find_by_id(self.input_id).send_keys("python")
            self.find_by_id(self.bauduSearch_btn_id).click()
            assert self.is_existence_element(By.PARTIAL_LINK_TEXT, 'python')
        else:
            assert False


if __name__ == "__main__":
    pytest.main(["-s", "test_HomePage.py::Test_Home_page"])
