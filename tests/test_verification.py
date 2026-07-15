import json
import time

import pytest

from pages.admin_only_pages.kyc_review_page import KYCReviewPage
from pages.common_pages.verification_page import VerificationPage
from pages.header import Header
from pages.login_page import LoginPage
from pages.sidebar import SideBar


@pytest.mark.usefixtures("driver")
class TestVerification:
    with open("data/verification_data.json") as f:
        data = json.load(f)

    @pytest.mark.parametrize("data", data)
    def test_verification(self,driver,data):
        hpd = Header(driver)
        hpd.click_login()
        lgp = LoginPage(driver)
        lgp.login("test@example.com", "password")
        sdp = SideBar(driver)
        sdp.click_verification()
        vp = VerificationPage(driver)
        vp.upload_approver_file(data["file"],data["document_type"])
        print()
        print(data["Scenario"])
        print(data["expected"])
        time.sleep(2)

    def test_scenario_upload_verification_and_approve_from_admin(self,driver):
        hpd = Header(driver)
        hpd.click_login()
        lgp = LoginPage(driver)
        lgp.login("test@example.com", "password")
        sdp = SideBar(driver)
        sdp.click_verification()
        vp = VerificationPage(driver)
        vp.upload_approver_file("C:\\Users\\admin\\PycharmProjects\\TestAssessment\\asset\\automation.png","Passport")
        sdp.click_logout()
        hpd.click_login()
        lgp.login("admin@tradevault.test", "password")
        sdp.click_review_kyc()
        kyc = KYCReviewPage(driver)
        kyc.click_approve(1)
        time.sleep(2)

    def test_scenario_upload_verification_and_reject_from_admin(self,driver):
        hpd = Header(driver)
        hpd.click_login()
        lgp = LoginPage(driver)
        lgp.login("test@example.com", "password")
        sdp = SideBar(driver)
        sdp.click_verification()
        vp = VerificationPage(driver)
        vp.upload_approver_file("C:\\Users\\admin\\PycharmProjects\\TestAssessment\\asset\\automation.png","Passport")
        sdp.click_logout()
        hpd.click_login()
        lgp.login("admin@tradevault.test", "password")
        sdp.click_review_kyc()
        kyc = KYCReviewPage(driver)
        kyc.click_reject(1)
        time.sleep(2)
