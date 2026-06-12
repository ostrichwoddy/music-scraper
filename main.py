import requests
import selectorlib
from dotenv import load_dotenv
import os
import smtplib
import ssl


load_dotenv()
token = os.getenv("EMAIL_TOKEN")
URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """
    Scrape the full page source of the given URL
    """
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def store(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "williambottlebanger@gmail.com"
    password = token

    receiver = "williambottlebanger@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

def read():
    with open("data.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    content = read()
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            send_email("A new event was found")
            print("email function was triggered")