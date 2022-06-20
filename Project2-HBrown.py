caecar = input("Enter secret text: ")
distanceValue = int(input("Enter the distance value: "))
plain = ""
for ch in caecar:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distanceValue
    plain += chr(cipherValue)
print(plain)
