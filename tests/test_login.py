import json

import pytest


@pytest.mark.usefixtures("driver")
class TestLogin:
    with open("data/super_admin/articles/happy_scenarios.json") as f:
        data = json.load(f)
    @pytest.mark.parametrize("data", data)
    def test_login(self,driver,data):
        pass