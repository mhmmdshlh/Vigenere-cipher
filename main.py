uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

def encryption(plainText, key):
	cipherText = ""
	i = 0
	for char in plainText:
		if char in uppercase:
			idxChar = uppercase.index(char)
			idxKey = uppercase.index(key[i].upper())
			idxCipher = (idxChar + idxKey) % len(uppercase)
			cipherText += uppercase[idxCipher]
			i = (i + 1) % len(key)
		elif char in lowercase:
			idxChar = lowercase.index(char)
			idxKey = lowercase.index(key[i].lower())
			idxCipher = (idxChar + idxKey) % len(lowercase)
			cipherText += lowercase[idxCipher]
			i = (i + 1) % len(key)
		else:
			cipherText += char
	return cipherText

def decryption(text, key):
	plainText = ""
	i = 0
	for char in text:
		if char in uppercase:
			idxChar = uppercase.index(char)
			idxKey = uppercase.index(key[i].upper())
			idxPlain = (idxChar - idxKey) % len(uppercase)
			plainText += uppercase[idxPlain]
			i = (i + 1) % len(key)
		elif char in lowercase:
			idxChar = lowercase.index(char)
			idxKey = lowercase.index(key[i].lower())
			idxCipher = (idxChar + idxKey) % len(lowercase)
			plainText += lowercase[idxCipher]
			i = (i + 1) % len(key)
		else:
			plainText += char
	return plainText
	
def vigenere(text, key, mode):
	if mode == "encryption":
		return encryption(text, key)
	elif mode == "decryption":
		return decryption(text, key)
	else:
		return "Enter the valid mode!"

	
text = input("text : ")
key = input("key : ")
mode = input("mode (encryption/decryption) : ").lower()
print(vigenere(text,key,mode))