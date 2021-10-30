import random

class Scan:
    
    width = random.randint(15, 45)
    width_inch = width/2.54
    height = random.randint(15, 45)
    height_inch = height/2.54
    debth = 2**(random.randint(4, 8))
    compression = random.randint(4, 20)
    resolution = random.choice([300, 400, 500, 600, 700, 800, 900, 1000, 1200])
    
    def __init__(self):

        print("File size of a scan: ")
        print(f"Width: {self.width} cm")
        print(f"Height: {self.height} cm")
        print(f"Debth: {self.debth} bit")
        print(f"Compression: {self.compression} x")
        print(f"Resolution: {self.resolution} dpi")

        bitSize = ((((self.width_inch*self.resolution*self.height_inch*self.resolution))*self.debth)/self.compression)

        fileSize = bitSize/8/(1024*1024)
        fileSize = round(fileSize,2)

        return fileSize


class Video:
    width = random.choice([1280, 1920, 4096])
    height = random.choice([720, 1080, 2160])
    frame = width*height
    framesPerSecond = random.randint(50, 4000)
    debth = 2**(random.randint(6, 12))
    compression = random.randint(4, 20)
    duration = random.randint(60,240)
    duration_sec = duration * 60

    def __init__(self):
        print("Size of a video file:")
        print(f"Width: {self.width} px")
        print(f"Height: {self.height} px")
        print(f"Frames per second: {self.framesPerSecond}")
        print(f"Debth: {self.debth} bit")
        print(f"Compression: {self.compression} x")
        print(f"Duration: {self.duration} min")

        bitSize = ((self.frame*self.debth*self.framesPerSecond)/self.compression)+self.duration_sec

        fileSize = bitSize/8/(1024*1024)
        fileSize = round(fileSize,2)


class Sound:
    resolution = random.choice([8, 16, 32, 64])
    frequency = random.choice([1200, 1300, 1400, 1500, 1700, 1800, 2100, 2500, 2700, 3100, 3500, 4100])
    channels = random.randint(1,8)
    duration = random.randint(1, 60)
    duration_sec = duration*60

    def __init__(self):
        print("Size of a sound file:")
        print(f"Resolution: {self.resolution} bit")
        print(f"Frequency: {self.frequency} hz")
        print(f"Channels: {self.channels}")
        print(f"Duration: {self.duration} min")

        bitSize = (self.resolution*self.frequency*self.channels)*self.duration_sec
        fileSize = bitSize/8/(1024*1024)
        fileSize = round(fileSize,2)

        return fileSize
