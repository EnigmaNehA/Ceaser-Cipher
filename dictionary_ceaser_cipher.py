dictalpha1 = {'A' : 1 , 'B' : 2 , 'C' : 3 , 'D' : 4 , 'E' : 5 , 'F' : 6 , 'G' : 7 ,
             'H' : 8 , 'I' : 9 , 'J' : 10 , 'K' : 11 , 'L' : 12 , 'M' : 13 , 
             'N' : 14 , 'O' : 15 , 'P' : 16 , 'Q' : 17 , 'R' : 18 , 'S' : 19 , 
             'T' : 20 , 'U' : 21 , 'V' : 22 , 'W' : 23 , 'X' : 24 , 'Y' : 25 ,
             'Z' : 26}

dictalpha2 = {0 : 'Z' , 1 : 'A' , 2 : 'B' , 3 : 'C' , 4 : 'D' , 5 : 'E' , 6 : 'F' ,
              7 : 'G' , 8 : 'H' , 9 : 'I' , 10 : 'J' , 11 : 'K' , 12 : 'L' , 13 : 'M' ,
              14 : 'N' , 15 : 'O' , 16 : 'P' , 17 : 'Q' , 18 : 'R' , 19 : 'S' , 20 : 'T' ,
              21 : 'U' , 22 : 'V' , 23 : 'W' , 24 : 'X' , 25 : 'Y'}

def encrypttext(messagestr , shiftcode):
    ciphertext = ''
    for letterstr in messagestr :
        if(letterstr != ' '):
            num1 = (dictalpha1[letterstr] + shiftcode)%26
            ciphertext += dictalpha2[num1]
        else:
            ciphertext += ' '
    return ciphertext

def decrypttext(messagestr , shiftcode):
    deciphertext = ''
    for letterstr in messagestr :
        if(letterstr != ' '):
            num1 = (dictalpha1[letterstr] - shiftcode + 26)%26
            deciphertext += dictalpha2[num1]
        else:
            deciphertext += ' '
    return deciphertext

def main():
    messagestr = 'this is Python HACKING with CEASER CIPHER'
    dhiftcode = 13
    resultstr = encrypttext(messagestr.upper(),dhiftcode)
    messagestr2 = 'GUVF VF CLGUBA UNPXVAT JVGU PRNFRE PVCURE'
    resultstr2 = decrypttext(messagestr2.upper(),dhiftcode)
    print(resultstr )
    print(resultstr2)

if __name__ == '__main__':
    main()