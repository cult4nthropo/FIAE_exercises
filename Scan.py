import random

class Scan:
    
    width = 0
    height = 0
    debth = 0
    compression = 0
    resolution = 0
    
    def __init__(self):

        print("File size of a scan: ")

        self.width = random.randint(15, 45)
        print(f"Width: {self.width} cm")
        width_inch = self.width/2.54
        self.height = random.randint(15, 45)
        print(f"Height: {self.height} cm")
        height_inch = self.height/2.54
        self.debth = 2**(random.randint(4, 8))
        print(f"Debth: {self.debth} bit")
        self.compression = random.randint(4, 20)
        print(f"Compression: {self.compression} x")
        self.resolution = random.choice([300, 400, 500, 600, 700, 800, 900, 1000, 1200])
        print(f"Resolution: {self.resolution} dpi")

        bitSize = ((((width_inch*self.resolution*height_inch*self.resolution))*self.debth)/self.compression)

        fileSize = bitSize/8/(1024*1024)
        fileSize = round(fileSize,2)

        return fileSize
