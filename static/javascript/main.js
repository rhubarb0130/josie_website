//Copyright (c) 2020 Josephine Peacock all rights reserved


$(function() {
    var documentEl = $(document),
        fadeElem = $('.fade-scroll, .container, .icon_panel');

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

//sidepanel functions
function openNav() {
  document.getElementById("mySidepanel").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidepanel").style.width = "0";
}
