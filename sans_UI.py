from generator import WordGenerator
import msvcrt
import time


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

while RUN:
    char = msvcrt.getch().decode("utf-8")
    if char != CURRENT[0] :
        ERROR += 1
    if char == CURRENT[0] :
        CURRENT = CURRENT[1:]
        print(CURRENT)
        if char == ' ': W+=1
        if CURRENT == '':DONE = True
    if DONE == True:
        CURRENT = gen.next_sentence()
        print(CURRENT)
        DONE = False
    if char == '!':
        RUN = False
        print(f"{W} words total")
        print(f"in {time.time()-START} second(s)")
        print(f"{ERROR} Errors found")
        print(f"Typing speed is {W/(time.time()-START)} words per seconds")
    