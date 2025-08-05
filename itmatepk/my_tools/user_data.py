
# ! user_data.py
import requests
import rich
from agents import function_tool

@function_tool
def fetch_user_data()->list:
    """
    fetch function for user data and return list.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)
    data = res.json()
    return data

@function_tool
def fetch_user_data(id:int)->list:
    """
    fetch function for user data and return list.
    """
    url = "https://jsonplaceholder.typicode.com/users/${id}"
    res = requests.get(url)
    data = res.json()
    return data
# rich.print(fetch_user_data())