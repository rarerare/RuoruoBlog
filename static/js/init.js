window.onload=function(){
	trackUser();
	$('#commentForm').submit(function(event){
		event.preventDefault();
		var postData = $(this).serializeArray();
	    var formURL = $(this).attr("action");
	    $.ajax(
	    {
	        url : formURL,
	        type: "POST",
	        data : postData,
	        success:function(data, textStatus, jqXHR) 
	        {
	        	var newComment=document.createElement('div');
	        	newComment.innerHTML=data+"<hr>";
	            $('#preCommentsDiv').append(newComment);
	            alert("Comment Submitted")
	        },
	        error: function(jqXHR, textStatus, errorThrown) 
	        {
	            //if fails      
	        }
	    });
	})
}
function trackUser(){
	var TZO=(new Date()).getTimezoneOffset();
	$.ajax(
	    {
	        url : "trackUser",
	        type: "POST",
	        data : {'TZO': TZO}
	    });
}