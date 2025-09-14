from pyscript import display

# Restaurant Information
restaurant_name = "Hot to Go!"   # string
owner_name = "Jalainie R. Abdullah Jr."   # string
year_established = 2025   # integer
has_delivery = True       # boolean

# Menu with Prices
menu_prices = {
    "Pizza": 200,
    "Burger": 120,
    "Hotdog": 80,
    "Fries": 60,
    "Spaghetti": 150,
    "Fried Chicken": 180
}

# Business hours (tuple of strings)
business_hours = ("10:00", "22:00")  # open - close

# Display Restaurant Info
display(f"<h2>{restaurant_name}</h2>", target="div1", append=True)
display(f"<p>Owner: {owner_name}</p>", target="div1", append=True)
display(f"<p>Established: {year_established}</p>", target="div1", append=True)
display(f"<p>Delivery Available: {'Yes' if has_delivery else 'No'}</p>", target="div1", append=True)
display(f"<p>Business Hours: {business_hours[0]} - {business_hours[1]}</p>", target="div1", append=True)

# Display Menu
menu_html = "<h3>Menu</h3><ul>"
for item, price in menu_prices.items():
    menu_html += f"<li>{item} – ₱{price}</li>"
menu_html += "</ul>"

display(menu_html, target="div1", append=True)
