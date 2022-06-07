import re


def main(string):
    s = string.replace("\n", "")
    d = dict()
    li = []

    li_flag = ""
    while li_flag is not None:
        entry = re.search('{(.*?)}', s).group(1).replace("''", "")
        li.append(entry)
        s = s.split('.', 1)[1]
        li_flag = re.search('{(.*?)}', s)

    for i in range(len(li)):
        current_entry = li[i]
        d_flag = ""
        while d_flag is not None:
            key = re.search(r'opt.?"(.*?)"', current_entry).group(1)
            value = re.search("'(.*?)'", current_entry).group(1)
            d.setdefault(key, value)
            current_entry = current_entry.replace(value, "")
            current_entry = current_entry.replace("''", "")
            d_flag = re.search("'(.*?)'", current_entry)

    return d


if __name__ == "__main__":
    sentence = 'do { opt "soedat"\'tedima\'.}, {opt "xera" \'belare\'. }, end'

    print(main(sentence))
