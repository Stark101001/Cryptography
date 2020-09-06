from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b'Pawan KUmar')
print(token)
r=f.decrypt(token)
print(r)

