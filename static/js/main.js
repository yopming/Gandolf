$(document).ready(function() {
    
    // pass the qrcode to modal
    $(".dev_gen_link").bind("click", function() {
        var _this = $(this);
        var _realBottle = _this.parent().siblings('.involve').children('a');
        var _realBottleSpice = _realBottle.attr('data-spice');
        var link_href = '';
        if (_realBottleSpice == 'file') {
            link_href = encodeURI(_realBottle.attr('href'));
        } else if (_realBottleSpice == 'folder') {
            link_href = location.host + encodeURI(_realBottle.attr('href'));
        }

        // shorten url
        shorten_link_href = '';
        $.post(
            "http://demo.vemic.com:3590/j/shorten",
            {
                url: link_href
            },
            function(data) {
                shorten_link_href = data['shorten'];
                $(".dev_gened_link").text(shorten_link_href);
                $("#DEV-modal").modal('show');
            }
        );
    });

    $('#DEV-modal').on('hidden.bs.modal', function() {
        $(".dev_gened_link").text('');
    });
});
