from playwright.sync_api import Page


def load_complex_page(page: Page):
    html_content = '''<!DOCTYPE html>
<html>
<body>
    <div class="container" data-testid="main">
        <header class="site-header">
            <h1 class="site-title">Dashboard</h1>
            <nav class="sidebar" role="navigation">
                <ul class="menu">
                    <li class="menu-item active" data-role="nav-item">
                        <a href="/home">Home</a>
                    </li>
                    <li class="menu-item" data-role="nav-item">
                        <a href="/settings">Settings</a>
                    </li>
                    <li class="menu-item" data-role="nav-item">
                        <a href="/profile">Profile</a>
                    </li>
                </ul>
            </nav>
        </header>
        <main class="content">
            <section class="panel" id="user-panel">
                <h2 class="panel-heading">User Information</h2>
                <div class="form-group">
                    <label for="username" class="form-label">Username</label>
                    <input id="username" type="text" placeholder="Enter username" class="form-input" />
                </div>
                <div class="form-group">
                    <label for="email" class="form-label">Email</label>
                    <input id="email" type="email" placeholder="Enter email" class="form-input" />
                </div>
                <div class="form-group">
                    <label for="phone" class="form-label">Phone</label>
                    <input id="phone" type="tel" placeholder="Enter phone" class="form-input" />
                </div>
            </section>
            <section class="panel" id="order-panel">
                <h2 class="panel-heading">Recent Orders</h2>
                <table class="orders-table">
                    <thead>
                        <tr>
                            <th>Order ID</th>
                            <th>Status</th>
                            <th>Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="order-row completed" data-status="completed">
                            <td>#1001</td>
                            <td class="status-badge status-completed">Completed</td>
                            <td>$150.00</td>
                        </tr>
                        <tr class="order-row pending" data-status="pending">
                            <td>#1002</td>
                            <td class="status-badge status-pending">Pending</td>
                            <td>$75.50</td>
                        </tr>
                        <tr class="order-row cancelled" data-status="cancelled">
                            <td>#1003</td>
                            <td class="status-badge status-cancelled">Cancelled</td>
                            <td>$200.00</td>
                        </tr>
                    </tbody>
                </table>
            </section>
        </main>
        <footer class="footer">
            <p class="copyright">&copy; 2026 Company</p>
            <a href="https://company.com/privacy" class="footer-link">Privacy Policy</a>
            <a href="https://company.com/terms" class="footer-link">Terms of Service</a>
        </footer>
    </div>
</body>
</html>'''
    page.route("**/*", lambda route: route.fulfill(content_type="text/html", body=html_content))


def test_complex_selectors(page: Page):
    load_complex_page(page)
    page.goto("https://example.com")

    # 1
    page.locator('//li[not(@class="menu-item active")]/a').first.click()
    # 2
    page.locator('.form-input[type="email"]').first.fill("test@example.com")
    # 3
    page.locator('//label[text()="Phone"]').first.click()
    # 4
    page.locator('a[href$="terms"]').first.click()
    # 5
    page.locator('//input[contains(@id, "user")]').first.fill("admin")
    # 6
    page.locator('input[class*="form-input"][type="tel"]').first.fill("+1234567890")
    # 7
    page.locator('//a[starts-with(@href, "https://")]').first.click()
    # 8
    page.locator('.form-group:nth-of-type(3) label').first.click()
    # 9
    page.locator('//label[text()="Phone"]/parent::div/input').first.fill("+1234567890")
    # 10
    page.locator('tr.order-row:nth-child(3) td:nth-child(2)').click()
    # 11
    page.locator('//label[text()="Username"]/following-sibling::input').first.fill("John")
    # 12
    page.locator('td.status-badge.status-pending').first.click()
    # 13
    page.locator('//input[@id="email"]/preceding-sibling::label').first.click()
    # 14
    page.locator('#user-panel .form-label').first.click()
    # 15
    page.locator('//input[@id="phone"]/ancestor::div[@class="form-group"]').first.click()
    # 16
    page.locator('.menu > .menu-item > a').last.click()
    # 17
    page.locator('//li[@data-role="nav-item"][not(@class="menu-item active")]/a').first.click()
    # 18
    page.locator('[data-testid="main"] .panel-heading').first.click()
    # 19
    page.locator('//li[@data-role="nav-item"][not(@class="menu-item active")]/a[contains(@href, "settings")]').first.click()
    # 20
    page.locator('input[type="text"][placeholder="Enter username"]').first.fill("admin")
    # 21
    page.locator('tr[data-status="pending"] td:nth-child(2)').click()
    # 22
    page.locator('a[href*="company"]').first.click()
    # 23
    page.locator('input[placeholder^="Enter"]').nth(1).fill("test@test.com")
    # 24
    page.locator('a[href$="privacy"]').first.click()
    # 25
    page.locator('input[type="text"][class*="form-input"]').first.fill("admin")
    # 26
    page.locator('//div[@class="form-group"]/input[1]').first.fill("Welcome")
    # 27
    page.locator('(//div/input)[1]').first.fill("Hello!")
