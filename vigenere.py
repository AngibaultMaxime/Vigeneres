import time
import unicodedata

def remove_accents(text):
    normalized_text = unicodedata.normalize('NFD', text)
    return ''.join(c for c in normalized_text if unicodedata.category(c) != 'Mn')

def clearTerminal():
    from os import system     # Utilisé pour appeler os.system('cls')
    system('cls')

def showOptions():
    print("1/ Encrypter")
    print("2/ Décrypter")
    print("3/ Encrypter à partir du fichier 'input.txt'")
    print("4/ Décrypter à partir du fichier 'input.txt'")
    print("5/ Quitter")
    

def getUserInputOption():
    validEntries = ['1', '2', '3', '4', '5']
    while True:
        userInput = input("Choisissez votre option [1-5]: ")
        if userInput in validEntries:
            return userInput
        print("Entrée invalide, veuillez réessayer")

def getUserText():
    return remove_accents(input("Texte à encrypter/décrypter: "))

def getUserKey():
    return remove_accents(input("Veuillez entrer la clé: "))

# Si la clé est 'A' alors rien ne change (car 'A' = 0). Si on veut que 'A' = 1 alors voir fonctions Base1.
# Par défault le code de vigeneres est implémente avec A = 0 (exemple: dCode).
# Possibilité de fusionner vegenereEncryption(...) et vigenereDecryption(...) en 1 seule fonction: vigenereCypher(text, key, mode) avec mode = "encrypt" ou mode = "decrypt"
def vigenereEncryption(text, key):
    encryptedText = ''
    keyIndex = 0
    for char in text:
        shift = ord('A') if char.isupper() else ord('a')
        if char.isalpha():
            newChar = chr((((ord(char) - shift) + ((ord(key[keyIndex].upper()) - ord('A')))) % 26) + shift)
            while True:
                keyIndex = (keyIndex + 1) % len(key)
                if key[keyIndex].isalpha():
                    break
        else:
            newChar = char
        encryptedText += newChar
    return encryptedText

def vigenereDecryption(text, key):
    decyptedText = ''
    keyIndex = 0
    for char in text:
        shift = ord('A') if char.isupper() else ord('a')
        if char.isalpha():
            newChar = chr((((ord(char) - shift) - ((ord(key[keyIndex].upper()) - ord('A')))) % 26) + shift)
            while True:
                keyIndex = (keyIndex + 1) % len(key)
                if key[keyIndex].isalpha():
                    break
        else:
            newChar = char
        decyptedText += newChar
    return decyptedText

# Si la clé est 'A' alors le décalage est de 1.
# def vigenereEncryptionBase1(text, key):
#     result = ''
#     keyIndex = 0
#     for char in text:
#         shift = ord('A') if char.isupper() else ord('a')
#         if char.isalpha():
#             newChar = chr((((ord(char) - shift) + 1 + (ord(key[keyIndex].upper()) - ord('A') ) + 1) % 26) + shift - 1)
#             keyIndex = (keyIndex + 1) % len(key)
#         else:
#             newChar = char
#         result += newChar
#     return result

# def vigenereDecryptionBase1(text, key):
#     result = ''
#     keyIndex = 0
#     for char in text:
#         shift = ord('A') if char.isupper() else ord('a')
#         if char.isalpha():
#             newChar = chr(((((ord(char) - shift) + 1) - ((ord(key[keyIndex].upper()) - ord('A') ) + 1)) % 26) + shift - 1)
#             keyIndex = (keyIndex + 1) % len(key)
#         else:
#             newChar = char
#         result += newChar
#     return result
  
def encryptFromFile():
    try:
        with open("input.txt", "r") as inputFile:
            fileText = remove_accents(inputFile.read())
    except FileNotFoundError:
        print("ERREUR! Le fichier est introuvable.\n")
        return
    userKey = getUserKey()
    result = vigenereEncryption(fileText, userKey)
    with open("output.txt", "w") as outputFile:
        outputFile.write(result)
    print("Encryption terminée.\n")

def decryptFromFile():
    try:
        with open("input.txt", "r") as inputFile:
            fileText = remove_accents(inputFile.read())
    except FileNotFoundError:
        print("ERREUR! Le fichier est introuvable.\n")
        return
    userKey = getUserKey()
    result = vigenereDecryption(fileText, userKey)
    with open("output.txt", "w") as outputFile:
        outputFile.write(result)
    print("Decryption terminée.\n")

def main():
    while True:
        showOptions()
        userInputOption = getUserInputOption()
        clearTerminal()

        if userInputOption == '1':
            print("1/ Encrypter")
            userText = getUserText()
            userKey = getUserKey()
            print(f"\nRésultat:\n{vigenereEncryption(userText, userKey)}\n")
        elif userInputOption == '2':
            print("2/ Décrypter")
            userText = getUserText()
            userKey = getUserKey()
            print(f"\nRésultat:\n{vigenereDecryption(userText, userKey)}\n")
        elif userInputOption == '3':
            print("3/ Encrypter à partir du fichier 'input.txt'")
            encryptFromFile()
        elif userInputOption == '4':
            print("4/ Décrypter à partir du fichier 'input.txt'")
            decryptFromFile()
        else:
            print("5/ Quitter")
            print("Au revoir.")
            time.sleep(2)
            break

if __name__ == "__main__":
    main()
