//Copyright (c) 2020 Josephine Peacock all rights reserved

//$(window).on("load",function() {
//  $(window).scroll(function() {
//    var windowBottom = $(this).scrollTop() + $(this).innerHeight();
//    $(".fade").each(function() {
//      /* Check the location of each desired element */
//      var objectBottom = $(this).offset().top + $(this).outerHeight();
//
//      /* If the element is completely within bounds of the window, fade it in */
//      if (objectBottom < windowBottom) { //object comes into view (scrolling down)
//        if ($(this).css("opacity")==0) {$(this).fadeTo(500,1);}
//      }else { //object goes out of view (scrolling up)
//        if ($(this).css("opacity")==1) {$(this).fadeTo(500,0);}
//      }
//    });
//  }).scroll(); //invoke scroll-handler on page-load
//});

$(function() {
    var documentEl = $(document),
        fadeElem = $('.fade-scroll');

    documentEl.on('scroll', function() {
        var currScrollPos = documentEl.scrollTop();
//        console.log(currScrollPos);

        fadeElem.each(function() {
            var $this = $(this),
                elemOffsetTop = $this.offset().top;
            if (currScrollPos > elemOffsetTop) $this.css('opacity', 1 - (currScrollPos-elemOffsetTop)/400);
        });
    });

});
