'''Case-study Text-generator
Developers:
Zhambaeva D.(53%), Rashidova A.(48), Ganbat S.(50%)
'''


def open_file():
    file = input('Enter the file name: ')
    while True:
        try:
            with open(file, 'r'):
                pass
        except FileNotFoundError:
            print("File not found")
            file = input('Enter the file name: ')
        else:
            return file

def text_editing(text):
    symbols = '@#$"<>{}^%;»«+*/[]^&'
    for char in symbols:
        text = text.replace(char, "")
    for char in text:
        text = text.replace(' .', ".")
        text = text.replace(' !', "!")
        text = text.replace(' ?', "?")
        text = text.replace(' ,', ",")

    text = text.split()
    return text

def file_read(txt_file):
    with open(txt_file) as f:
        return f.read()

def creat_dict(lst_words):
    d = {}
    words = []
    for i in range(len(lst_words)-1):
        if lst_words[i] not in d:
            for j in range(len(lst_words)-1):
                if lst_words[i] == lst_words[j]:
                    words.append(lst_words[j+1])
            d.update({lst_words[i]: words})
        words = []
    d.update({lst_words[len(lst_words) - 1]: []})
    return d

def generator(num_sent, start, dct_words, stop):
    full_text = ''
    for i in range(num_sent):
        word = start[random.randint(0, len(start) - 1)]
        sent = word
        count = 1
        while count <= 3:
            word = dct_words[word][random.randint(0, len(dct_words[word]) - 1)]
            if word not in stop:
                count += 1
                sent += ' ' + word
            else:
                word = dct_words[word][random.randint(0, len(dct_words[word]) - 1)]
        while count < 20:
            word = dct_words[word][random.randint(0, len(dct_words[word]) - 1)]
            count += 1
            sent += ' ' + word
            if word in stop:
                count = 1
                break
        if count == 20 and word not in stop:
            if sent[-1] == ',':
                sent = sent[:len(sent) - 1]
            sent += '.'
        full_text += sent + ' '
    return full_text


def stop_words(dct_words):
    stop = []
    words = dct_words.keys()
    for word in words:
        if word[-1] == '.' or word[-1] == '!' or word[-1] == '?':
            stop.append(word)
    return stop

def start_words(lst_words):
    start_words = []
    for words in lst_words:
        if words[0].issuper() and words.find('.') == -1:
            start_words.append(words)
        return start_words

def main():
    file = open_file()
    lst_words = text_editing(file_read(file))
    dct_words = creat_dict(lst_words)
    start = start_words(lst_words)
    stop = stop_words(dct_words)
    sent = int(input('Number of sentences: '))
    print(generator(sent, start, dct_words,stop))


if __name__ == '__main__':
    main()
