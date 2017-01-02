#!usr/bin/python

""" module: entertainment_center
    python version: 2.7.12

    purpose: creates class instances of class movie
             creates and opens webpage
"""

# import module for webpage creation
import fresh_tomatoes

# import class definitions
import media

# creating movie instances
heartbreak_ridge = media.Movie("Heartbreak Ridge",
                        "A hard-nosed, hard-living Marine gunnery sergeant "
                        "clashes with his superiors and his ex-wife as he "
                        "takes command of a spoiled recon platoon with a "
                        "bad attitude.",

                        "https://images-na.ssl-images-amazon.com/images/M/"
                        "MV5BNWVhYTgzMjMtZDkyYy00ZTI3LWI4MTUtZGMxNTFjNzE1YTJm"
                        "XkEyXkFqcGdeQXVyNTI4MjkwNjA@._V1_UX182_CR0,"
                        "0,182,268_AL_.jpg",

                        "https://www.youtube.com/watch?v=ZOo4ir1MtoI")

field_of_dreams = media.Movie("Field of Dreams",
                              "An Iowa corn farmer, hearing voices, interprets"
                              " them as a command to build a baseball diamond "
                              "in his fields; he does, and the Chicago White "
                              "Sox come.",

                              "https://images-na.ssl-images-amazon.com/images"
                              "/M/MV5BNzk5OWY0YjAtYWU3ZS00Y2Q4LWFlNjItMzgwMTQ"
                              "2MjIyMDFmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyM"
                              "TQxNzMzNDI@._V1_SY1000_CR0,0,665,1000_AL_.jpg",

                              "https://www.youtube.com/watch?v=vlTX_ckJ4nM")

the_natural = media.Movie("The Natural",
                          "An unknown comes out of seemingly nowhere to become"
                          " a legendary player with almost divine talent.",

                          "https://images-na.ssl-images-amazon.com/images/M/"
                          "MV5BOWNlNTkzNzEtNDRhOS00MTE1LTk4MjQtZmY2YTgwMTNmM"
                          "WQwXkEyXkFqcGdeQXVyMTA0MjU0Ng@@._V1_UX182_CR0,"
                          "0,182,268_AL_.jpg",

                          "https://www.youtube.com/watch?v=LMnwlNm6xWs")

star_wars = media.Movie("Star Wars: Episode IV - A New Hope",
                        "Luke Skywalker joins forces with a Jedi Knight, "
                        "a cocky pilot, a wookiee and two droids to save the "
                        "galaxy from the Empire's world-destroying "
                        "battle-station, while also attempting to rescue "
                        "Princess Leia from the evil Darth Vader.",

                        "https://images-na.ssl-images-amazon.com/images/M/"
                        "MV5BYzQ2OTk4N2QtOGQwNy00MmI3LWEwNmEtOTk0OTY3NDk2MGJk"
                        "L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_UX"
                        "182_CR0,0,182,268_AL_.jpg",

                        "https://www.youtube.com/watch?v=H38MpZtujJc")

star_wars_I = media.Movie("Star Wars: Episode I - The Phantom Menace",
                          "Two Jedi Knights escape a hostile blockade to find "
                          "allies and come across a young boy who may bring "
                          "balance to the Force, but the long dormant Sith "
                          "resurface to reclaim their old glory.",

                          "https://images-na.ssl-images-amazon.com/images/M"
                          "/MV5BM2FmZGIwMzAtZTBkMS00M2JiLTk2MDctM2FlNTQ2OWY"
                          "wZDZkXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UX182_CR0,"
                          "0,182,268_AL_.jpg",

                          "https://www.youtube.com/watch?v=0MTp807E7_k")

major_league = media.Movie("Major League",
                           "The new owner of the Cleveland Indians puts "
                           "together a purposely horrible team so they'll lose "
                           "and she can move the team. But when the plot is "
                           "uncovered, they start winning just to spite her.",

                           "https://images-na.ssl-images-amazon.com/images/"
                           "M/MV5BMTcyMDE5NzIxMV5BMl5BanBnXkFtZTcwNDUwNzE0M"
                           "Q@@._V1_UY268_CR3,0,182,268_AL_.jpg",

                           "https://www.youtube.com/watch?v=59L-YMhWaZg")

# creating an array of movie instances
movies = [heartbreak_ridge, field_of_dreams,the_natural,
          star_wars,star_wars_I,major_league]

# opening webbrowser and display movies webpage
fresh_tomatoes.open_movies_page(movies)

# end
