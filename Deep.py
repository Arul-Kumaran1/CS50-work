a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
a = a.lower()
a = a.strip()
if a == "42" or a == "forty-two" or a == "forty two":
    print("Yes")
else:
    print("No")