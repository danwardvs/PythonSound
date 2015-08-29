import string

CODE = {'.-': 'A',     '-...': 'B',   '-.-.': 'C', 
        '-..':'D',    '.': 'E',      '..-.': 'F',
        '--.': 'G',    '....': 'H',   '..': 'I',
        '.---': 'J',   '-.-': 'K',    '.-..': 'L',
        '--': 'M',     '-.': 'N',     '---': 'O',
        '.--.': 'P',   '--.-': 'Q',   '.-.': 'R',
        '...': 'S',    '-': 'T',      '..-': 'U',
        '...-': 'V',   '.--': 'W',    '-..-': 'X',
        '-.--': 'Y',   '--..': 'Z',
        
        '-----': '0',  '.----': '1',  '..---': '2',
        '...--': '3',  '....-': '4',  '.....': '5',
        '-....': '6',  '--...': '7',  '---..': '8',
        '----.': '9' 
        }


def decode(code):
    code = code + " "
    letter = ""
    message = ""
    for i in range(0, len(code)):
        if code[i] != " ":
            letter = letter + code[i]
        
        if code[i] == " ":
            decoded_letter = str(CODE[letter],)
            message = message + decoded_letter
            letter = ""
        if code[i] == "/":
            message = message + " "
            
        
    print message
    

decode(str(raw_input("Enter Morse code message: ")))
