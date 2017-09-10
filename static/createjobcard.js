jQuery(document).ready(function($){

    $('.has-dropdown .dropdown').click(function(e){
        e.preventDefault();
        $(this).toggleClass('active');
        $(this).closest('li').find('ul').toggleClass('active');
    });

    var availableTags = [];

    var sparesTags = [];

    if ($('#delivery-time').length) {
        $('#delivery-time').datetimepicker({
            sideBySide : true
        });
    }

    if ($('#service-reminder-time').length) {
        $('#service-reminder-time').datetimepicker({
            sideBySide : true
        });
    }

    $('.add-customer').click(function(e){
        e.preventDefault();
        $('.show-me').removeClass('hidden');
        $(this).addClass('hidden');
    });

    var slug = function(str) {
        var $slug = '';
        var trimmed = $.trim(str);
        $slug = trimmed.replace(/[^a-z0-9-]/gi, '-').
        replace(/-+/g, '-').
        replace(/^-|-$/g, '');
        return $slug.toLowerCase();
    }

    $( "#customer-complaint" ).on('keypress', function(e) {
        var key = e.keyCode || e.which;
        if(key == 13) {
            var label = $(this).val();
            var sluggable = slug($(this).val());
            var html = '<div class="form-group checkbox">' +
                '<input type="hidden" class="customer-complaints" value="'+label+'"/>' +
                '<input type="hidden" class="customer-complaints-ids" value=""/>' +
                '<input type="checkbox" name="customer_complaints[]" value="1" class="uncheck-customer-complaint customer-checkbox" checked id="'+sluggable+'">' +
                '<label for="'+sluggable+'">'+label+'</label>'+
                '<a class="remove-me"><i class="ion-ios-close"></i></a>' +
                '</div>';
            $('#customer-items').append(html);
            e.preventDefault();
            e.stopPropagation();
            return false;
        }
    });

    $( "#recommended" ).on('keypress', function(e) {
        var key = e.keyCode || e.which;
        if(key == 13) {
            var label = $(this).val();
            var sluggable = slug($(this).val());
            var html = '<div class="form-group checkbox">' +
                '<input type="hidden" class="recommended-items" value="'+label+'"/>' +
                '<input type="hidden" class="recommended-items-ids" value=""/>' +
                '<input type="checkbox" disabled name="recommended-items[]" value="1" class="uncheck-recommended-item recommended-checkbox" checked id="'+sluggable+'">' +
                '<label for="'+sluggable+'">'+label+'</label>'+
                '<a class="remove-me"><i class="ion-ios-close"></i></a>' +
                '</div>';
            $('#recommended-items').append(html);
            e.preventDefault();
            e.stopPropagation();
            return false;
        }
    });

    $('body').on('change', '.uncheck-customer-complaint', function(e){
        if ($(this).is(':checked')) {
            //fireAjax('load-parts-checked.json');
        } else {
            //fireAjax('load-parts.json');
        }
    });


    $.ajax({
        url : '/api/auto/jobs',
        type: 'POST',
        success : function(response) {
            // response = JSON.parse(response);
            if (response.status == "success") {
                
                response.compliants.forEach(function(value) {
                    
                    availableTags.push(value.Description);
                    sparesTags.push(value);
                });

                $( "#customer-complaint" ).autocomplete({
                    source: availableTags,
                    select: function (event, ui) {
                        $("#customer-complaint").val('');
                        label = ui.item.label;
                        var sluggable = slug(label);
                        var html = '<div class="form-group checkbox">' +
                            '<input type="hidden" class="customer-complaints" value="'+label+'"/>' +
                            '<input type="hidden" class="customer-complaints-ids" value=""/>' +
                            '<input type="checkbox" class="uncheck-customer-complaint" value="1" checked id="'+sluggable+'">' +
                            '<label for="'+sluggable+'">'+label+'</label>'+
                            '<a class="remove-me"><i class="ion-ios-close"></i></a>' +
                            '</div>';
                        $('#customer-items').append(html);
                        return false;
                    },
                });

                $( "#recommended" ).autocomplete({
                    source: availableTags,
                    select: function (event, ui) {
                        $("#recommended").val('');
                        label = ui.item.label;
                        var sluggable = slug(label);
                        var html = '<div class="form-group checkbox">' +
                            '<input type="hidden" class="recommended-items" value="'+label+'"/>' +
                            '<input type="hidden" class="recommended-items-ids" value=""/>' +
                            '<input type="checkbox" disabled name="recommended-items[]" value="1" class="uncheck-recommended-item recommended-checkbox" checked id="'+sluggable+'">' +
                            '<label for="'+sluggable+'">'+label+'</label>'+
                            '<a class="remove-me"><i class="ion-ios-close"></i></a>' +
                            '</div>';
                        $('#recommended-items').append(html);
                        return false;
                    },
                });

            }
        }
    });


    $('body').on('click', '.remove-me', function(){
        $(this).closest('.checkbox').remove();
        //fireAjax('load-parts.json');
    });

    $('body').find("#customer-complaint").autocomplete({
            source: availableTags,
            select : function (event, ui) {
                //fireAjax('load-parts-checked.json');
            }
        });

    var identifier = [];
    var description = [];
    $.ajax({
        url : '/api/auto/spares',
        type: 'GET',
        success : function(response) {
            // response = JSON.parse(response);
            if (response.status == "success") {
                var availablePartsTags = [];
                response.data.forEach(function(value) {
                    availablePartsTags.push(value.description);
                    sparesTags.push(value);
                });



                $('body').find( ".description" ).autocomplete({
                    source: availablePartsTags,
                    select : function (event, ui) {
                        $('.parts').val(ui.item.identifier);
                        $('.price').val(ui.item.MRP);
                    }
                });

                sparesTags.forEach(function(part) {
                    identifier.push(Object.assign({
                        label:part.identifier
                    },part));

                    description.push(Object.assign({
                        label:part.description
                    },part));
                });

                $('body').find('.parts').autocomplete({
                      source: identifier,
                      select : function (event, ui) {
                          $('body').find('.description').val(ui.item.description);
                          $('body').find('.price').val(ui.item.MRP);
                          //$('body').find('.qty').val(ui.item.min_qty);
                      }
                });

                $('body').find('.description').autocomplete({
                      source: description,
                      select : function (event, ui) {
                          $('body').find('.parts').val(ui.item.identifier);
                          $('body').find('.price').val(ui.item.MRP);
                         // $('body').find('.qty').val(ui.item.min_qty);
                      }
                });
            }
        }
    });


    $('#kms').blur(function(){
        $.ajax({
            url : '/api/get/sch_maintenance',
            type: 'POST',
            dataType: 'json',
            data: {brand: $("#brand option:selected").val(), model: $("#jc").find( "input[name='model']" ).val(), fuel_type: $("#type option:selected").val(), km_ticked: $("#jc").find( "input[name='kms']" ).val()},
            success : function(response) {
                // response = JSON.parse(response);
                if (response.status == "success") {
                    var html = '<h4>Scheduled Service(s)</h4>';

                    response.services.forEach(function(service) {
                        $.each(service, function(key, value) {
                              var sluggable = slug(key);
                              html += '<div class="form-group checkbox">' +
                              '<input type="hidden" name="services[description]" class="services_description" value="'+key+'"/>' +
                             '<input name="service_items[]" value="1" class="services_availed" type="checkbox" id="'+sluggable+'" checked class="check-me">' +
                            '<label for="'+sluggable+'">'+key+'</label>'+
                            '<a class="remove-me"><i class="ion-ios-close"></i></a>' +
                            '</div>';
                        });
                    });

                    $('#service-items').html(html);

                }
            }
        });

        // sparesTags.forEach(function(part) {
        //     identifier.push(Object.assign({
        //         label:part.identifier
        //     },part));
        //
        //     description.push(Object.assign({
        //         label:part.description
        //     },part));
        // });
        loadParts();

        $('body').find('.parts').autocomplete({
              source: identifier,
              select : function (event, ui) {
                  $('body').find('.description').val(ui.item.description);
                  $('body').find('.price').val(ui.item.MRP);
                  //$('body').find('.qty').val(ui.item.min_qty);
              }
        });

        $('body').find('.description').autocomplete({
              source: description,
              select : function (event, ui) {
                  $('body').find('.parts').val(ui.item.identifier);
                  $('body').find('.price').val(ui.item.MRP);
                 // $('body').find('.qty').val(ui.item.min_qty);
              }
        });

    });

    $('body').on('change', '.check-me', function(){
        if ($(this).is(':checked')) {
            //fireAjax('load-parts-checked.json');
        } else {
             //fireAjax('load-parts.json');
        }
    });

    $('body').on('click', '.remove-this-row', function(e){
        e.preventDefault();
        $(this).closest('tr').remove();
        calculatePrice();
    });

    function calculatePrice() {
        var price = parseFloat(0);
        var total_price = $('body').find('.total_price');
        for (var i = 0; i < total_price.length;i++) {

          if (!isNaN($(total_price[i]).val()) && ($(total_price[i]).val()).length !=0) {
            price = parseFloat(price) + parseFloat($(total_price[i]).val());
          }



        }

        var oc = $('#oc').val();
        if ($.isNumeric(oc)) {
            oc = oc;
        } else {
            oc = 0;
        }

        // for(var i = 0; i < $('.total_price').length; i++) {
        //     if (!isNaN($($('.total_price')[i]).html())) {
        //         price = parseFloat(price) + parseFloat($($('.total_price')[i]).html());
        //     }
        // }
        $('#total-parts-cost').val(parseFloat(price)+parseFloat(oc));
        //$('#total-parts-cost').val(price);
        setTimeout(function(){
           $('#total-parts-cost').trigger('focus');
        }, 2000);
        
    }

    function loadParts() {
                    var html = "<div class='table-responsive'><table class='table'>" +
                    '<thead>' +
                    '<tr>'+
                        '<th>Parts</th>'+
                        '<th>Description</th>'+
                        '<th>Unit Price</th>'+
                        '<th>Qty</th>'+
                        '<th>Total Price</th>'+
                        '<th>Action</th>'+
                    '</tr>' +
                    '</thead><tbody>';
                    html += '<tr class="insert-after">'+
                    '<td><input type="text" class="form-control parts"/></td>'+
                    '<td><input type="text" class="form-control description sparesdescription"/></td>'+
                    '<td><input type="text" readonly disabled class="form-control price unit_price" id="u_price"/></td>'+
                    '<td><input type="number" min="0" class="form-control qty" id="quantity"/></td>'+
                    '<td><input type="text" class="form-control total_price" readonly id="tot_price"/></td>'+
                    '<td><a class="btn btn-success add-part">Add</a></td>'+
                    '</tr>'+
                    '</tbody></table></div>';
                    var price = 0;
                    $('#parts-estimation').html(html);
                    $('#total-parts-cost').val(price);
                    $('body').find('#total-parts-cost').trigger('focus');
                    $('body').find('#total-parts-cost').trigger('blur');
                    $('body').find('#total-estimation').trigger('focus');
                    $('body').find('#quantity').trigger('blur');


    }

    // $('body').on('click', '.delete-me', function(){
    //     $(this).closest('tr')
    // });

     $('body').on('click', '.add-part', function(e){
        e.preventDefault();

        var tr = $(this).closest('tr');
        var part = $(tr).find('.parts').val();
        var description = $(tr).find('.description').val();
        var price = $(tr).find('.price').val();
        var qty = $(tr).find('.qty').val();

        if (qty>0 && $.trim(part.length) >0 && $.trim(description.length) >0) {
          $(tr).find('.parts').val('');
          $(tr).find('.description').val('');
          $(tr).find('.price').val('');
          $(tr).find('.qty').val('');
          $(tr).find('#tot_price').val('');

          if ($.trim(part) && $.trim(description) && $.trim(price) && $.trim(qty) && !isNaN(price)) {
              var total_price = parseFloat(price) * parseFloat(qty);
              var html = '<tr>'+'<input type="hidden" value="-1" class="parts_ids" name="parts_ids[]">'+
                  '<td>'+part+'<input type="hidden" value="'+part+'" class="parts" name="parts[]"/></td>'+
                  '<td>'+description+'<input type="hidden" value="'+description+'" class="sparesdescription" name="sparesdescription[]"/></td>'+
                  '<td>'+price+'<input type="hidden" class="price unit_price" value="'+price+'" name="price[]"/></td>'+
                  '<td>'+qty+'<input type="hidden" value="'+qty+'" class="qty" id="qty" name="qty[]"/></td>'+
                  '<td>'+total_price+'<input type="hidden" class="total_price" id="total_price" value="'+total_price+'"</td>'+
                  '<td><a class="remove-this-row btn btn-danger btn-xs" href="#"><i class="ion-ios-trash-outline"></i></a></td>'+
                  '</tr>';
              $('body').find('.insert-after').after(html);
              calculatePrice();
          }
        } else {
          alert("Enter a valid part details");
        }

    });

    $('.transistion > .form-control').blur(function(){
        if (!$(this).val()) {
            $(this).closest('.form-group').find('label').removeClass('open');
        } else {
            $(this).closest('.form-group').find('label').addClass('open');
        }
    });

    if ($('.validate-form').length) {
        $('.validate-form').validate();
    }

    $('.form-control').focus(function(){
        $(this).closest('.form-group').find('label').addClass('open');
    });

    if ($('.datepicker').length) {
        $('.datepicker').datepicker({
            format : 'dd/mm/yyyy',
            autoclose: true,
            minDate: 0
        }).on('changeDate', function(ev){
            if (!$(this).val()) {
                $(this).closest('.form-group').find('label').removeClass('open');
            } else {
                $(this).closest('.form-group').find('label').addClass('open');
            }
        });
    }

    $('.show-sidebar').click(function(){
        $(this).toggleClass('active');
        $('#sidebar').toggleClass('open');
        new WOW().init();
    });

    if ($('.wow').length) {
        new WOW().init();
    }

    $('#oc').keyup(function(){
        calculatePrice();
    }).blur(function(){
        calculatePrice();
    });

    $('#labour-estimation').keyup(function(){
        updateCost();
    }).blur(function(){
        updateCost();
    });

    $('#total-parts-cost').keyup(function(){
        updateCost();
    }).blur(function(){
        updateCost();
    }).focus(function(){
        updateCost();
    });

    $('#quantity').blur(function(){
        computePartsCost();
    });

    function computePartsCost() {
        var price = $('tr').find('#u_price').val();
        var qty = $('tr').find('#quantity').val();
        var total_price = parseFloat(price) * parseFloat(qty);
        $('#tot_price').val(total_price);
    }

    $('.toggle-content').click(function(e){
        e.preventDefault();
        $($(this).attr('data-target')).removeClass('hidden');
        $(this).addClass('hidden');
    });

    function updateOtherCost() {
        var oc = $('#oc').val();
        if ($.isNumeric(oc)) {
            oc = oc;
        } else {
            oc = 0;
        }

        var cost = $('#total-parts-cost').val();
        if ($.isNumeric(cost)) {
            cost = cost;
        } else {
            cost = 0;
        }
        //Handle Other Prats calculation
        //var otherprice = $('tr').find('#other_price').val();
       // if ($.isNumeric(otherprice)) {
       //     otherprice = otherprice;
       // } else {
        //    otherprice = 0;
        //}
        $('#total-parts-cost').val(parseFloat(cost)+parseFloat(oc));
    }

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
        //Handle Other Prats calculation
        //var otherprice = $('tr').find('#other_price').val();
       // if ($.isNumeric(otherprice)) {
       //     otherprice = otherprice;
       // } else {
        //    otherprice = 0;
        //}
        $('#total-estimation').val(parseFloat(labour)+parseFloat(cost));
    }

    $( "#editjc" ).submit(function( event ) {
           event.preventDefault();
           var $form = $( this ),
           veh_numb = $form.find( "input[name='number']" ).val(),
           chasis_num = $form.find( "input[name='chasis']" ).val(),
           veh_brand = $('#brand :selected').text(),
           veh_model = $form.find( "input[name='model']" ).val(),
           f_type = $('#type :selected').text(),
           kms_ticked = $form.find( "input[name='kms']" ).val(),
           custr_name = $form.find( "input[name='cust_name']" ).val(),
           cont_numb = $form.find( "input[name='cont_num']" ).val(),
           cont_addr = $form.find( "input[name='cont_addr']" ).val(),
           delivery_time = $form.find( "input[name='delivery_time']" ).val(),
           lab_cost = $form.find( "input[name='labour_estimation']" ).val(),
           current_status = $('#status :selected').text(),
           jobcard_id = $form.find( "input[name='jobcard_id']" ).val(),
           pending_reason = $form.find( "input[name='reason']" ).val(),
           otherparts_desc = $form.find( "input[name='op']" ).val(),
           otherparts_cost = $form.find( "input[name='oc']" ).val();
           service_reminder_time = $form.find( "input[name='service-reminder-time']" ).val();
           if (current_status == "PENDING" && pending_reason.length == 0) {
               alert("Please enter the reason for jobcard pending");
           } else {
               var customerComplaints = [];
               var complaints = $('body').find('.customer-complaints');
               var complaints_id = $('body').find('.customer-complaints-ids');
               var checked = $('body').find('.customer-checkbox');

               for(var i = 0; i < complaints.length; i++) {
                   var temp = {};
                   temp.is_availed = ($(checked[i]).is(':checked')) ? $(checked[i]).val() : 0;
                   temp.description = $(complaints[i]).val();
                   var comp_id = $(complaints_id[i]).val();
                   temp.id = comp_id.length !=0 ? comp_id : "-1";
                   customerComplaints[i] = temp;
               }

               var spares      = [];
               var parts       = $('body').find('.parts');
               var description = $('body').find('.sparesdescription');
               var price       = $('body').find('.price');
               var qty         = $('body').find('.qty');
               var total_price = $('body').find('.total_price');
               var partsids = $('body').find('.parts_ids');

               for (var i = 0; i < parts.length;i++) {
                  var temp            =  {};
                  if (!(($(parts[i]).val()).length == 0)) {
                    temp.identifier  = $(parts[i]).val();
                    temp.description = $(description[i]).val();
                    temp.unit_price  = $(price[i]).val();
                    temp.qty         = $(qty[i]).val();
                    temp.total_price = $(total_price[i]).val();
                    temp.id = $(partsids[i]).val();

                    if (temp['identifier'] && temp['description'] && temp['unit_price'] && temp['qty']) {
                        spares.push(temp);
                    }
                  }
               }
               
               var recommendedServices = [];
               var recommendedserviceitems = $('body').find('.recommended-items');

               for(var i = 0; i < recommendedserviceitems.length; i++) {
                   recommendedServices[i] = $(recommendedserviceitems[i]).val();
               }

               if (!(customerComplaints.length == 0)) {
                   var url = $form.attr( "action" );
                   var data = JSON.stringify({ data : { jc_id: jobcard_id,labour_cost: lab_cost, veh_num: veh_numb, c_num: chasis_num, brand: veh_brand, model: veh_model, fuel_type: f_type, cust_name: custr_name, cont_num: cont_numb, cont_address: cont_addr, km_ticked: kms_ticked, del_time: delivery_time, reason: pending_reason, status: current_status, services : customerComplaints, spares: spares, recommendedservices : recommendedServices, otherparts_desc: otherparts_desc, otherparts_cost:otherparts_cost,service_reminder_time:service_reminder_time }});
                  //  Send the data using post
                   var posting = $.post( url, data);
                   posting.done(function( data ) {
                       if (data.status == "failure") {
                           alert(data.msg);
                       } else if (data.status == "success"){
                           window.location.replace(data.url);
                       }
                       else {
                           alert("Oops!! Something went wrong!");
                       }
                   });
               }

           }

    });


    // Attach a submit handler to the form
    $( "#jc" ).submit(function( event ) {

       
       event.preventDefault();
       var $form = $( this ),
       veh_numb = vehNumb,
       imgInput = $('#imgInp')[0].files[0],
       chasis_num = $form.find( "input[name='chasis']" ).val(),
       veh_brand = $('#brand :selected').text(),
       veh_model = $form.find( "input[name='model']" ).val(),
       f_type = $('#type :selected').text(),
       kms_ticked = $form.find( "input[name='kms']" ).val(),
       custr_name = $form.find( "input[name='cust_name']" ).val(),
       cont_numb = $form.find( "input[name='cont_num']" ).val(),
       cont_addr = $form.find( "input[name='cont_addr']" ).val(),
       delivery_time = $form.find( "input[name='delivery_time']" ).val(),
       lab_cost = $form.find( "input[name='labour_estimation']" ).val(),
       otherparts_desc = $form.find( "input[name='op']" ).val(),
       otherparts_cost = $form.find( "input[name='oc']" ).val(),
       mechanic_name = $form.find( "input[name='mechanic_name']" ).val(),
       service_type = $('#serviceType :selected').val();
       // service_type_class = []
       
       //  $('input[name=' + $('#serviceType :selected').val() +']:checked').each(function(){ 
       //      service_type_class.push($(this).val());
       //  });

       d_reason = "";
       
       if (!(veh_numb.length === 0 || veh_brand.length === 0 || veh_model.length === 0 || f_type.length === 0 || kms_ticked.length === 0 ||
         custr_name.length === 0 || cont_numb.length === 0 || delivery_time.length === 0 || lab_cost.length === 0)) {
           var services           = [];
           var serviceDescription = $('body').find('.services_description');
           var serviceAvailed     = $('body').find('.services_availed');

           for (var i = 0; i < serviceDescription.length; i++) {
              var temp         = {};
              temp.is_availed  = ($(serviceAvailed[i]).is(':checked')) ? $(serviceAvailed[i]).val() : 0;
              temp.description = $(serviceDescription[i]).val();
              services.push(temp);
           }

           var spares      = [];
           var parts       = $('body').find('.parts');
           var description = $('body').find('.sparesdescription');
           var price       = $('body').find('.unit_price');
           var qty         = $('body').find('.qty');
           var total_price = $('body').find('.total_price');

           for (var i = 0; i < parts.length;i++) {
              var temp            =  {};
              temp.identifier  = $(parts[i]).val();
              temp.description = $(description[i]).val();
              temp.price       = $(price[i]).val();
              temp.qty         = $(qty[i]).val();
              temp.total_price = $(total_price[i]).val();
              if (temp['identifier'] && temp['description'] && temp['price'] && temp['qty']) {
                  spares.push(temp);
              }
           }

           var customerComplaints = [];
           var complaints = $('body').find('.customer-complaints');
           var checked = $('body').find('.customer-checkbox');

           for(var i = 0; i < complaints.length; i++) {
               var temp = {};
               temp.is_availed = ($(checked[i]).is(':checked')) ? $(checked[i]).val() : 0;
               temp.description = $(complaints[i]).val();
               customerComplaints[i] = temp;
           }

           var recommendedServices = [];
           var recommendedserviceitems = $('body').find('.recommended-items');

           for(var i = 0; i < recommendedserviceitems.length; i++) {
               recommendedServices[i] = $(recommendedserviceitems[i]).val();
           }

           var all_services = $.merge(services, customerComplaints);
           
           if (!(all_services.length == 0)) {
               var url = $form.attr( "action" );

               var data = { data : {  service_type : service_type, mechanic_name : mechanic_name, labour_cost: lab_cost, veh_num: veh_numb, c_num: chasis_num, brand: veh_brand, model: veh_model, fuel_type: f_type, cust_name: custr_name, cont_num: cont_numb, cont_address: cont_addr, km_ticked: kms_ticked, del_time: delivery_time, reason: d_reason, status: "OPEN", services : all_services, spares: spares, recommendedservices : recommendedServices, otherparts_desc: otherparts_desc, otherparts_cost:otherparts_cost}};
               // Send the data using post
            
               var posting = $.post( url, data);
               posting.done(function( data ) {
                   if (data.status == "failure") {
                       alert(data.msg);
                   } else if (data.status == "success"){
                       window.location.replace(data.url);
                   }
                   else {
                       alert("Oops!! Something went wrong!");
                   }
               });
           }

       }

    });

    // $('.serviceTypeCheckbox').hide();
    // $('#'+$('#serviceType :selected').text()).show();

    // $("#serviceType").change(function () {
    //     $('.serviceTypeCheckbox').hide();
    //     $('#'+$('#serviceType :selected').text()).show();
    // });

    // $('#number').keypress(function(){
    //    if(vehicleNumbStatus == 'correct') {
    //          console.log($('#number').val());
    //     }
    // });
    // $('#number').change(function() {
    //     if(vehicleNumbStatus == 'correct') {
    //          console.log($('#number').val());
    //     }
   
    // });

    function vehNumbDetails(value) {
        $.get("/apis/jobcard/v1/user/vehicle", {vehicle_registration_number: value}, function(data, status){
          
            if(data['vehicle_data']['chassis_number']) {
                $("label[for='"+ 'chasis'+"']").addClass('open');
                $('#jc').find( "input[name='chasis']" ).val(data['vehicle_data']['chassis_number']);
            }
            if(data['vehicle_data']['model_name']) {
                $("label[for='"+ 'model'+"']").addClass('open');
                $('#jc').find( "input[name='model']" ).val(data['vehicle_data']['model_name']);
            }
            if(data['vehicle_data']['total_kms']) {
                $("label[for='"+ 'kms'+"']").addClass('open');
                $('#jc').find( "input[name='kms']" ).val(data['vehicle_data']['total_kms']);
            }
            if(data['vehicle_data']['brand_name']) {
                
               $('#brand').val(data['vehicle_data']['brand_name']);
            }
            if(data['vehicle_data']['fuel_type']) {
                
               $('#type').val(data['vehicle_data']['fuel_type']);
            }

        }).fail(function(data,status){
            // console.log("issue");
            console.log(status);
            // console.log(data);
            // return true;
        });
    }


    function vehNumbcheckDetails() {
        var veh_numb1 = $('#jc').find( "input[id='veh-numbr1']" ).val();
        var veh_numb2 = $('#jc').find( "input[id='veh-numbr2']" ).val();
        var veh_numb3 = $('#jc').find( "input[id='veh-numbr3']" ).val();
        var veh_numb4 = $('#jc').find( "input[id='veh-numbr4']" ).val();

        vehNumb = veh_numb1 + " "+ veh_numb2 + " " + veh_numb3 + " " + veh_numb4;

        if(vehNumb1Status == true && vehNumb2Status == true && vehNumb3Status == true && vehNumb4Status == true && prvVehNumbr != vehNumb) {
            prvVehNumbr = vehNumb;
            vehNumbDetails(vehNumb);

        }
    }



    // $.formUtils.addValidator({
    //     name : 'veh_numb',
    //     validatorFunction : function(value, $el, config, language, $form) {
           
    //         if(value.length == 10 && value.slice(0,2).match(/^[a-z]+$/gi)  && $.isNumeric(value.slice(2,4)) &&  value.slice(4,6).match(/^[a-z]+$/gi) &&  $.isNumeric(value.slice(6,10))) {
    //                 // vehicleNumbStatus = 'correct';
    //                 // console.log("checking once again");
    //                 vehNumbDetails(value);
    //                 // console.log("issue solved");
    //                 return true;
    //         }
                            
    //         else { vehicleNumbStatus = 'incorrect'; return false;}
            

    //     },
    //     errorMessage : 'Enter valid vehicle number',
    //     errorMessageKey: 'badVehNumber'
    // });

    vehNumb1Status = false;
    vehNumb2Status = false;
    vehNumb3Status = false;
    vehNumb4Status = false;
    prvVehNumbr = "";
    vehNumbcheckDetails();

    $.formUtils.addValidator({
        name : 'veh_numb1',
        validatorFunction : function(value, $el, config, language, $form) {
            if(value.length == 2 &&  value.match(/^[a-z]+$/gi))   {
                vehNumb1Status = true;
                vehNumbcheckDetails();
                return true;
            }

            else {
                vehNumb1Status = false;
                return false;
            }

        },

        errorMessage : 'Enter valid vehicle number',
        errorMessageKey: 'badVehNumber'
    });


    $.formUtils.addValidator({
            name : 'veh_numb2',
            validatorFunction : function(value, $el, config, language, $form) {
                if(value.length == 2 &&  $.isNumeric(value))  {
                    vehNumb2Status = true;
                    vehNumbcheckDetails();
                    return true;
                }
                else { 
                    vehNumb2Status = false;
                    return false;
                }

            },

            errorMessage : 'Enter valid vehicle number',
            errorMessageKey: 'badVehNumber'
    });

    $.formUtils.addValidator({
        name : 'veh_numb3',
        validatorFunction : function(value, $el, config, language, $form) {
            if(value.length >=1 &&  value.match(/^[a-z]+$/gi) && value.length <= 2)   {
                vehNumb3Status = true;
                vehNumbcheckDetails();
                return true;
            }

            else {
                vehNumb3Status = false;
                return false;
            }

        },

        errorMessage : 'Enter valid vehicle number',
        errorMessageKey: 'badVehNumber'
    });

    $.formUtils.addValidator({
        name : 'veh_numb4',
        validatorFunction : function(value, $el, config, language, $form) {
            if(value.length == 4 && $.isNumeric(value) )   {
                vehNumb4Status = true;
                vehNumbcheckDetails();
                return true;
            }

            else {
                vehNumb4Status = false;
                return false;
            }

        },

        errorMessage : 'Enter valid vehicle number',
        errorMessageKey: 'badVehNumber'
    });

    $.validate();

    // vehicleNumbStatus = 'incorrect';






    $(document).on('change', '.btn-file :file', function() {
    var input = $(this),
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.trigger('fileselect', [label]);
    });

    $('.btn-file :file').on('fileselect', function(event, label) {
        
        var input = $(this).parents('.input-group').find(':text'),
            log = label;
        
        if( input.length ) {
            input.val(log);
        } 
    
    });
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            
            reader.onload = function (e) {
                $('#img-upload').attr('src', e.target.result);
            }
            
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imgInp").change(function(){
        readURL(this);

    });     
});
