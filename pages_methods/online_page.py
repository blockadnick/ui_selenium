from base_page import *


class Online(BasePage):

    url = "https://www.sitexample/online/"

    sections = {'popular': 1, 'recently': 2, 'week': 3}

    '''Switches to the desired section, returns an item with products and a "show 20 more" button'''
    def choose_section(self, param):
        self.presence_click((css, f".product-tabs :nth-child({param})"), 1) 
        if param == 1:
            items = self.driver.find_element(By.ID, "populyrnoe_za_2_menu-list-item-block-inner")
            show_more_button = ((id, "populyrnoe_za_2_show-more-button"))
        elif param == 2:
            items = self.find((id, "nedavno_pokazivali_menu-list-item-block-inner"))
            show_more_button = ((id, "nedavno_pokazivali_show-more-button"))
        elif param == 3:
            items = self.driver.find_element(By.ID, "populyrnoe_za_7_menu-list-item-block-inner")
            show_more_button = ((id, "populyrnoe_za_7_show-more-button"))
        else:
            print("! param not found")
        result = {"items": items, "button": show_more_button}
        return result

    '''Presses "show 20 more" while it exists'''
    def show_more_results(self, show_more_button):
        while self.element_ready(show_more_button, 3) == True:
            self.presence_click(show_more_button, 1)

    '''Accepts an element with products, returns a list of SKUs for the corresponding section'''          
    def parse_online(self, list_of_items):
        sku_containers = list_of_items.find_elements(By.CSS_SELECTOR, ".catalog-product-wrap-dop div.pt-5 span")
        list_of_sku_id = [sku.get_attribute("innerText") for sku in sku_containers]
        print(list_of_sku_id)
        return list_of_sku_id

    '''Checking for duplicate SKUs'''
    def check_duplicates(self, list_of_sku_id):
        duplicates = dict((x, list_of_sku_id.count(x)) for x in set(list_of_sku_id) if list_of_sku_id.count(x) > 1)
        print("duplicates:")
        print(duplicates)
        return (duplicates)


        
        