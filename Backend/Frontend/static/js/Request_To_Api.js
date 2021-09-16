function SendingRequest(film_id)
{
    let xml = new XMLHttpRequest();
    
    xml.open("POST", 'api/Imdb');

    xml.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    //xml.onload

    xml.send(JSON.stringify({ 'film_id':film_id }));
}