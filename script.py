
from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://plato.stanford.edu/entries/socrates/")
    
    content = page.locator('#aueditable').text_content()
    print("the output should be of class string and response should be boolean true")
    print(type(content)==str)
