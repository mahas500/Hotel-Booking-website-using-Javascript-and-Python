
$("document").ready(function(){

    $("#sendingData").click(function(){
        var name = $("#customerName").val();
        var pass = $("#pass").val();
        $.ajax({
            url: "http://127.0.0.1:5000/customerLogin",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"username": name,"password":pass})
        }).done(function(data) {
            console.log(data);
        });
    });
});