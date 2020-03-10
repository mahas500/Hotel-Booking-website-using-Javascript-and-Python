
$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var name = $("#adminName").val();
        var pass = $("#pass").val();
        $.post({url: "http://127.0.0.1:5000/adminLogin",
            data: JSON.stringify({username: name, password : pass}),
            contentType: "application/json",
            success: function(result)
            {
                x =result.operationStatus;

                if(x===1){
                    console.log(x)
                    window.location.href = "http://127.0.0.1:5000/adminDashboard";
                }
                else if(x===-2){
                    console.log(x)
                    window.alert('Wrong credentials')
                }

            }});

    });
});


