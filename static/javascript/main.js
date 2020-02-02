//Copyright (c) 2020 Josephine Peacock all rights reserved


$(function() {
    var documentEl = $(document),
        fadeElem = $('.fade-scroll, .container');

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
