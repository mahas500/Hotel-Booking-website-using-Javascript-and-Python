$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var head = $("#userSession").val();
        var roomID = $("#RoomBookingId").val();

        $.post({url: "http://127.0.0.1:5000/addBooking",

            headers: {
        session_id:head
    },
           data: JSON.stringify({room_id: roomID}),
            contentType: "application/json",
            success: function(result)
            {

                window.location.href = "http://127.0.0.1:5000/RoomBookingConfirmation"
                console.log(result)


            }});

    });
});