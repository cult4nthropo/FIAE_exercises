import random
import Scan
import Sound
import Video

def calc(task):
    if task == Scan:
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
    elif task == Sound:
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
    else:
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

        bitSize = ((frame * debth * framesPerSecond) / compression) * duration_sec

        fileSize = bitSize / 8 / (1024 * 1024)
        fileSize = round(fileSize,2)

        return fileSize
