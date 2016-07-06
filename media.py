import webbrowser

class Movie():
    """A class that stores information about a movie and plays its youtube trailer"""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title=None, storyline=None, poster_image=None, trailer_url=None):

        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer)