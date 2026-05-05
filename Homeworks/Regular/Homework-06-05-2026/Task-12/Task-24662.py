text = 'TRICKORTREAT'
reversed_text = ''
amount = 1200/len(text)

for letter in text:
    if letter == 'T':
        reversed_text += 'A'
    elif letter == 'R':
        reversed_text += 'C'
    elif letter == 'A':
        reversed_text += 'K'
    elif letter == 'I':
        reversed_text += 'E'
    elif letter == 'E':
        reversed_text += 'E'
    elif letter == 'C':
        reversed_text += 'T'
    elif letter == 'O':
        reversed_text += 'R'
    else:
        reversed_text += 'O'

print(sum(1 for i in reversed_text if i in 'TRCK') * amount)