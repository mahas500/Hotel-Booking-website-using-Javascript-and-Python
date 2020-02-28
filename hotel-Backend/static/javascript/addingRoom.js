$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var roomnumber = $("#number").val();
        var roomprice = $("#roomprice").val();
        var ratings = $("#ratings").val();
        $.post({url: "http://127.0.0.1:5000/addRoom",
           data: JSON.stringify({room_number: roomnumber,price:roomprice,ratingOutofTen:ratings}),
            contentType: "application/json",
            success: function()
            {
                console.log("added!!!")

            }});

    });
});