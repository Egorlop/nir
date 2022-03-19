function station() {
    var elems = document.getElementsByClassName('leaflet-popup-content');
    for (var i = 0; i < elems.length; ++i) {
        var item = elems[i];
        var val=item.innerText
    }
    stat=val.substring(0,val.length-13);
    var select1 = document.getElementById("station-select");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].value==stat) {
                new_building.station.options[i].selected=true;}
        }
}