import sys
import socket
import requests
import json

# Function to get the IP address of a website
def get_ip_address(website):
    try:
        ip = socket.gethostbyname(website)
        return ip
    except socket.gaierror:
        print(f"Error: Unable to resolve {website}")
        sys.exit(1)

# Function to get the location information from ipinfo.io
def get_location_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        return response.json()
    except requests.RequestException as e:
        print(f"Error: Unable to fetch data from ipinfo.io. {e}")
        sys.exit(1)

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python infotool.py <websiteurl>")
        sys.exit(1)

    website = sys.argv[1]
    ip = get_ip_address(website)
    location_info = get_location_info(ip)

    # Print the results
    print(f"Website: {website}")
    print(f"IP Address: {ip}")
    print("Location Information:")
    print(f"  City: {location_info.get('city', 'N/A')}")
    print(f"  Region: {location_info.get('region', 'N/A')}")
    print(f"  Country: {location_info.get('country', 'N/A')}")

if __name__ == "__main__":
    main()
