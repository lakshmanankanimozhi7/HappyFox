from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AgentPageElements(BasePage):
    agent_login_user_name = (By.CSS_SELECTOR,".append-bottom #id_username")
    agent_login_password = (By.CSS_SELECTOR," #id_password")
    agent_login_button = (By.CSS_SELECTOR,'.form-buttons input[value="Login"]')
    ticket = (By.CSS_SELECTOR,"#ember26 #ember27 span")
    statuses = (By.CSS_SELECTOR,"#ember26 .hf-mod-module-switcher .hf-module-switcher .hf-module-switcher-links > div:nth-child(2) > div > ul > li:nth-child(2) a")
    priorities = (By.CSS_SELECTOR,"#ember26 .hf-mod-module-switcher .hf-module-switcher .hf-module-switcher-links > div:nth-child(2) > div > ul > li:nth-child(3) a")
    add_status_plus_symbol = (By.CSS_SELECTOR,".hf-manage-header button")
    status_name = (By.CSS_SELECTOR,'.hf-entity-content section .hf-form-field_value input[data-test-id="form-field-name"]')
    status_description = (By.CSS_SELECTOR,'.hf-entity-content section .hf-form-field_value textarea[data-test-id="form-field-description"]')
    add_status_button = (By.CSS_SELECTOR,'.hf-entity-footer button[data-test-id="add-status"]')
    add_priority_plus_symbol = (By.CSS_SELECTOR, ".hf-manage-header button")
    priority_name = (By.CSS_SELECTOR, '.hf-entity-content section .hf-form-field_value input[data-test-id="form-field-name"]')
    priority_description = (By.CSS_SELECTOR, '.hf-entity-content section .hf-form-field_value textarea[data-test-id="form-field-description"]')
    add_priority_button = (By.CSS_SELECTOR,'.hf-entity-footer button[data-test-id="add-priority"]')
    duplicate_status_or_priority_name_error = (By.CSS_SELECTOR,'.hf-entity-content section .hf-form-field_value .hf-validation-error-message')

    #Element to find the status by its name
    def find_status_by_name(self,num):
        status_name_from_the_list = (By.CSS_SELECTOR,f'.lt-body tr:nth-child({num}) td:nth-child(2) .ember-view div')
        return status_name_from_the_list

    delete_status_or_priority = (By.CSS_SELECTOR, '.hf-entity-header .hf-delete-item ')
    delete_button = (By.CSS_SELECTOR,'button[data-test-id="delete-dependants-primary-action"]')

    #Element to find the priority by its name
    def find_priority_by_name(self,num):
        priority_name_from_the_list = (By.CSS_SELECTOR,f'.lt-body tr:nth-child({num})  td:nth-child(2) span')
        return priority_name_from_the_list

    priority_or_status_deleted_success_message = (By.CSS_SELECTOR, '.hf-toast-message  div')

    #Element to make the status as default
    def make_status_as_default(self,num):
        print(num)
        default_status = (By.CSS_SELECTOR,f'.lt-body tr:nth-child({num}) td:nth-child(5) .ember-view .hf-make-default')
        return default_status

    #Element to make the status as default
    def make_priority_as_default(self,num):
        default_priority = (By.CSS_SELECTOR,f'.lt-body tr:nth-child({num}) td:nth-child(5) div div')
        return default_priority

    check_priority = (By.CSS_SELECTOR,".hf-update-activities-area li:nth-child(2) span")
    check_status = (By.CSS_SELECTOR,".hf-update-activities-area li:nth-child(3) span")
    reply = (By.CSS_SELECTOR,'.hf-floating-editor_minimized-view_links-container a[data-test-id="reply-link"]')
    canned_action = (By.CSS_SELECTOR,".hf-floating-editor_toolbar .hf-pop-over-container .hf-u-vertical-super")
    canned_reply = (By.CSS_SELECTOR,'.ember-basic-dropdown-content-- .ember-power-select-options li[data-option-index="0"]')
    apply_button = (By.CSS_SELECTOR,".hf-canned-action-footer button")
    add_reply = (By.CSS_SELECTOR,".hf-floating-editor_footer button")
    select_ticket =(By.CSS_SELECTOR,".hf-list-body.hf-js-list-body  section > div:first-child .hf-ticket-box_subject_text")
    staff_menu_drop_down = (By.CSS_SELECTOR,".hf-staff-menu-drop-down")
    logout = (By.CSS_SELECTOR,'.hf-staff-menu_list li[data-test-id="staff-menu_logout"]')
    choose_status_or_priority_before_deleting = (By.CSS_SELECTOR,'.hf-form-field_value div[data-test-id="form-field-alternateEntity"] .ember-basic-dropdown-trigger ')
    select_one_status_or_priority_before_deleting  = (By.CSS_SELECTOR,'.ember-power-select-options li[data-option-index="0"]')
    unresponded_by_agent = (By.CSS_SELECTOR,".hf-ticket_response-indicator .hf-mod-unresponded")
    responded_by_agent = (By.CSS_SELECTOR,' .hf-ticket_response-indicator div[aria-label="Responded by Agent"]')
    added_tag = (By.CSS_SELECTOR,'.hf-updates-section-body article:first-child  li:nth-child(3) span')

    def status_change(self,num):
        status_change = (By.CSS_SELECTOR,f'.hf-updates-section-body article:first-child  li:nth-child(2) span:nth-child({num})')
        return status_change

    def priority_change(self,num):
        priority_change = (By.CSS_SELECTOR,f'.hf-updates-section-body article:first-child  li:nth-child(1) span:nth-child({num})')
        return priority_change

    status_on_ticket = (By.CSS_SELECTOR,'.hf-ticket-status .hf-ticket-status_name')
    tickets_from_options = (By.CSS_SELECTOR,'#ember26 .hf-mod-module-switcher .hf-module-switcher .hf-module-switcher-links > div:nth-child(1) > div:nth-child(2) a')