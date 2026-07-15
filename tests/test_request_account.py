import json
import time

import pytest

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
