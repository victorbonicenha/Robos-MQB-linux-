from playwright.sync_api import Playwright, sync_playwright
from time import sleep
import os

home = os.path.expanduser("~")
chrome_path = os.path.join(home, ".cache", "ms-playwright", "chromium-1169", "chrome-linux", "chrome")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], executable_path="/home/tvmqb/.cache/ms-playwright/chromium-1169/chrome-linux/chrome")
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://datadriven.datawake.com.br:8057/data-driven/login.html")
    sleep(1)
    page.get_by_role("textbox", name="Email:").fill("tvmqb@datawake.com.br")
    sleep(1)
    page.get_by_role("textbox", name="Senha").fill("Paranoa.12345")
    sleep(1)
    page.get_by_role("button", name="Login").click()
    sleep(5)
    page.locator("header i").click()
    sleep(1)
    page.get_by_role("link", name="DASHBOARD ").click()
    sleep(1)
    page.get_by_role("link", name="MANUFATURA ").click()
    sleep(1)
    page.get_by_role("link", name="OEE Online").click()
    sleep(1)
    page.locator("header i").click()
    sleep(10)
    page.locator("iframe[title=\"OEE Online Dashboard\"]").content_frame.locator(".header-expand-icon").click()
    sleep(10)
    page.locator("iframe[title=\"OEE Online Dashboard\"]").content_frame.locator(".btn-unit").nth(19).click()
    sleep(20)
    page.locator("iframe[title=\"OEE Online Dashboard\"]").content_frame.locator(".indicator__body__title", has_text="META PRODUÇÃO").click()

    sleep(14400)

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
