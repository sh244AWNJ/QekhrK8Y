# 代码生成时间: 2025-10-18 17:39:06
import requests
from requests.exceptions import RequestException

class SocialMediaManager:
    """
    A class to manage social media accounts using the Requests framework.
    This class is designed to be easily extended and maintained.
    """

    def __init__(self, base_url):
        """
        Initialize the SocialMediaManager with a base URL.
        :param base_url: The base URL for the social media API.
        """
        self.base_url = base_url

    def post_update(self, message):
        """
        Post an update to the social media account.
        :param message: The message to be posted.
        :return: A boolean indicating success or failure.
        """
        try:
            url = f"{self.base_url}/posts"
            response = requests.post(url, json={'message': message})
            response.raise_for_status()
            return True
        except RequestException as e:
            print(f"An error occurred: {e}")
            return False

    def get_updates(self, limit=10):
        """
        Retrieve recent updates from the social media account.
        :param limit: The maximum number of updates to retrieve.
        :return: A list of update dictionaries.
        """
        try:
            url = f"{self.base_url}/posts?limit={limit}"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f"An error occurred: {e}")
            return []

# Example usage:
if __name__ == '__main__':
    manager = SocialMediaManager('https://api.example.com')
    success = manager.post_update('Hello, world!')
    if success:
        print('Update posted successfully.')
    else:
        print('Failed to post update.')

    updates = manager.get_updates(limit=5)
    print('Recent updates:', updates)