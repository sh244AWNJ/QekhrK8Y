# 代码生成时间: 2025-10-23 03:06:40
import requests

class CharacterAnimationSystem:
    """
    A class to handle character animations using the requests framework.
    This system is designed to be easily understandable, maintainable,
    and extensible. It includes error handling and proper documentation.
    """

    def __init__(self, base_url):
        """
        Initialize the CharacterAnimationSystem with a base URL.
        :param base_url: The base URL for the animation API.
        """
        self.base_url = base_url

    def load_animation(self, character_id, animation_id):
        """
        Load an animation for a given character.
        :param character_id: The ID of the character.
        :param animation_id: The ID of the animation.
        :return: A response object from the requests library.
        """
        try:
            url = f"{self.base_url}/characters/{character_id}/animation/{animation_id}"
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

    def play_animation(self, character_id, animation_id):
        """
        Play an animation for a given character.
        :param character_id: The ID of the character.
        :param animation_id: The ID of the animation.
        :return: A response object from the requests library.
        """
        try:
            url = f"{self.base_url}/characters/{character_id}/animation/{animation_id}/play"
            response = requests.post(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

    def stop_animation(self, character_id, animation_id):
        """
        Stop an animation for a given character.
        :param character_id: The ID of the character.
        :param animation_id: The ID of the animation.
        :return: A response object from the requests library.
        """
        try:
            url = f"{self.base_url}/characters/{character_id}/animation/{animation_id}/stop"
            response = requests.post(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

# Example usage:
if __name__ == "__main__":
    base_url = "http://example.com/api"  # Replace with the actual API base URL
    character_system = CharacterAnimationSystem(base_url)
    character_id = "123"
    animation_id = "456"
    
    # Load an animation
    response = character_system.load_animation(character_id, animation_id)
    if response:
        print("Animation loaded successfully.")
        print(response.json())
    
    # Play an animation
    response = character_system.play_animation(character_id, animation_id)
    if response:
        print("Animation played successfully.")
        print(response.json())
    
    # Stop an animation
    response = character_system.stop_animation(character_id, animation_id)
    if response:
        print("Animation stopped successfully.")
        print(response.json())