import json
import time
import pytest
from pages.admin_only_pages.approve_deposit_page import ApproveDepositPage
from pages.admin_only_pages.approve_withdrawals_page import ApproveWithdrawalsPage
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

    def test_scenario_deposit_and_approve_from_admin(self,driver):
        hpd = Header(driver)
        hpd.click_login()
        lgp = LoginPage(driver)
        lgp.login("test@example.com", "password")
        sdp = SideBar(driver)
        sdp.click_wallet()
        wp = WalletPage(driver)
        wp.create_deposit(100,"Card")
        sdp.click_logout()
        hpd.click_login()
        lgp.login("admin@tradevault.test","password")
        sdp.click_approve_deposit()
        apdp = ApproveDepositPage(driver)
        apdp.click_approve(1)
        time.sleep(2)

    def test_scenario_withdraw_and_approve_from_admin(self,driver):
        hpd = Header(driver)
        hpd.click_login()
        lgp = LoginPage(driver)
        lgp.login("test@example.com", "password")
        sdp = SideBar(driver)
        sdp.click_wallet()
        wp = WalletPage(driver)
        wp.create_withdraw(100,"Card")
        sdp.click_logout()
        hpd.click_login()
        lgp.login("admin@tradevault.test","password")
        sdp.click_approve_withdraw()
        wdp = ApproveWithdrawalsPage(driver)
        wdp.click_approve(1)
        time.sleep(2)

    def test_scenario_withdraw_and_reject_from_admin(self,driver):
        hpd = Header(driver)
        hpd.click_login()
        lgp = LoginPage(driver)
        lgp.login("test@example.com", "password")
        sdp = SideBar(driver)
        sdp.click_wallet()
        wp = WalletPage(driver)
        wp.create_withdraw(100,"Card")
        sdp.click_logout()
        hpd.click_login()
        lgp.login("admin@tradevault.test","password")
        sdp.click_approve_withdraw()
        wdp = ApproveWithdrawalsPage(driver)
        wdp.click_reject(1)
        time.sleep(2)