from src.pages.web_page_element.agent_page_elements import AgentPageElements
import logging
from selenium.common.exceptions import TimeoutException
import time
import json
import pytest
from src.tests.base_test import BaseTest
import src.framework.global_config as config


class AgentHelpers(BaseTest):

    agent_page = AgentPageElements()

    """open Agent login page"""

    def open_agent_login_page(self):
        self.agent_page.open_url(uri=self.agent_page.agent_url)

    """Enter Agent username"""

    def enter_agent_user_name(self,agent_user_name):
        self.agent_page.type(self.agent_page.agent_login_user_name,agent_user_name)

    """Enter Agent password"""

    def enter_agent_password(self, agent_password):
        self.agent_page.type(self.agent_page.agent_login_password, agent_password)

    """Click login button"""

    def click_login_button(self):
        self.agent_page.click(self.agent_page.agent_login_button)
        self.agent_page.wait(5)

    """Read json file"""

    def read_json(self):
        with open('C:/Users/HP/PycharmProjects/HappyFox/src/helpers/json_file.json') as d:
            data = json.load(d)
        return data

    """hover to manage"""

    def hover_to_options(self):
        self.agent_page.wait_for_presence(self.agent_page.ticket,timeout=10)
        self.agent_page.wait(5)
        self.agent_page.click(self.agent_page.ticket,timeout=10,max_retries=3)
        self.agent_page.wait(2)

    """select statuses option from manage"""

    def select_statuses_option(self):
        self.agent_page.scroll_to_element(self.agent_page.statuses)
        self.agent_page.click(self.agent_page.statuses)
        self.agent_page.wait(2)

    """select Priorities option from manage"""

    def select_priorities_option(self):
        self.agent_page.scroll_to_element(self.agent_page.priorities)
        self.agent_page.click(self.agent_page.priorities)
        self.agent_page.wait(2)

    """Click add status symbol"""

    def click_add_status_symbol(self):
        self.agent_page.click(self.agent_page.add_status_plus_symbol)

    """Enter status name"""

    def enter_status_name(self,status_name):
        self.agent_page.type(self.agent_page.status_name,status_name)

    """Enter status description"""

    def enter_status_description(self,status_description):
        self.agent_page.type(self.agent_page.status_description,status_description)

    """click add status button"""

    def click_add_status_button(self):
        self.agent_page.click(self.agent_page.add_status_button)
        self.agent_page.wait(2)

        try:
            a = self.agent_page.is_element_present(self.agent_page.duplicate_status_or_priority_name_error)
            logging.error("Trying to create status with duplicate name")
            pytest.fail()
        except TimeoutException:
            pass


    """Click add priority symbol"""

    def click_add_priority_symbol(self):
        self.agent_page.click(self.agent_page.add_priority_plus_symbol)

    """Enter Priority name"""

    def enter_priority_name(self, priority_name):
        self.agent_page.type(self.agent_page.priority_name, priority_name)

    """Enter priority description"""

    def enter_priority_description(self, priority_description):
        self.agent_page.type(self.agent_page.priority_description, priority_description)

    """click add priority button"""

    def click_add_priority_button(self):
        self.agent_page.click(self.agent_page.add_priority_button)
        self.agent_page.wait(2)
        try:
            a = self.agent_page.is_element_present(self.agent_page.duplicate_status_or_priority_name_error)
            logging.error("Trying to create priority with duplicate name")
            pytest.fail()
        except TimeoutException:
            pass

    """select the status by name"""

    def select_status_by_name__or_check_status_name_in_status_list(self, status_name,check_created_status_name_in_status_page =None):
        for x in range(1,10,1):
            status = self.agent_page.get_attribute(self.agent_page.find_status_by_name(num=x),"innerText")
            if check_created_status_name_in_status_page == "yes" and status == status_name.upper():
                return status
            if status == status_name.upper():
                self.agent_page.click(self.agent_page.find_status_by_name(num=x))
                break

    """ Delete status or priority button"""

    def click_delete_status_button(self):
        self.agent_page.click(self.agent_page.delete_status_or_priority)
        if self.check_choose_status_or_priority_option() is True:
            self.choose_status_or_priority_before_deleting_it()
            self.select_any_status_or_priority()

    """Click delete button"""

    def click_delete_button(self):
        self.agent_page.click(self.agent_page.delete_button)
        self.agent_page.wait(2)

    """select the priority by name"""

    def select_priority_by_name_or_check_priority_on_priority_page(self, priority_name, check_created_status_name_in_priority_page=None):
        for x in range(1, 10, 1):
            priority = self.agent_page.get_attribute(self.agent_page.find_priority_by_name(num=x), "innerText")
            if check_created_status_name_in_priority_page == "yes" and priority == priority_name:
                return priority
            if priority == priority_name:
                self.agent_page.click(self.agent_page.find_priority_by_name(num=x))
                break

    """Check priority deleted message"""

    def check_priority_or_status_deleted_success_message(self):
        actual_message = self.agent_page.get_attribute(self.agent_page.priority_or_status_deleted_success_message, 'innerText')
        return actual_message

    """Make status as default"""

    def make_the_status_as_default(self, status_name):
        for x in range(1,10,1):
            status = self.agent_page.get_attribute(self.agent_page.find_status_by_name(num=x),"innerText")
            if status == status_name.upper():
                element = self.agent_page.make_status_as_default(num=x)
                self.agent_page.click_hidden_element(element[1])
                self.agent_page.wait(2)
                break

    """Make priority as default"""

    def make_the_priority_as_default(self, priority_name):
        for x in range(1,10,1):
            priority = self.agent_page.get_attribute(self.agent_page.find_priority_by_name(num=x),"innerText")
            if priority == priority_name:
                element = self.agent_page.make_priority_as_default(num=x)
                self.agent_page.click_hidden_element(element[1])
                self.agent_page.wait(2)
                break

    """check priority of the ticket"""

    def check_priority(self):
        priority = self.agent_page.get_attribute(self.agent_page.check_priority,"innerText")
        return priority

    """check status of the ticket"""

    def check_status(self):
        status = self.agent_page.get_attribute(self.agent_page.check_status, "innerText")
        return status

    """ Click reply button"""
    def click_reply_button(self):
        self.agent_page.click(self.agent_page.reply)

    """ Click canned_action"""

    def click_canned_action_button(self):
        self.agent_page.click(self.agent_page.canned_action)

    """ Click canned reply button"""

    def click_canned_reply_button(self):
        self.agent_page.click(self.agent_page.canned_reply)
        time.sleep(5)

    """ Click apply button"""

    def click_apply_button(self):
        self.agent_page.click(self.agent_page.apply_button)

    """ Click add reply button"""

    def click_add_reply_button(self):
        self.agent_page.click(self.agent_page.add_reply)

    """Select ticket"""
    def select_ticket(self):
        self.agent_page.wait(3)
        self.agent_page.click(self.agent_page.select_ticket)

    """Click staff menu drop down """

    def staff_menu_drop_down(self):
        self.agent_page.refresh()
        self.agent_page.scroll_to_element(self.agent_page.staff_menu_drop_down)
        self.agent_page.click(self.agent_page.staff_menu_drop_down)

    """click logout"""

    def click_logout(self):
        self.agent_page.click(self.agent_page.logout)
        self.agent_page.wait(5)

    """check choose status or priority option is visible"""

    def check_choose_status_or_priority_option(self):
        try:
            a = self.agent_page.is_element_present(self.agent_page.choose_status_or_priority_before_deleting)
        except TimeoutException:
            a = False
        return a

    """click drop down choose status or priority"""

    def choose_status_or_priority_before_deleting_it(self):
        self.agent_page.click(self.agent_page.choose_status_or_priority_before_deleting)

    """Select any status or priority"""

    def select_any_status_or_priority(self):
        self.agent_page.click(self.agent_page.select_one_status_or_priority_before_deleting)

    """Check Unresponded by agent status of the ticket"""

    def check_unresponded_by_agent(self):
        self.agent_page.is_element_displayed(self.agent_page.unresponded_by_agent)

    """Check Responded by agent status of the ticket"""

    def check_Responded_by_agent(self):
        self.agent_page.is_element_displayed(self.agent_page.responded_by_agent)

    """Added tag text"""

    def check_tag_text(self):
        tag = self.agent_page.get_attribute(self.agent_page.added_tag,"innerText")
        return tag

    """Status on ticket"""

    def status_on_ticket(self):
        status = self.agent_page.get_attribute(self.agent_page.status_on_ticket,"innerText")
        return status

    """status change"""

    def status_change_on_ticket(self):
        status_changes_from = self.agent_page.get_attribute(self.agent_page.status_change(num=1),"innerText")
        status_changes_to = self.agent_page.get_attribute(self.agent_page.status_change(num=2),"innerText")
        return status_changes_from,status_changes_to

    """Priority change"""

    def priority_change_on_ticket(self):
        priority_changes_from = self.agent_page.get_attribute(self.agent_page.priority_change(num=1), "innerText")
        priority_changes_to = self.agent_page.get_attribute(self.agent_page.priority_change(num=2), "innerText")
        return priority_changes_from, priority_changes_to

    """switch between windows"""

    def switch_between_windows(self,num):
        window_handles = self.agent_page.list_window_handles()
        self.agent_page.switch_to_window(window_handles[num])


    """Duplicate status or priority name error"""

    def duplicate_status_or_priority_name_error(self):
        error = self.agent_page.is_element_present(self.agent_page.duplicate_status_or_priority_name_error)
        return error

    """Select Ticket option"""
    def select_tickets_from_options(self):
        self.agent_page.click(self.agent_page.tickets_from_options)

    """Wait until success message not present"""
    def priority_or_status_deleted_success_message_not_present(self):
        self.agent_page.wait_for_element_not_present(self.agent_page.priority_or_status_deleted_success_message)