$(document).ready(function() {
    
    // pass the qrcode to modal
    $(".dev_toggle_modal").bind("click", function() {
        var link_href = encodeURI($(this).attr('data-href'));
        var link_real = $(this).attr('data-real');
        var file_name = $(this).find(".dev_toggle_modal_name").text().trim();

        // shorten url
        shorten_link_href = '';
        $.post(
            "http://demo.vemic.com:3590/j/shorten",
            {
                url: link_href
            },
            function(data) {
                shorten_link_href = data['shorten'];
                $("#DEV_QRCODE").qrcode({
                    width   :   250,
                    height  :   250,
                    color   :   '#f60',
                    text    :   data['shorten']
                });
            }
        );

        $('#QRModal').modal('show').on('shown.bs.modal', function() {
            $('.dev_modal_title').text(file_name);
            $('.dev_modal_reallink').attr('href', link_real);
        });

        // clea previous qrcode
        $('#QRModal').on('hidden.bs.modal', function() {
            $("#DEV_QRCODE").html('');
            $("#QRModal .dev_modal_title").text(' ');
            $("#QRModal .dev_modal_reallink").attr('href', ' ');
        });
    });

    // tooltip
    $("#DEV-h1").tooltip('toggle');
    $("#DEV-h1").tooltip('hide');

});
