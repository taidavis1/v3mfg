$(document).ready(function(){

    $('form').on('submit' , function(event){

        $.ajax({

            data: {

                name: $('#name').val(),

                email: $('#email').val(),

                messages: $('#messages').val(),

            },

            type: 'POST',

            url: '/Company',


        })

        .done(function(data){

            if (data.success){

                $('#v3_form').hide();

                $('#message_form').show();


            }

        });

        event.preventDefault();

    });


});