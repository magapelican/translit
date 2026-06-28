from tranliterator import cyrillic_to_latin


def main():
    print("Avar Cyrillic -> Avar Latin")
    print("Type 'exit' to exit\n")

    while True:
        text = input("Avar Cyrillic: ")

        if text.lower() == "exit":
            break

        print("Latin :", cyrillic_to_latin(text))
        print()

if __name__ == "__main__":
    main()