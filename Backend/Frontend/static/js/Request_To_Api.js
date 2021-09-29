function SendingRequest(film_id)
{
    let xml = new XMLHttpRequest();

    xml.open("POST", 'api/Imdb');

    xml.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    xml.send(JSON.stringify({ 'film_id':film_id }));

    xml.onload = function(){
        const response = JSON.parse(xml.response);
        console.log(response.status)
        if (response.status == "succesful")
        {
            sessionStorage.setItem("ApiResponse", JSON.stringify({'status': response.status,
                                                                  'Film_Title': response.Film_Title,
                                                                  'Original_Film_Title': response.Original_Film_Title,
                                                                  'Name_Of_Actors': response.Name_Of_Actors,
                                                                  'Type_Film': response.Type_Film,
                                                                  'Raiting': response.Raiting,
                                                                  'Original_Date': response.Original_Date}))
            window.location = 'film';
        }
    }
}