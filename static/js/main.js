//document.getElementById("done").onclick = function(){
//    alert('done')
//};
console.log("connected")
$('#done').click(function() {
    $.ajax({
        type: 'GET',
        url: '/data',
        success: function(response){
            console.log(response);
        }
    })
});
