class Collection:
    
    def __init__(self, movieList, gameList):
        self.movieList = []
        self.gameList = []
        self.favGame = ""
        self.favMovie = ""

        self.movieList = movieList
        self.gameList = gameList

    def AddGame(self, game):
        if game in self.gameList:
            print("Game is already in collection")
        else:
            self.gameList.append(game)

    
    def AddMovie(self, movie):
        if movie in self.movieList:
            print("Movie is already in collection")
        else:
            self.movieList.append(movie)


    def RemoveGame(self, game):
        if game in self.gameList:
            self.gameList.remove(game)
        else:
            print("Game Not Found")

    def RemoveMovie(self, movie):
        if movie in self.movieList:
            self.movieList.remove(movie)
        else:
            print("Game Not Found")

    def DisplayCollection(self):
        for game in self.gameList:
            print(game)

    def DisplayGames(self):
        for game in self.gameList:
            print(game)
    
    def DisplayMovies(self):
        for movie in self.movieList:
            print(movie)

    def DisplayFavGame(self):
        print(f'Fav Game: {self.favGame}')

    def DisplayFavMovie(self):
        print(f'Fav Movie: {self.favMovie}')

    def DisplayCollection(self):
        self.DisplayGames()
        self.DisplayFavGame()
        self.DisplayMovies()
        self.DisplayFavMovie()

    def SetFavMovie(self, movie):
        if movie not in self.movieList:
            self.AddMovie(movie)
        self.favMovie = movie

    def SetFavGame(self, game):
        if game not in self.gameList:
            self.AddMovie(game)
        self.favMovie = game


    