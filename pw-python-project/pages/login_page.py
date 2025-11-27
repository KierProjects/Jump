from playwright.sync_api import Page 

class LoginPage:
    def __init__(self, page: Page):
        self._page = page
        # keep locators here
        self._username = page.get_by_label("Username")
        self._password = page.get_by_label("Password")
        self._submit = page.get_by_role("button", name="Sign in")

    def goto(self, base_url: str):
        self._page.goto(f"{base_url}/login")

    def login(self, username: str, password: str):
        self._username.fill(username)
        self._password.fill(password)
        self._submit.click()

    def is_logged_in(self) -> bool:
        # return boolean state for assertions in tests
        return self._page.get_by_role("menuitem", name="Profile").is_visible()
