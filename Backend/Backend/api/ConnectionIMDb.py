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

    return HttpResponse(json.dumps({'status':'successful'}))


#'Film_Title': movieInfo[0],
#'Original_Film_Title': movieInfo[1],
#'Name_Of_Actors': movieInfo[2],
#'Type_Film': movieInfo[3],
#'Raiting': movieInfo[14],
#'Original_Date': movieInfo[21]