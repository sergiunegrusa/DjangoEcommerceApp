from re import A

import pytest
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.selenium
def test_dashboard_admin_login(
    live_server, django_db_setup, chrome_browser_instance
):

    # i = User.objects.get(id=1)
    # print(i.username)

    browser = chrome_browser_instance

    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    user_name = browser.find_element(By.NAME, "username")
    user_passwprd = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, '//input[@value="Log in"]')

    user_name.send_keys("admin")
    user_passwprd.send_keys("password")
    submit.send_keys("Keys.RETURN")

    # assert "Site administration" in browser.page_source
