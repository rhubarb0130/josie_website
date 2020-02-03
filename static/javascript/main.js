//Copyright (c) 2020 Josephine Peacock all rights reserved


$(function() {
    var documentEl = $(document),
        fadeElem = $('.fade_up');

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
    // get screen width to be responsive
    var width = screen.width;
    if (width < 1000){
    document.getElementById("mySidepanel").style.width = "75%";
    }else{
    document.getElementById("mySidepanel").style.width = "350px";
    }
}
function closeNav() {
    document.getElementById("mySidepanel").style.width = "0";
}
