from imdb import imdb
mv = imdb.IMDb()
top = mv.get_top250_movies()

for i in range(5):
    print(top[i])