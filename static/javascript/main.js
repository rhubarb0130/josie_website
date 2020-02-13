//Copyright (c) 2020 Josephine Peacock all rights reserved


$(function() {
    var documentEl = $(document);
    var fadeElem = $('.fade_up');

    documentEl.on('scroll', function() {
        var currScrollPos = documentEl.scrollTop();

        fadeElem.each(function() {
            var fade_obj = $(this);
            var elemOffsetTop = fade_obj.offset().top;

            if (currScrollPos > elemOffsetTop) fade_obj.css('opacity', 1 - (currScrollPos-elemOffsetTop)/400);
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
