
import csv
import webbrowser
import random

file_path = "/Users/vsolis/Desktop/BING/webs.csv"
urls_count = 25

def open_random_websites_from_csv(file_path, num_urls=urls_count):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            urls = [url for row in reader for url in row]
            random_urls = random.sample(urls, min(num_urls, len(urls)))
            for url in random_urls:
                webbrowser.open(url)
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

if __name__ == "__main__":
    open_random_websites_from_csv(file_path)
