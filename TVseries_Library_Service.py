class Library:
    def __init__(self, listofseriesname):
        self.series = listofseriesname

    def displayAvailbleSeries(self):
        print("The Series availble in Library are: ")
        for series in self.series:
            print("\t" + series)

    def borrowSeries(self, seriesName):
        if seriesName in self.series:
            print(
                f"You have been issued {seriesName}. Thanks for choosing our Series Library, please kept dvd safe and return it in 30 days.")
            self.series.remove(seriesName)
            return True
        else:
            print("This series is either not available or has already been issued to someone else. Please, try again Later.")
            return False

    def returnSeries(self, seriesName):
        self.series.append(seriesName)
        print("Hope, you enjoyed the series. Come back again, Thank you.")


class Person:
    def requestSeries(self):
        self.book = input("Enter the name of a series you want to watch: ")
        return self.book

    def returnSeries(self):
        self.book = input(
            "Enter the name of a tv series, You want to return:  ")
        return self.book


if __name__ == "__main__":
    centralTvshowLibrary = Library(["The Originals", "Supernatural", "Grimm", "Dark", "Lucifer",
                                   "Game of thrones", "Sex education", "Penny dreadfull", "The Huanting of hill-house"])
    person = Person()

    while(True):
        message = ''' ***** Welcome to the world's biggest Tv show collection Library *****
        Please choose an option to proceed:
        1. List of Available Tv shows.
        2. Request a Tv show
        3. Add/return Tv show
        4. Exit the Library. 
        '''
        print(message)
        a = int(input("Enter your choice here: "))
        if a == 1:
            centralTvshowLibrary.displayAvailbleSeries()
        elif a == 2:
            centralTvshowLibrary.borrowSeries(person.requestSeries())
        elif a == 3:
            centralTvshowLibrary.returnSeries(person.returnSeries())
        elif a == 4:
            print("Thanks for choosing our services, Have a great day!!")
            exit()
        else:
            print("INVALID CHOICE!! CHOOSE AGAIN.")
