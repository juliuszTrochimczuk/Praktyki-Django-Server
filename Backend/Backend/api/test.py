from imdb

movie = IMDb()

matrix = movie.get_movie('0910970')

matrixInfo = matrix.values()

print(matrixInfo[2])

#Index 0 title of film
# Index 1 original title of film
# Index 2 name of actors
# Index 3 type of film
# Index 4 ??? WTF IS THIS
# Index 5 place where film was filmed
# Index 6 shortcut of places
# Index 7 Language
# Index 8 ??? WTF IS THIS
# Index 9 Time of film?
# Index 14 Raiting
# Index 16 link of picture of film
# Index 18 desription of film
#Index 21 original date of realese
