# Assignment

This my solution to the Label A assignment. 

**Tech stack**

The tech stack used in this assignment includes:

* Python
* Django Rest Framework

The assignment
---------
A company specialised in car parts wants to modernise their company, and start selling their parts online. Being the pro car salesmen that they are, they decided to develop the front-end via another agency. They entrust the back-end to none other than Label A.

Setup
----------

To run the project locally, the virtual environment must be activated and dependencies installed. Then migrations should be created and applied. Run the server with the command `python manage.py runserver` and open the api at http://127.0.0.1:8000/api/ (or any other Django configuration you have chosen). It is also possible to run the application with postgresql rather than sqllite by creating a database (`CREATE DATABASE myautocompanydb;`) and creating a user for it (`CREATE USER autocompany WITH PASSWORD 'auto123';`), and then commenting out the following code from the `settings.py` file:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'autocompanydb',
        'USER': 'autocompany',
        'PASSWORD': 'auto123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```


However, a faster way to test it is as a Heroku app here: https://autocompany-jb.herokuapp.com/api/

Features
------------
User stories were defined after some initial research. The following are testing instructions based on the Heroku deployment:

* As a company, I want all my products in a database, so I can offer them via our new platform to customers
    * Products can be added through the Django admin page here: https://autocompany-jb.herokuapp.com/admin/login/?next=/admin/ , with the username 'admin@test.com' and the password 'auto123', as this is a superuser.
    * Products can also be added directly from the api, here: https://autocompany-jb.herokuapp.com/api/product/

* As a client, I want to add a product to my shopping cart, so I can order it at a later stage

    * A shopping cart is created automatically for every user. A product can be added to the user's shopping cart here: https://autocompany-jb.herokuapp.com/api/cart_item/ , specifying the user, product and quantity of product

* As a client, I want to remove a product from my shopping cart, so I can tailor the order to what I actually need
    * A product can be removed from a shopping cart through a DELETE request here: https://autocompany-jb.herokuapp.com/api/cart_item/<cart_item_number> 

* As a client, I want to order the current contents in my shopping cart, so I can receive the products I need to repair my car
    * The current contents of the shopping cart are ordered here: https://autocompany-jb.herokuapp.com/api/order/. Upon making an order, the shopping cart is emptied automatically, and the total amount to be paid is calculated from current product prices.
* As a client, I want to select a delivery date and time, so I will be there to receive the order
    * The client can select the delivery date and time here: https://autocompany-jb.herokuapp.com/api/shipment/. Delivery times are shown in blocks (morning, afternoon, evening)

* As a client, I want to see an overview of all the products, so I can choose which product I want
    * Clients can find a list of all the products in their shopping cart here: http://127.0.0.1:8000/api/cart_item/?user=<user_id>
    * Clients can see a list of all products available here: http://127.0.0.1:8000/api/product/
* As a client, I want to view the details of a product, so I can see if the product satisfies my needs
    * Clients can view the details of a specific product here: http://127.0.0.1:8000/api/product/<product_id>/

The following assumptions were made:

* We don't have to worry about the front-end, but should think of a data format a JavaScript application can handle
* We don't need to worry about the payment of the order. Who needs money anyway?
* Authentication was added to user profiles, and non-staff/non-admin users are restricted from deleting products in order to show the authentication function, but this wasn't implemented in any other user stories in order to simply testing.




