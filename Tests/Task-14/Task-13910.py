for p in range(int(max('THNQUL'), 36) + 1, 37):
    if int('TH', p) + int('NQ', p) + int('U', p) == int('1L7', p):
        print(p)