url_test = 'https://www.saucedemo.com/'

login_ele = {"UserName": "[data-test='username']",           # "input[@id='username']"
             "PassWord" : "[data-test='password']",          # "input[@id='password']"
             "Login_Button" : "[data-test='login-button']"}  # "input[@id='login-button']"

success_login = [{'username':'standard_user',
                  'password':'secret_sauce',
                  'expect_url':'https://www.saucedemo.com/inventory.html',
                  'error_info1':'wrong net address'}]

select_add = {
    "Backpack":"[data-test='add-to-cart-sauce-labs-backpack']",
    "Bike_Light":"[data-test='add-to-cart-sauce-labs-bike-light']",
    "Bolt_T-Shirt":"[data-test='add-to-cart-sauce-labs-bolt-t-shirt']",
    "Fleece_Jacket":"[data-test='add-to-cart-sauce-labs-fleece-jacket']",
    "Onesie":"[data-test='add-to-cart-sauce-labs-onesie']",
    "T-Shirt (Red)":"[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']"
}

select_remove = {
    "Backpack":"[data-test='remove-sauce-labs-backpack']",
    "Bike_Light":"[data-test='remove-sauce-labs-bike-light']",
    "Bolt_T-Shirt":"[data-test='remove-sauce-labs-bolt-t-shirt']",
    "Fleece_Jacket":"[data-test='remove-sauce-labs-fleece-jacket']",
    "Onesie":"[data-test='remove-sauce-labs-onesie']",
    "T-Shirt (Red)":"[data-test='remove-test.allthethings()-t-shirt-(red)']"
}

product_button = {
    "Backpack":"[data-test='item-4-img-link']",
    "Bike_Light":"[data-test='item-0-img-link']",
    "Bolt_T-Shirt":"[data-test='item-1-img-link']",
    "Fleece_Jacket":"[data-test='item-5-img-link']",
    "Onesie":"[data-test='item-2-img-link']",
    "T-Shirt (Red)":"[data-test='item-3-img-link']"
}

shop_cart_link = "[data-test='shopping-cart-link']"

continue_shop = "[data-test='continue-shopping']"

check_out = "[data-test='checkout']"

first_name = "[data-test='firstName']"

last_name = "[data-test='lastName']"

postal_code = "[data-test='postalCode']"

cancel = "[data-test='cancel']"

continue_button = "[data-test='continue']"

finish_button = "[data-test='finish']"

complete= "[data-test='complete-header']"

menu_button = "[id='react-burger-menu-btn']"

logout_button = "[id='logout_sidebar_link']"