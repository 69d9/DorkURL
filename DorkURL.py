import time
from duckduckgo_search import DDGS
from colorama import Fore
import random

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
        /-.--' .-\  
   ,--./    ---'    \,--. 
   \   |(  )     (  )|   /  
hjw \  |         |  /  
97  \ | /|\     /|\ | /  
     /  \-._     _,-/  \  
    //| \  ---'  // |\\  
   /,-.,-.\       /,-.,-.\  
  o   o   o      o   o    o  
"""
    print(logo.format(Fore.YELLOW))  # Apply yellow color for logo text

# Get links
def search_links(dork, country_code):
    query = f"{dork} site:{country_code}"
    with DDGS() as ddgs:
        search_results = ddgs.text(query, max_results=50)
    return search_results

# Run the tool
def main():
    try:
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
