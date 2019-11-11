# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://localhost:8069/web/login")
        driver.find_element_by_xpath("//div[@id='wrapwrap']/main/div").click()
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Register'])[1]/following::div[4]").click()
        driver.find_element_by_link_text("Study Course").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Configuration'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("Study Course").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Configuration'])[1]/preceding::a[3]").click()
        # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Become Superuser'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("//*[contains(@class, 'oe_topbar_name')]").click()
        driver.find_element_by_link_text("Log out").click()
        driver.find_element_by_id("login").click()
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("matthias")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("login")
        driver.find_element_by_id("password").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Register'])[1]/following::div[4]").click()
        driver.find_element_by_link_text("Student Data").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Student Exams'])[1]/following::span[1]").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
