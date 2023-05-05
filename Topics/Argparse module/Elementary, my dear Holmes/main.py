import argparse


def decode_caesar_cipher(s):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    n = -13
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)


parser = argparse.ArgumentParser()
parser.add_argument("--file")
args = parser.parse_args()

filename = args.file
opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string
decode_caesar_cipher(encoded_text)
opened_file.close()  # always close the files you've opened
