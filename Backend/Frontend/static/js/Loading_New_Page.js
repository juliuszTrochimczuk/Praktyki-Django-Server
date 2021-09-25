function ChangingText()
{
    let json = sessionStorage.getItem("ApiResponse")
    let Response = JSON.parse(json)
    document.getElementById('a').innerHTML = Response.status
}

window.onload = ChangingText;