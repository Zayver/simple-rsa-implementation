import random
import utils
import math

def generate_keys(size: int, debug = False):
    p = utils.getPrime(size)
    q = utils.getPrime(size)
    
    if debug:
        print(f"P: {p} \n Q: {q}\n\n")

    n = p*q
    if debug:
        print(f"p*q = {n}\n\n")
    phi = (p-1) * (q-1)

    if debug:
        print(f"phi(n) = (p-1) - (q-1) = ({p}-1)*({q-1}) = {phi}\n\n")
    e = 65537
    if debug:
        print(f"Default public exponent: {e}\n\n")
    d = utils.modinv(e, phi)
    if debug:
        print(f"Private exponent: {d}\n\n")
    
    if debug:
        print(f"Private key: ({d}, {n}), Public key: ({e}, {n})\n\n")
    saveKeys(e, n, d)

    
def saveKeys(e, n, d):
    with open("public_key.key", "w") as file:
        file.write(f"{hex(e)}\n")
        file.write(f"{hex(n)}\n")
    with open("private_key.key", "w") as file:
        file.write(f"{hex(int(d))}\n")
        file.write(f"{hex(n)}\n")




