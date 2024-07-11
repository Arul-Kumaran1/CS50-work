# faces.py

def convert(a):
    a = a.replace(":)", "🙂")
    a = a.replace(":(", "🙁")
    return a

def main():
    user_input = input("Enter text: ")
    converted_text = convert(user_input)
    print("Converted text:", converted_text)

main()
