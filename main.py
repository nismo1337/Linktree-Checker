import requests
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("github.com/nismo1337 | nismo#1337 | t.me/nismo1337")

url = "https://linktr.ee/%s"

with open("usernames.txt", "r") as file:
    usernames = file.read().splitlines()

checked_usernames = set()

while True:
    for username in usernames:
        if username in checked_usernames:
            continue

        response = requests.get(url % username)

        if response.status_code == 404:
            with open("available_usernames.txt", "a") as output_file:
                output_file.write(username + "\n")
                
            print(f"Username available: {username}")

        checked_usernames.add(username)

    time.sleep(10)
