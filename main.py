from pyscript import display
from datetime import time

# Restaurant info
restaurant_name = 'Hot to Go!'  # string
owner_name = 'Jalainie R. Abdullah Jr.'  # string
year_established = 2025  # integer
has_delivery = True  # boolean

# Products with prices
products = {
    "Pizza": 200,
    "Burger": 120,
    "Hotdog": 80
}

# Business hours as a tuple
business_hours = (time(10, 0), time(22, 0))  # tuple

# --- DISPLAY SECTION ---

# Restaurant details
display(f"<p><strong>Owner:</strong> {owner_name}</p>", target="div1", append=True)
display(f"<p><strong>Established:</strong> {year_established}</p>", target="div1", append=True)
display(f"<p><strong>Delivery Available:</strong> {'Yes' if has_delivery else 'No'}</p>", target="div1", append=True)
display(f"<p><strong>Business Hours:</strong> {business_hours[0].strftime('%I:%M %p')} - {business_hours[1].strftime('%I:%M %p')}</p>", target="div1", append=True)

# Menu section
menu_html = "<h3>Our Menu</h3><ul class='menu-list'>"
for item, price in products.items():
    menu_html += f"<li><span class='item'>{item}</span><span class='price'>₱{price}</span></li>"
menu_html += "</ul>"

display(menu_html, target="div1", append=True)
