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

def stop_words(dct_words):
    stop = []
    words = dct_words.keys()
    for word in words:
        if word[-1] == '.' or word[-1] == '!' or word[-1] == '?':
            stop.append(word)
    return stop

def main():
    file = open_file()
    lst_words = text_editing(file_read(file))
    dct_words = creat_dict(lst_words)
    sent = int(input('Number of sentences: '))
