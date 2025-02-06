import requests
from bs4 import BeautifulSoup
from langdetect import detect
import deepseek

def fetch_web_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch the webpage. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def compare_texts(text1, text2):
    return text1.lower() in text2.lower()

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

def detect_ai_generated(text):
    deepseek.api_key = "YOUR_DEEPSEEK_API_KEY"
    response = deepseek.check_ai_generated(text)
    return response['ai_detected']

def main():
    url = input("Enter the URL to check for plagiarism: ")
    original_text = input("Enter the original text: ")

    web_content = fetch_web_content(url)
    if web_content is None:
        print("Could not fetch the web content.")
        return

    soup = BeautifulSoup(web_content, 'html.parser')
    page_text = soup.get_text()

    if compare_texts(original_text, page_text):
        print("Plagiarism detected!")
    else:
        print("No plagiarism detected.")

    language = detect_language(original_text)
    print(f"Detected language of the original text: {language}")

    ai_generated = detect_ai_generated(original_text)
    print(f"Is the original text AI-generated? {'Yes' if ai_generated else 'No'}")

if __name__ == "__main__":
    main()
