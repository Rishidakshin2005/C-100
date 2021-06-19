class Movie:
    def __init__(self, director,actor,music,movie):
        self.director= director
        self.actor = actor
        self.music = music 
        self.movie = movie    
    def startmovie(self):
         print("Movie started")

    def stopmovie(self):
        print("Movie stoped")

movie1=Movie("Atlee", "Vijay","A.R.Rahman","Mersal")

print(movie1.music)