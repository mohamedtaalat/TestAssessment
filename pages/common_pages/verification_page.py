from selenium.webdriver.common.by import By

from base.basis import Base


class VerificationPage(Base):
    def __init__(self,driver):
        super().__init__(driver)

    def upload_file(self,file):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//input[@id='document']"
        ).send_keys(file)

    def click_submit_document(self):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

    def select_document_type(self,document_type):
        self.wait_until_element_be_clickable(
            By.XPATH,
            "//button[@role='combobox']"
        ).click()
        if document_type == "Passport":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[1]"
            ).click()

        elif document_type == "National ID":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[2]"
            ).click()

        elif document_type == "Proof of address":
            self.wait_until_element_be_clickable(
                By.XPATH,
                "(//div[@role='option'])[3]"
            ).click()

    def upload_approver_file(self,file,document_type):
        self.upload_file(file)
        self.select_document_type(document_type)
        self.click_submit_document()

