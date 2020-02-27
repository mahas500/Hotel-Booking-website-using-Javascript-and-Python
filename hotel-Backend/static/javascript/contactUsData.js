

$("document").ready(function()
{

    $("#sendingData").click(function()
    {

        var description = $("#description").val();
        $.post({url: "http://127.0.0.1:5000/contactUS",
            data: JSON.stringify({description: description}),
            contentType: "application/json",
            success: function()
            {

            }});

    });
});