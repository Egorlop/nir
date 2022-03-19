function map(coords,names) {
    let Regex = /&#39;/gi;
    let new_names=names.replace(Regex, '');
    let newn=new_names.replace('[', '');
    let newna=newn.replace(']', '');
    let namemas=newna.split(',')
    var map = L.map('map').setView([coords[0][0], coords[0][1]], 6);
    var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(map);
    for (var index = 0; index < coords.length; ++index) {
        var marker = L.marker([coords[index][0], coords[index][1]]).addTo(map);
        marker.bindPopup(namemas[index]+' ('+coords[index][0]+'-'+coords[index][1]+')'+"<input onclick='station()' style='' value='Select' type='submit'>")
    }
}