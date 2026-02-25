from playwright.sync_api import Page


def load_checkout_page(page: Page):
    """Инициализация страницы с формой оплаты."""
    page.set_content('''
        <div id="app">
            <main>
                <form class="checkout-form">
                    <div class="input-group">
                        <label for="card">Credit Card</label>
                        <input id="card" type="text" class="input-field rnd-8932" />
                    </div>
                    <button type="submit" class="btn btn-primary mt-4" data-testid="submit-order">
                        Pay Now
                    </button>
                </form>
            </main>
        </div>
    ''')


def test_checkout_approach_a(page: Page):
    load_checkout_page(page)
    
    page.locator('//html/body/div/main/form/div/input').fill("1234 5678 9101 1121")
    page.locator('.btn-primary.mt-4').click()


def test_checkout_approach_b(page: Page):
    load_checkout_page(page)
    
    page.locator('#card').fill("1234 5678 9101 1121")
    page.locator('button[type="submit"]').click()


def test_checkout_approach_c(page: Page):
    load_checkout_page(page)
    
    page.get_by_label("Credit Card").fill("1234 5678 9101 1121")
    page.get_by_role("button", name="Pay Now").click()
