import pyautogui as pyautogui

from src.pages.web_page_element.support_center_page_elements import SupportCenterPageElements
from src.tests.base_test import BaseTest
import src.framework.global_config as config
import time
import json
from src.tests.base_test import BaseTest
from src.helpers.agent_helpers import AgentHelpers



class SupportCenterHelpers(BaseTest):

    support_page = SupportCenterPageElements()
    agent_helper = AgentHelpers()

    """Visit support center page"""

    def visit_support_center_page(self):
        self.support_page.open_url_in_new_tab(url=self.support_page.support_center_url)
        self.agent_helper.switch_between_windows(num=1)


    """Enter ticket subject"""

    def enter_ticket_subject(self,ticket_subject):
        self.support_page.wait(5)
        self.support_page.type(self.support_page.ticket_subject,ticket_subject)

    """Enter ticket message"""

    def enter_ticket_message(self,ticket_message):
        self.support_page.type(self.support_page.ticket_message, ticket_message)

    """Attach file"""

    def attach_screenshot(self,file_path):
        element = self.support_page.attach_file
        self.support_page.file_upload(element[1], path=file_path)

    """Enter Name"""

    def enter_name(self,name):
        self.support_page.type(self.support_page.full_name,name)

    """Enter Email"""

    def enter_mail(self,mail_id):
        self.support_page.type(self.support_page.email,mail_id)

    """Enter phone number"""

    def enter_phone_number(self,phone_number):
        self.support_page.type(self.support_page.phone_number,phone_number)

    """Click create ticket button"""

    def click_create_ticket_button(self):
        self.support_page.click(self.support_page.create_ticket_button)
