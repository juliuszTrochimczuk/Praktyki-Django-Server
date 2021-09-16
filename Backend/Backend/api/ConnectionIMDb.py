from imdb import IMDb
from django import http
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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

    return HttpResponse(json.dumps({'status':"successful"}))
