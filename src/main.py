# Name          : I Nyoman Surya Pradipta
# Student ID    : E1900344
# Date          : April 28, 2020

# Import all class from divingAssoc file.
from divingAssoc import *

# A method for providing a user interface.
class DivingCompetition:
    def __init__(self):
        # Enter name of competition.
        competitionTitle = input("Enter competition title: ")
        # Create a single Competition object.
        self.competition = Competition(competitionTitle)
        self.main()

    # Provides a selection menu for users.
    def main(self):
        choice = -1
        while choice != 0:
            # Name of competition.
            print("\n" + self.competition.getCompetitionName())
            print("~" * 30)
            # Menu.
            print("1. Register Diver")
            print("2. Display all divers")
            print("3. Display current leader")
            print("4. Update information of diver")
            print("5. Display all divers, sorted according to name "
                  "or average score")
            print("6. Save data to file")
            print("7. Load data from file")
            print("\n" + "0. Quit" + "\n")
            # User input choices.
            choice = eval(input("Your choice? "))

            if choice == 0:
                # If the number of divers in competition more than 0.
                if self.competition.noOfDivers() > 0:
                    # Call the class competition
                    currentLeader = \
                        str(self.competition.highestAverageScoreSoFar())
                    # Print if success.
                    print("The winner is: " + currentLeader)
                # If the number of divers in competition less than 0.
                else:
                    print("Competition is cancelled due to "
                          "lack of response.")

            elif choice == 1:
                # Print text.
                print("Adding diver")
                # User input name of diver.
                name = input("Name: ")
                # Initialise an empty list for storing score.
                score = []
                # Executing data.
                for i in range(7):
                    # Get input data diver from user.
                    scoreDiver = eval(input("Score " + str(i + 1) + ": "))
                    # Add data from scoreDiver to score
                    score.append(scoreDiver)
                # Object diver.
                dataDiver = Diver(name, score)
                # Register diver.
                self.competition.register(dataDiver)
                # Print if success.
                print("Addition success...")

            elif choice == 2:
                # If there are divers in the competition
                if self.competition.noOfDivers() > 0:
                    # Print registered divers.
                    print(self.competition)
                # If there's no diver data.
                else:
                    # Print text.
                    print("No diver has signed up yet")

            elif choice == 3:
                # If there are divers in the competition
                if self.competition.noOfDivers() > 0:
                    # Call the method highestAverageScoreSoFar.
                    currentLeader = \
                        str(self.competition.highestAverageScoreSoFar())
                    # Print the current leader.
                    print("Current leader is: " + currentLeader + "\n")
                    # If there's no diver data.
                else:
                    print("No diver has signed up yet")

            elif choice == 4:
                # Print divers
                print(self.competition)
                # Enter the ID to be changed.
                idUpdate = eval(input("Which diver to update? "))
                # Update ID.
                if idUpdate <= self.competition.noOfDivers():
                    print(self.competition.diverList[idUpdate - 1])
                    # Enter the name to be changed.
                    nameUpdate = input("New name? <Enter> to skip ")
                    # Update name.
                    if nameUpdate != "":
                        self.competition.diverList[idUpdate - 1]\
                            .setName(nameUpdate)
                        # Enter the score to be changed.
                    scoreUpdate = input("Update score? <Y>es of "
                                        "<Enter> to skip ")
                    # update score.
                    if scoreUpdate.lower() == "y":
                        oriScore = \
                            self.competition.diverList[idUpdate - 1]\
                                .getScores()
                        for i in range(7):
                            inScore = input("Score " + str(i + 1) +
                                            " <Enter> to skip ")
                            if oriScore[i] != inScore and inScore != "":
                                oriScore[i] = eval(inScore)
                    # If there is no update input name and score
                    if nameUpdate == "" and scoreUpdate == "":
                        print("Update aborted")
                    # If there is an update enter the name and score
                    if nameUpdate != "" or scoreUpdate.lower() == "y":
                        print("Information Updated")
                # if not, print invalid number.
                else:
                    print("Invalid number")

            elif choice == 5:
                # Enter sort by name or average.
                sortDiver = input(str("Sort according to <N>ame "
                                      "or <A>verage score? "))
                # Call method.
                sortData = self.competition.sortAllDivers(sortDiver)
                # Start number by 1.
                number = 1
                # Print sort data diver.
                for i in sortData:
                    print(str(number) + ". " + str(i))
                    # Number added with 1.
                    number += 1

            elif choice == 6:
                # Enter file name to save.
                fileName = input("File name to save? ")
                # Call the method save.
                self.competition.saveToFile(fileName)

            elif choice == 7:
                # If there are divers in the competition.
                if self.competition.noOfDivers() > 0:
                    # Ask to user.
                    saveCurrentData = input("Do you want to "
                                            "save current data? (Y/N) ")
                    if saveCurrentData == "y" or saveCurrentData == "Y":
                        # Ask file name.
                        fileName = input("File name to save? ")
                        # Save file.
                        self.competition.saveToFile(fileName)
                        # Delete data.
                        self.competition.diverList.clear()
                    elif saveCurrentData == "n" or saveCurrentData == "N":
                        print("Data not saved...")
                        # Delete Data
                        self.competition.diverList.clear()
                # Load file.
                fileName = input("File name to load: ")
                # Call method readFromFile.
                self.competition.readFromFile(fileName)

# Running the program.
def main():
    DivingCompetition()
main()