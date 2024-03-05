import pdfkit
import requests


def url_to_pdf(url, output_filename):

    response = requests.get(url)
    if response.status_code == 200:

        pdfkit.from_string(response.text, output_filename)
        print(f"PDF successfully created as '{output_filename}'")
    else:
        print("Failed to fetch the webpage")


# Example usage
url = "https://sf.streetsblog.org/2013/01/31/advocates-call-on-gov-brown-to-prioritize-biking-walking-in-state-budget"  # Replace this with the URL you want to convert
output_filename = "article.pdf"  # The name of the PDF file you want to create
url_to_pdf(url, output_filename)
