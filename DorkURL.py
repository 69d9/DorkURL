import time
import random
import subprocess
import sys
from colorama import Fore
from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup
from googlesearch import search

# Function to check and install missing libraries
def install_libraries():
    libraries = ['requests', 'beautifulsoup4', 'googlesearch-python', 'duckduckgo-search']
    for lib in libraries:
        try:
            __import__(lib)
        except ImportError:
            print(Fore.YELLOW + f"Library '{lib}' not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Print the logo
def print_logo():
    logo = r"""
{0}
    Coded By GhosT LulzSec
    Telegram : @WW6WW6WW6
    GitHub: https://github.com/69d9
    All rights reserved.

            o  o   o  o
         |\/ \^/ \/|  
         |,-------.|  
       ,-.(|)   (|),-. 
       \_*._ ' '_.* _/  
        /-.--' .-`\  
   ,--./    `---'    \,--. 
   \   |(  )     (  )|   /  
hjw \  |         |  /  
`97  \ | /|\     /|\ | /  
     /  \-._     _,-/  \  
    //| \  `---'  // |\\  
   /,-.,-.\       /,-.,-.\  
  o   o   o      o   o    o  
"""
    print(logo.format(Fore.YELLOW))  # Apply yellow color for logo text

# DuckDuckGo Search
def search_duckduckgo(dork, country_code):
    query = f"{dork} site:{country_code}"
    with DDGS() as ddgs:
        return ddgs.text(query, max_results=50)

# Google Search (via googlesearch-python)
def search_google(dork, country_code):
    query = f"{dork} site:{country_code}"
    results = []
    for url in search(query, num_results=50):
        results.append({'href': url})
    return results

# Bing Search (using BeautifulSoup)
def search_bing(dork, country_code):
    query = f"{dork} site:{country_code}"
    url = f"https://www.bing.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    results = []
    for link in soup.find_all("a", href=True):
        href = link['href']
        if "http" in href:
            results.append({'href': href})
    
    return results

# Get links from all sources
def search_links(dork, country_code):
    # Try DuckDuckGo first
    try:
        return search_duckduckgo(dork, country_code)
    except Exception as e:
        print("Error with DuckDuckGo:", e)
    
    # If DuckDuckGo fails, try Bing
    try:
        return search_bing(dork, country_code)
    except Exception as e:
        print("Error with Bing:", e)

    # If both DuckDuckGo and Bing fail, try Google
    try:
        return search_google(dork, country_code)
    except Exception as e:
        print("Error with Google:", e)

    return []

# Run the tool
def main():
    try:
        install_libraries()  # Install missing libraries
        print_logo()  # Print the logo
        dork = input("Enter the Dork: ")  # Search query
        country = input("Enter the Country code (il.,.sa, .eg, .OR?) or press Enter for random: ")  # Country code

        # If no country code is entered, choose a random one
        if not country:
            country = random.choice(['il', 'sa', 'eg', 'us', 'uk'])  # List of example country codes

        results = search_links(dork, country)

        if results:
            print(Fore.GREEN + "Found the following links:")  # Apply green color for result header
            for res in results:
                print(Fore.GREEN + res['href'])  # Apply green color for each result
            print(Fore.GREEN + f"Found {len(results)} links.")  # Display the number of links found
        time.sleep(3)  # Add a delay of 3 seconds to avoid hitting rate limits
    except KeyboardInterrupt:
        print("\nExecution stopped by user. Exiting...")

# Entry point
if __name__ == "__main__":
    main()
