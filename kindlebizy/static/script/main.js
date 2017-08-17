/* Smooth scrolling */
$(document).on('click', 'a', function(event){
    event.preventDefault();

    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
}); 

    $(window).scroll(function() {
        if ($(this).scrollTop() > 390) {
           
             $('.top').addClass('add');
        } else {
         $('.top').removeClass('add');
        }
    });

/* removes div button on screen resize*/
$(function() {
    if (window.matchMedia("(max-width:150px)" && "(max-width:680px)").matches) {

        $('div.one').remove();
        $('div.shield').remove();
    }
});