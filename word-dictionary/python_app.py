from PyDictionary import PyDictionary


dictionary = PyDictionary()

while True:
    word = input("Enter your word: ")
    if word == "":
        break

    print(dictionary.printMeanings(word))

    # Print dictionary formating
    print(dictionary.getMeanings(word))
