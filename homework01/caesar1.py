import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for c in plaintext:
        if (ord(c) <= 64) or (91 <= ord(c) <= 96) or (123 <= ord(c)):
            ciphertext += chr(ord(c))
        elif (97 <= ord(c) + 3 <= 122) or (65 <= ord(c) + 3 <= 90):
            ciphertext += chr(ord(c) + 3)
        else:
            ciphertext += chr(ord(c) + 3 - 26)
     return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for c in ciphertext:

