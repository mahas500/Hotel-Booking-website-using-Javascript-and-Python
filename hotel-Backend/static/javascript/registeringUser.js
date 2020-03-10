$("document").ready(function()
{

    $("#sendingData").click(function()
    {
        var name = $("#name").val();
        var username = $("#username").val();
        var password = $("#password").val();
        var email = $("#email").val();
        var contact_no = $("#contact_no").val();
        $.post({url: "http://127.0.0.1:5000/addCustomerInDB",
            data: JSON.stringify({name: name, username : username,password: password,email: email,contact_no: contact_no}),
            contentType: "application/json",
            success: function(result)
            {
                console.log(result);
                if (result.operationStatus===-14){
                    window.alert('Invalid Email')
                }
                else if(result.operationStatus===-15){
                    window.alert('Invalid Contact Number!!')
                }
                else if(result.operationStatus===-19){
                    window.alert('Password too short!!')
                }
                else if(result.operationStatus===-16){
                    window.alert('Invalid Name!!')
                }
                else if(result.operationStatus===1){
                    window.alert('Registration Successful!!')
                }

            }});

    });
});