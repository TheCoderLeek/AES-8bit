import json
from pprint import pprint 
from random import randint

with open("data.json", "r") as file:     
    data = json.load(file) 

print(data["user_files"][0]["files_secrets"])

text = data["user_files"][0]["files_secrets"]

for character in text:
    number = ord(character)
    binary = format(number, "08b")

    print(character, number, binary)

key = randint(0, 255)

print("Key:", key)
print("Binary:", format(key, "08b"))

decryptionKey_josn = {
    "key": key
}

with open("encryption_key.json", "w") as file:
    json.dump(decryptionKey_josn, file , indent=4)

encrypted_data = []

for character in text:
    number = ord(character)
    encrypted = number ^ key

    encrypted_data.append(encrypted)

print(encrypted_data)

encrypted_json = {
    "user_files": [
        {
            "files_secrets": encrypted_data
        }
    ]
}

with open("encrypted.json", "w") as file:
    json.dump(encrypted_json, file, indent= 4)