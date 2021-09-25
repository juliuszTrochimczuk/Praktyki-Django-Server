function SendingRequest(film_id)
{
    let xml = new XMLHttpRequest();
    
    xml.open("POST", 'api/Imdb');

    xml.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    xml.send(JSON.stringify({ 'film_id':film_id }));

    xml.onload = function(){
        const response = JSON.parse(xml.response);
        if (response.status == 'successful')
        {
            sessionStorage.setItem("ApiResponse", JSON.stringify({'status': response.status}))
            window.location = 'film'; 
        }       
    }
}