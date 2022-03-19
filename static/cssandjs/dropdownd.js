function dropdowns() {
    $('#multi-select1').dropdown();
    $('#multi-select2').dropdown();
    $('#multi-select3').dropdown();
    $('#multi-select4').dropdown();
    $('#multi-select5').dropdown();
    $('#multi-select6').dropdown();
    $('#multi-select7').dropdown();
    $('#multi-select8').dropdown();
    $('#multi-select9').dropdown();
    $('#multi-select10').dropdown();
    $('#multi-select11').dropdown();
    $('#multi-select12').dropdown();
    $('#rangestart').calendar({
      type: 'date',
      endCalendar: $('#rangeend')
    });
    $('#rangeend').calendar({
      type: 'date',
      startCalendar: $('#rangestart')
    });
    $( "#multi-select1" ).change(function() {
        var select1 = document.getElementById("multi-select1");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].selected) selected1.push(select1.options[i].value);}
    });
    $( "#multi-select2" ).change(function() {
        var select1 = document.getElementById("multi-select2");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].selected) selected1.push(select1.options[i].value);}
    });
    $( "#multi-select3" ).change(function() {
        var select1 = document.getElementById("multi-select3");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].selected) selected1.push(select1.options[i].value);}
    });
    $( "#multi-select4" ).change(function() {
        var select1 = document.getElementById("multi-select4");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].selected) selected1.push(select1.options[i].value);}
    });
    $( "#multi-select5" ).change(function() {
        var select1 = document.getElementById("multi-select5");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].selected) selected1.push(select1.options[i].value);}
    });
    $( "#multi-select6" ).change(function() {
        var select1 = document.getElementById("multi-select6");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].selected) selected1.push(select1.options[i].value);}
    });
    $( "#multi-select7" ).change(function() {
        var select1 = document.getElementById("multi-select7");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].selected) selected1.push(select1.options[i].value);}
    });
    $( "#multi-select8" ).change(function() {
        var select1 = document.getElementById("multi-select8");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].selected) selected1.push(select1.options[i].value);}
    });
    $( "#multi-select9" ).change(function() {
        var select1 = document.getElementById("multi-select9");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].selected) selected1.push(select1.options[i].value);}
    });
    $( "#multi-select10" ).change(function() {
        var select1 = document.getElementById("multi-select10");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].selected) selected1.push(select1.options[i].value);}
    });
    $( "#multi-select11" ).change(function() {
        var select1 = document.getElementById("multi-select11");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].selected) selected1.push(select1.options[i].value);}
    });
    $( "#multi-select12" ).change(function() {
        var select1 = document.getElementById("multi-select12");
        for (let i = 0; i < select1.length; i++) {
            if (select1.options[i].selected) selected1.push(select1.options[i].value);}
    });
}