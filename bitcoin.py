import sys
import urllib.request
import json

# Function to validate and parse the command-line arguments
def parse_arguments():
    if len(sys.argv) != 3:
        sys.exit("Usage: python program.py <number_of_bitcoins> <currency>")
    
    # Validate the first argument (number of Bitcoins)
    try:
        number_of_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: The number of Bitcoins must be a float.")
    
    # Validate the second argument (currency)
    valid_currencies = {"GBP", "USD", "EUR"}
    currency = sys.argv[2].upper()
    if currency not in valid_currencies:
        sys.exit(f"Error: The currency must be one of {', '.join(valid_currencies)}.")
    
    return number_of_bitcoins, currency

# Function to get the current price of Bitcoin from the API
def get_bitcoin_price(currency):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            json_data = json.loads(data)
            return json_data["bpi"][currency]["rate_float"]
    except urllib.error.URLError:
        sys.exit("Error: Unable to fetch Bitcoin prices from the API.")
    except KeyError:
        sys.exit("Error: Unexpected API response structure.")

# Main program logic
def main():
    # Parse command-line arguments
    number_of_bitcoins, currency = parse_arguments()
    
    # Fetch the current price of Bitcoin in the specified currency
    bitcoin_price = get_bitcoin_price(currency)
    
    # Calculate the total cost
    total_cost = number_of_bitcoins * bitcoin_price
    
    # Output the result formatted to four decimal places with ',' as a thousands separator
    print(f"The cost of {number_of_bitcoins:.4f} Bitcoins in {currency} is: {total_cost:,.4f}")

if __name__ == "__main__":
    main()
