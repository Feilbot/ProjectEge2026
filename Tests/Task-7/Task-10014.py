stereo = 2
period = 48_000
i = 8
size = 5 * 1024 * 1024 * 1024 * 8

print((size/stereo/period/i/3600).__ceil__())