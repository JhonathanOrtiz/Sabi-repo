import random
from time import sleep
from collections import defaultdict

def next_page(driver):

    if driver is None:
        print('Driver must be object not None')
    
    li_tag = driver.find_element_by_xpath('//li[@class="andes-pagination__button andes-pagination__button--next"]')
    button = li_tag.find_element_by_xpath('.//a[@class="andes-pagination__link ui-search-link"]')
    button.click()   

def get_info(driver=None):

    last = 0

    if driver == None:
        print('Driver must be an object not None')

    
    element = driver.find_element_by_xpath('//div[@class="vip-navigation-breadcrumb"]')
    element = element.find_element_by_xpath('.//ul')
    ul_list = element.find_elements_by_xpath('.//li')
    product_path = [item.text for item in ul_list]

    element = driver.find_element_by_xpath('//header[@class="item-title"]')
    product_title = element.find_element_by_xpath('.//h1[@class="item-title__primary "]').text
    last = scroll_down(last, element, driver)

    element = driver.find_element_by_xpath('//fieldset[@class="item-price  "]')
    product_price = element.find_element_by_xpath('.//span[@class="price-tag-fraction"]').text 

    element = driver.find_element_by_xpath('//article[@class="shipment-methods "]')
    product_location = element.find_elements_by_xpath('.//p')[1].text
    

    try:
        product_char = driver.find_element_by_xpath('//li[@class="specs-item specs-item-primary"]').text
    except:
        product_char = " "

    element = driver.find_element_by_xpath('//div[@class="item-description__text"]')
    last = scroll_down(last, element, driver)
    product_description = element.find_element_by_xpath('.//p').text
    
    element = driver.find_element_by_xpath('//div[@class="gallery-content item-gallery__wrapper"]')
    product_images = element.get_attribute('data-full-images')
    
    element = driver.find_element_by_xpath('//div[@class="vip-navigation-breadcrumb"]')
    last = scroll_down(last, element, driver)

    stop_exec(2)

    return {'title': product_title, 
            'price': product_price, 
            'char':product_char, 
            'description':product_description, 
            'path':product_path, 
            'location':product_location, 
            'image': product_images
        }
    
def restart_cat_page(cat_idx, driver=None):

    if driver == None:
        print('Driver must be an object not None')

    categories = driver.find_elements_by_xpath('//div[@class="categories__container"]')
    sub_path   = categories[cat_idx].find_element_by_xpath('.//h2[@class="categories__title"]')
    element    = categories[cat_idx].find_element_by_xpath('.//ul[@class="categories__list"]')
    return categories, sub_path, element

def go_to_product_list(driver=None):

    if driver == None:
        print('Driver must be an object not None')
    
    element = driver.find_element_by_xpath('//div[@class="vip-navigation-breadcrumb"]')
    button = element.find_element_by_xpath('.//a[@id="backToCateg"]')
    button.click()
    print('Going to product list')

def go_to_subcat_list(driver=None):

    if driver == None:
        print('Driver must be an object not None')

    ul_li = driver.find_element_by_xpath('//li[@class="nav-menu-item"]')
    go_back = ul_li.find_element_by_xpath('.//a') 
    go_back.click()
    print('Going to Subcat list')

def stop_exec(N):

    sleep_time = random.uniform(10, 20)
    print('Sleeping time {} {}'.format(N, sleep_time))
    sleep(sleep_time)

def product_page(driver):

    if driver == None:
        print('driver must be an object not None')

    products = driver.find_elements_by_xpath('//a[@class="ui-search-item__group__element ui-search-link"]')
    return products

def scroll_down(last, obj, driver=None):

    if driver is None:
        print('Driver must be an object not None')

    y = obj.location['y']
    driver.execute_script("window.scrollTo({},{});".format(last, y-10))
    last = y
    return last

def load_info(info, dictionary):
 
    dictionary['title'].append(info['title'])
    dictionary['price'].append(info['price'])
    dictionary['char'].append(info['char'])
    dictionary['description'].append(info['description'])
    dictionary['path'].append(info['path'])
    dictionary['location'].append(info['location'])
    dictionary['image'].append(info['image'])
    return dictionary


