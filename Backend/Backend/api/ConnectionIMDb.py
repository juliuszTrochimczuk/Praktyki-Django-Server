from imdb import IMDb
from django import http
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import json
import os

@csrf_exempt
def GettingFilmInfo(request):
    os.chdir(os.path.dirname(__file__))

    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
    except:
        return HttpResponse(json.dumps({'status':"error","message":'Invalid request'}))

    if 'film_id' not in body:
        return HttpResponse(json.dumps({'status':"error", 'message': "Invalid request"}))

    imdbInfo = IMDb()

    movie = imdbInfo.get_movie(body['film_id'])

    movieInfo = movie.values()

    actor1 = str(movieInfo[2][0])
    actor2 = "  "+str(movieInfo[2][1])
    actor3 = "  "+str(movieInfo[2][2])
    actor4 = "  "+str(movieInfo[2][3])
    actor5 = "  "+str(movieInfo[2][4])



    List_of_actors = [actor1, actor2, actor3, actor4, actor5]

    return HttpResponse(json.dumps({
        'status': "succesful",
        'Film_Title': str(movieInfo[0]),
        'Original_Film_Title': str(movieInfo[1]),
        'Name_Of_Actors': List_of_actors,
        'Type_Film': str(movieInfo[3]),
        'Raiting': str(movieInfo[14]),

    }))

#'Film_Title': movieInfo[0],
#'Original_Film_Title': movieInfo[1],
#'Name_Of_Actors': movieInfo[2],
#'Type_Film': movieInfo[3],
#'Raiting': movieInfo[14],
#'Original_Date': movieInfo[21]