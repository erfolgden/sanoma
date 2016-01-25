# # -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# from selenium.webdriver.support import expected_conditions as EC
# import unittest, time, re
#
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# class Untitled2(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "www.sanoma.nl/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
#         self.driver.maximize_window()
#
#     def test_untitled2(self):
#         driver = self.driver
#         driver.get("http://www.sanoma.nl/")
#         self.assertEqual("Sanoma - Home", driver.title)
#         driver.find_element_by_id("nav-main-contact").click()
#         self.assertEqual("Sanoma", driver.title)
#         self.assertEqual("ik wil even reageren", driver.find_element_by_css_selector("span.btn").text)
#         driver.switch_to.active_element
#
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='contact-form']/fieldset[10]/div/div/input")))
#         driver.find_element_by_xpath("//*[@id='contact-form']/fieldset[10]/div/div/input").click()
#         self.assertTrue(
#             self.is_element_present(By.XPATH, "//label[@id='id_reason' and contains(.,'Dit veld is verplicht')]"))
#
#     def is_element_present(self, how, what):
#         try:
#             self.driver.find_element(by=how, value=what)
#         except NoSuchElementException as e:
#             return False
#         return True
#
#     def is_alert_present(self):
#         try:
#             self.driver.switch_to_alert()
#         except NoAlertPresentException as e:
#             return False
#         return True
#
#     def close_alert_and_get_its_text(self):
#         try:
#             alert = self.driver.switch_to_alert()
#             alert_text = alert.text
#             if self.accept_next_alert:
#                 alert.accept()
#             else:
#                 alert.dismiss()
#             return alert_text
#         finally:
#             self.accept_next_alert = True
#
#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)
#
#
# if __name__ == "__main__":
#     unittest.main()
