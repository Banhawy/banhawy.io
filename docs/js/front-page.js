$(document).ready(function() {
    //Hide Cards
    $('.about').hide();

    $(".front-hero").hide().animate({
        right: 1000
    }).show("fast", function() {
        //Show Hero Banner and Slide into screen
        $(this).show().animate({
            left: 0
        });

        $('.about').show(900, function showNext() {
            $(this).fadeIn(400).next().show(900, showNext);
        });
    });
})