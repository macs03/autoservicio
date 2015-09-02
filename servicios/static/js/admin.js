$(function(){
	
	/**************************************************************

		FACTURACIÓN; CALCULOS; Y TODO SOBRE LA FACTURACIÓN

	***************************************************************/
	/********************************
		SELECT2
	************************************/
	$(".multiple-select").select2({
		  placeholder: "Seleccione un producto"
	});

/*	$(".option").click(function  () {
	 	
		var atributo = $(".option").attr('data-cantidad');
		
		var identificador = "#cantidad-"+atributo;
		console.log(identificador);
		$(identificador).css("display","block");


	});*/

	function getServicios(id){
		$.ajax({
			url: 'http://localhost:8000/administracion/getservicios/',
			type: 'post',
			data: {
				"id": id
			},
			success : function(json) {
				console.log("añadiendo el vacio");
                console.log(json);
                $('#serviciosRealizado').empty();
                $('#serviciosRealizado').append($('<option>', {
                    value: '0',
                    text: 'N/A'
                }));
                for (var i = json.length - 1; i >= 0; i--) {
					 $('#serviciosRealizado').append($('<option>', {
					 		value: json[i]['id'],
					 		text: json[i]['servicio']+' - '+json[i]['vehiculo_cliente']+' - '+json[i]['fecha']+' - '+json[i]['costo']
					 }));
				};
      	    },
	        error : function(xhr,errmsg,err) {
	           console.log(err);
	           console.log(xhr);

        	}
   
		});
	}

	$('#selectCliente').click(function(){
		var id = $('#selectCliente').val()
		getServicios(id);
	});
	
   var totalServ = 0;
   var totalPro = 0;
    $( "#serviciosRealizado" ).change(function() {
		    var str = "";
		     var servicios=[] 
		    var precioStr = "";	
		     var precio = 0;
		     var  precioTotal;
		    $( "#serviciosRealizado option:selected" ).each(function() {

		      str += $( this ).text() + "_";
		    	console.log(str);
		    });

		  servicios = str.split('_')
		  for (var i = servicios.length - 1; i >= 0; i--) {
		  	if(servicios[i].split('-')[6]){
		  		precioStr = servicios[i].split('-')[6];
		  		precio = precio + parseInt(precioStr);
		  		
		  	}
		  	console.log(precioStr);
		  };
		  totalServ =  precio;
		  
    })
	.trigger( "change" );

	var proGlbl = [];	
	 $( "#listProducts" ).change(function() {
		    var str = "";
		    var productos=[] 
		    var precioStr = "";	
		    var precio = 0;
		    var  precioTotal;
		    $( "#listProducts option:selected" ).each(function() {
		      str += $( this ).text() + "_";
		      

		    });
		    productos = str.split('_');
			  for (var i = productos.length - 1; i >= 0; i--) {
			  	if(productos[i].split('-')[1]){
			  		precioStr = productos[i].split('-')[1];
			  		precio = precio + parseInt(precioStr) ;
			  		
			  	}
			  };
	      proGlbl = productos;		  
	     totalPro = precio;
    })
	.trigger( "change" );


	 
	
	

	$('#totalInput').click(function(){
		console.log(proGlbl);
		var precioT = 0;
		var precio = 0;
		var precioStr ="";
		for (var i =0; i< proGlbl.length - 1; i++) {
			  	if(proGlbl[i].split('-')[1]){
			  		var producto = proGlbl[i].split('-')[0];
			  		console.log(producto);
			  		
			  	    $('.input-producto').each(function(){
			  	    	if( proGlbl[i] === $(this).data('producto')){
			  	    		precioStr = proGlbl[i].split('-')[1];
			  	    		precio = parseInt(precioStr) * $(this).val();
			  	    		console.log("Precio--"+ precio);
			  	    		precioT = precioT + precio;
			  	    		
			  	    	}
			  	    });
			  		
			  	}
			  };
			  console.log(precioT);
		$('#totalInput').val(totalServ+precioT);
	})
	/************
	datepicker de factura
	************/

	
	 $('#datepicker').datepicker({
	   dateFormat: "yy-mm-dd",
       numberOfMonths: 2,
         showWeek: true
	});

    $('#id_fecha_fin').datepicker({
       dateFormat: "yy-mm-dd",
       numberOfMonths: 2,
        showWeek: true
   });

    $('#id_fecha_inicio').datepicker({
       dateFormat: "yy-mm-dd",
       numberOfMonths: 2,
        showWeek: true
   });

    $('#id_fecha').datepicker({
       dateFormat: "yy-mm-dd",
       numberOfMonths: 2,
        showWeek: true
   });
    var productosCant = []

    $('.option').on('click', function(){
    	var selected = $(this)[0].selected;
    	var value = $(this).data('cantidad');
    	if(selected){
    		$('#'+value).css('display', 'block');
    	}else{
    		$('#'+value).css('display', 'none');
    	}
    });

	 /*****************************
	   FUNCION DE RELOJ
	 *****************************/
	



});

var cantidad = function  (arg) {
	//alert(arg)us
	
	console.log("#cantidad-"+arg)
	var identificador = "cantidad-"+arg
	document.getElementById(identificador).style.display='block';
}
