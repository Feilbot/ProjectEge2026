size = 2560*1440
i = 30

new_size = 1920*1080
new_i = 28

amount = 130

full_size_1 = size * i / 8 / 1024
full_size_2 = new_size * new_i / 8 / 1024

print((full_size_1 - full_size_2) * amount)