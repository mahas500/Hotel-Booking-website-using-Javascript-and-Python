
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
                if(result.operationStatus===1){
                    window.location.href = "http://127.0.0.1:5000/adminDashboard";
                }
                else if(result.operationStatus===-2){
                    window.alert('Wrong credentials')
                }

            }});

    });
});


