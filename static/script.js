jQuery(document).ready(function($){

	$('.sr-accept-btn').click(function(){
	// console.log($(this).attr('value'));
		$.post("/apis/jobcard/v1/service/accept",
	    {
	        booking_id: $(this).attr('value')
	        
	    },
	    function(data, status){
	
	    	if(data['jc_id']) {
	    		window.location.href = '/jobcard/edit/?jc='+data['jc_id'];
	    	}
	        
	    });

	});

	$('.dropdown').click(function(e){
		e.preventDefault();
		$(this).toggleClass('active');
		$(this).closest('li').find('ul').toggleClass('active');
	});
	if ($('.datepicker').length) {
		$('.datepicker').datepicker({
			format : 'dd/mm/yyyy'
		});
	}


	$('#labour-estimation').keyup(function(){
		updateCost();
	}).blur(function(){
		updateCost();
	});

	$('#total-parts-cost').keyup(function(){
		updateCost();
	}).blur(function(){
		updateCost();
	});

	function updateCost() {
		var labour = $('#labour-estimation').val();
		if ($.isNumeric(labour)) {
			labour = labour;
		} else {
			labour = 0;
		}

		var cost = $('#total-parts-cost').val();
		if ($.isNumeric(cost)) {
			cost = cost;
		} else {
			cost = 0;
		}

		$('#total-estimation').val(parseFloat(labour)+parseFloat(cost));
	}
});


