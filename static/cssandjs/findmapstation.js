function find(){
    let elements = document.querySelector('leaflet-popup-content')
    for (let elem of elements) {
        alert(elem.innerHTML); // "тест", "пройден"
    }
}