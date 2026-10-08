import time
import random
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from urllib.parse import urlparse, parse_qs, unquote

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X)",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
    ]
    return random.choice(user_agents)

class printer:
    @staticmethod
    def success(msg):
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} {msg}")
    
    @staticmethod
    def error(msg):
        print(f"{Fore.RED}[-]{Style.RESET_ALL} {msg}")
    
    @staticmethod
    def info(msg):
        print(f"{Fore.CYAN}[i]{Style.RESET_ALL} {msg}")

class timer:
    @staticmethod
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            printer.info(f"Finished in {end - start:.2f} seconds.")
            return result
        return wrapper

class Search:
    @timer.timer
    def __init__(self, query) -> None:
        self.query = query.strip()
        if not self.query:
            printer.error("No query provided!")
            return

        url = f"https://duckduckgo.com/html/?q={self.query}"
        self.headers = {
            "User-Agent": get_random_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://duckduckgo.com/"
        }

        try:
            response = self.send_request(url)
            if response:
                self.parse_and_print_results(response.text)
            else:
                printer.error("No response received.")
        except requests.exceptions.RequestException as e:
            printer.error(f"Error: {e}")
        except KeyboardInterrupt:
            printer.error("Cancelled..!")

    def send_request(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException:
            return None

    def parse_and_print_results(self, response_text):
        soup = BeautifulSoup(response_text, "html.parser")
        results = soup.find_all("div", {"class": "result__body"})

        if not results:
            printer.error(f"No results found for '{self.query}'!")
            return

        printer.info(f"Searching for: {Style.BRIGHT}{self.query}{Style.RESET_ALL} [{self.headers['User-Agent']}]")

        for result in results:
            self.print_search_result(result)

    def print_search_result(self, result):
        title_tag = result.find("a", {"class": "result__a"})
        if not title_tag:
            return

        title = title_tag.text.strip()
        raw_link = title_tag.get("href", "").strip()

        parsed = urlparse(raw_link)
        if 'uddg' in parse_qs(parsed.query):
            link = unquote(parse_qs(parsed.query)['uddg'][0])
        else:
            link = raw_link

        status = self.get_status_code(link)

        printer.success(f"{Style.BRIGHT}{title}{Style.RESET_ALL} : {link} \t[{status}]")

    def get_status_code(self, url):
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            return response.status_code
        except requests.exceptions.RequestException:
            return "?"

def start_search():
    try:
        query = input(f"{Fore.CYAN}Enter your DuckDuckGo search query: {Style.RESET_ALL}")
        Search(query)
    except KeyboardInterrupt:
        printer.error("Interrupted by user.")

if __name__ == "__main__":
    start_search()
