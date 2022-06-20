caesar = input("Enter a message: ")
distanceValue = int(input("Enter the distance value: "))
plain = ""
for x in caesar:
    plain += chr(ord(x)+distanceValue)
print(""+plain)

