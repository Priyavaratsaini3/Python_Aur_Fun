import requests

def fetch_product():
    url = "https://api.freeapi.app/api/v1/public/randomproducts"

    response = requests.get(url)
    data = response.json()

    new_dict = {}
    
    if data["success"]:
        product_names = data["data"]["data"]
        for product in product_names:
            category = product['category']
            price = product['price']

            if category not in new_dict:
                new_dict[category] = []

            new_dict[category].append(price)

    return new_dict


def main():
    product = fetch_product()
    print(f"products Price: {product}")

if __name__ == "__main__":
    main()