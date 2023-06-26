
// $(document).ready(function(){

//     $("#dropdownid").change(function(){
//         console.log("Some changed has occured");
//         debugger;
//         var values = [];
//         $(".optext").each(function() {
//             var value = $(this).text();
//             values.push(value);
//           });
//         console.log(values);
//     });

// });
$(document).ready(function(){
    $("#textid").hide();
    $("#imageid").hide();
    $("#audioid").hide();
    $('#id_dropdown').on("change",function(){
        $("#textid").hide();
        $("#imageid").hide();
        $("#audioid").hide();
        var selected_value=$(this).val();
        
        $.each(selected_value,function(index,value){
        if(value == "Text"){
            $("#textid").show();
        }else if(value == "Image"){
            $("#imageid").show();
        }else if(value == "Audio"){
            $("#audioid").show();
        }
        
        console.log("value",selected_value)
    })
    console.log("value",selected_value)
    

})
})
