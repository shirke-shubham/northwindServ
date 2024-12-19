import requests
import json
import argparse

def fetch_suppliers(northwind_url, output_file):
    try:
        response = requests.get(northwind_url, headers={"Accept": "application/json"})
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        suppliers = data.get('value', [])  # Extract the suppliers

        with open(output_file, 'w') as file:
            json.dump(suppliers, file, indent=4)

        print(f"Supplier data has been written to {output_file}")
    except Exception as e:
        print(f"Error fetching supplier data: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--northwind_url', type=str, required=True, help='Northwind OData Service URL')
    parser.add_argument('--output_file', type=str, required=True, help='Output JSON file path')
    args = parser.parse_args()

    fetch_suppliers(args.northwind_url, args.output_file)
