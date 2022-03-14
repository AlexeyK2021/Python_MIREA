from itertools import groupby


def rle_encode(data):
    return [(k, len(list(g))) for k, g in groupby(data)]


def encrypt(text):
    l = len(text)
    word_num = 0
    arr = [""] * l
    for i in range(l):
        arr[i] = text[i:l] + text[0:i]
    # return arr

    arr.sort()
    for i in range(l):
        if arr[i] == text:
            word_num = i

    encrypted_phrase = ""
    for i in range(l):
        encrypted_phrase += arr[i][-1]
    return encrypted_phrase, word_num


def decrypt(encrypted_phrase, word_num):
    l = len(encrypted_phrase)
    arr = [""] * l
    for i in range(l):
        for j in range(l):
            new_text = encrypted_phrase[j] + arr[j]
            arr[j] = new_text
        arr.sort()
    return arr[word_num]


if __name__ == "__main__":
    text_ = "ABACABA"
    print(*rle_encode(text_))
    text, key = encrypt(text_)
    print(f"Encrypted text: {text}, key: {key}")
    print(*rle_encode(text))

    decrypted_text = decrypt(text, key)
    print(f"Decrypted text: {decrypted_text}")
