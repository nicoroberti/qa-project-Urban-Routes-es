import time
from faulthandler import is_enabled
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import UrbanRoutesPage_Methods
from UrbanRoutesPage_Methods import UrbanRoutePage_LM
from data import phone_number


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service

        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.UrbanRoutesPage_Methods = UrbanRoutePage_LM(cls.driver)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        route_page = UrbanRoutePage_LM(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        route_page.set_route(address_from, address_to)
        assert route_page.get_from() == address_from
        assert route_page.get_to() == address_to

    def test_click_order_taxi_button(self):
        self.driver.get(data.urban_routes_url)
        route_page = UrbanRoutePage_LM(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        assert route_page.order_taxi_button_enabled()
        self.driver.find_element(*self.UrbanRoutesPage_Methods.order_taxi_button).click()

    def test_select_comfort_tariff(self):
        self.driver.get(data.urban_routes_url)
        route_page = UrbanRoutePage_LM(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.click_order_taxi_button()
        is_selected = route_page.select_comfort_tariff_enabled()
        assert is_selected == True

    def test_enter_phone_number(self):
        self.driver.get(data.urban_routes_url)
        route_page = UrbanRoutePage_LM(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.click_order_taxi_button()
        phone_number = data.phone_number
        route_page.enter_phone_number(phone_number)
        assert route_page.get_phone_number() == phone_number

    def test_set_phone_number(self):
        self.driver.get(data.urban_routes_url)
        route_page = UrbanRoutePage_LM(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.click_order_taxi_button()
        phone_number = data.phone_number
        route_page.set_phone_number(phone_number)
        assert route_page.get_phone_number() == phone_number

    def test_set_payment_method(self):
        self.driver.get(data.urban_routes_url)
        route_page = UrbanRoutePage_LM(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.click_order_taxi_button()
        route_page.set_payment_method(data.card_number, data.card_code)
        added_card = self.driver.find_element(*route_page.added_card)
        assert "Tarjeta" in added_card.text

    def test_send_message_to_driver(self):
        self.driver.get(data.urban_routes_url)
        route_page = UrbanRoutePage_LM(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.click_order_taxi_button()
        route_page.send_message_to_driver(data.message_to_driver)
        assert route_page.get_message_to_driver() == data.message_to_driver

    def test_order_blanket_and_kerchief(self):
        self.driver.get(data.urban_routes_url)
        route_page = UrbanRoutePage_LM(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.click_order_taxi_button()
        route_page.select_comfort_tariff_enabled()
        route_page.order_blanket_and_kerchief()
        blanket_kerchief_button = self.driver.find_element(By.CLASS_NAME, 'switch-input')
        assert blanket_kerchief_button.is_selected()

    def test_order_2_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        route_page = UrbanRoutePage_LM(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.click_order_taxi_button()
        route_page.order_2_ice_cream()
        ice_cream_counter = route_page.ice_creams_counter()
        assert ice_cream_counter == 2

    def test_car_search_modal_appear(self):
        self.driver.get(data.urban_routes_url)
        route_page = UrbanRoutePage_LM(self.driver)
        route_page.car_search_modal_appear()
        assert self.driver.find_element(*self.UrbanRoutesPage_Methods.order_taxi_details).is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
