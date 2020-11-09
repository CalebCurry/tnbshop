from nacl.signing import SigningKey
import requests
import time


def get_balance(address):
    url = f"http://54.183.17.224/accounts/{address}/balance"
    r = requests.get(url)
    balance = r.json().get('balance')
    if balance is None:
        return 0
    else:
        return balance


signing_key = SigningKey.generate()
# don't show this to anyone lol print(bytes(signing_key).hex())
print(bytes(signing_key.verify_key).hex())
# https://stackoverflow.com/questions/57183362/pynacl-printing-privatekey-raw-hex-value
address = bytes(signing_key.verify_key).hex()
# example address #address = "d84543947090d300910f8d1b9604c0c0a56fafca6cfbe52511c1e31757187bac"


cost = 5 - 2
print("Welcome! You weant to buy course")
print("cost =", cost, "tnb")
print("send coins to", address)
print("press any key to confirm")
# input()

balance = get_balance(address)
while balance < cost:
    time.sleep(3)
    balance = get_balance(address)
    print(balance, end=" ")

print()
print("Congrats! What's your email?")
