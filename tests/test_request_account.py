import json
import time

import pytest

from pages.admin_only_pages.account_requests_page import AccountRequestsPage
from pages.common_pages.trading_accounts_page import TradingAccountsPage, RequestAccountForm
from pages.header import Header
from pages.login_page import LoginPage
from pages.sidebar import SideBar


@pytest.mark.usefixtures("driver")
class TestRequestAccount:
    with open("data/request_account_data.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    def test_request_account(self,driver,data):
        hpd = Header(driver)
        hpd.click_login()
        lgp = LoginPage(driver)
        lgp.login("test@example.com","password")
        sdp = SideBar(driver)
        sdp.click_trading_account()
        trdp = TradingAccountsPage(driver)
        trdp.click_request_account()
        rqp = RequestAccountForm(driver)
        rqp.create_account_request(data["account_type"],data["base_currency"],data["leverage"],data["trading_purpose"])
        print()
        print(data["Scenario"])
        print(data["expected"])
        time.sleep(2)
        assert driver.current_url != "https://asciisd-software-testing.on-forge.com/accounts/create"

    def test_scenario_create_account_request_and_approve_from_admin(self,driver):
        hpd = Header(driver)
        hpd.click_login()
        lgp = LoginPage(driver)
        lgp.login("test@example.com", "password")
        sdp = SideBar(driver)
        sdp.click_trading_account()
        trdp = TradingAccountsPage(driver)
        trdp.click_request_account()
        rqp = RequestAccountForm(driver)
        rqp.create_account_request("demo","USD","1:50","note")
        sdp.click_logout()
        hpd.click_login()
        lgp.login("admin@tradevault.test", "password")
        sdp.click_account_request()
        acrp = AccountRequestsPage(driver)
        acrp.click_approve(1)
        time.sleep(2)

    def test_scenario_create_account_request_and_reject_from_admin(self, driver):
        hpd = Header(driver)
        hpd.click_login()
        lgp = LoginPage(driver)
        lgp.login("test@example.com", "password")
        sdp = SideBar(driver)
        sdp.click_trading_account()
        trdp = TradingAccountsPage(driver)
        trdp.click_request_account()
        rqp = RequestAccountForm(driver)
        rqp.create_account_request("demo", "USD", "1:50", "note")
        sdp.click_logout()
        hpd.click_login()
        lgp.login("admin@tradevault.test", "password")
        sdp.click_account_request()
        acrp = AccountRequestsPage(driver)
        acrp.reject(1,2,"hello i am mohamed i think this is reason")
        time.sleep(2)

