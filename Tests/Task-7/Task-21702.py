size = 7680*4320

i = 16

one_card_size = 9 * 1024 * 1024 * 1024 * 8

amount_of_photos = 4010

print(amount_of_photos - (one_card_size/(size*i)).__floor__() * (amount_of_photos / (one_card_size/(size*i)).__floor__()).__floor__())