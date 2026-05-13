# Images
# V = h * w * i
# i = log2(N)
# h - height
# w - weight
# i - bits

# Music
# V = k * t * i * n
# V - объём, t - время, i - биты, n - этта (дискретизация)

# Video

# video_quality = 3840 * 2160
# fps = 60
# disc = 48_000
# depth = 16
# time = 90
# memory = 54691875 * 1024 * 8
# stereo = 2
#
# print(2**((memory - stereo * time * depth * disc) / time / fps / video_quality)) -
# - макс. палитра для 1 кадра

# 2 ** (i - 1) + 1 - мин. палитра