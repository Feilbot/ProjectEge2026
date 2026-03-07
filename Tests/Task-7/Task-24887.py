stereo = 2
disc = 56_000
i = 15
amount_of_tracks = 28
time_of_all_tracks = 27*60 + 27
v = 367_217_732
# time > 332

size_of_title = 1

while (stereo * disc * i * time_of_all_tracks + size_of_title * 1024 * 8 * amount_of_tracks) / v <= 332:
     size_of_title += 1

print(size_of_title)