from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SupportCenterPageElements(BasePage):
    ticket_subject = (By.CSS_SELECTOR,".hf-custom-container #subject-input-container input")
    ticket_message = (By.CSS_SELECTOR,".hf-custom-container #cke_id_html .cke_editable_themed")
    attach_file = (By.CSS_SELECTOR,'.hf-ticket-fields #attach-file-drop-area input')
    full_name = (By.CSS_SELECTOR,".hf-contact-fields  #id_name")
    email = (By.CSS_SELECTOR,".hf-contact-fields  #id_email")
    phone_number = (By.CSS_SELECTOR,".hf-contact-fields  #id_phone")
    create_ticket_button = (By.CSS_SELECTOR,".hf-form-field #submit")
    ticket_created_success_message = (By.CSS_SELECTOR," .hf-custom-message-after-ticket-creation_content.hf-editor-reset_list")