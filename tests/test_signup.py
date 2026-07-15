import json
import time

import pytest

from pages.header import Header
from pages.signup_page import SignUpPage


@pytest.mark.usefixtures("driver")
class TestSignup:
    with open("data/signup_data.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    def test_signup(self,driver,data):
        hdp = Header(driver)
        hdp.click_open_account()
        sgp = SignUpPage(driver)
        sgp.create_account(data["full_name"],data["email"],data["password"],data["confirm_password"])
        print()
        print(data["Scenario"])
        print(f"Expected : {data['expected']}")
        time.sleep(2)
        if data["expected"] == "Signup":
            assert driver.current_url != "https://asciisd-software-testing.on-forge.com/register"

        elif data["expected"] == "Not Signup":
            assert driver.current_url == "https://asciisd-software-testing.on-forge.com/register"
