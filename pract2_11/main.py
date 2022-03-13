def burrows_wheeler(text):
    text_ = "." + text + "."
    l = len(text_)
    arr = [""] * l
    for i in range(len(text) + 2):
        arr[i] = text_[-i:l - i]
    pass


if __name__ == "__main__":
    burrows_wheeler("BANANA")
