class HumanPlayer:

    def read(self,env):
        userInput = int(input("\nChoose one of the 7 slots (0,1,2,3,4,5,6): "))
        while(userInput < 0 or userInput > 6):
            print('What are you trying to do?, there is no slot '+str(userInput) +' try again!')
            userInput = int(input("\nChoose one of the 7 slots (0,1,2,3,4,5,6): "))

        print("\nThe Player has enter: " + str(userInput))

        for row in reversed(env):
            if row[userInput] == 0:
                row[userInput] = 1
                break
        return env