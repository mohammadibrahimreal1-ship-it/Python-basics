"""Given a dictionary of products and their prices, find the product with the highest price."""

prod_price = {"bag":1000, "laptop":80000, "pen":20}

most_expensive = max(prod_price, key=prod_price.get)
print(most_expensive)