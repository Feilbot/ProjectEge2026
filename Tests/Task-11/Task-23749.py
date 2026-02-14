kolvo = 3_845_627
mem = 11 * 2**30
L = 2783

I = (mem / kolvo).__ceil__()
print('Объём сообщения:', I)
i_c = (mem / kolvo / L * 8).__ceil__()
i_f = (mem / kolvo / L * 8).__floor__()
# I = L * i
print('Округлённое вверх: ', i_c, 'Округлённое вниз: ', i_f)
print(I, '<', (L * i_c / 8).__ceil__(), I, '<', L * i_f / 8)
print('=> округлённое вверх. i = 9')
print('Ответ:', 2**(9-1) + 1)