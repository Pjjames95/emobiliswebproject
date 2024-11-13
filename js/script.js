document.addEventListener("DOMContentLoaded", function () {
   let myDiv = document.getElementById("footersection")
    console.log(myDiv)
    let emptypara = document.getElementById("emptypara")
    emptypara.innerText = "this is my portfolio"
    emptypara.setAttribute("class", "styledpara")
    emptypara.style.fontSize='20px'
    emptypara.style.borderRadius="20px"
})