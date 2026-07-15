from selenium.webdriver.common.by import By

from base.basis import Base


class Transactions(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_reference_in_searchbar(self,reference):
        self.wait_until_element_be_presence(
            By.XPATH,
            "//input[@placeholder='Search by reference...']"
        ).send_keys(reference)

    def click_apply(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@class='inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive bg-primary text-primary-foreground hover:bg-primary/90 h-9 px-4 py-2 has-[>svg]:px-3']"
        ).click()

    def select_filter_type(self,filter_type):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@role='combobox']"
        ).click()
        if filter_type == "All types":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[1]"
            ).click()

        elif filter_type == "Deposit":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[2]"
            ).click()

        elif filter_type == "Withdrawal":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[3]"
            ).click()

        elif filter_type == "Transfer":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[4]"
            ).click()

        elif filter_type == "Trade":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[5]"
            ).click()

