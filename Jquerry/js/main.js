function consultaCep(){
    var cep= document.getElementById('cep').value
    var url= "https://viacep.com.br/ws/"+ cep +"/json/"
    $.ajax({
        url: url,
        type: "GET",
        success: function (response){
            $(".bar").show();
            $('#rua').html(response.logradouro);//o mesmo que: document.getElementById('rua').innerHTML= response.logradouro;
            $('#bairro').html(response.bairro);
            $('#cidade').html(response.localidade);
            $('#uf').html(response.uf);
            $('#titulo').html(response.cep);
            $(".cep").show();
            $(".bar").hide()
        }
    })
}

$(function(){
    $(".cep").hide();
    $(".bar").hide();
});