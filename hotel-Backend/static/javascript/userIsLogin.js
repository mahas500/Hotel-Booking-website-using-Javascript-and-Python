
$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var name = $("#customerName").val();
        var pass = $("#pass").val();
        $.post({url: "http://127.0.0.1:5000/customerLogin",
            data: JSON.stringify({username: name, password : pass}),
            contentType: "application/json",
            success: function(result)
            {

                if(result.operationStatus===1){
                    window.location.href = "http://127.0.0.1:5000/dashboard";
                }
                else if(result.operationStatus===-4){
                   window.alert('Rooms not available')
            }
                else {
                    window.alert('Wrong credentials')
                }

            }});

    });
});

