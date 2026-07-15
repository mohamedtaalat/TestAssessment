from selenium.webdriver.common.by import By

from base.basis import Base


class AccountRequestsPage(Base):
    def __init__(self,driver):
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

    def enter_reason_of_reject(self,n,reason):
        element = self.wait_until_element_be_presence(
            By.XPATH,
            f"/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[2]/div[{n}]/div[2]/div[3]/form[2]/div[1]/input[1]"
        )
        self.scroll_to_element(element)
        element.send_keys(reason)

    def reject(self,number,n,reason):
        self.enter_reason_of_reject(n,reason)
        self.click_reject(number)