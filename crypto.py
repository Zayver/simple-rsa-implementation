def encrypt(filename, key, output, debug = False):
    (key_control, n) = read_key(key)
    with open(filename, "r") as file, open(output, "w") as output:
        for line in file:
            for char in line:
                if debug:
                    print(f"char: {char}, encrypt: {pow(ord(char), key_control, n)}\n")
                output.write(f"{pow(ord(char), key_control, n)}\n")

def decrypt(filename, key, output, debug = False):
    nl = "\n"
    (key_control, n) = read_key(key)
    with open(filename, "r") as file, open(output, "w") as output:
        for line in file:
            if debug:
                print(f"encrypt: {line}, decrypt: {chr(pow(int(line.removesuffix(nl)), key_control, n))}")
            output.write(f"{chr(pow(int(line.removesuffix(nl)), key_control, n))}")

def read_key(key):
    with open(key) as file:
        control = int(file.readline().removesuffix("\n"), 16)
        n = int(file.readline().removesuffix("\n"), 16)
        return control, n
        