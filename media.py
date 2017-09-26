import webbrowser

#class for movie objects
class Movie():
    """ This class provides a way to store movie related information"""
    def __init__(self, movie_title, movie_storyline, 
                 poster_image, trailer_youtube):
        """ This is the constructor for the Movie class. Each movie needs 
                a title, storyline, poster image, and movie trailer """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
