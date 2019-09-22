$(document).ready(function() {
    //toggle the component with class slideout
    $(".box").click(function() {
      if ($('.slideout').is(':visible')) {
        $(".slideout").slideUp(300);
        $(".plusminus").text('+');
      }
      if ($(this).next(".slideout").is(':visible')) {
        $(this).next(".slideout").slideUp(300);
        $(this).find(".plusminus").text('+');
      } else {
        $(this).next(".slideout").slideDown(300);
        $(this).find(".plusminus").text('–');
      }
    });
  });
