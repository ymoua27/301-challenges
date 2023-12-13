#!/usr/bin/env python3
# Script:                       Creat python script to prompt user to select HTTP method
# Author:                       Yue Moua
# Date of latest revision:      12/12/2023
# Purpose:                      Python Request

import requests

def get_user_input():
    url = input("Enter the destination URL: ")
    return url

def print_menu():
    print("\nHTTP Method Menu:")
    print("1. GET")
    print("2. POST")
    print("3. PUT")
    print("4. DELETE")
    print("5. HEAD")
    print("6. PATCH")
    print("7. OPTIONS")
    print("0. Exit")

def get_http_method_choice():
    while True:
        print_menu()
        choice = input("Choose an option (0-7): ")

        if choice.isdigit() and 0 <= int(choice) <= 7:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 0 and 7.")

def print_request_info(url, http_method):
    print(f"\nPreparing to send {http_method} request to: {url}")
    confirmation = input("Do you want to proceed? (y/n): ").lower()
    
    if confirmation != 'y':
        print("Request aborted.")
        exit()

def send_request(url, http_method):
    try:
        if http_method == 'GET':
            response = requests.get(url)
        elif http_method == 'POST':
            response = requests.post(url)
        elif http_method == 'PUT':
            response = requests.put(url)
        elif http_method == 'DELETE':
            response = requests.delete(url)
        elif http_method == 'HEAD':
            response = requests.head(url)
        elif http_method == 'PATCH':
            response = requests.patch(url)
        elif http_method == 'OPTIONS':
            response = requests.options(url)
        else:
            print("Invalid HTTP Method.")
            exit()
        return response
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        exit()

def translate_status_code(status_code):
    status_codes = {
    100: "Continue",
    101: "Switching Protocols",
    200: "OK",
    201: "Created",
    202: "Accepted",
    204: "No Content",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    304: "Not Modified",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
}


    translated_status = status_codes.get(status_code, "Unknown Status Code")
    return f"Status Code: {status_code} - {translated_status}"

def print_response_info(response):
    print("\nResponse Header Information:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    translated_status = translate_status_code(response.status_code)
    print(translated_status)

if __name__ == "__main__":
    destination_url = get_user_input()

    while True:
        choice = get_http_method_choice()
        if choice == 0:
            print("Exiting the program.")
            break

        http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']
        http_method = http_methods[choice - 1]

        print_request_info(destination_url, http_method)
        response = send_request(destination_url, http_method)
        print_response_info(response)


        # REF
        # https://github.com/codefellows/seattle-ops-301d14/blob/main/class-12/challenges/README.md
        # https://realpython.com/python-requests/#getting-started-with-requests
        # https://chat.openai.com/share/886eed87-956e-41df-9cc3-6021c9e02e5f