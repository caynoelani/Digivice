const navMobile = document.getElementById("navMobile");
const navList = document.getElementById("navList");

navMobile.addEventListener("click", () => {
    navList.classList.toggle("active");
})

document.querySelectorAll(".nav__list-link").forEach( e => e.addEventListener("click", () => {
    navList.classList.remove("active");
}))