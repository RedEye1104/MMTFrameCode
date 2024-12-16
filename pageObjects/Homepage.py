from selenium.webdriver.common.by import By


class Homepage():
    LoginSection_Xpath = '//*[@id="SW"]/div[1]/div[2]/div[2]/div/section/span'
    SearchSection_Xpath = '//*[@id="city"]'
    EnterCityName_Xpath = '//*[@id="top-banner"]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/input'
    SelectCity_Xpath = '//*[@id="react-autowhatever-1-section-0-item-3"]/div/div[2]/div[2]/p'
    SelectCheckIN_Xpath = '//*[@id="top-banner"]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[5]/div[4]'
    SelectCheckOut_Xpath = '//*[@id="top-banner"]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[5]/div[6]'
    SelectRoom_Xpath = '//*[@id="top-banner"]/div[2]/div/div[1]/div[2]/div/div[1]/div[4]/div[1]/div[2]/button'
    SelectSearch_Xpath = '//*[@id="hsw_search_button"]'

    def __init__(self, driver):
        self.driver = driver

    def ClickLoginSection(self):
        self.driver.find_element(By.XPATH, self.LoginSection_Xpath).click()

    def ClickSearchSection(self):
        self.driver.find_element(By.XPATH, self.SearchSection_Xpath).click()

    def ClickEnterCityName(self, GetLocation):
        self.driver.find_element(By.XPATH, self.EnterCityName_Xpath).send_keys(GetLocation)

    def ClickSelectCity(self):
        self.driver.find_element(By.XPATH, self.SelectCity_Xpath).click()

    def ClickCheckIn(self):
        self.driver.find_element(By.XPATH, self.SelectCheckIN_Xpath).click()

    def ClickCheckOut(self):
        self.driver.find_element(By.XPATH, self.SelectCheckOut_Xpath).click()

    def ClickRoom(self):
        self.driver.find_element(By.XPATH, self.SelectRoom_Xpath).click()

    def ClickSearch(self):
        self.driver.find_element(By.XPATH, self.SelectSearch_Xpath).click()
