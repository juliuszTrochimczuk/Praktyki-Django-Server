function ChangingText()
{
    let json = sessionStorage.getItem("ApiResponse");
    let Response = JSON.parse(json);
    console.log(Response);
    document.getElementById('Film_Title').innerHTML = Response.Film_Title;
    document.getElementById('Original_Film_Title').innerHTML = Response.Original_Film_Title;
    document.getElementById('List_Of_Actors').innerHTML = Response.Name_Of_Actors;
    document.getElementById('Type_Of_Film').innerHTML = Response.Type_Film;
    document.getElementById('Raiting').innerHTML = Response.Raiting;

}

window.onload = ChangingText;