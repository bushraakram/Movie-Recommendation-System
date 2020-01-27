from flask import Flask,render_template
from flask import request
from sample import get_title_from_index
from sample import get_index_from_title
from sample import get_poster_from_index
from sample import get_releasedate_from_index
from sample import get_runtime_from_index
from sample import get_genre_from_index
from sample import get_cast_from_index
from sample import get_director_from_index
from sample import get_overview_from_index
from sample import similar_movies
from flask import jsonify
from PIL import Image
import array as arr

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def predict():
    try:
        if 'movie_input' in request.form:
            movie_input= request.form['movie_input']
            movie_index = get_index_from_title(movie_input)
            movie_poster=get_poster_from_index(movie_index)
            movie_genre=get_genre_from_index(movie_index)
            movie_runtime=get_runtime_from_index(movie_index)
            movie_cast=get_cast_from_index(movie_index)
            movie_director=get_director_from_index(movie_index)
            movie_overview=get_overview_from_index(movie_index)
            movie_release=get_releasedate_from_index(movie_index)
            movies = similar_movies(movie_input)
            i=0
            print("Top 5 similar movies are:")
            e1= []
            p1=[]
            for element in movies:
            
                e1.insert(0,get_title_from_index(element[0]))
                p1.insert(0,get_poster_from_index(element[0]))
                i=i+1
                if i>5:
                  break
            return render_template('predictor.html', movie=e1,poster=p1,movie_poster=movie_poster,runtime=movie_runtime,release=movie_release,director=movie_director,cast=movie_cast,overview=movie_overview,genre=movie_genre,movie_input=movie_input)
                  
        else:
            msg= "Search a movie"
            return render_template('abc.html', message=msg)
                
                

        
    except :
        print("Movie not found")
       
        msg="Movie not found"
   
        return render_template('abc.html', message=msg)
     
    
                                     
    

if __name__ == '__main__':
    app.run(debug=True)
    