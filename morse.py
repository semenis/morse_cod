lol = 'ОСТОРОЖНО! НЕ УДАЛИТЕ ЛИШНЮЮ СТРОКУ! ИНАЧЕ ВАШ WINDOWS КРАШНЕТСЯ!МЫ НЕ БУДЕМ В ЭТОМ ВИНОВАТЫ! (0_0)'
MorseCodeEng = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
                "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
                "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
                "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "Ä": ".-.-", "Ü": "..--",
                "ß": "...--..", "À": ".--.-", "È": ".-..-", "É": "..-..", ".": ".-.-.-", ",": "--..--", ":": "---...",
                ";": "-.-.-.", "?": "..--..", "-": "-....-", "_": "..--.-", "(": "-.--.", ")": "-.--.-", "'": ".----.",
                "=": "-...-", "+": ".-.-.", "/": "-..-.", "@": ".--.-.", " ": "\t", "": ""}
MorseCodeRus = {"А": ".-", "Б": "-...", "В": ".--", "Г": "--.", "Д": "-..", "Е": ".", "Ж": "...-", "З": "--..",
                "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..", "М": "--", "Н": "-.", "О": "---", "П": ".--.",
                "Р": ".-.", "С": "...", "Т": "-", "У": "..-", "Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.",
                "Ш": "----", "Щ": "--.-", "Ы": "-.--", "Ь": "-..-", "Э": "..-..", "Ю": "..--", "Я": ".-.-",
                "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
                "8": "---..", "9": "----.", "Ä": ".-.-", "Ü": "..--", "ß": "...--..", "À": ".--.-", "È": ".-..-",
                "É": "..-..", ".": ".-.-.-", ",": "--..--", ":": "---...", ";": "-.-.-.", "?": "..--..", "-": "-....-",
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
                return 'eng'
            elif language in varRus:
                return 'rus'
            else:
                print('Не правильный язык или ввод, повторите снова.')
                continue
def main():
    language = 'eng'
    func = 'encode'
    print('Помощь : help')
    print('Завершение работы функции : exit')
    
    while True:
        n = input()
        if n == 'Код из говна и палок!':
            print(lol)
        elif n == 'help':
            print('Текущий язык: ', language)
            print('Текущее действие: ',func)
            print('Вы можете вводить значения после двоеточия, чтобы изменить настройки.')
            print('Смена языка : change')
            print('Кодирование : encode')
            print('Декодирование : decode')
            print('Завершение работы функции : exit')
            print('Разработчики: TevaSTARK, semenis, Dikower')
        elif n == 'exit':
            return
        elif n == 'encode':
            func = 'encode'
        elif n == 'decode':
            func = 'decode'
        elif n == 'change':
            language = askLanguage()
        else:
            if language == 'rus':
                arg2 = MorseCodeRus
            else:
                arg2 = MorseCodeEng
            if func == 'decode':
                try:
                    print(decodeFromMorse(n,arg2))
                except:
                    print('Языки различаются! Текущия язык:', language + '. Чтобы поменять введите:change')
            else:
                try:
                    print(encodeToMorse(n,arg2))
                except:
                    print('Языки различаются! Текущия язык:',language+'. Чтобы поменять введите:change')
main()
