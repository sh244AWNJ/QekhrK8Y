# 代码生成时间: 2025-09-23 12:50:32
import requests

class DocumentConverter:
    """
    A simple document converter class that uses an external API to convert documents.
    It can currently handle conversions from PDF to text and from text to PDF.
    """
    def __init__(self, api_url, api_key):
        """
        Initializes the DocumentConverter with the API URL and API key.
        :param api_url: The URL of the document conversion API.
        :param api_key: The API key for authentication with the service.
        """
        self.api_url = api_url
        self.api_key = api_key

    def convert_pdf_to_text(self, file_path):
        """
        Converts a PDF file to text using the external API.
        :param file_path: The path to the PDF file to be converted.
        :return: The text content of the PDF file.
        """
        try:
            with open(file_path, 'rb') as file:
                response = requests.post(
                    self.api_url + '/pdf_to_text',
                    headers={"Authorization": f"Bearer {self.api_key}"},
                    files={'file': file}
                )
                response.raise_for_status()
                return response.text
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def convert_text_to_pdf(self, text, output_path):
        """
        Converts text to a PDF file using the external API.
        :param text: The text to be converted to PDF.
        :param output_path: The path where the PDF file will be saved.
        """
        try:
            response = requests.post(
                self.api_url + '/text_to_pdf',
                headers={"Authorization": f"Bearer {self.api_key}"},
                data={'text': text}
            )
            response.raise_for_status()
            with open(output_path, 'wb') as file:
                file.write(response.content)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Example usage:
    api_url = 'https://api.example.com'
    api_key = 'your_api_key_here'
    converter = DocumentConverter(api_url, api_key)

    # Convert PDF to text
    pdf_text = converter.convert_pdf_to_text('path/to/your/pdf_file.pdf')
    if pdf_text:
        print('PDF to text conversion successful:
', pdf_text)

    # Convert text to PDF
    converter.convert_text_to_pdf('Hello, this is a test.', 'path/to/save/your/text_file.pdf')
    print('Text to PDF conversion successful.')