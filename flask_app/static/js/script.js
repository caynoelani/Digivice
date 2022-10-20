//NAVBAR VARIABLES
const navMobile = document.getElementById("navMobile");
const navList = document.getElementById("navList");


// NAVBAR FUNCTIONALITY
navMobile.addEventListener("click", () => {
    navList.classList.toggle("active");
})

document.querySelectorAll(".nav__list-link").forEach( e => e.addEventListener("click", () => {
    navList.classList.remove("active");
}))

