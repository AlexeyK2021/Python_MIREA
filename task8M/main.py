def main(text):
    result = {}
    text = text.replace("\n", " ")
    data = text.split('end')
    for str in data:
        if str.find(">>") == -1:
            result[str[str.find('opt ') + 4:str.rfind('list') - 1]] = \
                str[str.find("list(") + 5:str.find(").")]\
                .replace(" ", "")\
                .split(".")
    return result


if __name__ == "__main__":
    print(main(
        "<< do opt inxe_39 list( orge . veon). end do opt mala list( biin .\naza_679 . tedi . rean ). end >>"))
    print(main("<<do opt teer_701 list(quma_99 . orra ). end do opt ate_190 list( soce\n. quonan . erlexe_22 . edmati ). end>>"))
