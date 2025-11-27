import pytest
from pages.login_page import LoginPage

BASE_URL = "https://example.com"  # replace with your app

def test_user_can_login(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    login.login("alice", "correcthorsebatterystaple")
    assert login.is_logged_in()
