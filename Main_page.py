import allure
from selenium.webdriver.common.by import By
from Base_page import BasePage

user = {"login":"test63ivanov","password":"b383747b"}
email = {"adres":"test63ivanov@yandex.ru", "theme": "Simbirsoft Тестовое задание. <Орехов>"} 

class SeacrhLocators:
    LOC_ENTER = (By.CLASS_NAME, "HeadBanner-Button-Enter")
    LOC_FIELD_LOGIN = (By.ID, "passp-field-login")
    LOC_BUTTON_OK = (By.ID, "passp:sign-in")
    LOC_FIELD_PASSWORD = (By.ID, "passp-field-passwd")
    LOC_COUNT_ENTER_MAILS = (By.CLASS_NAME, "mail-NestedList-Item-Info-Link-Text")
    LOC_BUTTON_ELSE_MAILS = (By.CLASS_NAME, "_nb-large-pseudo-button")
    LOC_COUNT_TARGET_MAILS = (By.CSS_SELECTOR, "[title='Simbirsoft Тестовое задание']")
    LOC_BUTTON_WRITE_MESSAGE = (By.CLASS_NAME, "mail-ComposeButton-Text")
    LOC_ADRESS_MASSAGE= (By.CSS_SELECTOR, "[is='x-bubbles']")
    LOC_THEME_MESSAGE = (By.NAME, "subject")
    LOC_TEXT_MESSAGE = (By.XPATH, "//*[@id='cke_1_contents']/div")
    LOC_BUTTON_SEND_MESSAGE = (By.CLASS_NAME, "ComposeSendButton_desktop")
    LOC_FOOTER = (By.CLASS_NAME, "mail-App-Footer-Group_mobile")
    
    
class Mail(BasePage):

    @allure.story("Переход на страницу с логином")
    def go_to_login_page(self):
        self.find_element(SeacrhLocators.LOC_ENTER).click()
        assert self.browser.title == "Авторизация", "Переход на страницу с логином не удался"

    
    @allure.title("Логинимся в почте")
    def login_password(self):
        search_field_log = self.find_element(SeacrhLocators.LOC_FIELD_LOGIN)
        search_field_log.send_keys(user["login"])
        but_ok = self.find_element(SeacrhLocators.LOC_BUTTON_OK)
        but_ok.click()
        with allure.step("Ввели логин"):
            assert "Такого аккаунта нет" not in self.browser.page_source, "Ошибка в логине" 
        search_field_pas = self.find_element(SeacrhLocators.LOC_FIELD_PASSWORD)
        search_field_pas.send_keys(user["password"])
        but_ok = self.find_element(SeacrhLocators.LOC_BUTTON_OK)
        but_ok.click()
        with allure.step("Ввели пароль"):
            assert "Неверный" not in self.browser.page_source, "Ошибка в пароле"

    
    @allure.title("Ищем письмо по критерию")
    def find_mail(self):
        count = self.find_element(SeacrhLocators.LOC_COUNT_ENTER_MAILS).text
        count = int(count)
        i = 1
        while i <= (count/30): 
            footer = self.find_element(SeacrhLocators.LOC_FOOTER)  
            footer.location_once_scrolled_into_view   
            but_else_mail = self.find_element(SeacrhLocators.LOC_BUTTON_ELSE_MAILS)
            but_else_mail.click()
            mail = self.find_elements(SeacrhLocators.LOC_COUNT_TARGET_MAILS)
            i += 1
        mail = self.find_elements(SeacrhLocators.LOC_COUNT_TARGET_MAILS)
        footer = self.find_element(SeacrhLocators.LOC_FOOTER) 
        footer.location_once_scrolled_into_view
        with allure.step("Нашли письма"):
            assert len(mail) != 0, "Нет писем удовлетворяющих данному критерию"
        return mail

    
    @allure.title("Отправляем письмо")
    def write_message(self,mail):
        but_write_message = self.find_element(SeacrhLocators.LOC_BUTTON_WRITE_MESSAGE)
        but_write_message.click()
        adres_message = self.find_element(SeacrhLocators.LOC_ADRESS_MASSAGE)
        adres_message.send_keys(email["adres"])
        theme_message = self.find_element(SeacrhLocators.LOC_THEME_MESSAGE)
        theme_message.send_keys(email["theme"])
        message = self.find_element(SeacrhLocators.LOC_TEXT_MESSAGE )
        message.send_keys(len(mail))
        but_send_message = self.find_element(SeacrhLocators.LOC_BUTTON_SEND_MESSAGE)
        but_send_message.click()
        with allure.step("Отправили письмо"):
            assert "Письмо не отправлено" not in self.browser.page_source, "Письмо не отправлено" 
           
            


