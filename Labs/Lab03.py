name_of_cafe = "Juniper Café Collective"
currency = "SEK"

table_number = input("Table number: ")      # 7
client_name = input("Client name: ")        # Ada Lovelace

product1 = input("Product 1: ")             # Tea
price1 = input("Price 1: ")                 # 18.5

product2 = input("Product 2: ")             # Sandwich
price2 = input("Price 2: ")                 # 42

product3 = input("Product 3: ")             # Fruit
price3 = input("Price 3: ")                 # 12.75

# Process the values here

prices = [price1, price2, price3]

float_prices = []

for price in prices:
    price = float(price)
    float_prices.append(price)

subtotal = float_prices[0] + float_prices[1] + float_prices[2]

name_of_cafe_upper = name_of_cafe.upper()
client_name_upper = client_name.upper()

# Print the receipt here

print(f"\n{name_of_cafe_upper}")
print(f"Table: {table_number}")
print(f"Client: {client_name_upper}\n")
print(f"{product1:.<20}  {float_prices[0]:.2f} {currency}")
print(f"{product2:.<20}  {float_prices[1]:.2f} {currency}")
print(f"{product3:.<20}  {float_prices[2]:.2f} {currency}\n")
print(f"Subtotal: {subtotal:>17.2f} {currency}\n")

