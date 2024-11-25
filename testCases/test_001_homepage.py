import time
from pageObjects.Homepage import Homepage
from utilities.customLogger import Log_maker


class TestRunning:
    baseURL = "https://www.makemytrip.com/hotels/"
    logger = Log_maker.log_gen()
    def test_homepage(self, Setup):
        self.logger.info("Test started for the homepage.")
        self.driver = Setup
        self.logger.info(f"Opening the URL: {self.baseURL}")
        self.driver.get(self.baseURL)

        self.driver.maximize_window()
        self.logger.info("Maximized the browser window.")

        self.driver.implicitly_wait(20)
        self.logger.info("Set an implicit wait of 20 seconds.")

        self.hp = Homepage(self.driver)

        self.logger.info("Clicking on the login section.")
        self.hp.ClickLoginSection()

        time.sleep(5)
        self.logger.info("Waiting for 5 seconds after clicking login section.")

        self.logger.info("Clicking on the search section.")
        self.hp.ClickSearchSection()

        self.logger.info("Entering city name: New Delhi.")
        self.hp.ClickEnterCityName("New delhi")

        self.logger.info("Selecting the entered city.")
        self.hp.ClickSelectCity()

        time.sleep(3)
        self.logger.info("Waiting for 3 seconds after selecting the city.")

        self.logger.info("Clicking on the check-in date.")
        self.hp.ClickCheckIn()

        self.logger.info("Clicking on the check-out date.")
        self.hp.ClickCheckOut()

        self.logger.info("Clicking on the room selection.")
        self.hp.ClickRoom()

        self.logger.info("Clicking on the search button to search for hotels.")
        self.hp.ClickSearch()

        self.logger.info("Test for the homepage completed successfully.")
