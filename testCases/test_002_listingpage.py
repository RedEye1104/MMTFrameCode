import time

from utilities.customLogger import Log_maker
from pageObjects.Listingpage import ListingPage


class TestListing:
    baseURL = 'https://www.makemytrip.com/hotels/hotel-listing/?_uCurrency=INR&checkin=01292025&checkout=01312025&city=CTDEL&country=IN&locusId=CTDEL&locusType=city&reference=hotel&roomStayQualifier=2e0e&rsc=1e2e0e&searchText=Delhi&type=city'
    logger = Log_maker.log_gen()

    def test_listingPage(self, Setup):
        self.logger.info("Test Started for the listingPage.")
        self.driver = Setup
        self.logger.info(f"Opening the URL: {self.baseURL}")
        self.driver.get(self.baseURL)

        self.driver.maximize_window()
        self.logger.info("Maximized the browser window.")

        self.driver.implicitly_wait(20)
        self.logger.info("Set an implicit wait of 20 seconds.")
        self.lp = ListingPage(self.driver)

        self.logger.info("Clicking on the Search Section.")
        self.lp.ClickSearch()

        self.logger.info("Clicking on the Location Section.")
        self.lp.ClickLocation()

        self.logger.info("Entering the Saket Location.")
        self.lp.ClickEnterLocation("Saket")

        self.logger.info("Entering some extra time so that it can locate the element.")
        time.sleep(5)

        self.logger.info("Clicking on the Selected Location")
        self.lp.ClickSelectLocation()

        self.logger.info("Clicking on the Selected Hotel.")
        self.lp.ClickHotelName()
