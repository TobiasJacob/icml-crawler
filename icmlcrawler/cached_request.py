#%%
import os
import requests
from bs4 import BeautifulSoup
import hashlib

cache_folder = "cache"

# create cache folder at module import
os.makedirs(cache_folder, exist_ok=True)

def cached_request(url: str) -> str:
    """Creates a cached request for a given url.

    Args:
        url (str): url to request.

    Returns:
        str: html of the requested url.
    """
    cache_file = hashlib.sha512(bytes(url, "utf-8")).hexdigest() + ".html"
    path = os.path.join(cache_folder, cache_file)
    if os.path.exists(path):
        with open(path, "r") as f:
            page_text = f.read()
    else:
        page_text = requests.get(url).text
        with open(path, "w") as f:
            f.write(page_text)
    soup = BeautifulSoup(page_text, "html.parser")
    return soup

# %%
# cached_request("https://nips.cc/Conferences/2021/AcceptedPapersInitial")
