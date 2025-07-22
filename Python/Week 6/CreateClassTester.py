import CreateClass

movies = ["Home Alone, Problem Child, Shrek"]
games = ["Madden, 2k, Fortnite"]

myCollection = CreateClass.Collection(movies, games)

myCollection.SetFavGame("2k")
myCollection.SetFavMovie("Home Alone")
myCollection.DisplayCollection()