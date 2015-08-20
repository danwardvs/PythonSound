import string

letters = [('A',".-"),   ('B',"-..."), ('C',"-.-."), ('D',"-.."), ('E',"."),
           ('F',"..-."), ('G',"--."),  ('H',"...."), ('I',".."),  ('J',".---"),
           ('K',"-.-"),  ('L',".-.."), ('M',"--"),   ('N',"-."),  ('O',"---"),
           ('P',".--."), ('Q',"--.-"), ('R',".-."),  ('S',"..."), ('T',"-"),
           ('U',"..-"),  ('V',"...-"), ('W',".--"),  ('X',"-..-"),('Y',"-.--"),
           ('Z',"--..")]


def decode(code):
    letter = ""
    message = ""
    for i in range(0, len(code)):
        if code[i] != " ":
            letter = letter + code[i]
        if code[i] == " ":
            
                decoded_letter = "a"
                message = message + decoded_letter
                letter = ""
                
    print message
    

decode(str(raw_input("HEAKFJD: ")))
