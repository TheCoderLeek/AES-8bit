import json

with open("encryption_key.json", "r") as file:
    data = json.load(file)

key = data["key"]

with open("encrypted.json", "r") as file:
    data = json.load(file)

encrypted_data = data["user_files"][0]["files_secrets"]

decrypted_text = ""

for number in encrypted_data:
    decrypted_number = number ^ key
    decrypted_text += chr(decrypted_number)

print(decrypted_text)