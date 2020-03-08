$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var head = $("#userSession").val();
        var roomID = $("#number").val();
        $.post({url: "http://127.0.0.1:5000/deleteRoom",
            headers: {
        session_id:head
    },
           data: JSON.stringify({room_id: roomID}),
            contentType: "application/json",
            success: function(result)
            {
                console.log(result)
                window.alert("Room deleted successfully")
            }});

    });
});