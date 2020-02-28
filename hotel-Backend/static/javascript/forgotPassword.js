$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var customerID = $("#customerID").val();
        var email = $("#email").val();
        $.post({url: "http://127.0.0.1:5000/forgotPassword",
           data: JSON.stringify({customer_id: customerID,email:email}),
            contentType: "application/json",
            success: function()
            {
                window.location.href = "http://127.0.0.1:5000/addOTP"

            }});

    });
});