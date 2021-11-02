import random
import Scan
import Sound
import Video
import calc

def main():
    
    def user_input():
        checker = False
        while checker==False:

            count = input("How many tasks do you want?  ")

            try:
                count =int(count)
                checker = True
                return count
            except:
                print("Please... an integer please...  ")
                checker = False
                continue


    def exercise():
       
        count = user_input()
    
        while count > 0:
            checker = False
            task = random.choice([Scan,Video, Sound])
            calc.calc(task)
            while checker==False:
                answer = input("what would be your solution in MiB? Please round to 2 decimals  ")
                try:
                    answer = float(answer)
                    checker=True
                except:
                    print("Please... a two decimal float please...  ")
                    checker = False
                continue
            
            if answer == calc.calc(task):
                print("yay, correct answer")
            else:
                print(f"sorry, the correct answer was: {calc.calc(task)}")

            count -=1
    exercise()

main()






