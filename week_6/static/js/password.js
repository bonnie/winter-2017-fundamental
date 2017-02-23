$('#submit-pass').on('click', function(evt) {

    // evt.preventDefault();

    console.log('starting submit event handler');

    var oldpass = $('#oldpass').val();
    var newpass = $('#newpass').val();

    data = {'old': oldpass,
            'new': newpass}

    $.post('/change_password', data, function(response) {

        console.log(response);

    });


});