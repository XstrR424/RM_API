import requests

from config import RM_API_URL

def get_characters():
    response = requests.get(RM_API_URL + "/character")
    return response.json()

def get_episodes():
    response = requests.get(RM_API_URL + "/episode")
    return response.json()

def get_locations():
    response = requests.get(RM_API_URL + "/location")
    return response.json()