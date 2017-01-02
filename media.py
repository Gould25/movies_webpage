#!/usr/bin/env python

# import webrowser module
import webbrowser

class Movie():
    """ Defines class template of my favorite movie

    Attributes:
        title: movie title
        storyline: storyline of movie
        poster_image: image of box cover for the movie
        trailer_youtube_url: you tube trailer for movie
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ initialize a movie """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ play movie trailer """
        webbrowser.open(self.trailer_youtube_url)
