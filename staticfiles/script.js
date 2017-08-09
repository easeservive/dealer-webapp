jQuery(document).ready(function($){
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
