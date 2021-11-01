import random

class Sound:
    def __init__(self):
        self.resolution = 0
        self.frequency = 0
        self.channels = 0
        self.duration = 0
        self.duration_sec = 0
    
    def calc():
        print("Size of a sound file:\n")
        resolution = random.choice([8, 16, 32, 64])
        print(f"Resolution: \t{resolution} bit")
        frequency = random.choice([1200, 1300, 1400, 1500, 1700, 1800, 2100, 2500, 2700, 3100, 3500, 4100])
        print(f"Frequency: \t{frequency} hz")
        channels = random.randint(1,8)
        print(f"Channels:\t {channels}")
        duration = random.randint(1, 60)
        print(f"Duration:\t {duration} min")
        duration_sec = duration*60

        bitSize = (resolution*frequency*channels)*duration_sec
        fileSize = bitSize/8/(1024*1024)
        fileSize = round(fileSize,2)

        return fileSize

