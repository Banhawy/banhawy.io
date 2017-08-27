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

var typed = new Typed('.monitor', {
    strings: ["a Web Developer.", "a Blogger.", "a Gamer.", "a technology enthusiast.", "a Software Engineer."],
    typeSpeed: 90,
    smartBackspace: true,
    backSpeed: 20,
    backDelay: 2000,
    loopCount: 3
  });