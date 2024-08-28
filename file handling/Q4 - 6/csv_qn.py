"""
You are given two CSV files:

Shopping_file: Contains details of items purchased by the customer which includes names and quantity of the items purchased. SNo,ProductName,Qty

Prices_file: Contains details like product Id, name and price of all available items.
Id,ProductName,Price

The variable shopping_file represents the name of the file containing product purchase details, and prices_file represents the name of the file containing product prices.

Define a function calculate_total_price that takes shopping_file and prices_file as argument and returns the total amount of goods purchased by the customer.
"""

def calculate_total_price(prices_file: str, shopping_file: str) -> int:
    '''
    Compute the total amount spent on the products.
    Args:
        Prices_file (str): path of file containing product purchase details.
        Shopping_file (str): path of file containing product prices.
    Returns:
        Float: The total amount.
    '''
    ... 