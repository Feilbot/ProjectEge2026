x = 1

mono = 2
perc = 0.6
intence = 1
quality = 1

mono_2 = 1
perc_2 = 0.4
intence_2 = 16 * intence
quality_2 = 4 * quality

size_1 = perc * x * quality * mono * intence
size_2 = perc_2 * x * quality_2 * mono_2 * intence_2

print((size_2 / size_1).__floor__())