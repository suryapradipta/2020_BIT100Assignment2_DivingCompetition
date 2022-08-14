# Name          : I Nyoman Surya Pradipta
# Student ID    : E1900344
# Date          : April 28, 2020


# This class defines the attributes of the object participants
# who take part in diving competitions.
class Diver:
    """The class that defines simple object types that
    represent dive competitors."""

    # The nextDiverID variable is a class variable that is
    # shared with all instances / objects of Diver class.
    # save the next diver ID, and initialize it with 1.
    nextDiverID = 1

    # The constructor method for initializing the creation of objects from
    # the diver class.
    # Constructor with name and score arguments to initialize
    # the object's attributes with this parameter value.
    def __init__(self, name, scores):
        # Declare name variable.
        # Use the word "self" which shows that "variable" belongs
        # to the class "Diver".
        self.name = name
        # Declare scores variable.
        self.scores = scores
        # Access class variables with dot notation (.)
        self.id = Diver.nextDiverID
        # id is automatically generated using class variables.
        Diver.nextDiverID += 1

    # A method that reads the name variable value.
    def getName(self):
        return self.name

    # A method that reads the id variable value
    def getID(self):
        return self.id

    # A method that reads the scores variable value
    def getScores(self):
        return self.scores

    # A method that updates value of a name variable
    def setName(self, newName):
        self.name = newName

    # A method that compute a score that represents the average score
    # of the 5 remaining scores, after removing
    # the highest and lowest score.
    def getAverageScore(self):
        # Create object average.
        average = self.scores
        average = (sum(average) - max(average) -
                   min(average)) / (len(average) - 2)
        # Format 2 decimal places after the comma.
        return format(average, '.2f')

    # A string method ( __str__ ) which return
    # a single string containing the details of a competitor.
    def __str__(self):
        # method str.format()
        return "{} ({}) with scores {}, and average score {}"\
            .format(self.name, self.id, self.scores,self.getAverageScore())


# This class declares object which maintains a list of Competitor objects.
class Competition:
    """The class defines the object which is the container
    of the Competitor object."""

    # A constructor with one argument of type ‘str’ used to
    # initialise the competition name.
    def __init__(self, competitionName):
        # Initialise an empty list for storing divers.
        self.diverList = []
        # Declare competition name variable.
        self.competitionName = competitionName

    # A method that reads the competition name variable.
    def getCompetitionName(self):
        return self.competitionName

    # A method that reads the divers variable.
    def getDiverList(self):
        return self.diverList

    # A method that updates value of a competition name variable.
    def setCompetitionName(self, newCompetitionName):
        self.competitionName = newCompetitionName

    # A method that updates value of a divers variable.
    def setDiverList(self, newDiverList):
        self.diverList = newDiverList

    # A method will save a reference to the Diver object.
    def register(self, diverObject):
        # The append () method adds items to diverList.
        self.diverList.append(diverObject)

    # A method that returns divers with an average score so far.
    def highestAverageScoreSoFar(self):
        # Create object highest.
        highest = self.diverList[0]
        # Divers that are stored in the diverList.
        for diver in self.diverList:
            if diver.getAverageScore() > highest.getAverageScore():
                highest = diver
        # Returns divers with the highest average score so far.
        return highest

    # Returns the number of divers stored in the collection
    def noOfDivers(self):
        return len(self.diverList)

    # Returns the details of all divers, one per line.
    def __str__(self):
        # More than one diver.
        if len(self.diverList) > 1:
            strAll = "Divers: \n"
        # Less than one diver.
        else:
            strAll = "Diver: \n"
        # The number start with 1.
        number = 1
        # Items in diverList.
        for i in self.diverList:
            # Format display.
            # Adding dot(.) after number.
            strAll += str(number) + ". " + str(i) + "\n"
            # Numbers added by 1.
            number += 1
        #  Returns the details of all divers.
        return strAll

    # A method that accepts an integer representing the index
    # where the diver is stored in the list.
    def getDiver(self, index):
        # The found diver with that index is returned.
        if index < len(self.diverList):
            return self.diverList[index]
        # If this index is out of bounds, the method returns none.
        else:
            return "None"

    # A method that save all diver information to file.
    def saveToFile(self, fileName):
        # Write file.
        output = open(fileName, "w")
        # Executing one per line in diverList.
        for i in self.diverList:
            # Initialization.
            formatScore = ""
            # Executing one per line in getScores.
            for j in i.getScores():
                # Adding comma(,) before scores
                formatScore += "," + str(j)
            # Save one per line to file.
            print(str(i.getName()) + formatScore, file=output)
        # Close file.
        output.close()
        # Print if success
        print("Data successfully save to " + fileName)

    # A method that load all the divers info from the file.
    def readFromFile(self, fileName):
        # Set the nextDiverID to 1 before reading the data from file.
        Diver.nextDiverID = 1
        # Read file.
        openFile = open(fileName, "r")
        # Read every line that split by comma(,).
        readFile = openFile.readlines()
        for line in readFile:
            diverDataLine = line.split(",")
            # 0 Index is Diver's name.
            diverName = diverDataLine[0]
            # 1 until 7 is Diver's score.
            scoreAll = []
            for i in range(1, len(diverDataLine)):
                scoreDiver = eval(diverDataLine[i])
                scoreAll.append(scoreDiver)
            # Register Diver.
            diverData = Diver(diverName, scoreAll)
            self.register(diverData)
        # Close file.
        openFile.close()
        # Print if success.
        print("Data successfully loaded from " + fileName)

    # A method that accept the criteria
    # that determine the sorting order of the Divers collection.
    def sortAllDivers(self, sortDiver):
        # If input equal to "n"
        if sortDiver.lower() == "n":
            # A list for storing sort data objects.
            sortData = []
            # Add items to sortData list.
            for h in self.diverList:
                sortData.append(h)
            # The number of sessions used to check data from the start.
            for i in range(len(sortData)):
                for j in range(len(sortData) - 1):
                    # Comparing data name.
                    if sortData[j + 1].getName() < sortData[j].getName():
                        temp = sortData[j]
                        sortData[j] = sortData[j + 1]
                        sortData[j + 1] = temp

        # If input equal to "a"
        elif sortDiver.lower() == "a":
            # A list for storing sort data objects.
            sortData = []
            # Add items to sortData list.
            for h in self.diverList:
                sortData.append(h)
            # The number of sessions used to check data from the start.
            for i in range(len(sortData)):
                for j in range(len(sortData) - 1):
                    # Comparing data average score.
                    if sortData[j + 1].getAverageScore() \
                            < sortData[j].getAverageScore():
                        temp = sortData[j]
                        sortData[j] = sortData[j + 1]
                        sortData[j + 1] = temp
        return sortData
