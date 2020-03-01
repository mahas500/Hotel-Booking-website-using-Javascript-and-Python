
$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var name = $("#customerName").val();
        var pass = $("#pass").val();
        $.post({url: "http://127.0.0.1:5000/customerLogin",
            data: JSON.stringify({customer_id: name, password : pass}),
            contentType: "application/json",
            success: function(result)
            {
                console.log(result);
            window.location.href = "http://127.0.0.1:5000/dashboard";
            }});

    });
});

