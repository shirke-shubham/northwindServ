import requests

def fetch_suppliers():
    # OData Service URL
    url = "https://11f3cbectrial-dev-demo-ai-srv.cfapps.us10-001.hana.ondemand.com/odata/v4/ideal-rga-srv/Rga_Header?$format=json"

    try:
        # Send GET request to fetch supplier data
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors

        # Parse JSON response
        data = response.json()
        suppliers = response.get("value", [])

        # Display supplier data
        print("Supplier Data:")
        for supplier in suppliers:
            print("ID: {supplier['SupplierID']}, Name: {supplier['CompanyName']}, Country: {supplier['Country']}")
            # print("ID: {supplier[1]}")

    except Exception as e:
        print(f"Error fetching supplier data: {e}")

if __name__ == "__main__":
    fetch_suppliers()
