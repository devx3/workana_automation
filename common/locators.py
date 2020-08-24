from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[@type = "submit"]')
    ALERT_ERROR = (By.XPATH, '//div[contains(@class, "alert-error")]')


class DashboardPageLocators(object):
    FREELA_NAME = (
        By.XPATH, '//*[contains(@class, "user-info")]/*[contains(@class, "h4 user-name")]/span'
    )
    TOTAL_AMOUNT = (
        By.XPATH, '//p[contains(text(), "Saldo")]/preceding-sibling::h4'
    )
    CONNECTIONS_AVAILABLE = (
        By.XPATH, '//span[contains(text(), "Conexões sem")]/following-sibling::span/strong'
    )
    TOTAL_CONNECTIONS = (
        By.XPATH, '//span[contains(text(), "Conexões sem")]/following-sibling::span/span[2]'
    )


class ProjectsPageLocators(object):
    pass
