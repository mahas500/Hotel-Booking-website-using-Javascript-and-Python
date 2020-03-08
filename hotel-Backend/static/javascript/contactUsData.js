

$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var head = $("#userSession").val();
        var description = $("#description").val();
        $.post({url: "http://127.0.0.1:5000/contactUS",
            headers: {
        session_id:head
    },
            data: JSON.stringify({description: description}),
            contentType: "application/json",
            success: function()
            {
                window.alert("Mail sent to admin!!!")

            }});

    });
});