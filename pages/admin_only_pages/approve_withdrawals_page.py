from selenium.webdriver.common.by import By

from base.basis import Base


class ApproveWithdrawalsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def click_approve(self,number):
        element = self.wait_until_element_be_clickable(
            By.XPATH,
            f"(//button[@type='submit'][normalize-space()='Approve'])[{number}]"
        )
        self.scroll_to_element(element)
        element.click()

    def click_reject(self,number):
        element = self.wait_until_element_be_clickable(
            By.XPATH,
            f"(//button[@type='submit'][normalize-space()='Reject'])[{number}]"
        )
        self.scroll_to_element(element)
        element.click()