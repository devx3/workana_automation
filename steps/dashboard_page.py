from selenium.webdriver.common.keys import Keys
from persisters.config import Config
from common.locators import DashboardPageLocators
from common.utils import get_remaining_proposes_per_day
from steps.base_page import BasePage
import json
import os


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.name = None
        self.total_ammount = None
        self.total_connections = 0
        self.connections_available = 0

    def collect(self):
        self._get_name()
        self._get_total_ammount()
        self._get_connections()

    def _is_title_matches(self):
        ''' Check if is dashboard page '''
        return 'dashboard-component' in self.driver.page_source

    def _get_name(self):
        ''' Get freelancer name '''
        try:
            name = self.driver.find_element(*DashboardPageLocators.FREELA_NAME)
            self.name = name.text.split(' ')[0]
        except Exception:
            pass

    def _get_total_ammount(self):
        ''' Get freelancer name '''
        try:
            total_ammount = self.driver.find_element(*DashboardPageLocators.TOTAL_AMOUNT)
            total_ammount = total_ammount.text
            total_ammount = total_ammount.replace('R$ ', '')
            total_ammount = total_ammount.replace(',', '.')
            self.total_ammount = float(total_ammount)
        except Exception:
            pass

    def _welcome_message(self):
        ''' Send welcome message '''
        return f'Bem vindo(a) {self.name} - Seu saldo atual é de: {self.total_ammount}'

    def _get_connections(self):
        self.__get_connections_available()
        self.__get_total_connections()

    def __get_total_connections(self):
        ''' Get total connections '''
        try:
            total_connections = self.driver.find_element(*DashboardPageLocators.TOTAL_CONNECTIONS)
            self.total_connections = int(total_connections.text)
        except Exception:
            pass

    def __get_connections_available(self):
        ''' Get connections available '''
        try:
            connections_available = self.driver.find_element(
                *DashboardPageLocators.CONNECTIONS_AVAILABLE
            )
            self.connections_available = int(connections_available.text)
        except Exception:
            pass

    def _number_of_proposes_to_use(self, current_proposes: int):
        ''' Calculate how much proposes can you send today '''
        return get_remaining_proposes_per_day(current_proposes)

    def get_num_proposes(self):
        return self._number_of_proposes_to_use(self.connections_available)

    def save_connections_info(self):
        ''' Save total connections and connections available '''
        config = Config()
        config.up()
        try:
            config.update('connections.total', str(self.total_connections))
            config.update('connections.current', str(self.connections_available))
            return True
        except Exception:
            return False
