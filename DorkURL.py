import time
from duckduckgo_search import DDGS
from colorama import Fore, Style
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
    print(Style.RESET_ALL)

# List of proxies
proxies_list = [
    "208.89.96.91:10288",
    "194.87.244.67:8080",
    "188.164.199.34:5011",
    "185.31.117.48:1080",
    "180.254.145.27:1080",
    "178.141.210.200:7788",
    "178.44.195.157:7788",
    "178.44.38.156:7788",
    "178.44.30.188:7788",
    "171.224.90.227:20029",
    "171.224.90.227:20027",
    "171.224.90.227:20026",
    "115.74.10.48:20027",
    "115.74.10.48:20024",
    "115.74.8.201:20019",
    "114.238.39.118:8989",
    "105.214.109.70:5678",
    "105.214.96.99:1080",
    "105.214.30.173:1080",
    "103.3.246.97:31743",
    "101.109.12.227:4153",
    "98.188.47.150:4145",
    "98.178.72.21:10919",
    "98.175.31.222:4145",
    "94.182.199.249:8080",
    "93.183.89.191:12543"
]

# Get links
def search_links(dork, country_code):
    query = f"{dork} site:{country_code}"
    try:
        with DDGS(proxies={"http": random.choice(proxies_list), "https": random.choice(proxies_list)}) as ddgs:
            search_results = []
            for result in ddgs.text(query, max_results=50):
                search_results.append(result)
                time.sleep(1)  # تأخير لمدة ثانية لتجنب الحظر
        return search_results
    except Exception as e:
        print(Fore.RED + f"[!] Error during search: {e}")
        return []

# Run the tool
def main():
    try:
        print_logo()  # Print the logo
        dork = input(Fore.CYAN + "Enter the Dork: ")  # Search query
        country = input(Fore.CYAN + "Enter the Country code (il, sa, eg, us, uk) or press Enter for random: ")  # Country code

        # If no country code is entered, choose a random one
        if not country:
            country = random.choice(['il', 'sa', 'eg', 'us', 'uk'])
            print(Fore.YELLOW + f"[!] No country code provided. Using random: {country}")

        results = search_links(dork, country)

        if results:
            print(Fore.GREEN + "\n[+] Found the following links:")
            for idx, res in enumerate(results, 1):
                print(Fore.GREEN + f"[{idx}] {res['href']}")
            print(Fore.GREEN + f"\n[+] Total links found: {len(results)}")
        else:
            print(Fore.RED + "[!] No results found.")
        
        time.sleep(3)  # Add a delay of 3 seconds to avoid hitting rate limits
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Execution stopped by user. Exiting...")
    except Exception as e:
        print(Fore.RED + f"[!] An unexpected error occurred: {e}")
    finally:
        print(Style.RESET_ALL)

# Entry point
if __name__ == "__main__":
    main()
