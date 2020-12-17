from src.helpers.agent_helpers import AgentHelpers
from src.helpers.support_center_helpers import SupportCenterHelpers
import pytest
import logging
from src.tests.base_test import BaseTest
from src.pages.base_page import BasePage



@pytest.mark.happy_fox_tests
class HappyFoxTests(BaseTest):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)


    """Test 1 = scenario1&3"""

    @pytest.mark.test_run_1
    def test_run_1(self):

        # create object
        agent_helper = AgentHelpers()
        base_page = BasePage()

        # Get data from json file
        data = agent_helper.read_json()

        # Step1 - visit agent login page
        agent_helper.open_agent_login_page()
        logging.info("visit agent login page")

        # Step2 - Enter user name
        agent_helper.enter_agent_user_name(agent_user_name=data["agent_user_name"])
        logging.info("Enter user name of the agent")

        # Step3 - Enter agent password
        agent_helper.enter_agent_password(agent_password=data["agent_password"])
        logging.info("Enter password of the agent")

        # Step4- Click login button
        agent_helper.click_login_button()
        logging.info("Logged into the Agent portal")

        # Step5 - Navigate to options and create new status
        agent_helper.hover_to_options()
        agent_helper.select_statuses_option()
        agent_helper.click_add_status_symbol()
        agent_helper.enter_status_name(status_name=data["status_Name"])
        agent_helper.enter_status_description(status_description=data["status_description"])
        agent_helper.click_add_status_button()
        status_in_page = agent_helper.select_status_by_name__or_check_status_name_in_status_list(status_name=data["status_Name"], check_created_status_name_in_status_page="yes")
        assert data["status_Name"].upper() == status_in_page
        logging.info("Created new status successfully")

        # #Step6 - Navigate to options and create new priority
        agent_helper.hover_to_options()
        agent_helper.select_priorities_option()
        agent_helper.click_add_priority_symbol()
        agent_helper.enter_priority_name(priority_name=data["Priority_Name"])
        agent_helper.enter_priority_description(priority_description=data["priority_description"])
        agent_helper.click_add_priority_button()
        priority_in_page = agent_helper.select_priority_by_name_or_check_priority_on_priority_page(priority_name=data["Priority_Name"], check_created_status_name_in_priority_page="yes")
        assert data["Priority_Name"] == priority_in_page
        logging.info("Created new Priority successfully")

        # delete the created status
        agent_helper.hover_to_options()
        agent_helper.select_statuses_option()
        agent_helper.select_status_by_name__or_check_status_name_in_status_list(status_name=data["status_Name"])
        agent_helper.click_delete_status_button()
        agent_helper.click_delete_button()
        expected_message = 'Status "%s" is deleted successfully.' % data["status_Name"]
        actual_message = agent_helper.check_priority_or_status_deleted_success_message()
        assert expected_message == actual_message
        logging.info("Deleted the created Status")

        # delete the created priority
        agent_helper.priority_or_status_deleted_success_message_not_present()
        agent_helper.hover_to_options()
        agent_helper.select_priorities_option()
        agent_helper.select_priority_by_name_or_check_priority_on_priority_page(priority_name=data["Priority_Name"])
        agent_helper.click_delete_status_button()
        agent_helper.click_delete_button()
        expected_message = 'Priority "%s" is deleted successfully.'% data["Priority_Name"]
        actual_message = agent_helper.check_priority_or_status_deleted_success_message()
        assert expected_message == actual_message
        logging.info("Deleted the created Priority")

        #logout from the agent portal
        agent_helper.staff_menu_drop_down()
        agent_helper.click_logout()
        logging.info("Logged out from the Agent portal")

    """Test 2 = scenario1,2&3"""

    @pytest.mark.test_run_2
    def test_run_2(self):

        # create object
        agent_helper = AgentHelpers()
        base_page = BasePage()
        support_helper = SupportCenterHelpers()

        # Get data from json file
        data = agent_helper.read_json()

        # Step1 - visit agent login page
        agent_helper.open_agent_login_page()
        logging.info("visit agent login page")

        # Step2 - Enter user name
        agent_helper.enter_agent_user_name(agent_user_name=data["agent_user_name"])
        logging.info("Enter user name of the agent")

        # Step3 - Enter agent password
        agent_helper.enter_agent_password(agent_password=data["agent_password"])
        logging.info("Enter password of the agent")

        # Step4- Click login button
        agent_helper.click_login_button()
        base_page.wait(5)
        logging.info("Logged into the Agent portal")

        # Step5 - Navigate to options and create new status
        agent_helper.hover_to_options()
        agent_helper.select_statuses_option()
        agent_helper.click_add_status_symbol()
        agent_helper.enter_status_name(status_name=data["status_Name"])
        agent_helper.enter_status_description(status_description=data["status_description"])
        agent_helper.click_add_status_button()
        status_in_page = agent_helper.select_status_by_name__or_check_status_name_in_status_list(status_name=data["status_Name"], check_created_status_name_in_status_page="yes")
        assert data["status_Name"].upper() == status_in_page
        logging.info("Created new status successfully")

        # make status as default
        agent_helper.make_the_status_as_default(status_name=data["status_Name"])
        logging.info("Set created status as default")

        # #Step6 - Navigate to options and create new priority
        agent_helper.hover_to_options()
        agent_helper.select_priorities_option()
        agent_helper.click_add_priority_symbol()
        agent_helper.enter_priority_name(priority_name=data["Priority_Name"])
        agent_helper.enter_priority_description(priority_description=data["priority_description"])
        agent_helper.click_add_priority_button()
        priority_in_page = agent_helper.select_priority_by_name_or_check_priority_on_priority_page(priority_name=data["Priority_Name"], check_created_status_name_in_priority_page="yes")
        assert data["Priority_Name"] == priority_in_page
        logging.info("Created new Priority successfully")

        #make priority as default
        agent_helper.make_the_priority_as_default(priority_name=data["Priority_Name"])
        logging.info("Set created Priority as default")


        #open support center page in new tab and Create ticket
        support_helper.visit_support_center_page()
        logging.info("visit support center page and create ticket")
        support_helper.enter_ticket_subject(data["ticket_subject"])
        support_helper.enter_ticket_message(data["ticket_message"])
        support_helper.attach_screenshot(file_path='C:/Users/HP/PycharmProjects/HappyFox/src/helpers/sample_screenshot.PNG')
        support_helper.enter_name(data["ticket_full_name"])
        support_helper.enter_mail(data["ticket_email"])
        support_helper.enter_phone_number(data["ticket_phone_number"])
        support_helper.click_create_ticket_button()
        logging.info("Ticket created successfully")


        # reply to ticket
        agent_helper.switch_between_windows(num=0)
        logging.info("Visit agent portal")

        #visit tickets page and select the ticket
        agent_helper.hover_to_options()
        agent_helper.select_tickets_from_options()
        agent_helper.select_ticket()

        # check ticket is in unresponded state before giving any reply
        agent_helper.check_unresponded_by_agent()
        logging.info("Ticket is in unresponded state before giving any reply")

        # check status and priority are same as the default status and priority
        priority = agent_helper.check_priority()
        assert priority == data["Priority_Name"]
        logging.info("Ticket Created with default Priority")

        status = agent_helper.check_status()
        assert status == data["status_Name"].upper()
        logging.info("Ticket Created with default Status")

        # Give canned reply to the ticket
        agent_helper.click_reply_button()
        agent_helper.click_canned_action_button()
        agent_helper.click_canned_reply_button()
        agent_helper.click_apply_button()
        agent_helper.click_add_reply_button()
        logging.info("Canned reply given successfully")

        # check ticket changed to responded state after giving any reply
        agent_helper.check_Responded_by_agent()
        logging.info("Ticket changed to responded state after giving any reply")

        # check tag,status,priority after replied to the ticket
        tag = agent_helper.check_tag_text()
        assert tag == "customer_query"
        logging.info("Ticket tag - customer_query")

        status_change_from, status_change_to = agent_helper.status_change_on_ticket()
        assert status_change_from == data["status_Name"].upper()
        assert status_change_to == "CLOSED"
        logging.info("Ticket status changed from default to CLOSED")

        priority_change_from, priority_change_to = agent_helper.priority_change_on_ticket()
        assert priority_change_from == data["Priority_Name"]
        assert priority_change_to == "Medium"
        logging.info("Ticket priority changed from default to Medium")

        # Status on header of the ticket after reply
        status = agent_helper.status_on_ticket()
        assert status == "CLOSED"

        # delete the created status
        agent_helper.priority_or_status_deleted_success_message_not_present()
        agent_helper.hover_to_options()
        agent_helper.select_statuses_option()
        agent_helper.select_status_by_name__or_check_status_name_in_status_list(status_name=data["status_Name"])
        agent_helper.click_delete_status_button()
        agent_helper.click_delete_button()
        expected_message = 'Status "%s" is deleted successfully.' % data["status_Name"]
        actual_message = agent_helper.check_priority_or_status_deleted_success_message()
        assert expected_message == actual_message
        logging.info("Deleted the created Status")

        # delete the created priority
        agent_helper.priority_or_status_deleted_success_message_not_present()
        agent_helper.hover_to_options()
        agent_helper.select_priorities_option()
        agent_helper.select_priority_by_name_or_check_priority_on_priority_page(priority_name=data["Priority_Name"])
        agent_helper.click_delete_status_button()
        agent_helper.click_delete_button()
        expected_message = 'Priority "%s" is deleted successfully.' % data["Priority_Name"]
        actual_message = agent_helper.check_priority_or_status_deleted_success_message()
        assert expected_message == actual_message
        logging.info("Deleted the created Priority")

        # logout from the agent portal
        agent_helper.staff_menu_drop_down()
        agent_helper.click_logout()
        logging.info("Logged out from the Agent portal")

