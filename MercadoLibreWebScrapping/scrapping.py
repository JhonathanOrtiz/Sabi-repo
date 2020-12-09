import random
from time import sleep
import pandas as pd 

from collections import defaultdict
from tqdm import tqdm

from selenium import webdriver

from utils import *


dictionary = defaultdict(list)
driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://www.mercadolibre.com.ve/categorias#nav-header')
sub_cat_list = driver.find_elements_by_xpath('//li[@class="categories__item"]')
products_scrpped = 0


for sub_cat_idx in tqdm(range(len(sub_cat_list)-1)):

    subcat = sub_cat_list[sub_cat_idx].find_element_by_xpath('.//a')
    subcat.click()
    stop_exec(1)

    while True:

        product_object = product_page(driver)
        last = 0
        for product_idx in range(len(product_object)-1):
            last = scroll_down(last, product_object[product_idx], driver)
            product_object[product_idx].click()
            product_info = get_info(driver)
            go_to_product_list(driver)
            stop_exec(3)
            dictionary = load_info(product_info, dictionary)
            print(dictionary)
            product_object = product_page(driver)
            products_scrpped+=1
            print('{} products have been scrapped'.format(products_scrpped))
        
        try:
            next_page(driver)
        except:
            print("SubCategory has been scrapped succesfully")
            break
    
    go_to_subcat_list()
    sub_cat_list = restart_cat_page(driver)