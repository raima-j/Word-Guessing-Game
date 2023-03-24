import random,time
import mysql.connector as ms

user=#user
password=#password
host=#mostly localhost
db=#name of game db

ConOb=ms.connect(host='###',user='###',password='###',db='###')

if ConOb.is_connected():
    print ('\n\n-----------------------------------✨ ✨ ✨ WELCOME!✨ ✨ ✨------------------------------------')
    time.sleep(2)

colours1=['blue','pink','red','grey','teal','gold','lime','tan']    #a simple list of colours
colours2=['black','white','brown','crimson','orange']

while True:

    def menu():
        print ("\n\n                              --- 🎶 --- GAME LOBBY --- 🎶  ---                            ")
        time.sleep(1)
        print ('\n---->> Please select an option...\n')
        global play
        play = input("----> Press P to play the game...\n----->Press D to display the records...\n------>Press U to update a "
            "score...\n------->Press R to remove a record...\n-------->Press Q to Quit\n")
    menu()
    break

    print ('')


    # to add a player record, to play the game
    # to remove a record
    # to change a score

while True:

    if play.upper()=='P':

        GamerName= input("\nHi! Enter your name: ")
        player_id= id(GamerName)
        Player_ID=str(player_id)

        print ("Hello,", GamerName.upper() , "let's start playing... \n")   #intro and rules
        time.sleep(2)
        print ("============================================================================================")
        print ("                                   COLOUR  ME  RIGHT !!!                                    ")
        print ("============================================================================================")
        time.sleep(2)
        print ("\n\t\t\t         >>>>>The Objective<<<<<\n")
        print ("Guess the secret word chosen by the computer from the category of colours.")
        time.sleep(2)
        print ("You can guess only one letter at a time... Press the 'Enter key' after each try.")
        time.sleep(2)
        print ("You will be given 3 extra attempts.")
        time.sleep(1.5)


        print ("If you have all 3 attempts left, you will get 30 points...")
        print ("With 2 attempts, you get 20, and with 1 left you get 10...")
        print ("If you win with no extra attempts left, you get 5 points.")
        time.sleep(5)
        print ("You have to play two rounds, the first round has 3-4 letter colours.\n")
        time.sleep(2)
        print("\t\t\t    ------>LET'S BEGIN ROUND 1!<------\n")



        def TheGame(): #wrapped the game in one function


            gamerGuessList=[]            #for round 1
            gamerGuesses=[]
            wannaPlay=wannaplay= True
            quitGame=False
            gamerGuessList2=[]           #for round 2
            gamerGuesses2=[]
            score=total=0
            continueGame = 'Y'


            secretWord1= random.choice(colours1)    #chosen a colour from list randomly and stored in a variable
            secretWord2= random.choice(colours2)

            #LEVEL 1

            if wannaPlay:

                print ('')
                secretWord1L=list(secretWord1)   #makes a list of the letters of the secret word
                count=len(secretWord1L)      #number of letters in the secret word
                attempts= count + 3

                def GuessedLetter():
                    print ("\n====> Your secret word was," + ''.join(secretWord1L).upper())
                #since we created a  list of the word, to present it back to the gamer, we need to join the elements of the list

                for l in range(count):
                    gamerGuessList.append("_")
                time.sleep(1)

                print (">>>Your word has," ,count, "letters.")

                time.sleep(1)

                print (">>>The number of guesses you have for this word are,", attempts)

                time.sleep(2)

                #now, starting in 3...2...1...

                while True:   #while playing
                    print ('')
                    print ("----->Guess a letter...")   #asked gamer to guess...stored in a variable
                    theLetter= input()


                    while theLetter.isalpha():

                        if theLetter in (gamerGuesses):  #if the letter entered exists in the guessed letters list, try again
                            print ("Whoops...already guessed...try again...")

                        else:                            #for every new letter attempt,reduce the number of attempts by 1
                            attempts = attempts - 1
                            gamerGuesses.append(theLetter)    #add the guessed letter in the list of gamer guesses


                            if theLetter in secretWord1L:
                                print ("Good guess :P")

                                if attempts> 0:
                                    print ("You have," ,attempts, " guesses left.")


                                for p in range(count):#for the position of the found letter in the length of the secret word

                                    if theLetter == secretWord1L[p]: #if the guessed letter is in some position of the secret word list
                                        letterPos= p
                                        gamerGuessList[letterPos]=theLetter.upper() #the letter entered at that position is capitalized


                            else:
                                print ("Oops! Letter not found...try again.")


                                if attempts>0:
                                    print ("You have," , attempts, " guesses left.")

                        break

                    else:
                        print ("/!\ Invalid input...enter a letter.")


                    fullGuessList= ''.join(gamerGuessList)   #joins the final gamer guessed list into a word


                    if fullGuessList.upper()==secretWord1.upper(): #if the joined final list is the same as the secret word of the computer
                        time.sleep(1)
                        print ("\n ###---###---### YAY!!! YOU WON :D ###---###---###\n")
                        time.sleep(1)
                        GuessedLetter()

                        if attempts==0:
                            score=5           #scoring for each attempt left
                            print ("====>  Your score is ",score, " POINTS!")

                        else:
                            score = 10* attempts
                            print ("====>  Your score is,", score, " POINTS!!!")

                        break

                                         #else, if the attempts left is 0

                    elif attempts==0:
                        time.sleep(1)
                        print (" \n :(  No more guesses left...sorry...  ")
                        time.sleep(1)
                        print ("===> The word was," + secretWord1.upper())
                        time.sleep(1)
                        print ("===> Better luck next time!!")
                        time.sleep(1)
                        score = 0
                        print ("===> You get, ", score, " POINTS...")

                        break


            #LEVEL 2

            print (" ")
            time.sleep(3)
            print ("*** Starting ROUND 2 now... ***\n")
            time.sleep(2)
            print("Each word has 5-7 letters.")
            time.sleep(2)
            print ("The score for the word will be 10 POINTS...")
            print ("If all three attempts are left, 60 POINTS...")
            print ("If two left, 40 POINTS, and if one left, 20 POINTS will be granted.")
            time.sleep(5)
            print ("\n===>  GOOD LUCK!!  <===\n")

            if wannaplay:   #takes same logic, different variables

                secretWord2L=list(secretWord2)   #makes a list of the letters of the new secret word
                count2=len(secretWord2L)      #number of letters in the secret word
                attempts2= count2 + 3

                def GuessedLetter2():
                    print ("\n===> Your next secret word was," + ''.join(secretWord2L).upper())

                for q in range(count2):
                    gamerGuessList2.append("_")
                time.sleep(1)

                print (">>> Your new word has," ,count2, "letters.")

                time.sleep(1)

                print (">>> The number of guesses you have for this word are,", attempts2 )

                time.sleep(2)

                #now, starting in 3...2...1...

                while True:   #while playing the second round
                    print ('')
                    print ("Guess a letter...")   #asked gamer to guess...stored in a new variable
                    theLetter2= input()

                    while theLetter2.isalpha():

                        if theLetter2 in (gamerGuesses2):  #if the letter entered exists in the guessed letters list, try again
                            print ("Whoops...already guessed...try again...")

                        else:                            #for every new letter attempt,reduce the number of attempts by 1
                            attempts2 = attempts2 - 1
                            gamerGuesses2.append(theLetter2)    #add the guessed letter in the list of gamer guesses

                            if theLetter2 in secretWord2L:
                                print ("There you go!!")

                                if attempts2> 0:
                                    print ("You have," ,attempts2, " guesses left.")


                                for i in range(count2):#for the position of the found letter in the length of the secret word
                                    if theLetter2 == secretWord2L[i]: #if the guessed letter is in some position of the secret word list
                                        letterPos2 = i
                                        gamerGuessList2[letterPos2]=theLetter2.upper() #the letter entered at that position is capitalized


                            else:
                                print ("Oops! Letter not found...try again.")


                                if attempts2>0:
                                    print ("You have," , attempts2, " guesses left.")
                        break

                    else:
                        print ("/!\  Invalid input...please enter a letter.")


                    fullGuessList2= ''.join(gamerGuessList2)   #joins the second final gamer guessed list into a word


                    if fullGuessList2.upper()==secretWord2.upper(): #if the joined final list is the same as the secret word of the computer
                        time.sleep(2)
                        print ("\n%%%---%%%---%%%  YAY!!! YOU WON :D  %%%---%%%---%%%\n")
                        time.sleep(1)
                        GuessedLetter2()

                        if attempts2==0:
                            score2=10
                            print ("====> Your score is ", score2," POINTS!")

                            break

                        else:
                            score2 = 20* attempts2
                            print ("====>Your score is,", score2, " POINTS!!!\n")
                            time.sleep(1)
                            print ("Your total score is...")
                            time.sleep(2)
                            total= score+score2       #adding for total score
                            print ('$$$', total, 'POINTS  $$$!')

                            print ("\n ^.^.^ Congratulations, matey! You have completed the game!! ^.^.^\n")
                            time.sleep(2)

                            break


                                         #else, if the attempts left is 0

                    elif attempts2==0:
                        time.sleep(2)
                        print ("\n :( No more guesses left...sorry... ")
                        time.sleep(1)
                        print (">>> The word was," + secretWord2.upper())
                        time.sleep(1)
                        print (">>>Better luck next time!!\n")
                        time.sleep(1)
                        score2=0
                        print ("*** You get, ", score2, " POINTS... ***")
                        time.sleep(2)
                        total=score+score2

                        print ('*** You get' , total, 'POINTS! ***')
                        print ("\n^.^.^ Congratulations, matey! You have completed the game!! ^.^.^\n")
                        time.sleep(2)


                        break

                #TO SHOW THE RECORDS WITH SQL
                print ('')
                time.sleep(1)
                print ("These are the player records----->\n")
                time.sleep(1)


                print ('')
                Score=str(total)
                CurOb=ConOb.cursor() #cursor object
                data= "insert into thegame(Player_Name,Player_ID,SecretWord_1,SecretWord_2,Score)values(%s,%s,%s,%s,%s)"
                rows=(GamerName,Player_ID,secretWord1,secretWord2,Score)
                CurOb.execute(data,rows)

                ConOb.commit() #connects with the object

                CurOb.execute("select * from thegame")
                stuff=CurOb.fetchall()
                for row in stuff:
                    print (row) #prints all rows in the table

                time.sleep(2)
                continueGame= input("\nWant to play again?? Press Y to continue, any other letter to quit.")

                while True:
                    if continueGame.upper()== 'Y':
                        time.sleep(1)
                        print ("\n^-^ Okay, then. Get ready to play again!! ^-^\n")
                        TheGame() #called the function to play the game again

                    else:
                        time.sleep(1)
                        print ("\nThanks for playing! Buh-Bye!!\nThese are the player records...\n\n")
                        time.sleep(3)

                        ConOb.commit() #connects with the object

                        CurOb.execute("select * from thegame")
                        stuff=CurOb.fetchall()
                        for row in stuff:
                            print (row) #prints all rows in the table


                    break

        TheGame()     #called the function at the end to run the whole game
        time.sleep(2)
        menu()

#---------------------------------------------------------D.I.S.P.L.A.Y.I.N.G-----------------------------------------------------------------#

    elif play.upper()=='D':

        def display():
            time.sleep(2)
            print ("\n\n============================================================================================")
            print ("                                  DISPLAYING RECORDS NOW                                    ")
            print ("============================================================================================\n\n")
            time.sleep(1.5)
            print ("    Here are the records of each player-->")
            print ('')
            time.sleep(1)
            CurOb=ConOb.cursor()
            ConOb.commit()
            CurOb.execute("select * from thegame")
            stuff=CurOb.fetchall()
            for row in stuff:
                print ('   ',row)           #shows table


        display()
        time.sleep(2)
        menu()

#----------------------------------------------------------D.E.L.E.T.I.O.N---------------------------------------------------------------------#

    elif play.upper()=='R':

        def remove():
            time.sleep(2)
            print ("\n\n============================================================================================")
            print ("                                    REMOVING RECORDS NOW                                    ")
            print ("============================================================================================\n\n")
            time.sleep(1.5)
            print ('')
            print ('    Original table--->\n')
            CurOb=ConOb.cursor()
            ConOb.commit()
            CurOb.execute("select * from thegame")
            stuff=CurOb.fetchall()
            for row in stuff:
                print ('   ',row)                       #shows table once for reference

            print ('')
            time.sleep(1.5)
            del_name= str(input("    Enter the Player Name: "))
            del_id=str(input("    Enter the ID of the Player from the table: "))
            flag= False


            del_data="delete from thegame where Player_Name='%s' && Player_ID='%s'" % (del_name,del_id)  #to delete record with name and id
                       # %s here takes the values assigned to the variables

            CurOb.execute(del_data)#executes the deletion command
            ConOb.commit()

            time.sleep(2)

            CurOb.execute("select * from thegame") #displays the table after deleting record
            stuff=CurOb.fetchall()

            for row in stuff:
                if del_name in row:
                    print('\n    *** RECORD SUCCESSFULLY DELETED ***\n')
                    print ('   ',row)
                    flag=True
                    break
                break

            if flag==False:
                time.sleep(1)
                print ('\n    No records found :( ')

        remove()
        time.sleep(2)
        menu()

#----------------------------------------------------------U.P.D.A.T.I.O.N--------------------------------------------------------------------#

    elif play.upper()=='U':

        def update():
            time.sleep(2)
            print ("\n\n============================================================================================")
            print ("                                    UPDATING RECORDS NOW                                    ")
            print ("============================================================================================\n\n")
            print ('')
            time.sleep(1.5)
            print ('    Original table--->\n')
            CurOb=ConOb.cursor()
            ConOb.commit()
            CurOb.execute("select * from thegame")
            stuff=CurOb.fetchall()
            for row in stuff:
                print ('   ',row)                       #shows table once for reference

            time.sleep(1.5)
            update_name= str(input("\n    Enter the Player Name: "))
            update_id=str(input("    Enter the ID of the Player from the table: "))
            new_score= str(input("    Enter your new score: "))
            print ('')

            flag= False

            update_data= "update thegame set Score='%s' where Player_Name='%s' && Player_ID='%s'" % (new_score,update_name,update_id)
                                    # update and set commands used to change the score of the player
            CurOb.execute(update_data)
            ConOb.commit()

            time.sleep(1)


            CurOb.execute("select * from thegame where Player_Name='%s' && Player_ID='%s'" % (update_name,update_id) )
                                                                             #displays the table after deleting record

            stuff=CurOb.fetchall()

            for row in stuff:
                print ('\n    *** RECORD SUCCESSFULLY UPDATED ***\n')
                print ("    This is the updated record-->")
                if update_name in row:
                    print ('   ',row)
                    flag=True
                    break
            if flag==False:                       #if a flag has been raised
                print ('\n    No records found :( ')

        update()
        time.sleep(2)
        menu()

#---------------------------------------------------------------E.X.I.T------------------------------------------------------------------------#

    else:
        time.sleep(1)
        print ('\n\n^-^ Thanks for your time!')
        time.sleep(1)
        print (':") BUH-BYE!')
        time.sleep(3)
        break



