import random

class Video:
    width = 0
    height = 0
    framesPerSecond = 0
    debth = 0
    compression = 0
    duration = 0

    def __init__(self):
        print("Size of a video file:")
        self.width = random.choice([1280, 1920, 4096])
        print(f"Width: {self.width} px")
        self.height =  random.choice([720, 1080, 2160])
        print(f"Height: {self.height} px")
        frame = self.width*self.height
        self.framesPerSecond = random.randint(50, 4000)
        print(f"Frames per second: {self.framesPerSecond}")
        self.debth = 2**(random.randint(6, 12))
        print(f"Debth: {self.debth} bit")
        self.compression = random.randint(4, 20)
        print(f"Compression: {self.compression} x")
        self.duration = random.randint(60,240)
        print(f"Duration: {self.duration} min")
        duration_sec = self.duration * 60

        bitSize = ((frame*self.debth*self.framesPerSecond)/self.compression)+duration_sec

        fileSize = bitSize/8/(1024*1024)
        fileSize = round(fileSize,2)

        return fileSize