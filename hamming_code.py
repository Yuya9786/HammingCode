import random
import sys

G = [
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 0, 1],
]
H = [
    [1, 1, 0],
    [0, 1, 1],
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
def encode(msg):
    try:
        w = []
        for i in range(7):
            wi = 0
            for j in range(4):
                wi += msg[j] & G[j][i]
            wi %= 2
            w.append(wi)
        return w
    except ValueError:
        print("occured ValueError.")

def decode(msg):
    try:
        s = [0, 0, 0]
        for j in range(3):
            for i in range(7):
                s[j] += msg[i] & H[i][j]
            s[j] %= 2
        print("↓ decode s = {}".format(s))
        if s[0] == 0 and s[1] == 0 and s[2] == 0:
            pass
        else:
            for i in range(7):
                if H[i] == s:
                    msg[i] += 1
                    msg[i] %= 2
                    break
        output = 0
        for i in range(4):
            output += msg[i] * (2 ** (3-i))
        return output
    except ValueError:
        print("occured ValueError.")

def transfer(msg):
    if random.randrange(2) == 0:
        index = random.randrange(7)
        msg[index] += 1
        msg[index] %= 2
    return msg

if __name__ == "__main__":
    args = sys.argv
    try:
        msg = int(args[1])
    except ValueError:
        print("ValueError: The msg must be integer.")
        sys.exit(1)
    except IndexError:
        print("usage: $ python3 hamming_code.py [msg(0 <= msg < 16)]")
        sys.exit(1)

    if msg < 0 or 15 < msg:
        print("The msg must be between 0 and 15.")
        sys.exit(1)
    print("message: {}".format(msg))
    print("↓ encode")

    x = [0, 0, 0, 0]
    for j in range(4):
        x[j] = msg >> (3-j) & 0b1

    encoded_msg = encode(x)
    print("encoded message: {}".format(encoded_msg))
    print("↓ transfer")

    transfered_msg = transfer(encoded_msg)
    print("recieved message: {}".format(transfered_msg))

    decoded_msg = decode(transfered_msg)
    print("decoded message: {}".format(decoded_msg))