#hope it works :)
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

# Function to load dorks from a file and generate URLs
def load_dorks(filename, prefix, suffix=''):
    with open(filename) as wordlist:
        return [prefix.format(website, line, suffix) for line in wordlist]

# Prompt user for website
website = input("Enter Website: ")

# Prompt user for dork selection
print("Dork Selection:")
print("1. GitHub")
print("2. Google")
print("3. Both")
selection = input("Enter your choice (1, 2, or 3): ")

# Load dorks based on user selection
if selection == '1':
    print("======GITHUB DORKS STARTING======")
    github_urls = load_dorks('githubdorks.txt', "https://github.com/search?q={}{line}{}",
                             "&s=indexed&type=Code")
    urls = github_urls
elif selection == '2':
    print("======GOOGLE DORKS STARTING======")
    google_urls = load_dorks('googledorks.txt', "https://www.google.com/search?q=site:{}{}")
    urls = google_urls
else:
    print("======GITHUB DORKS STARTING======")
    github_urls = load_dorks('githubdorks.txt', "https://github.com/search?q={}{line}{}",
                             "&s=indexed&type=Code")
    print("======GOOGLE DORKS STARTING======")
    google_urls = load_dorks('googledorks.txt', "https://www.google.com/search?q=site:{}{}")
    urls = github_urls + google_urls

# Check URLs and save results
results = []

# Check URLs with loading animation
print("\nChecking URLs...")
with tqdm(total=len(urls), unit='URL', ncols=80, dynamic_ncols=True) as pbar:
    start_time = time.time()
    for i, url in enumerate(urls):
        if check_url(url):
            results.append(url)
        time.sleep(0.1)  # Add a small delay for smoother animation
        pbar.update(1)
        progress_percentage = (i + 1) / len(urls) * 100
        if progress_percentage % 5 == 0:
            # Save the results to result.txt every 5%
            with open('result.txt', 'w') as file:
                file.write('\n'.join(results))
        elapsed_time = time.time() - start_time
        remaining_time = (elapsed_time / (i + 1) * (len(urls) - (i + 1))) - elapsed_time
        pbar.set_postfix({'Elapsed Time': f'{elapsed_time:.1f}s', 'Remaining Time': f'{remaining_time:.1f}s'})

# Save the final results to result.txt
with open('result.txt', 'w') as file:
    file.write('\n'.join(results))

print("\n======DORKS CHECKING ENDED======")
