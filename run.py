import requests
import time
from tqdm import tqdm

# Function to check if URL is working
def check_url(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# Prompt user for website
website = input("Enter Website: ")

# Load GitHub dorks
print("======GITHUB DORKS STARTING======")
time.sleep(2)

with open('githubdorks.txt') as githubWordlist:
    github_urls = ["https://github.com/search?q=" + website + line + "&s=indexed&type=Code" for line in githubWordlist]

# Load Google dorks
print("======GOOGLE DORKS STARTING======")
time.sleep(2)

with open('googledorks.txt', encoding='cp850') as googleWordlist:
    google_urls = ["https://www.google.com/search?q=site:{}{}".format(website, line) for line in googleWordlist]

# Combine all URLs
urls = github_urls + google_urls

# Check URLs and save results
results = []

# Check URLs with loading animation
print("\nChecking URLs...")
with tqdm(total=len(urls), unit='URL', ncols=80, dynamic_ncols=True) as pbar:
    start_time = time.time()
    for url in urls:
        if check_url(url):
            results.append(url)
        time.sleep(0.1)  # Add a small delay for smoother animation
        pbar.update(1)
        elapsed_time = time.time() - start_time
        remaining_time = (elapsed_time / (len(results) / len(urls))) - elapsed_time
        pbar.set_postfix({'Elapsed Time': f'{elapsed_time:.1f}s', 'Remaining Time': f'{remaining_time:.1f}s'})

# Save the results to result.txt
with open('result.txt', 'w') as file:
    file.write('\n'.join(results))

print("\n======DORKS CHECKING ENDED======")
