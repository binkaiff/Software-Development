responses = {
    "yes": "You are on the right course",
    "no": "You might change your mind"
}

res = input("Do you like Python? (yes/no): ").lower()

message = responses.get(res, "I did not understand")
print(message)
