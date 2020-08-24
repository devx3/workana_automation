class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def collect(self):
        pass
    
    def _is_title_matches(self):
        pass
