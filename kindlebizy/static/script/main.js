/* Smooth scrolling */
$(document).on('click', '.about1', function(event){
    event.preventDefault();

    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
}); 
$(document).on('click', '.order1', function(event){
    event.preventDefault();

    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
}); 
$(document).on('click', '.home1', function(event){
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

        $('div.left').remove();
        $('div.right').remove();
    }
});
$(function() {
    if (window.matchMedia("(max-width:150px)" && "(max-width:680px)").matches) {

        $('nav.desktop').remove();
        $('nav.mobile').add();
        $('div.mainabout').remove();
        $('div#order').remove();
        $('div.order').remove();
    }
    else{
         $('nav.desktop').add();
        $('nav.mobile').remove();

    }
});