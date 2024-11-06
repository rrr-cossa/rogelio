import csv
def read_products(filename):
    products = {}
    with open(filename, mode = "r", newline="") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        
        for row in reader:
            key =row[0]
            prod_desc = row[1]
            prod_price = row[2]
            products[key] = [prod_desc, prod_price]     
                 
    return products
def read_request(filename):
    product_ids = []
    quantities = []
    with open(filename, "rt") as csv_request:
        next(reader)
    
    for row in reader:
        product_ids.append(row[0])
        quantities.append(row[1])
        
    return product_ids, quantities

def main():
    products = read_products("products.csv")
    products_ids = read_request("request.csv")[1]
    quantities = read_request("request.csv")[1]
    print()
    print("Pollos el Poller")
    print()
    
    subtotal = 0 
    for i in range(len(products_ids)):
        product = products[products_ids[1]]
    name = product[0]
    price = float(product[1])
    quantity = quantities[1]
    print(f"{name}: {quantity} @ {price}")
    
main()
read_products("products.csv")