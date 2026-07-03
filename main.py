# from tranliterator import cyrillic_to_latin, latin_to_cyrillic


# def main():
#     print("Avar Cyrillic -> Avar Latin")
#     print("Choose mode:\n1.Latin to Cyrillic\n2.Cyrillic to Latin")
#     choise=int(input())
#     print("Type 'exit' to exit\n")

#     while True:
#         if choise == 1:
#             text = input("Avar Latin: ")
#             if text.lower() == "exit":
#                 break
#             print("Cyrillic :", latin_to_cyrillic(text))
#             print()
#         elif choise == 2:
#             text = input("Avar Cyrillic: ")
#             if text.lower() == "exit":
#                 break
#             print("Latin :", cyrillic_to_latin(text))
#             print()
#         else:
#             print("Wrong input!\nTry again")
#             choise = int(input())

# if __name__ == "__main__":
#     main()