import argparse
import sys
import generator
import crypto


def parseArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="RSA Encryption, decryption algorithm")
    parser.add_argument("-d", "--enable-debug", action="store_true")

    subparsers = parser.add_subparsers(title="action", dest='command')

    parser_generator = subparsers.add_parser(name="generate", add_help=False, help="Generate public and private key-pair")
    parser_generator.add_argument("-s", "--key-size", type=int, help="Tamaño de la llave", choices=[512, 1024, 2048], required=True)

    encrypter_parser = subparsers.add_parser(name="encrypt", add_help=False, help="Encrypt a file using a private or a public key")
    encrypter_parser.add_argument("-k", "--key", required=True)
    encrypter_parser.add_argument("-f", "--filename", help="Input file", required=True)
    encrypter_parser.add_argument("-o", "--output", help="Output file", required=True)

    decrypter_parser = subparsers.add_parser(name="decrypt", add_help=False, help="Decrypt a file using a private or a public key")
    decrypter_parser.add_argument("-k", "--key", required=True)
    decrypter_parser.add_argument("-f", "--filename", help="Input file")
    decrypter_parser.add_argument("-o", "--output", help="Output file")


    return parser.parse_args(args=None if sys.argv[1:] else ['--help'])

def action(args: argparse.Namespace):
    act = args.command
    if act == "generate":
        generator.generate_keys(args.key_size/2, args.enable_debug)
    elif act == "encrypt":
        crypto.encrypt(args.filename, args.key, args.output, args.enable_debug)
    elif act == "decrypt":
        crypto.decrypt(args.filename, args.key, args.output, args.enable_debug)


def main():
    args = parseArgs()
    action(args)


if __name__ == '__main__':
    main()