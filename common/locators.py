from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[@type = "submit"]')
    ALERT_ERROR = (By.XPATH, '//div[contains(@class, "alert-error")]')


class DashboardPageLocators(object):
    pass


class ProjectsPageLocators(object):
    pass
