from playwright.sync_api import Page


def load_page(page: Page):
    """Инициализация страницы с кнопкой."""
    page.set_content('<button class="submit-btn">Submit</button>')


def trigger_dom_rebuild(page: Page):
    """Эмуляция перерисовки DOM (например, после ответа от бэкенда в React/Vue)."""
    page.evaluate("document.querySelector('.submit-btn').outerHTML = '<button class=\"submit-btn\">Submit</button>'")


def test_submit_form_with_element_handle(page: Page):
    load_page(page)
    
    submit_btn = page.query_selector(".submit-btn")
    trigger_dom_rebuild(page)
    submit_btn.click()


def test_submit_form_with_locator(page: Page):
    load_page(page)
    
    submit_btn = page.locator(".submit-btn")
    trigger_dom_rebuild(page)
    submit_btn.click()
