import re
from playwright.sync_api import sync_playwright

def test_click_myaccount():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=150)
        page = browser.new_page()

        page.goto("https://www.asos.com/", wait_until="domcontentloaded")

        # Accept cookies if exists
        try:
            page.get_by_role("button", name=re.compile("Accept", re.I)).click(timeout=1000)
        except:
            pass

        # Click My Account icon
        page.get_by_role("button", name="My Account").click()

        page.wait_for_timeout(1000)

        # Click Sign In
        page.get_by_role("link", name=re.compile("Sign In", re.I)).click()

        page.wait_for_timeout(1000)

        # Close the browser
        browser.close()