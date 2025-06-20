# riot_api.py

import requests
from config import API_KEY, REGION, ROUTING

def get_summoner_data(summoner_name):
    url = f"https://{REGION}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {"X-Riot-Token": API_KEY}
    response = requests.get(url, headers=headers)

    # Debug için log basalım:
    print(">> URL:", url)
    print(">> Headers:", headers)
    print(">> Status:", response.status_code)
    print(">> Response:", response.json())

    return response.json()