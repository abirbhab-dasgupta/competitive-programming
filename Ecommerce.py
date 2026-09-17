n = int(input("Enter number of products: "))
prices=[]
for i in range(n):
    price = float(input(f"Enter price of product {i + 1}: "))
    prices.append(price)
prices.sort()
print("\nProduct prices in ascending order:")
for price in prices:
    print(price)