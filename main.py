import random
import files

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
            task = random.choice([files.Scan,files.Video, files.Sound])
            task.__init__(task)
            checker = False
            
            while checker==False:
                answer = input("what would be your solution in MiB? Please round to 2 decimals  ")
                try:
                    answer = float(answer)
                    checker=True
                except:
                    print("Please... a two decimal float please...  ")
                    checker = False
                continue
            
            if answer == task:
                print("yay, correct answer")
            else:
                print(f"sorry, the correct answer was: {task}")

            count -=1
    exercise()

main()





