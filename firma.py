# Firma DIgital Usando RSA
# 2025-02-19
# Israel Hernandez
# Anahuac Mayab

# Importamos las librerias
import Crypto.Random
import Crypto.Util.number
import hashlib

# Para 'e' va,ps a isar el numero 4  de Fermat
e = 65537

# calculamos las llaves de Alice 
pA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

nA = pA * qA
print('\n', 'RSA llave publica nAlice: ', nA)

# calculamos las llaves de Bob
# pB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
# qB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

# nB = pB * qB
# print('\n', 'RSA nAlice: ', nB)

# Calcular la llave Privada de Alice
phiaA = (pA - 1) * (qA - 1)

dA = Crypto.Util.number.inverse(e, phiaA)

print('\n', 'Llave privada Alice dA: ', dA)

# Calcular la llave Privada de Bob
# phiaB = (pB - 1) * (qB - 1)

# dB = Crypto.Util.number.inverse(e, phiaB)

# print('\n', 'Llave privada Bob dB: ', dB)

# Firmamos el mensaje

mensaje = "Hola Mundo"
print("\n", "Mensaje: ", mensaje)

# Generamos el HASH del mensaje
hM = int.from_bytes(hashlib.sha256(mensaje.encode('utf-8')).digest(), byteorder='big')
print("\n", "HASH de hM: ", hex(hM))

# Firmamos el HASH usando la llave privada de Alice y se lo enviamos a Bob
sA = pow(hM, dA, nA)
print("\n", "Firma: ", sA)

# Bob Verifica la firma de Alice usando la llave Publica de Alice
hM1 = pow(sA, e, nA)
print("\n", "HASH de hM1: ", hex(hM))

# Verificamos
print("\n", "Firma Valida: ", hM==hM1, "\n")


