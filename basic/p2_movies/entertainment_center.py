# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
    "A story of a boy and his toys that come to life",
    "https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268/sign=52d1d685908fa0ec7fc7630b1e97594a/d62a6059252dd42a1835151d023b5bb5c9eab843.jpg",
    "https://v.youku.com/v_show/id_XNDY0Mzg4MjMy.html")

avatar = media.Movie("Avatar",
    "A marine on an alien planet",
    "https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike220%2C5%2C5%2C220%2C73/sign=8983a693612762d09433acedc185639f/eaf81a4c510fd9f9f7454cd9272dd42a2834a42b.jpg",
    "https://v.youku.com/v_show/id_XNjYyMzAzMTc2.html?spm=a2h1n.8261147.0.0&s=de0eef689fa311df97c0")

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
