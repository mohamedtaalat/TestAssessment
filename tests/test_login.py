import json
import logging
import time

import pytest

from pages.header import Header
from pages.login_page import LoginPage


@pytest.mark.usefixtures("driver")
class TestLogin:
    with open("data/login_data.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    def test_login(self,driver,data):
        hdp = Header(driver)
        hdp.click_login()
        lgp = LoginPage(driver)
        lgp.login(data["email"], data["password"])
        time.sleep(2)
        print()
        print(data["Scenario"])
        print(f"Expected : {data['expected']}")
        if data["expected"] == "Login" :
            assert driver.current_url != "https://asciisd-software-testing.on-forge.com/login"
        elif data["expected"] == "Not Login" :
            assert driver.current_url == "https://asciisd-software-testing.on-forge.com/login"