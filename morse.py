MorseCodeEng = {"A": ".-","B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","0": "-----","1": ".----","2": "..---","3": "...--","4": "....-","5": ".....","6": "-....","7": "--...","8": "---..","9": "----.","Ä": ".-.-","Ü": "..--","ß": "...--..","À": ".--.-","È": ".-..-","É": "..-..",".": ".-.-.-",",": "--..--",":": "---...",";": "-.-.-.","?": "..--..","-": "-....-","_": "..--.-","(": "-.--.",")": "-.--.-","'": ".----.","=": "-...-","+": ".-.-.","/": "-..-.","@": ".--.-."," ": "\t","" : ""}
MorseCodeRus = {"А": ".-","Б": "-...","В": ".--","Г":"--.","Д": "-..","Е": ".","Ж": "...-","З": "--..","И": "..","Й": ".---","К": "-.-","Л": ".-..","М": "--","Н": "-.","О": "---","П": ".--.","Р": ".-.","С": "...","Т": "-","У": "..-","Ф": "..-.","Х": "....","Ц": "-.-.","Ч": "---.","Ш": "----","Щ": "--.-","Ы": "-.--","Ь": "-..-","Э":"..-..","Ю":"..--","Я":".-.-","1": ".----","2": "..---","3": "...--","4": "....-","5": ".....","6": "-....","7": "--...","8": "---..","9": "----.","Ä": ".-.-","Ü": "..--","ß": "...--..","À": ".--.-","È": ".-..-","É": "..-..",".": ".-.-.-",",": "--..--",":": "---...",";": "-.-.-.","?": "..--..","-": "-....-","_": "..--.-","(": "-.--.",")": "-.--.-","'": ".----.","=": "-...-","+": ".-.-.","/": "-..-.","@": ".--.-."," ": "\t","" : ""}
def encodeToMorse(text = 'Developers: TevaSTARK,semenis,Dikower',language = MorseCodeEng):
    res = []
    for i in text.upper():
        if i in language:
            res.append(language[i])
    return(' '.join(res))#Потому что потом сплитоваться не правильно будет
def decodeFromMorse(text, language = MorseCodeEng):
    arr=text.split('\t')
    res=[]
    for i in range(len(arr)):
        arr[i]=arr[i].split()
        for j in range(len(arr[i])):
            for a,b in language.items():
                if b==arr[i][j]:
                    res.append(a)
        res.append(' ')
    return(''.join(res).lower().strip())
def main():
    pass
print(decodeFromMorse(encodeToMorse('Any text')))
