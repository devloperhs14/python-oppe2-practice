import random

def create_csv_files(num_outputs: int):
    product_names = [f"Product{i+1}" for i in range(num_outputs)]

    # Create shopping_file.csv
    with open('shopping_file.csv', 'w') as f:
        f.write("SNo,ProductName,Qty\n")
        for i, product in enumerate(product_names, start=1):
            qty = random.randint(1, 10)  # Random quantity between 1 and 10
            f.write(f"{i},{product},{qty}\n")

    # Create prices_file.csv
    with open('prices_file.csv', 'w') as f:
        f.write("Id,ProductName,Price\n")
        for i, product in enumerate(product_names, start=1):
            price = random.randint(1, 20)  # Random price between 1 and 20
            f.write(f"{i},{product},{price}\n")

# Example usage
create_csv_files(150)
