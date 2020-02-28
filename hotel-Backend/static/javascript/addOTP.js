$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var otp = $("#OtpReceived").val();
        var pass = $("#newPass").val();
        $.post({url: "http://127.0.0.1:5000/newPassword",
           data: JSON.stringify({OTP: otp,password:pass}),
            contentType: "application/json",
            success: function()
            {
                window.location.href = "http://127.0.0.1:5000/passwordChangedPage"

            }});

    });
});