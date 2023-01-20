from base_page import *
from time import sleep
from random import choice


class CheckOut(BasePage):

    url = "https://www.sitexample.com/checkout/"

    dev_url = "https://www.dev.sitexample.com/checkout/"

    session_id = "vdi9861m1lt9a8bbp13n9fdufn"


    '''Getting order number'''
    def check_order_sucsess(self):
        self.element_ready((css, ".my-2 h2"), 15)
        order_number = self.get_element_text((css, ".my-2 h2")) 
        return True

    '''Random city'''
    def random_city(self):
        list = ["City1", "City2", "City3", "City4", "City5", "City6", "City7", "City8", "City9", "City10"]
        return choice(list)

    '''Transformation of url'''
    def open_dynamic_url(self, session_id, *branch):
        if branch == "dev":
            sessioned_url = CheckOut.dev_url + "?PHPSESSIONID=" + session_id
        else:
            sessioned_url = CheckOut.url + "?PHPSESSIONID=" + session_id
        self.open(sessioned_url)

    '''Getting name, phone, email'''
    def initial_personal_data(self):
        array = self.get_element_text((css, "#collapse-1 .text-info"))
        first = array.split(r"\n")
        return first

    '''Checks the availability of a section of personal data or an address and opens it if it is closed'''
    def check_expanded_area(self, area):
        if area == "pdata":
            expanded_area = self.element_ready((css, "#collapse-2.show"), 2)
            if expanded_area == True:
                pass
            else:
                self.click((xpth, "//h2[text()='your data']/..//span"))       
        elif area == "address":
            expanded_area = self.element_ready((css, "#collapse-4.show"), 2)
            if expanded_area == True:
                pass
            else:
                self.click((xpth, "//h2[text()='delivery type']/..//span"))   
        else:
            print("input error")
        
    '''Clearing personal data fields'''
    def clear_personal_data(self, *fields):
        self.check_expanded_area("pdata")      
        for field in fields:
            self.clear_by_keys((css, f"input[placeholder='{field}']"))

    '''Filling in personal data fields'''
    def entering_personal_data(self, **fields):
        self.check_expanded_area("pdata") 
        iter = -1                                           
        keys = list(fields.keys())                            
        values = list(fields.values())                        
        for field in fields:
            iter += 1
            if field=="post":
                self.send_keys((css, f"input[placeholder='email {keys[iter]}']"), values[iter])
            else:
                self.send_keys((css, f"input[placeholder='{keys[iter]}']"), values[iter])

    '''Clearing address fields'''
    def clear_address(self, *fields):
        self.check_expanded_area("address")
        for field in fields:
            if "address" in field:
                self.clear_by_keys((css, f"input[placeholder='input address']"))
            elif "flat" in field:
                self.clear_by_keys((css, f"input[placeholder='flat']"))
            else:
                print("input error!")

    '''Input an address'''
    def entering_address(self, address, *flat):
        self.check_expanded_area("address")   
        array = [address, flat]                                                                  
        self.send_keys((css, "input[placeholder='input address']"), address)
        self.click((css, "#collapse-4 .position-relative ul li"))
        if flat in array:
            self.send_keys((css, "input[placeholder='flat']"), flat)
        else:
            pass

    '''Checks the green marker if the field is filled in correctly, returns 1 if not found'''
    def check_field_success(self, field):
        if field == "address":
            result = self.element_presence((css, f"input[placeholder='input address']~.input-check-icon"), 3)
        else:
            result = self.element_presence((css, f"input[placeholder='{field}']~.input-check-icon"), 3)
        if result == False:
            return 1
        else:
            return 0
    
    '''Checks for notification of incorrect field completion, returns 1 if notification is found''' 
    def check_field_error(self, field):
        dfields = {"phone": 1, "last_name": 2, "first_name": 3, "email": 4, "address": 1, "flat": 2} 
        param = dfields[field] 
        if field == "address" or "flat":
            result = self.element_presence((css, f"#collapse-4>:nth-child({param}) label span"), 2)
        else:
            result = self.element_presence((css, f"#collapse-2>:nth-child({param}) label span"), 2)
        if result == True:
            return 1
        else:
            return 0

    '''Select delivery type'''
    def delivery_type(self, delivery_type):
        if delivery_type == "pvz":
            self.presence_click((css, ".flicking-pagination-bullet:nth-last-child(1)"), 5)
            self.presence_click((css, ".flicking-camera .delivery-card-container:nth-last-child(1) img"), 3) 
            self.hover_click((css, ".ymaps-2-1-79-places-pane .ymaps-2-1-79-image"))   
            self.hover_click((css, ".delivery-card-inactive-icon"))
        elif delivery_type == "delivery":
            self.click((css, ".flicking-camera .delivery-card-container:nth-child(1) img")) 
        else:
            print("type_error")
    
    '''Select payment type'''
    def change_payment_type(self, type):
        change = {
            "postpayment": 1,
            "prepayment": 2,
            "SBP": 3,
            "yandex": 4,
        }
        self.click((css, f".rounded div:nth-child({change[type]})"))

    '''Click to continue button'''
    def click_to_continue_button(self):
        self.presence_click((css, "button.btn"), 3)






