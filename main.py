# PYTHON
from pyscript import display
from datetime import time

restaurant_name = 'Hot to Go!'  # string
owner_name = 'Jalainie R. Abdullah Jr.'  # string
year_established = 2025  # integer
popular_item_price = 200  # integer
has_delivery = True  # boolean

product_names = ['Pizza', 'Burger', 'Hotdog']  # list
business_hours = (time(10, 0), time(22, 0))  # tuple
weight = 56.09  # float

# Display information
display(f"<h2>{restaurant_name}</h2>", target="div1")
display(f"<p>Owned by {owner_name}, established in {year_established}</p>", target="div1")
display(f"<p>Popular item price: ₱{popular_item_price}</p>", target="div1")
display(f"<p>Delivery Available: {has_delivery}</p>", target="div1")
display(f"<p>Products: {', '.join(product_names)}</p>", target="div1")
display(f"<p>Business Hours: {business_hours[0]} - {business_hours[1]}</p>", target="div1")
