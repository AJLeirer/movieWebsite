import media, fresh_tomatoes


#Define values for class Movie (movie_title, movie_storyline, poster_image, trailer_youtube)
empire_strikes = media.Movie("The Empire Strikes Back",
                        "Luke Skywalker continues his journey with the Force.",
                        "http://images4.fanpop.com/image/photos/20600000/empire-movie-poster-star-wars-empire-strikes-back-20604952-1369-2125.jpg", # NOQA
                        "https://www.youtube.com/watch?v=96v4XraJEPI")

raiders = media.Movie("Raiders of the Lost Ark",
                     "Indiana Jones races against the Nazis to find the Lost Ark.",
                     "https://www.movieposter.com/posters/archive/main/157/MPW-78716", # NOQA
                     "https://www.youtube.com/watch?v=0ZOcoxjeUYo")

big_lebowski = media.Movie("The Big Lebowski",
                     "The Dude just wants to get his rug back.",
                     "http://ia.media-imdb.com/images/M/MV5BMTQ0NjUzMDMyOF5BMl5BanBnXkFtZTgwODA1OTU0MDE@._V1_SY1000_CR0,0,670,1000_AL_.jpg", # NOQA
                     "https://www.youtube.com/watch?v=cd-go0oBF4Y")
                           
dead_pool = media.Movie("Dead Pool",
                     "A mercenary becomes a mutant and fights his nemisis.",
                     "http://s3.foxmovies.com/foxmovies/production/films/103/images/posters/464-asset-page.jpg", # NOQA
                     "https://www.youtube.com/watch?v=oCvLUxICxEI")

godfather = media.Movie("The Godfather",
                     "The story of the Corleone family in America. ",
                     "https://www.movieposter.com/posters/archive/main/10/MPW-5399", # NOQA
                     "https://youtu.be/8V2k2YQEQJ4")

dark_knight_rises = media.Movie("The Dark Knight Rises",
                     "Batman must face more than Bane in his fight to save Gotham. ",
                     "https://www.movieposter.com/posters/archive/main/147/MPW-73816", # NOQA
                     "https://www.youtube.com/watch?v=g8evyE9TuYk")

holy_grail = media.Movie("Monty Python and the Holy Grail",
                     "King Arthur and his knights go on a quest for the Holy Grail.",
                     "https://www.movieposter.com/posters/archive/main/199/MPW-99540", # NOQA
                     "https://www.youtube.com/watch?v=RDM75-oXGmQ")

fisher_king = media.Movie("The Fisher King",
                     "Two men connected by tragedy struggle to find their road back.", # NOQA
                     "https://www.movieposter.com/posters/archive/main/31/A70-15804", # NOQA
                     "https://www.youtube.com/watch?v=NHaZuRo3DZ4")

what_dreams = media.Movie("What Dreams May Come",
                     "A husband goes to Hell to save his wife.",
                     "https://upload.wikimedia.org/wikipedia/en/9/91/Whatdreamsposter.jpeg", # NOQA
                     "https://www.youtube.com/watch?v=TPZpQsEFcKI")

#Create a list (movies) to store movie values
movies = [empire_strikes, raiders, big_lebowski, dead_pool, godfather,
          dark_knight_rises, holy_grail, fisher_king, what_dreams]

#Pass movies list to fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)

