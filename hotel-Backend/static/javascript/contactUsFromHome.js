

$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var name = $("#name").val();
        var email = $("#email").val();
        var description = $("#description").val();
        $.post({url: "http://127.0.0.1:5000/contactUsViaHome",
           data: JSON.stringify({name: name,email: email,description: description}),
            contentType: "application/json",
            success: function(result)
            {
                if(result.operationStatus===1){
                window.alert("Mail sent to admin!!!")
                }
                else if(result.operationStatus===-14){
                    window.alert('Invalid Email')
                }
                else if(result.operationStatus===-16){
                    window.alert('Invalid Name!!')
                }

            }});

    });
});