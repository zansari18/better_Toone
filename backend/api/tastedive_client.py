import requests
import os
import urllib.parse  # new import

API_KEY = os.getenv("TASTEDIVE_API_KEY")
BASE_URL = "https://tastedive.com/api/similar"

def search_tastedive(query, media_type):
    """
    Query TasteDive for a given search term and type.
    media_type can be: 'music', 'movies', 'shows', 'books', 'authors', etc.
    """
    safe_query = urllib.parse.quote(query)  # make the query URL-safe

    params = {
        "q": safe_query,
        "type": media_type,
        "k": API_KEY,
        "limit": 10  # number of results
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()
