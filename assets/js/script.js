function redirectToHome(){
    document.getElementById("transition-overlay").style.opacity = "1";
    document.getElementById("transition-overlay").style.zIndex = "2";
    setTimeout(function(){
      window.location='/';
    }, 1000);
}
