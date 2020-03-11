

$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var head = $("#userSession").val();
        var description = $("#description").val();
        $.post({url: "http://127.0.0.1:5000/contactUS",
            headers: {
        session_id:head
    },
            data: JSON.stringify({description: description}),
            contentType: "application/json",
            success: function(result)
            {
                if(result.operationStatus===1){
                    console.log('result');
                    window.alert("Mail sent to admin!!!")
                }

                else if(result.operationStatus===-18){
                    console.log('result');
                    window.alert('Description cannot be empty!!')
                }

            }});

    });
});