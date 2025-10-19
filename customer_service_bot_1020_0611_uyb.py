# 代码生成时间: 2025-10-20 06:11:37
import requests

class CustomerServiceBot:
    """
    A simple customer service bot that interacts with an API to resolve customer queries.
    """

    def __init__(self, base_url):
        """
        Initialize the bot with the base URL of the customer service API.
        :param base_url: The base URL of the API
        """
        self.base_url = base_url

    def get_response(self, query):
        """
        Send a query to the API and get the response.
        :param query: The customer's query
        :return: The response from the API
        """
        try:
            # Construct the full URL for the API endpoint
            url = f"{self.base_url}/query"

            # Set up the headers and payload for the request
            headers = {"Content-Type": "application/json"}
            payload = {"query": query}

            # Make the POST request to the API
            response = requests.post(url, headers=headers, json=payload)

            # Check if the request was successful
            response.raise_for_status()

            # Return the response from the API
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            print(f"HTTP error occurred: {http_err}