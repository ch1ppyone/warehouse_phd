from moviepy.editor import *

resolution = [(128, 128), (1280, 720), (460, 720)]
bitrate = [1200, 5000, 1500000]

clip = VideoFileClip("data/test.mp4")

for r in resolution:
    for b in bitrate:
        final = clip.resize(r)
        final.write_videofile("output/test_" + str(r) + "_" + str(b) + ".mp4", bitrate=str(b))
