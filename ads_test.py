import unittest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ProductSearch(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.amazon.com")

    def searchAndListProduct(self):
        search1 = self.driver.find_element_by_id('twotabsearchtextbox')
        search1.clear()
        search1.send_keys("camera")
        search1.send_keys(Keys.RETURN)
        assert search1 is not None
        time.sleep(8)

        n = 0
        products = []
        while n <= 5:
            search2 = self.driver.find_elements_by_xpath("//*/a/h2")
            for s in search2:
                products.append(s.text)
            time.sleep(4)

            search3 = self.driver.find_element_by_id("pagnNextString")
            search3.click()
            time.sleep(4)
            n += 1

        self.createCSV(products)

    def createCSV(self, list):
        df = pd.DataFrame(list, columns=["Products"])
        df.to_csv("products.csv", index=False)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()