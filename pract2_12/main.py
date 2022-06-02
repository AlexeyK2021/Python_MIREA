def replace(text):
    edited_text = ""
    quo_times = 0
    for i in range(0, len(text) - 1):
        if text[i] == '"':
            if text[i + 1] == " " and quo_times > 0:
                edited_text += '»'
                quo_times -= 1
            elif text[i + 1] != " " and quo_times <= 0:
                edited_text += '«'
                quo_times += 1
        else:
            edited_text += text[i]
        # if text[i] == '"' and text[i + 1] != " ":
        #     edited_text += '«'
        # elif text[i] == '"' and text[i - 1] != " ":
        #     edited_text += '»'
        # else:
        #     edited_text += text[i]
    return edited_text


if __name__ == "__main__":
    print(*replace(input("Enter text:\n")), sep="")
