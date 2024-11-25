
from selenium.webdriver.common.by import By

class ListingPage:
    SearchSection_Xpath = '//*[@id="hsw_search_button"]'
    SearchLocation_Xpath = '//*[@id="_Hlisting_area"]/div[2]/div/div[2]/div/div/input'
    EnterLocation_Xpath = '//*[@id="_Hlisting_area"]/div[2]/div/div[2]/div/div/input'
    SelectLocation_Xpath = '//*[@id="react-autowhatever-1--item-0"]/a/p'
    HotelName_Xpath = '//*[@id="htl_id_seo_201003191729135374"]'

    def __init__(self, driver):
        self.driver = driver

    def ClickSearch(self):
        self.driver.find_element(By.XPATH, self.SearchSection_Xpath).click()

    def ClickLocation(self):
        self.driver.find_element(By.XPATH, self.SearchLocation_Xpath).click()

    def ClickEnterLocation(self,EnterLocation):
        self.driver.find_element(By.XPATH, self.EnterLocation_Xpath).send_keys(EnterLocation)

    def ClickSelectLocation(self):
        self.driver.find_element(By.XPATH, self.SelectLocation_Xpath).click()

    def ClickHotelName(self):
        self.driver.find_element(By.XPATH, self.HotelName_Xpath).click()
