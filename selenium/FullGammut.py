# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class FullGammut(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_full_gammut(self):
        driver = self.driver
        driver.get("http://localhost:8069/web/login")
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("matthias")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("login")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::button[1]").click()
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=password | ]]
        driver.find_element_by_id("password").send_keys(Keys.ENTER)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("//a/div").click()
        driver.find_element_by_link_text("Student Data").click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Contacts'])[1]/following::span[1]").click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Discard'])[1]/following::button[1]").click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath("//*[starts-with(@id, 'o_field_input')]").click()
        driver.find_element_by_xpath("//*[contains(text(),'Create and E')]").click()
        data_dic = {
            'last_name' : 'Fleissig',
            'gender' : {'type' : 'select', 'text' : 'Male'},
            'birthdate' : {'type' : 'input', 'text' : "27/8/1988"},
            'matriculation_number' : '12345',
            'ahv_number' : "'999.9999.9999.99'",
            'academic_title' : 'Bürsten-Binder',
            #'' : '',
            #'' : '',
            #'' : '',
        }
        elem = driver.find_element_by_name("name").find_element(By.TAG_NAME, "input")
        elem.clear()
        elem.send_keys("Student")
        for k,v in data_dic.items():
            if isinstance(v, dict):
                v_type = v['type']
                if v_type == 'select':
                    # for the time being just assume select, with slect by visible text
                    elem = Select(driver.find_element_by_name(k))
                    elem.select_by_visible_text(v.get('text', ''))
                elif v_type == 'input':
                    elem = driver.find_element_by_name(k)
                    name = v.get('name', k)
                    value = v.get('text', '')
                    elem = elem.find_elements_by_name(name)
                    if elem:
                        elem = elem[0]
                    elem.clear()
                    elem.send_keys(value)                    
            else:                
                elem = driver.find_element_by_name(k)
                elem.clear()
                elem.send_keys(v)
        driver.find_element_by_id("o_field_input_416").click()
        driver.find_element_by_id("ui-id-25").click()
        driver.find_element_by_id("o_field_input_592").click()
        driver.find_element_by_id("o_field_input_592").clear()
        driver.find_element_by_id("o_field_input_592").send_keys("Schweiz")
        driver.find_element_by_id("o_field_input_593").click()
        driver.find_element_by_id("ui-id-27").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Active'])[4]/following::td[1]").click()
        driver.find_element_by_id("o_field_input_602").click()
        driver.find_element_by_id("o_field_input_602").clear()
        driver.find_element_by_id("o_field_input_602").send_keys("Schweiz")
        driver.find_element_by_id("o_field_input_601").click()
        driver.find_element_by_id("o_field_input_601").clear()
        driver.find_element_by_id("o_field_input_601").send_keys("10")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Name'])[6]/following::span[1]").click()
        driver.find_element_by_id("o_field_input_591").click()
        driver.find_element_by_id("o_field_input_591").clear()
        driver.find_element_by_id("o_field_input_591").send_keys("1")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='BFS Nationality ID'])[1]/following::span[1]").click()
        Select(driver.find_element_by_id("o_field_input_414")).select_by_visible_text("Male")
        driver.find_element_by_id("o_field_input_414").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Gender'])[1]/following::td[2]").click()
        driver.find_element_by_id("o_field_input_415").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Discard'])[3]/following::th[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Discard'])[3]/following::th[1]").click()
        driver.find_element_by_xpath("//th/span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sa'])[1]/following::td[11]").click()
        driver.find_element_by_id("o_field_input_415").click()
        driver.find_element_by_xpath("//th/span").click()
        driver.find_element_by_xpath("(//a[contains(@href, '#')])[132]").click()
        driver.find_element_by_id("o_field_input_419").click()
        driver.find_element_by_id("o_field_input_419").clear()
        driver.find_element_by_id("o_field_input_419").send_keys("999.9999.9999.99")
        driver.find_element_by_id("o_field_input_422").click()
        driver.find_element_by_id("o_field_input_422").clear()
        driver.find_element_by_id("o_field_input_422").send_keys("FussTrampler")
        driver.find_element_by_id("o_field_input_420").click()
        driver.find_element_by_id("ui-id-31").click()
        Select(driver.find_element_by_id("o_field_input_423")).select_by_visible_text("German / Deutsch")
        driver.find_element_by_id("o_field_input_423").click()
        driver.find_element_by_id("o_field_input_421").click()
        driver.find_element_by_id("o_field_input_421").clear()
        driver.find_element_by_id("o_field_input_421").send_keys("KopfKlopfer")
        driver.find_element_by_id("o_field_input_554").click()
        driver.find_element_by_id("o_field_input_585").clear()
        driver.find_element_by_id("o_field_input_585").send_keys("Robert Rottermann")
        driver.find_element_by_id("o_field_input_554").clear()
        driver.find_element_by_id("o_field_input_554").send_keys("Sickingerstr 3")
        driver.find_element_by_id("o_field_input_556").clear()
        driver.find_element_by_id("o_field_input_556").send_keys("3014")
        driver.find_element_by_id("o_field_input_557").clear()
        driver.find_element_by_id("o_field_input_557").send_keys("Bern")
        driver.find_element_by_id("o_field_input_427").clear()
        driver.find_element_by_id("o_field_input_427").send_keys("+41313331020")
        driver.find_element_by_id("o_field_input_554").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=o_field_input_554 | ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Address Type'])[1]/following::tr[1]").click()
        driver.find_element_by_id("o_field_input_427").click()
        driver.find_element_by_id("o_field_input_427").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=o_field_input_427 | ]]
        driver.find_element_by_id("o_field_input_427").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=o_field_input_427 | ]]
        driver.find_element_by_id("o_field_input_427").click()
        driver.find_element_by_id("o_field_input_427").clear()
        driver.find_element_by_id("o_field_input_427").send_keys("+313331020")
        driver.find_element_by_id("o_field_input_432").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='​'])[37]/following::label[1]").click()
        driver.find_element_by_id("o_field_input_556").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=o_field_input_556 | ]]
        driver.find_element_by_id("o_field_input_558").click()
        driver.find_element_by_id("ui-id-45").click()
        driver.find_element_by_id("o_field_input_558").clear()
        driver.find_element_by_id("o_field_input_558").send_keys("Switzerland")
        driver.find_element_by_id("o_field_input_559").click()
        driver.find_element_by_id("ui-id-46").click()
        driver.find_element_by_id("o_field_input_611").click()
        driver.find_element_by_id("o_field_input_611").clear()
        driver.find_element_by_id("o_field_input_611").send_keys("Bern")
        driver.find_element_by_id("o_field_input_612").clear()
        driver.find_element_by_id("o_field_input_612").send_keys("3000")
        driver.find_element_by_id("ui-id-80").click()
        driver.find_element_by_id("o_field_input_613").click()
        driver.find_element_by_id("o_field_input_613").click()
        driver.find_element_by_id("o_field_input_613").click()
        driver.find_element_by_id("o_field_input_613").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=o_field_input_613 | ]]
        driver.find_element_by_id("o_field_input_613").clear()
        driver.find_element_by_id("o_field_input_613").send_keys("swi")
        driver.find_element_by_id("o_field_input_613").clear()
        driver.find_element_by_id("o_field_input_613").send_keys("Switzerland")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create and edit'])[3]/following::span[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create and edit'])[2]/following::span[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create a Country'])[1]/following::button[1]").click()
        driver.find_element_by_id("o_field_input_613").click()
        driver.find_element_by_id("o_field_input_613").clear()
        driver.find_element_by_id("o_field_input_613").send_keys("Switzerland")
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create and edit'])[1]/following::span[1]").click()
        driver.find_element_by_id("o_field_input_613").click()
        driver.find_element_by_id("o_field_input_613").clear()
        driver.find_element_by_id("o_field_input_613").send_keys("Switzerland")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='×'])[2]/following::div[5]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Country'])[1]/following::span[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Matthias'])[1]/following::span[2]").click()
        driver.find_element_by_id("o_field_input_257").click()
        driver.find_element_by_id("ui-id-203").click()
        driver.find_element_by_id("o_field_input_630").click()
        driver.find_element_by_id("o_field_input_630").clear()
        driver.find_element_by_id("o_field_input_630").send_keys("ss20")
        driver.find_element_by_id("o_field_input_629").click()
        driver.find_element_by_id("o_field_input_629").clear()
        driver.find_element_by_id("o_field_input_629").send_keys("Sommer Semester 2020")
        Select(driver.find_element_by_id("o_field_input_631")).select_by_visible_text("Summer")
        driver.find_element_by_id("o_field_input_631").click()
        driver.find_element_by_id("o_field_input_632").click()
        driver.find_element_by_id("o_field_input_632").clear()
        driver.find_element_by_id("o_field_input_632").send_keys("2020")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Study Course'])[8]/following::button[1]").click()
        driver.find_element_by_id("o_field_input_259").click()
        driver.find_element_by_id("ui-id-205").click()
        driver.find_element_by_id("o_field_input_650").click()
        driver.find_element_by_id("o_field_input_650").clear()
        driver.find_element_by_id("o_field_input_650").send_keys("SS22")
        driver.find_element_by_id("o_field_input_649").click()
        driver.find_element_by_id("o_field_input_649").clear()
        driver.find_element_by_id("o_field_input_649").send_keys("Sommer Semester 2022")
        driver.find_element_by_id("o_field_input_652").click()
        driver.find_element_by_id("o_field_input_652").clear()
        driver.find_element_by_id("o_field_input_652").send_keys("2022")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Study Course'])[8]/following::button[1]").click()
        Select(driver.find_element_by_id("o_field_input_651")).select_by_visible_text("Summer")
        driver.find_element_by_id("o_field_input_651").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Study Course'])[8]/following::span[1]").click()
        driver.find_element_by_id("o_field_input_256").click()
        driver.find_element_by_id("o_field_input_256").clear()
        driver.find_element_by_id("o_field_input_256").send_keys("20")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create'])[1]/following::button[1]").click()
        driver.find_element_by_id("o_field_input_260").click()
        driver.find_element_by_id("ui-id-206").click()
        driver.find_element_by_id("o_field_input_666").clear()
        driver.find_element_by_id("o_field_input_666").send_keys("Leberschaden")
        driver.find_element_by_id("o_field_input_668").click()
        driver.find_element_by_id("o_field_input_668").clear()
        driver.find_element_by_id("o_field_input_668").send_keys("Der Leberschaden schadet der Leber")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='reason exmatriculation'])[1]/following::label[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Immatriculation Date'])[2]/following::span[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Action'])[1]/following::span[5]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Print'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='False'])[1]/following::div[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Student Semester'])[2]/following::a[1]").click()
        driver.find_element_by_link_text("Permission").click()
        driver.find_element_by_link_text("Works").click()
        driver.find_element_by_link_text("Resources").click()
        driver.find_element_by_link_text("Remarks").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='False'])[1]/following::button[1]").click()
        driver.find_element_by_link_text("PUD").click()
        driver.find_element_by_link_text("PUF").click()
        driver.find_element_by_link_text("General Study Remarks").click()
        driver.find_element_by_link_text("Earlier Immatriculations").click()
        driver.find_element_by_link_text("Study dates").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create'])[1]/following::button[1]").click()
    
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
