let mybutton = document.getElementById("back-to-top");

window.onscroll = function () {
    if (document.documentElement.scrollTop > 80) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
};

mybutton.addEventListener("click", ()=>{
    window.scrollTo({top: 0, behavior: 'smooth'});
});