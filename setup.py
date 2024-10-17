from cx_Freeze import setup, Executable

icon_path = "cadenas.ico"

setup(
    name = "vigenere_cypher",
    version = "0.1",
    description = "Encryption et Decryption Vigenere",
    executables = [Executable("vigenere.py", icon = icon_path)]
)