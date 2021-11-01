import random

class Scan:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.debth = 0
        self.compression = 0
        self.resolution = 0
        
    
    def calc():
        print("File size of a scan: \n")

        width = random.randint(15, 45)
        print(f"Width:\t\t {width} cm")
        width_inch = width/2.54
        height = random.randint(15, 45)
        print(f"Height:\t\t {height} cm")
        height_inch = height/2.54
        debth = 2**(random.randint(4, 8))
        print(f"Debth:\t\t {debth} bit")
        compression = random.randint(4, 20)
        print(f"Compression:\t {compression} x")
        resolution = random.choice([300, 400, 500, 600, 700, 800, 900, 1000, 1200])
        print(f"Resolution:\t {resolution} dpi")

    
        bitSize = ((((width_inch*resolution*height_inch*resolution))*debth)/compression)

        fileSize = bitSize/8/(1024*1024)
        fileSize = round(fileSize,2)

        return fileSize


    
