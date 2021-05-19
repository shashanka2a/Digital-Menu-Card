# Digital-Menu-Card

We have come up with a solution to avoid social contact, that is to replace the physical presence of the server and the ‘menu’ with a digital menu card. The customer will be given a QR code at his table. After the QR Code scanning the customer gets into our website home page displaying the menu items and their respective price.

#### Customer View:
It tracks all the information and details about the customers. We have read, ordering functionalities to this view. Users can view the food items available in the restaurant and order the items according to their interests.
#### Manager View:
All the records of the food items can be update by the admin and the customers can view the food item lists. Also this view manages the order detail i.e the food items ordered and the details of the table number, where that food item has to be served. 


## Environment

```sh
$  pip install -r requirements.txt
```


## Run


```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


## UI

### Customer View

![home](homepage.jpeg)

![cart](cartdetails.jpeg)

### Manager View

![order](ordersdisplay.jpeg)
