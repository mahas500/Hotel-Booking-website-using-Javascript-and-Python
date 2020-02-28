$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var roomID = $("#number").val();
        $.post({url: "http://127.0.0.1:5000/deleteRoom",
           data: JSON.stringify({room_id: roomID}),
            contentType: "application/json",
            success: function()
            {
                console.log("deleted!!!")

            }});

    });
});