import time
from utilities.customLogger import Log_maker
from pageObjects.Detailpage import DetailPage

class TestDetail:
    baseURL = 'https://www.makemytrip.com/hotels/hotel-details/?hotelId=200701211455342954&_uCurrency=INR&checkin=01292025&checkout=01312025&city=CTDEL&country=IN&lat=28.63166&lng=77.22723&locusId=CTDEL&locusType=city&rank=1&regionNearByExp=3&roomStayQualifier=2e0e&rsc=1e2e0e&searchText=Delhi&viewType=PREMIUM&mtkeys=-8714995777564938516'
    logger = Log_maker.log_gen()

    def test_DetailPage(self, Setup):
        self.logger.info("Test started for the DetailPage.")
        self.driver = Setup

        # Open the URL
        self.logger.info(f"Opening the URL: {self.baseURL}")
        self.driver.get(self.baseURL)
        self.logger.info("Maximizing the browser window.")
        self.driver.maximize_window()

        # Implicit wait
        self.logger.info("Setting an implicit wait of 20 seconds.")
        self.driver.implicitly_wait(20)

        # Interacting with DetailPage
        self.dp = DetailPage(self.driver)

        self.logger.info("Clicking on the Read More button.")
        self.dp.ClickReadMore()

        self.logger.info("Clicking on the Close Read More button.")
        self.dp.ClickCloseReadMore()

        self.logger.info("Clicking on the Amenities button.")
        self.dp.ClickAmenities()

        self.logger.info("Clicking on the Close Amenities button.")
        self.dp.ClickCloseAmenities()

        self.logger.info("Clicking on the More Option button.")
        self.dp.ClickMoreOption()

        self.logger.info("Clicking on the Close More Option button.")
        self.dp.ClickMoreDetails()

        self.logger.info("Clicking on the Close More Details button.")
        self.dp.ClickCloseMoreDetail()

        self.logger.info("Clicking on the Select Package button.")
        self.dp.ClickSelectPackage()

        # Adding a delay for observation.
        time.sleep(5)

        self.logger.info("Test for the DetailPage completed successfully.")
