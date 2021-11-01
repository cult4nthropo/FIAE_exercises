import random

class Video:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.framesPerSecond = 0
        self.debth = 0
        self.compression = 0
        self.duration = 0
    
    def calc():

        print("Size of a video file:")
        width = random.choice([1280, 1920, 4096])
        print(f"Width: {width} px")
        height =  random.choice([720, 1080, 2160])
        print(f"Height: {height} px")
        frame = width*height
        framesPerSecond = random.randint(50, 4000)
        print(f"Frames per second: {framesPerSecond}")
        debth = 2**(random.randint(6, 12))
        print(f"Debth: {debth} bit")
        compression = random.randint(4, 20)
        print(f"Compression: {compression} x")
        duration = random.randint(60,240)
        print(f"Duration: {duration} min")
        duration_sec = duration * 60

        bitSize = ((frame*debth*framesPerSecond)/compression)*duration_sec

        fileSize = bitSize/8/(1024*1024)
        fileSize = round(fileSize,2)

        return fileSize
