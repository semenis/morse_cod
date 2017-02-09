MorseCodeEng = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
                "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
                "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
                "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",  "Ä": ".-.-", "Ü": "..--",
                "ß": "...--..", "À": ".--.-", "È": ".-..-", "É": "..-..", ".": ".-.-.-", ",": "--..--", ":": "---...",
                ";": "-.-.-.", "?": "..--..", "-": "-....-", "_": "..--.-", "(": "-.--.", ")": "-.--.-", "'": ".----.",
                "=": "-...-", "+": ".-.-.", "/": "-..-.", "@": ".--.-.", " ": "\t", "": ""}
MorseCodeRus = {"А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..", "Е": ".", "Ж": "...-", "З": "--..",
                "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..", "М": "--", "Н": "-.", "О": "---", "П": ".--.",
                "Р": ".-.", "С": "...", "Т": "-", "У": "..-", "Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.",
                "Ш": "----", "Щ": "--.-", "Ы": "-.--", "Ь": "-..-", "Э": "..-..", "Ю": "..--", "Я": ".-.-",
                "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
                "8": "---..", "9": "----.", "0":"-----", "Ü": "..--", "ß": "...--..", "À": ".--.-", "È": ".-..-",
                ".": ".-.-.-", ",": "--..--", ":": "---...", ";": "-.-.-.", "?": "..--..", "-": "-....-",
                "_": "..--.-", "(": "-.--.", ")": "-.--.-", "'": ".----.", "=": "-...-", "+": ".-.-.", "/": "-..-.",
                "@": ".--.-.", " ": "\t", "": ""}
def encodeToMorse(text='Введите что-нибудь', language=MorseCodeRus):
    res = []
    for i in text.upper():
        if i in language:
            res.append(language[i])
    return (' '.join(res))  # Потому что потом сплитоваться не правильно будет
def decodeFromMorse(text, language=MorseCodeEng):
    arr = text.split('\t')
    res = []
    for i in range(len(arr)):
        arr[i] = arr[i].split()
        for j in range(len(arr[i])):
            for a, b in language.items():
                if b == arr[i][j]:
                    res.append(a)
        res.append(' ')
    return (''.join(res).lower().strip())
def askLanguage():
        while True:
            language = input('Choose the language (eng or rus): ')
            language = language.lower()
            varEng = ['eng','english']
            varRus = ['rus','russian','рус','русский']
            if language in varEng:
                print('Выбрано - eng')
                return 'eng'
            elif language in varRus:
                print('Выбрано - rus')
                return 'rus'
            else:
                print('Не правильный язык или ввод, повторите снова.')
                continue
def main():
    language = 'eng'
    print('Текущий язык -', language)
    print('Для изменения языка введите change(1).')
    print('Для кодирования введите encode(2).')
    print('Для декодирования из кода морзе введите decode(3)')
    print('Для выхода введите exit(4)')
    while True:
        dey=input()
        if dey=='change' or dey=='1':
            language=askLanguage()
            continue
        elif dey=='encode' or dey=='2':
            if language=='eng':
                print(encodeToMorse(text=input(), language=MorseCodeEng))
            elif language=='rus':
                print(encodeToMorse(text=input(), language=MorseCodeRus))
        elif dey=='decode'  or dey=='3':
            if language=='eng':
                print(decodeFromMorse(text=input(), language=MorseCodeEng))
            elif language=='rus':
                print(decodeFromMorse(text=input(), language=MorseCodeRus))
        elif dey=='exit' or  dey=='4':
            return
        elif dey=='egg' or dey=='2017'or dey.lower()=='пасхалка':
            print(decodeFromMorse(text='.--. .-. .. .-- . - 	 .. --.. 	 ..--- ----- .---- --... .-.-.- 	 ..-.. - --- - 	 -.- --- -.. --..-- 	 .--. --- 	 ... .-.. --- .-- .- -- 	 -.. .. -- -.-- 	 .. --.. 	 --. .--.-. .--.-. .--.-. .--.-. 	 .. 	 .--. .- .-.. --- -.- .-.-.-', language=MorseCodeRus))
            continue
        else:
            print('File or command dont exist.')
            continue
main()
