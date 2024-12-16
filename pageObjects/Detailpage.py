from selenium.webdriver.common.by import By

class DetailPage:

    ReadMore_Xpath = '//*[@id="overviewSection"]/div/div[2]/div[1]/p/a'
    CloseReadMore = '//*[@id="overviewSection"]/div/div[2]/div[1]/div[3]/div[1]/span'
    Amenities_Xpath = '//*[@id="overviewSection"]/div/div[2]/div[1]/div[1]/ul/li[4]/a'
    CloseAmenities_Xpath = '//*[@id="overviewSection"]/div/div[2]/div[1]/div[1]/span/div/div[1]/span'
    MoreOptions_Xpath = '//*[@id="overviewSection"]/div/div[2]/div[2]/div/span/div/div/div[3]/button'
    MoreDetails_Xpath = '//*[@id="room0"]/div[2]/div/div[1]/div/div/p'
    CloseMoreDetails_Xpath = '//*[@id="roomSection"]/div/span/div/div[1]/span'
    SelectPackage_Xpath = '//*[@data-testid="-483838241895818751-selectRoom"]'

    def __init__(self, driver):
        self.driver = driver

    def ClickReadMore(self):
        self.driver.find_element(By.XPATH, self.ReadMore_Xpath).click()

    def ClickCloseReadMore(self):
        self.driver.find_element(By.XPATH,self.CloseReadMore).click()

    def ClickAmenities(self):
        self.driver.find_element(By.XPATH, self.Amenities_Xpath).click()

    def ClickCloseAmenities(self):
        self.driver.find_element(By.XPATH, self.CloseAmenities_Xpath).click()

    def ClickMoreOption(self):
        self.driver.find_element(By.XPATH, self.MoreOptions_Xpath).click()

    def ClickMoreDetails(self):
        self.driver.find_element(By.XPATH, self.MoreDetails_Xpath).click()

    def ClickCloseMoreDetail(self):
        self.driver.find_element(By.XPATH, self.CloseMoreDetails_Xpath).click()

    def ClickSelectPackage(self):
        self.driver.find_element(By.XPATH, self.SelectPackage_Xpath).click()
