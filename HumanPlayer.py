class HumanPlayer:

    def read(self,env, piece):
        print('*************************************************')
        print('*             Player '+str(piece)+' Your Move!               *')
        print('*************************************************')
        userInput = int(input("\nChoose one of the 7 slots (0,1,2,3,4,5,6): "))
        while(userInput < 0 or userInput > 6):
            print('What are you trying to do?, there is no slot '+str(userInput) +' try again!')
            userInput = int(input("\nChoose one of the 7 slots (0,1,2,3,4,5,6): "))

        print("\nThe Player has entered: " + str(userInput))

        if env[0][userInput] != 0:
            print("Column is full, try another one")
            check = False
            while not check:
                userInput = int(input("\nChoose one of the 7 slots (0,1,2,3,4,5,6): "))
                if env[0][userInput] == 0:
                    check = True

        for row in reversed(env):
            if row[userInput] == 0:
                row[userInput] = piece
                break
        return env