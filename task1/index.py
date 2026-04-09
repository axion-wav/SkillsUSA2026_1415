# TASK 1: Input two strings, s and t. Simulate typing them, with '#' functioning as a backspace. Check if the final results of 'typing' each string are equal.

import time, random

s = "AAAA####SkXX##illsUSA"
t = "Qqq###SSS###SkXYZ###illsUSA"

s_ch = list(s)
t_ch = list(t)

s_final = ""
t_final = ""

print("String S:")

for i, ch in enumerate(s_ch):
    if ch == '#':
        s_final = s_final[:-1]

        time.sleep((random.random() * 0.5) + 0.1)
        print('\b \b', end="", flush=True)

        time.sleep((random.random() * 0.5) + 0.3)
        continue
    
    print(ch, end="", flush=True)
    s_final += ch

    time.sleep((random.random() * 0.5) + 0.1)

print("\n\nString T:")

for i, ch in enumerate(t_ch):
    if ch == '#':
        t_final = t_final[:-1]

        time.sleep((random.random() * 0.5) + 0.1)
        print('\b \b', end="", flush=True)

        time.sleep((random.random() * 0.5) + 0.3)
        continue
    
    print(ch, end="", flush=True)
    t_final += ch

    time.sleep((random.random() * 0.5) + 0.1)

if s_final == t_final:
    print("\n\nTRUE. Results are equal.")
else:
    print("\n\nFALSE. Results are not equal.")