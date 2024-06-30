from pytest import fixture

from tests import PASSWORD, USERNAME


@fixture
def secure_page(login_page):
    return login_page.login(USERNAME, PASSWORD)


class TestSecurePage:

    def test_secure_page(self, secure_page):

        assert secure_page.is_open

    def test_secure_page_banner_text(self, secure_page):

        assert "You logged into a secure area!" in secure_page.banner_text

    def test_secure_page_header_text(self, secure_page):

        assert "Secure Area" in secure_page.header_text

    def test_secure_page_body_text(self, secure_page):

        assert "Welcome to the Secure Area. When you are done click logout below." in secure_page.body_text

    def test_secure_page_logout(self, secure_page):
        login_page = secure_page.logout()

        assert "You logged out of the secure area!" in login_page.banner_text
