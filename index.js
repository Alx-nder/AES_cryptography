$("#encrypt").click(function(){
    var message=$('[name=encrypt]').val();
    if (message==''){
        //do nothing
    }
    else{
        $.ajax({
            url:"aes.py",
            method: "POST",
            data: {message_py:""},
            dataType:"text",
            success: function(data){
                alert("done");
                // $('[name=encrypted]').val()=data;
            }
        })
    }
})