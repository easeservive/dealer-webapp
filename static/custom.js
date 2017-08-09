$(function () {
      $("#meshanchor").click(function () {
        $('html, body').animate({
          scrollTop: $("#mesh").offset().top
        }, 700);
      });
      $("#contactanchor").click(function () {
        $('html, body').animate({
          scrollTop: $("#contact").offset().top
         }, 1500);
      });
      $("#aboutanchor").click(function () {
        $('html, body').animate({
          scrollTop: $("#about").offset().top
        }, 1500);
      });
      $("#fetchschmaint").click(function(e){
        e.preventDefault();
         $.get("/test/", function(data, status){
           sch_div = document.querySelector('#scheduledMaintenance');
           fetch_div = document.querySelector('#fetchButton');
           fetch_div.innerHTML = '';
           sch_div.innerHTML = data.scheduled;
           document.querySelector('#inputbox').style.display = 'block';
           document.querySelector('#addjobbtn').style.display = 'block';
           //job_div = document.querySelector('#inputbox');
           //job_div.innerHTML = '<input id="inputjob" type="text" name="inputjob" placeholder="Enter Job"/>'
           //job_div = document.querySelector('#addjobbtn');
           //job_div.innerHTML = '<input id="addjob" type="submit" value="Add Job" style="padding-top:7px;padding-bottom:7px;height:37px"/>'
         });
      });
      $("#addjob").click(function(e){
        e.preventDefault();
        sch_div = document.querySelector('#scheduledMaintenance');
        var job = document.getElementById('inputjob').value;
        document.getElementById('inputjob').value = "";
        sch_div.innerHTML += '<input type="checkbox" name="'+ job +'" value="'+ job +'" checked="checked"> '+ job +'<br>' 
      });

});

window.onload = function() {

  document.querySelector('#inputbox').style.display = 'none';
  document.querySelector('#addjobbtn').style.display = 'none';

  var cars = {'Audi'           : ['A3','A3 CABRIOLET','A4','A6','A8 L','Q3','Q5','Q7','R8','RS5','RS6','RS7 SPORT BACK','S6','TT'],
              'BMW'            : ['1 SERIES','3 SERIES','3 SERIES GT','5 SERIES','6 SERIES','7 SERIES','BMW M3','BMW M4','BMW M5','BMW M6','BMW i8','X1','X3','X5','X6','Z4'],
              'Chevrolet'      : ['BEAT','CAPTIVA','CRUZE','ENJOY','SAIL','SAIL HATCH BACK','SPARK','TAVERA'],
              'Datsun'         : ['GO ','GO PLUS'],
              'Fiat'           : ['AVVENTURA','LINEA','LINEA CLASSIC','500- ABBARTH','PUNTO'],
              'Force'          : ['FORCE ONE','GURKHA'],
              'Ford'           : ['CLASSIC','ECO SPORTS','ENDEAVOUR','FIESTA ','FIGO','FIGO ASPIRE','FUSION','IKON'],
              'Honda'          : [],
              'Hyundai'        : [],
              'ICML'           : [],
              'ISUZU'          : [],
              'Jaguar'         : [],
              'Land Rover'     : [],
              'Mahindra'       : [],
              'Maruthi Suzuki' : [],
              'Mercedes Benz'  : [],
              'Mini'           : [],
              'Mitsubishi'     : [],
              'Nissan'         : [],
              'Porsche'        : [],
              'Renault'        : [],
              'Skoda'          : [],
              'Ssangyong'      : [],
              'Tata'           : [],
              'Toyota'         : [],
              'Volkswagen'     : [],
              'Volvo'          : []
  }
  
  brand_select = document.querySelector('#brand');
  model_select = document.querySelector('#model');

  setOptions(brand_select, Object.keys(cars));
  setOptions(model_select, cars[brand_select.value]);
  
  brand_select.addEventListener('change', function() {
    setOptions(model_select, cars[brand_select.value]);
  });
    
  function setOptions(dropDown, options) {
    dropDown.innerHTML = '';
    options.forEach(function(value) {
      dropDown.innerHTML += '<option name="' + value + '">' + value + '</option>';
    });
  }  
};
