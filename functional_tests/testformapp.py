# functional_tests/testformapp.py

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

from formapp.models import Data_User

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestFormApp(StaticLiveServerTestCase):
    
    def setUp(self):
        try:
            self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
        except:
            self.browser = webdriver.Chrome('functional_tests/chromedriver')
        
    def tearDown(self):
        
        self.browser.close()

    def test_user_see_index_page(self):
        
        self.browser.get(self.live_server_url)
        
        self.assertEquals(
            self.browser.find_element(By.TAG_NAME,'h3').text,
            'Base de datos - usuarios'
        )
        
    def test_click_add_user_url(self):
        
        self.browser.get(self.live_server_url)
        
        create_url = self.live_server_url + reverse('create')
        
        self.browser.find_element(By.TAG_NAME,'a').click()
        self.assertEquals(
            self.browser.current_url,
            create_url
        )
    
    def test_user_see_create_page(self):
        
        self.browser.get(self.live_server_url)
        
        self.browser.find_element(By.TAG_NAME,'a').click()
        
        self.assertEquals(
            self.browser.find_element(By.TAG_NAME,'h3').text,
            'Agregar usuario'
        )
    
    def test_user_add_data(self):
        
        self.browser.get(self.live_server_url)
        
        sleep(1)
        
        self.browser.find_element(By.TAG_NAME,'a').click()
        
        data = ['Adriana','Rodriguez','adriana.rodriguez@outlook.com','Medellin']
        
        nombres = self.browser.find_element(By.NAME, 'nombres')
        nombres.send_keys(data[0])
        apellidos = self.browser.find_element(By.NAME, 'apellidos')
        apellidos.send_keys(data[1])
        correo = self.browser.find_element(By.NAME, 'correo')
        correo.send_keys(data[2])
        ciudad = self.browser.find_element(By.NAME, 'ciudad')
        ciudad.send_keys(data[3])
        
        sleep(1)
        
        self.browser.find_element(By.TAG_NAME,'button').click()
        li = self.browser.find_elements(By.TAG_NAME,'td')
        
        count = 0
        
        for j in range(len(data)):
            for i in range(len(li)):
                t = li[i].text
                if  t == data[j]:
                    count = count + 1
                    
        self.assertEquals(4,count)
        