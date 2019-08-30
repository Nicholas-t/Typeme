from generator import WordGenerator
import msvcrt
import time
import cv2

"""alpha = ['`':(3,3), '1!':(68, 3), '2@', '3#', '4$','5%','6^','7&','8*','9(','0)','-_','=+',
        'q':(100,75),'w','e','r','t','y','u','i','o','p','[{',']}','\|',
        'a':(127,147),'s','d','f','g','h','j','k','l',';:','\'\"',
        'z':(154, 219),'x','c','v','b','n','m',',<','.>','/?']"""
def analyze(dict={}):
    #dict is a dictionary with letters 
    #as keys and how many errors per letter
    print(dict)
    KEYBOARD_IMG = 'img/keyboard.png'
    img = cv2.imread(KEYBOARD_IMG)
    overlay = img.copy()
    SIZE = 57
    ALPHA = ['`~', '1!', '2@', '3#', '4$','5%','6^','7&','8*','9(','0)','-_','=+',
        'q','w','e','r','t','y','u','i','o','p','[{',']}','\|',
        'a','s','d','f','g','h','j','k','l',';:','\'\"',
        'z','x','c','v','b','n','m',',<','.>','/?']
    LAYOUT =[(3+67*i,3) for i in range (13)]
    LAYOUT+=[(100+67*i,75) for i in range (13)]
    LAYOUT+=[(127+66*i,147) for i in range (11)]
    LAYOUT+=[(154+66*i,219) for i in range (10)]
    for i in range (len(ALPHA)):
        total = 0
        for t in ALPHA[i]:
            if t in dict:
                total += dict[t]
                print(total, t)
        if total != 0:
            (a,b) = LAYOUT[i]
            cv2.rectangle(overlay, (a, b), (a+SIZE,b+SIZE), (0, 50, 255), -1)
    alpha = 0.4 
    img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
    cv2.imshow('kb',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#---------------
gen = WordGenerator()
DONE = False
RUN = True
START = None
W = 0
ERROR = 0
CURRENT = gen.next_sentence()

#------------------

print("Press any button to START")
msvcrt.getch()
print(CURRENT)
START = time.time()
ERROR_DICT = {}

while RUN:
    char = msvcrt.getch().decode("utf-8")
    if char != CURRENT[0] and char != '!':
        ERROR += 1
        char = char.lower()
        if char in ERROR_DICT.keys():
            ERROR_DICT[char] += 1
        else:
            ERROR_DICT[char] = 1
    if char == CURRENT[0] :
        CURRENT = CURRENT[1:]
        print(CURRENT)
        if char == ' ': W+=1
        if CURRENT == '':DONE = True
    elif char == '!':
        RUN = False
        analyze(ERROR_DICT)
        print(f"{W} words total")
        print(f"in {time.time()-START} second(s)")
        print(f"{ERROR} Errors found")
        print(f"Typing speed is {W/(time.time()-START)} words per seconds")
        analyze(dict)
    if DONE == True:
        CURRENT = gen.next_sentence()
        print(CURRENT)
        DONE = False
"""alpha = ['`':(3,3), '1!':(68, 3), '2@', '3#', '4$','5%','6^','7&','8*','9(','0)','-_','=+',
        'q':(100,75),'w','e','r','t','y','u','i','o','p','[{',']}','\|',
        'a':(127,147),'s','d','f','g','h','j','k','l',';:','\'\"',
        'z':(154, 219),'x','c','v','b','n','m',',<','.>','/?']"""

