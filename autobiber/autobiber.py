import argparse
from utils import execPool, reqSpider
from xml.dom.minidom import parseString

dblp_api = "https://dblp.org/search/publ/api?h=1000&q="
spider = reqSpider()


def alpha(txt):
    return "".join(filter(str.isalpha, txt)).lower()


def bibformat(bib):
    return bib


# make sure title is precise
def getbib(title, nickname=None):
    # search
    bibs = []
    txt = spider.get_raw_txt(dblp_api + title)
    url = ""
    for info in parseString(txt).documentElement.getElementsByTagName("info"):
        if not alpha(title) == alpha(info.childNodes[1].childNodes[0].data):
            continue
        for i in range(len(info.childNodes)):
            if info.childNodes[i].tagName == 'url':
                url = info.childNodes[i].childNodes[0].data
                bib = spider.get_raw_txt(url + ".bib")
                # replace nickname
                if nickname is not None:
                    a, b = bib.index('{') + 1, bib.index(',')
                    bib = bib[:a] + nickname + bib[b:]
                bib = bibformat(bib)
                bibs.append(bib)
    if len(bibs) == 0:
        print(title, 'no find')
    elif len(bibs) > 1:
        print(title, "find many, please choose manually")
    return bibs


def parse_input_file(file: str):
    """
    [line] for txt, [title,nickname] for bib
    :param file:
    :return:
    """
    lines = open(file, 'r', encoding='utf-8').readlines()
    titles = []
    if file.endswith('.txt'):  # every line is title
        for line in lines:
            line=line.replace('\n', '')
            if not ':' in line:
                titles.append([line,alpha(line), ])
                continue
            ls = line.split(':')
            titles.append([ ":".join(ls[1:]),ls[0]])
    elif file.endswith(".bib"):  # search for 'title'
        title, nick = "", ""
        for li, line in enumerate(lines):
            if '@' in line or li == len(lines) - 1:
                if title != "":
                    if nick == "":
                        nick = alpha(title)
                    titles.append([title, nick])
            if '@' in line:
                nick = line[line.index('{') + 1:line.index(',')]
            if 'title' in line and 'booktitle' not in line:
                dat = "".join(lines[li:])
                title = dat[dat.index('{') + 1:dat.index('}')]
    return titles


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, help="path of in.bib", default="")
    parser.add_argument('-o', type=str, help='path of out.bib', default="out.bib")
    parser.add_argument('-t', type=str, help='title of article', default="")
    arg = parser.parse_args()

    if arg.t != "":
        bibs = getbib(arg.t)
        for bib in bibs:
            print(bib + '\n')
        return

    if arg.i != "":
        titles = parse_input_file(arg.i)
    else:
        print("no input")
        return

    bibss = execPool(getbib, titles)
    with open(arg.o, 'w', encoding='utf-8') as f:
        for bibs in bibss:
            for bib in bibs:
                f.write(bib + '\n')


main()
