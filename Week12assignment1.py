#Name: Nick Wolf
#Date: 4/19/2021
#Program: Week 12 assignment 1


#Function (open, write, close)
def file1 (): 
    #open file
    names_file = open ('Scoobynames.txt', 'w')

    #Write file
    names_file.write("Shaggy\n")
    names_file.write("Scooby\n")
    names_file.write("Daphne\n")
    names_file.write("Velma\n")
    names_file.write("Fred\n")
    names_file.write("Scrappy\n")

    #close file
    names_file.close ()

#Body
file1()

