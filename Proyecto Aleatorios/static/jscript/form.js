/*Para ir creando dinamicamente los inputs de los parametros*/
$(document).ready(function(){
    $(window).bind("pageshow", function() {
        $("#numRestricciones").val("");
        $("#tamPoblacion").val("");
        $("#numPoblaciones").val("");
        $("#funcionObjetivo").val("");
        $("#restric").remove();
        $("#negatividad").prop("checked", true);
        var noRestricciones = 0;
        $("#gifLoad").hide();
        $("#btnRestricciones").attr("disabled", false); 
    });
    

    $("#formulario").validetta({
        bubblePosition: "bottom",
        bubbleGapTop: 10,
        bubbleGapLeft: -5,
        onError:function(e){
            e.preventDefault();
            $.confirm({
                icon: "fa fa-exclamation-triangle",
                title: "Campos vacíos",
                content: "Por favor, rellene los campos obligatorios",
                type :"red",
                typeAnimated: true,
                buttons: {
                    tryAgain: {
                        text: "Entendido",
                        btnClass: "btn-red",
                        action: function(){
                        }
                    },
                }
            });
        }
    });
    
    $("#btnRestricciones").click(function(){
        /*Leemos el numeros de restricciones*/
        noRestricciones = $("#numRestricciones").val(); 
        

        /*Si no es vacio, creamos los inputs para las restricciones*/
        if(noRestricciones != ""){
            $("#btnRestricciones").attr("disabled", true); 
            nuevoDiv = "<div class = 'row' id = 'restric'></div>";
             $("#formulario").append(nuevoDiv);
            for(var i = 0; i < noRestricciones; i++){
                var nuevoInput = 
                    "<div class = 'col s12 m6 offset-m3 input-field'>" +
                    "<label for = 'lblRestriccion' id = 'lblRestriccion'>Restriccion No. " + (i + 1) + "</label>" +
                    "<input type = 'text' id = 'restriccion' name = 'restriccion' data-validetta='required' /></p>" +
                    "</div>";
                
                /*Añadimos los inputs al formulario (metodo POST)*/
                $('#restric').append(nuevoInput);
            }

            var submit = 
                    "<div class='col s12 m6 offset-m3 input-field'>" +
                    "<button type='submit' id='btnCalcular' name = 'btnCalcular' class='waves-effect waves-light btn-small' style='width: 100%'>Calcular</button>" +
                    "</div>";

            /*Añadimos el submit*/
            $('#restric').append(submit);
        }
    });

    $("#btnLimpiar").click(function(){
        $("#numRestricciones").val("");
        $("#tamPoblacion").val("");
        $("#numPoblaciones").val("");
        $("#funcionObjetivo").val("");
        $("#restric").remove();
        $("#negatividad").prop("checked", true);
        $("#btnRestricciones").attr("disabled", false); 
    });
});