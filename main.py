import csv
import webbrowser
import random

file_path = "/Users/vsolis/Desktop/BING/"
file_name = "URLS.csv"  # Corrected the typo
file_combine_name = file_path + file_name
urls_count = 25

def open_random_websites_from_csv(file_combine_name, num_urls=urls_count):
    try:
        with open(file_combine_name, 'r') as file:
            reader = csv.reader(file)
            urls = [url for row in reader for url in row]
            if not urls:
                print("The CSV file is empty.")
                return
            random_urls = random.sample(urls, min(num_urls, len(urls)))
            for url in random_urls:
                webbrowser.open(url)
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except ValueError:
        print("Not enough URLs in the file to sample from.")

if __name__ == "__main__":
    open_random_websites_from_csv(file_combine_name)

