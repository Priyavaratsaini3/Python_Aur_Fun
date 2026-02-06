import requests

def fetch_quote_api():
    url = "https://api.freeapi.app/api/v1/public/quotes"

    response = requests.get(url)
    data = response.json()

    quote_list = []
    if data["success"]:
        user_data = data['data']['data']
        for quote in user_data:
            quote_list.append(quote['content'])
        # quotes = user_data['data'][1]['content']
        return quote_list
    else:
        raise Exception("Failed to fetch data")
    

def main():
    try:
        quotes = fetch_quote_api()
        for i, quote in enumerate(quotes, start=1):
            print(f"{i}, Quotes: {quote}")
       
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()