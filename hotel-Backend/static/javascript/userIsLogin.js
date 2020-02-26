
/*$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var name = $("#customerName").val();
        var pass = $("#pass").val();
        $.ajax({
            url: "http://127.0.0.1:5000/customerLogin",
            type: "GET",
            contentType: "application/json",
            data: JSON.stringify(
                {"username": name,"password":pass})
        }).done(function(data)
        {
            console.log("Data = ",data);
        });
    });
});*/


/*$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var name = $("#customerName").val();
        var pass = $("#pass").val();
        $.post("http://127.0.0.1:5000/customerLogin",{"\"username\"": name,"\"password\"":pass},function(res){
            console.log(res);

        }).done(function(res){
           window.location.href = "http://127.0.0.1:5000/dashboard";
            console.log("success")

        }).fail(function(){
            console.log("Failure")
        });


    });
});
*/


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
                console.log(result);
            window.location.href = "http://127.0.0.1:5000/dashboard";
            }});

    });
});