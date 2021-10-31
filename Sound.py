import random

class Sound:
    resolution = 0
    frequency = 0
    channels = 0
    duration = 0
    duration_sec = 0

    def __init__(self):
        print("Size of a sound file:")
        self.resolution = random.choice([8, 16, 32, 64])
        print(f"Resolution: {self.resolution} bit")
        self.frequency = random.choice([1200, 1300, 1400, 1500, 1700, 1800, 2100, 2500, 2700, 3100, 3500, 4100])
        print(f"Frequency: {self.frequency} hz")
        self.channels = random.randint(1,8)
        print(f"Channels: {self.channels}")
        self.duration = random.randint(1, 60)
        print(f"Duration: {self.duration} min")
        duration_sec = self.duration*60

        bitSize = (self.resolution*self.frequency*self.channels)*duration_sec
        fileSize = bitSize/8/(1024*1024)
        fileSize = round(fileSize,2)

        return fileSize
