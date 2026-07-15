import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.common_pages.wallet_page import WalletPage
from pages.header import Header
from pages.login_page import LoginPage
from pages.sidebar import SideBar

@pytest.mark.usefixtures("driver")
class TestWallet:
    with open("data/deposit_data.json") as f:
        data = json.load(f)

    @pytest.mark.parametrize("data", data)
    def test_deposit(self,driver,data):
        hpd = Header(driver)
        hpd.click_login()
        lgp = LoginPage(driver)
        lgp.login("test@example.com", "password")
        sdp = SideBar(driver)
        sdp.click_wallet()
        wp = WalletPage(driver)
        wp.create_deposit(data["deposit_amount"],data["deposit_method"])
        time.sleep(2)
        # toast = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, "//body/div[@id='app']/div[@class='tradevault-theme dark min-h-svh bg-background text-foreground']/div[1]"))
        # )
        print()
        print(data["Scenario"])
        print(data["expected"])
        # if data["expected"] == "Created":
        #     assert toast.text == "Deposit request submitted."
        # elif data["expected"] == "Refused":
        #     assert toast.text != "Deposit request submitted."

    with open("data/withdraw_data.json") as f:
        data = json.load(f)

    @pytest.mark.parametrize("data", data)
    def test_withdraw(self,driver,data):
        hpd = Header(driver)
        hpd.click_login()
        lgp = LoginPage(driver)
        lgp.login("test@example.com", "password")
        sdp = SideBar(driver)
        sdp.click_wallet()
        wp = WalletPage(driver)
        wp.create_withdraw(data["withdraw_amount"],data["withdraw_method"])
        time.sleep(2)
        # toast = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, "//body/div[@id='app']/div[@class='tradevault-theme dark min-h-svh bg-background text-foreground']/div[1]"))
        # )
        print()
        print(data["Scenario"])
        print(data["expected"])
        # if data["expected"] == "Created":
        #     assert toast.text == "Withdraw request submitted."
        # elif data["expected"] == "Refused":
        #     assert toast.text != "Withdraw request submitted."