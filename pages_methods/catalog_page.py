from pages_methods.base_page import *


class Auth(BasePage):
    
    logpass = {"login": "login", "password": "password"}

    '''Main auth'''
    def login(self, logpass):
        self.click((css, "#login-1920"))
        self.send_keys((css, ".login-email"), logpass["login"])
        self.send_keys((css, ".login-password"), logpass["password"])
        self.click((css, ".login-button"))
        self.disappear((css, ".login-button"))

class Catalog(BasePage):

    url = "https://www.sitexample.com/catalog/"

    sorts = {
    'popularity__DESC':'popularity', 
    'price__ASC':'price',
    'discount__DESC':'discount'}
        
    '''Using sort'''
    def sort(self, sort_by):
        self.presence_click((css, "#order_by_dir_dropdown_img"), 2)
        self.click((xpth, f"//div[@class='webui-popover-content']//a[contains(text(),'{sort_by}')]"))
        self.disappear((css, ".webui-popover-content"))

    '''Add 1st item on catalog'''
    def choose_1st_item(self):
        self.hover_to_element((css, "#catalog-product-wrap-1 .currency-wrap span")) 
        size_exist = self.element_ready((css, "#catalog-product-wrap-1 .catalog-product-size span"), 3)
        if size_exist == True:                                         
            self.driver.find_element(By.CSS_SELECTOR, "#catalog-product-wrap-1 .catalog-product-size span").click() 
        self.click((css, "#catalog-product-wrap-1 .product-order-button button"))
        self.click((css, ".webui-popover-content #order-btn-desktop"))

    '''Add item from page'''
    def from_card_to_cart(self):  
        self.element_ready((css, ".product-order-button"), 1)
        try:  
            self.driver.find_element(By.CSS_SELECTOR, ".product-top-right-part .size-grid > div").click()
        except:  
            pass
        self.click((css, ".product-order-button"))
        self.click((css, ".webui-popover-content #order-btn-desktop"))         
        self.disappear((css, ".webui-popover-content #order-btn-desktop"))     

    '''Search and go to product's page'''
    def search_and_open(self, sku_id):
        self.click((css, ".search-button-1920 > span"))  
        self.send_keys((css, ".webui-popover-content #id-search-field"), sku_id)  
        self.click((css, ".webui-popover-content .search-search-action-button"))  

    '''A loop to search for an product from an array of SKUs'''
    def search_and_open_many(self, sku_array, url_part):
        result = 0 
        for sku in sku_array:
            self.click((css, ".search-button-1920"))  
            self.send_keys((css, ".webui-popover-content #id-search-field"), sku) 
            self.click((css, ".webui-popover-inner button.search-search-action-button"))  
            if self.is_correct_page(url_part) == True:
                pass
            else:
                print(str(sku) + ": err")
                result += 1
        print("Total products: " + str(len(sku_array)))
        print("Num errors: " + str(result))
        return result

    '''Difference between the page of a regular product and a product with a set'''
    def search_set(self):
        table_element = self.get_element_text((css, ".menu-list-item"))
        if table_element == "set":
            sku_id = self.get_element_text((css, ".product-info-value"))
            print(sku_id + " : product have a set")
            return True
        else:
            print("product don't have a set")
            return False
 
    '''Getting of SKUs from the current catalog page'''           
    def sku_from_catalog(self):
        list_of_items = self.find((css, ".catalog-page-inner"))
        sku_containers = list_of_items.find_elements(By.CSS_SELECTOR, ".product-dop-info-label span")
        list_of_sku_id = [sku.get_attribute("innerText") for sku in sku_containers]
        return list_of_sku_id

    '''Using a paginator'''
    def pagination(self, side):
        if side == "left":
            self.presence_click((css, ".page-left-arrow"), 2)
        elif side == "right":
            self.presence_click((css, ".page-right-arrow"), 2)

    '''Getting of SKUs'''
    def catalog_parser(self, page_count):
        if page_count == "":
            count = 1
            result = self.sku_from_catalog()
        else:
            count = 1
            result = self.sku_from_catalog()
            while count < page_count:
                self.pagination("right")
                result.extend(self.sku_from_catalog())
                count+=1
        return result
