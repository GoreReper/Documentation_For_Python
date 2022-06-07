import re


def main(text: str) -> dict[str, list[str]]:
    text = text.replace("\n", ' ')
    result = dict()
    data_list = re.findall(r"q\(.*?\)", text)
    keys = re.findall(r"define\s*.*?<", text)
    for n in range(len(keys)):
        keys[n] = keys[n].replace('define', '')
        keys[n] = keys[n].replace(' ', '').replace('<', '')
        data_list[n] = data_list[n].replace('q(', '').replace(')', '')
        data_list[n] = data_list[n].replace(' ', '')
        result[keys[n]] = data_list[n]
    return result

text1='{{ do define onle_195<- q(edbile_134). end do define geon_382 <-\n\
q(bile). end do define quus_272 <- q(soama_983). end do define xeer <-\n\
q(lave). end }}'
print(main(text1))
text2 = '{{do define soxe_476 <- q(rerion_849). end do define quonza <-\n\
q(tequti). end do define tira_845<- q(lage). end }}'
print(main(text2))
