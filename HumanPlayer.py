class HumanPlayer:

    def read(self,env):
        userInput = int(input("Choose one of the 7 slots (0,1,2,3,4,5,6): "))
        print("\nThe Player has enter: " + str(userInput))

        for row in reversed(env):
            if row[userInput] != 1 or row[userInput] != 2:
                row[userInput] = 1
                break
        return env