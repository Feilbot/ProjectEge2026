size = 3840 * 2160
i = 24
card = 16 * 1024 * 1024 * 1024 * 8
paints = 3742
one_paint = size * i

paints_save = paints

while card - one_paint * paints < 0:
    paints -= 1
print(paints_save - paints * (paints_save/paints).__floor__())