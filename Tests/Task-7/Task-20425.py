video_quality = 3840 * 2160
fps = 60
disc = 48_000
i = 16
time = 90
memory = 54691875 * 1024 * 8
stereo = 2

print(2**((memory - stereo * time * i * disc) / time / fps / video_quality))