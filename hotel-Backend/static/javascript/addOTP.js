$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var otp = $("#OtpReceived").val();
        var pass = $("#newPass").val();
        $.post({url: "http://127.0.0.1:5000/newPassword",
           data: JSON.stringify({OTP: otp,password:pass}),
            contentType: "application/json",
            success: function(result)
            {
                console.log(result)
                if(result.operationStatus === 1){
                    window.location.href = "http://127.0.0.1:5000/passwordChangedPage"
                }
                else{
                    window.alert('OTP not correct')
                }

            }});

    });
});