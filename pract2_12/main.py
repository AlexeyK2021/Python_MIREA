def replace(text):
    edited_text = ""
    for i in range(0, len(text)):
        if text[i] == '"' and text[i + 1].isalpha():
            edited_text += '«'
        elif text[i] == '"' and text[i - 1].isalpha():
            edited_text += '»'
        else:
            edited_text += text[i]
    return edited_text


if __name__ == "__main__":
    print(*replace(input("Enter text:\n")), sep="")
