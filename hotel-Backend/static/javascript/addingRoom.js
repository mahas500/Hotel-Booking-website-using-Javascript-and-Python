$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var head = $("#userSession").val();
        var roomnumber = $("#number").val();
        var roomprice = $("#roomprice").val();
        var Average_Rating = $("#ratings").val();
        var facility = $("#facility").val();
        $.post({url: "http://127.0.0.1:5000/addRoom",

            headers: {
        session_id:head
    },

           data: JSON.stringify({room_number: roomnumber,price:roomprice,Average_Rating:Average_Rating,facilities:facility}),
            contentType: "application/json",
            success: function(result)
            {
                console.log(result)

            }});

    });
});