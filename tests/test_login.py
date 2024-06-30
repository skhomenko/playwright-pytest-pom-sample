from tests import PASSWORD, USERNAME


class TestLogin:

    def test_login_page(self, login_page):

        assert login_page.is_open

    def test_login_page_header_text(self, login_page):

        assert "Login Page" in login_page.header_text

    def test_login_page_body_text(self, login_page):

        assert "This is where you can log into the secure area." in login_page.body_text

    def test_login_valid_credentials(self, login_page):
        secure_page = login_page.login(USERNAME, PASSWORD)

        assert secure_page.is_open

    def test_login_invalid_user(self, login_page):
        login_page = login_page.login("invalid-user", PASSWORD)

        assert "Your username is invalid!" in login_page.banner_text

    def test_login_invalid_password(self, login_page):
        login_page = login_page.login(USERNAME, "invalid-password")

        assert "Your password is invalid!" in login_page.banner_text

    def test_loging_invalid_credentials(self, login_page):
        login_page = login_page.login("invalid-user", "invalid-password")

        assert "Your username is invalid!" in login_page.banner_text

    def test_login_empty_credentials(self, login_page):
        login_page = login_page.login("", "")

        assert "Your username is invalid!" in login_page.banner_text
