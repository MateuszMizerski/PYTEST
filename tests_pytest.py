# import pytest
from time import sleep
from webelements import Portal
from helpers import get_random_email


class TestList:

    service = Portal()
    correct_name = 'testuser'
    correct_last_name = 'lastname'
    correct_phone = '123456789'
    correct_email = get_random_email()

    @classmethod
    def setup_class(cls):
        print('\n===Setup Class===')
        cls.service.open_browser()
        cls.service.register_page_is_visible()
 
    @classmethod
    def teardown_class(cls):
        print('\n===Teardown Class===')
        cls.service.close_browser()

    @classmethod
    def setup_method(cls):
        cls.service.go_to_register_page()
        cls.service.register_page_is_visible()
    
    def _fill_all_correct_value(self):
        self.service.set_name(self.correct_name)
        self.service.set_last_name(self.correct_last_name)
        self.service.set_phone(self.correct_phone)
        self.service.set_email(self.correct_email)
        self.service.mark_email_marketing_agrement()
        self.service.mark_phone_marketing_agrement()

    def _register_with_success(self):
        self.service.click_register()
        self.service.success_page_is_visible()

    def _register_without_success(self):
        self.service.click_register()
        self.service.success_page_is_not_visible()
        self.service.register_page_is_visible()


    def test1(self):
        """all correct value"""
        self._fill_all_correct_value()
        self._register_with_success()
        assert True
    
    def test2(self):
        """incorrect phone value"""
        self._fill_all_correct_value()
        self.service.set_phone('1')
        self._register_without_success()
        assert True
    
    def test3(self):
        """incorrect email value"""
        self._fill_all_correct_value()
        self.service.set_email('t')
        self._register_without_success()
        assert True
    
    def test4(self):
        """empty name"""
        self.service.set_last_name(self.correct_last_name)
        self.service.set_phone(self.correct_phone)
        self.service.set_email(self.correct_email)
        self._register_without_success()
        assert True
    
    def test5(self):
        """empty last name"""
        self.service.set_name(self.correct_name)
        self.service.set_phone(self.correct_phone)
        self.service.set_email(self.correct_email)
        self._register_without_success()
        assert True
    
    def test6(self):
        """empty all value"""
        self._register_without_success()
        assert True

    def test7(self):
        """only marketing agrements marked"""
        self.service.mark_email_marketing_agrement()
        self.service.mark_phone_marketing_agrement()
        self._register_without_success()
        assert True

    def test8(self):
        """duplicated user"""
        email = 'duplicate@test.com'
        try:
            self.service.set_name(self.correct_name)
            self.service.set_last_name(self.correct_last_name)
            self.service.set_phone(self.correct_phone)
            self.service.set_email(email)
            self._register_with_success()
        except Exception:
            pass
        finally:
            self.service.go_to_register_page()
        self.service.set_name(self.correct_name)
        self.service.set_last_name(self.correct_last_name)
        self.service.set_phone(self.correct_phone)
        self.service.set_email(email)
        self._register_without_success()
        assert True

TestList()
