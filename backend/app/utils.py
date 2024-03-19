import pandas as pd
from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up the provider (Alchemy URL)
alchemy_api_url = os.getenv('ALCHEMY_API_URL')
w3 = Web3(Web3.HTTPProvider(alchemy_api_url))

# Print if web3 is successfully connected
print(w3.is_connected())

# NFT contract details
contract_address = Web3.toChecksumAddress('0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d')

contract_abi = [...]
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

token_id = 1  # Replace with the actual token ID
owner = contract.functions.ownerOf(token_id).call()

print(f'The owner of token ID {token_id} is {owner}')


import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Your Etherscan API Key
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')

def get_top_nft_contracts():
    currentData = pd.read_csv('data/nft_data.csv')

    # check all elements in x2y2
    listItemXpath = f"//*[@id=\"__next\"]/div[1]/section/ul/li/div[1]/div/div[1]/a"
    collection = requests.get("https://x2y2.io/collections")

    # search xpath within collection
    # save all links

    # for every link, open a new request and get the contract id
    # get abi on etherscan
    # append new data to currentData


def get_contract_abi(contract_address):
    url = f"https://api.etherscan.io/api"
    params = {
        "module": "contract",
        "action": "getabi",
        "address": contract_address,
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(url, params=params)
    response_json = response.json()
    if response_json['status'] == '1':
        return response_json['result']
    else:
        raise Exception(f"Error fetching contract ABI: {response_json['message']}")


# Example contract address
contract_address = '0x...'

# Fetch the ABI
contract_abi = get_contract_abi(contract_address)
print(contract_abi)
