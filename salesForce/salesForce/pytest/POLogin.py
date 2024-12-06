import time
from generate_random import GenerateRandom
from selenium.webdriver import Keys
from Log import Log
from salesforceSelenium import SalesForce
import os
from selenium import webdriver


class SF:
    def __init__(self, test_case, env="QA"):
        self.driver = webdriver
        self.url = "https://mxatt--qa.sandbox.my.salesforce.com/"
        self.sf = SalesForce(self.driver)
        self.log = Log(test_case, env)
        self.time_to_sleep = 2
        self.gr = GenerateRandom()

    def login(self):
        self.driver = self.sf.start_url(self.url, self.time_to_sleep)
        self.log.save_log("inicia SF " + self.url)

        self.sf.text_by_name("username", "ah989b@techmahindra.com.qa", self.time_to_sleep)
        self.sf.text_by_name("pw", "ah(1317)V", self.time_to_sleep)
        self.log.save_screen(self.driver, "inicia SF")
        self.sf.click_btn_by_name("Login", self.time_to_sleep)
        if self.sf.validate_identity_css("div[class='bottomCenter slds-col slds-size_1-of-3'] div["
                                         "class='flexipageComponent']", self.time_to_sleep):
            self.log.save_log("inicia SF " + "se necesita verificar identidad, en espera de un minuto para verificar "
                                             "identidad manualmente")
            self.log.save_screen(self.driver, "verificar identidad")
            print("se necesita verificar identidad, en espera de un minuto para verificar identidad manualmente")
            time.sleep(60)
            if not self.sf.validate_element('//*[@id="oneHeader"]/div[2]/div[1]/div', self.time_to_sleep):
                print("no se verifico identidad ")
        if not self.sf.validate_identity_css("a[title='Inicio']", self.time_to_sleep):
            self.sf.click_btn_by_xpath("//button[.='Mostrar menú de navegación']", self.time_to_sleep)
            self.sf.wait_element_by_xpath("//a[@data-label='Inicio']", self.time_to_sleep, 5)
            self.sf.click_btn_by_xpath("//a[@data-label='Inicio']", self.time_to_sleep)

    def pospago(self):

        self.sf.scroll_into_view("//*[@id='brandBand_1']/div/div/div/div/div/div[2]/div/div[2]/div/c-ccp_-home-elemento-pospago_lwc/div[2]/button",self.time_to_sleep)
        self.sf.click_btn_by_xpath("//*[@id='brandBand_1']/div/div/div/div/div/div[2]/div/div[2]/div/c-ccp_-home-elemento-pospago_lwc/div[2]/button", self.time_to_sleep)
        self.sf.scroll_into_view("//button[normalize-space()='>']", self.time_to_sleep)
        self.log.save_log("Inicio pospago")
        self.log.save_screen(self.driver, "inicio pospago")
        self.sf.click_btn_by_xpath("//button[@name='TipoVentaPospago']", self.time_to_sleep)
        time.sleep(2)
        self.sf.click_btn_by_xpath("//span[@title='Nueva']", self.time_to_sleep)
        self.sf.click_btn_by_xpath("//button[.='>']", self.time_to_sleep)
        time.sleep(self.time_to_sleep)
        self.venta_nueva()
        self.venta()

    def venta_nueva(self):
        intent = 0
        while intent <= 2:
            self.datos_cliente()
            if self.sf.validate_element("//span[contains(text(),'Detalles del domicilio')]", self.time_to_sleep):
                self.direccion_cliente()
            if self.sf.validate_element("//span[.='¿Desea facturar?']", self.time_to_sleep):
                self.datos_facturacion()
            if self.sf.validate_element("//span[.='¿Autoriza consulta de buró?']", self.time_to_sleep):
                self.buro_credito()
            if self.sf.validate_element("//span[.='¿Permite recopilación de información?']", self.time_to_sleep):
                self.consentimientos()
            if self.verificar():
                print("Campos llenados incorrectamente")
                self.sf.click_btn_by_xpath("//span[contains(text(),'¿Desa')]", self.time_to_sleep)
                intent += 1
            else:
                print("Campos llenados correctamente")
                num_cliente = self.sf.get_inner_text_by_xpath("//p[contains(text(),'Cliente creado')]",
                                                              self.time_to_sleep)
                self.log.save_log(str(num_cliente))
                break
            if intent == 3:
                raise Exception("Fallido")

    def datos_cliente(self):
        intent = 0
        name = self.gr.generate_text(10)
        last_name = self.gr.generate_text(10)
        second_last_name = self.gr.generate_text(10)
        date_of_birthday = self.gr.generate_date_of_birthday()
        day = date_of_birthday[0:2]
        month = date_of_birthday[3:5]
        year = date_of_birthday[6:10]

        rfc = self.gr.generate_rfc(name, last_name, second_last_name, year, month, day)
        self.log.save_log("datos: ")
        self.log.save_log(name)
        self.log.save_log(last_name)
        self.log.save_log(second_last_name)
        self.log.save_log(date_of_birthday)
        self.log.save_log(rfc)
        self.log.save_screen(self.driver, "inicio pospago")
        while intent <= 2:

            self.sf.text_by_xpath("//input[contains(@name,'NombreAccRes')]", name, self.time_to_sleep)
            self.sf.text_by_xpath("//input[contains(@name,'Apellido_paternoAccRes')]", last_name, self.time_to_sleep)
            self.sf.text_by_xpath("//input[contains(@name,'Apellido_maternoAccRes')]", second_last_name,
                                  self.time_to_sleep)
            self.sf.text_by_xpath("//input[contains(@name,'FechaNacimiento')]", date_of_birthday, self.time_to_sleep)
            self.sf.text_by_xpath("//input[contains(@name,'RFC')]", rfc, self.time_to_sleep)
            self.sf.select_xpath_by_index("//select[@name='TipoIdentificacionResMas']", 1, self.time_to_sleep)
            self.log.save_screen(self.driver, "datos cliente 1")
            self.sf.scroll_into_view("//select[@name='TipoIdentificacionResMas']", self.time_to_sleep)
            # self.sf.click_btn_by_xpath("//span[contains(text(),'Si')]", self.time_to_sleep)
            self.sf.text_by_xpath("//input[@name='Numero_de_ID_ResMas']", self.gr.generate_number(10),
                                  self.time_to_sleep)
            self.sf.select_xpath_by_index("//select[@name='Rango_de_ingresos']", 3, self.time_to_sleep)
            self.sf.text_by_xpath("//input[@name='Passcode']", "123245", self.time_to_sleep)
            self.sf.select_xpath_by_index("//select[@name='MetodoContactoPreferido']", 1, self.time_to_sleep)
            self.sf.scroll_into_view("//button[.='Siguiente']", self.time_to_sleep)
            self.log.save_screen(self.driver, "datos cliente 2")
            self.sf.select_xpath_by_index("//select[@name='Horario_preferrido_de_contacto']", 1, self.time_to_sleep)
            self.sf.text_by_xpath("//input[@placeholder='Sólo números (10)']", self.gr.generate_phone(),
                                  self.time_to_sleep)
            self.sf.click_btn_by_xpath("//button[.='Siguiente']", self.time_to_sleep)
            if self.sf.validate_element("//div[@class='flowruntime-input-error slds-form-element__help']",
                                        self.time_to_sleep):
                intent += 1
                print("campos llenados incorrectanmente, intentando de nuevo")
            else:
                break
        if intent == 3:
            self.log.save_log("Tc fallido")
            self.log.save_screen(self.driver, "fallido")
            raise Exception("Fallido")

    def direccion_cliente(self):
        intent = 0
        while intent <= 2:
            self.sf.text_by_xpath("//input[@name='enter-search']", "01020", self.time_to_sleep)
            self.sf.click_btn_by_xpath("//button[.='Buscar']", self.time_to_sleep)
            time.sleep(6)
            self.sf.click_btn_by_xpath("//button[@name='colonia']", self.time_to_sleep)
            self.sf.send_keyboards_by_xpath("//button[@name='colonia']", Keys.ENTER, self.time_to_sleep)
            self.sf.text_by_xpath("//textarea[@name='calle']", self.gr.generate_text(20), self.time_to_sleep)
            self.sf.text_by_xpath("//input[@name='numExterno']", self.gr.generate_number(2), self.time_to_sleep)
            self.log.save_screen(self.driver, "dirección cliente")
            self.sf.scroll_into_view("//button[.='Siguiente']", self.time_to_sleep)
            self.sf.click_btn_by_xpath("//button[.='Siguiente']", self.time_to_sleep)
            if self.sf.validate_identity_css("flowruntime-input-error slds-form-element__help",
                                             self.time_to_sleep):
                intent += 1
                print("campos llenados incorrectanmente, intentando de nuevo")
                self.log.save_screen(self.driver, "Error al llenar campos")
            else:
                break
        if intent == 3:
            self.log.save_log("Tc fallido")
            self.log.save_screen(self.driver, "fallido")
            raise Exception("Fallido")

    def datos_facturacion(self):
        self.sf.click_btn_by_xpath("//span[.='¿Desea facturar?']", self.time_to_sleep)
        self.sf.click_btn_by_xpath("//button[.='Siguiente']", self.time_to_sleep)

    def buro_credito(self):
        self.sf.select_xpath_by_index("//select[@name='AutorizaConsultaBuro']", 1, self.time_to_sleep)
        self.sf.select_xpath_by_index("//select[@name='CuentaConTarjetaCredito']", 2, self.time_to_sleep)
        self.sf.select_xpath_by_index("//select[@name='CuentaConCreditoAutomotriz']", 2, self.time_to_sleep)
        self.sf.select_xpath_by_index("//select[@name='CuentaConCreditoHipotecario']", 2, self.time_to_sleep)

        self.log.save_screen(self.driver, "buró de crédito")
        # Referencia 1
        self.sf.scroll_into_view("//select[@name='Tipo_de_telefonoRef1']", self.time_to_sleep)
        self.sf.text_by_xpath("//input[@name='NombreRef1']", self.gr.generate_text(7), self.time_to_sleep)
        self.sf.select_xpath_by_index("//select[@name='ParentescoRef1']", 1, self.time_to_sleep)
        self.sf.text_by_xpath("//input[@name='TelefonoRef1_txt']", self.gr.generate_phone(), self.time_to_sleep)
        self.sf.text_by_xpath("//input[@name='Apellido_paternoRef1']", self.gr.generate_text(7), self.time_to_sleep)

        self.log.save_screen(self.driver, "Referencia 1")

        # Referencia 2
        self.sf.scroll_into_view("//select[@name='Tipo_de_telefonoRef2']", self.time_to_sleep)
        self.sf.text_by_xpath("//input[@name='NombreRef2']", self.gr.generate_text(7), self.time_to_sleep)
        self.sf.select_xpath_by_index("//select[@name='ParentescoRef2']", 1, self.time_to_sleep)
        self.sf.text_by_xpath("//input[@name='TelefonoRef2_txt']", self.gr.generate_phone(), self.time_to_sleep)
        self.sf.text_by_xpath("//input[@name='Apellido_paternoRef2']", self.gr.generate_text(7), self.time_to_sleep)

        self.log.save_screen(self.driver, "Referencia 2")

        self.sf.scroll_into_view("//button[.='Siguiente']", self.time_to_sleep)
        self.sf.click_btn_by_xpath("//button[.='Siguiente']", self.time_to_sleep)

    def consentimientos(self):
        self.sf.select_xpath_by_index("//select[@name='Permite_recopilacion_de_informacion']", 1, self.time_to_sleep)
        self.sf.select_xpath_by_index("//select[@name='Permite_envio_de_propaganda']", 1, self.time_to_sleep)
        self.log.save_screen(self.driver, "concentimientos")
        self.sf.click_btn_by_xpath("//button[.='Siguiente']", self.time_to_sleep)

    def verificar(self):
        if self.sf.validate_element("//span[contains(text(),'¿Desa')]", self.time_to_sleep):
            self.log.save_screen(self.driver, "Cliente existente")
            self.sf.click_btn_by_xpath("//label[.='Sí']", self.time_to_sleep)
            return True
        else:
            self.log.save_screen(self.driver, "Cliente creado de forma correcta")
            self.sf.click_btn_by_xpath("//button[.='Siguiente']", self.time_to_sleep)
            return False

    def venta(self):
        self.sf.wait_element_by_xpath("//button[.='Validación de buró de crédito']", self.time_to_sleep, 10)
        self.sf.click_btn_by_xpath("//button[@title='Nueva Venta']", self.time_to_sleep)
        self.sf.wait_element_by_xpath("//span[normalize-space()='Es necesario procesar la venta']", self.time_to_sleep,
                                      60)
        #self.sf.scroll_into_view()
        self.sf.wait_element_by_xpath("(//iframe)[1]", self.time_to_sleep, 60)
        self.sf.change_iframe("(//iframe)[1]", self.time_to_sleep)
        self.sf.change_iframe_by_id("canvas-outer-_:CCP_BlueMarbleShoppingCart:j_id0:j_id10:canvasapp", self.time_to_sleep)
        self.sf.change_iframe_by_id("canvas-inner-_:CCP_BlueMarbleShoppingCart:j_id0:j_id10:canvasapp", self.time_to_sleep)
        self.sf.scroll_into_view("//h6[normalize-space()='Planes']", self.time_to_sleep)


    def set_plan(self,plan):
        self.sf.click_btn_by_xpath(f"(//span[.='{plan}'])[1]",self.time_to_sleep)
        self.sf.wait_element_by_xpath()

    def close_driver(self):
        self.sf.close_window()

    def prepago(self):
        if not self.sf.validate_element("//a[@title='Inicio']", self.time_to_sleep):
            self.sf.click_btn_by_xpath("(//span[@class='menuLabel slds-listbox__option-text "
                                       "slds-listbox__option-text_entity'][normalize-space()='Inicio'])[1]",
                                       self.time_to_sleep)
