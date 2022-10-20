//NAVBAR VARIABLES
const navMobile = document.getElementById("navMobile");
const navList = document.getElementById("navList");

//LOGIN/REG VARIABLES
const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");
const loginBtn = document.getElementById("loginBtn");
const registerBtn = document.getElementById("registerBtn");


//NAVBAR FUNCTIONALITY
navMobile.addEventListener("click", () => {
    navList.classList.toggle("active");
})

document.querySelectorAll(".nav__list-link").forEach( e => e.addEventListener("click", () => {
    navList.classList.remove("active");
}))


//LOGIN/REG FUNCTIONALITY
loginBtn.addEventListener("click", () => {
    loginBtn.classList.toggle("active");
    registerBtn.classList.toggle("active");
    loginForm.classList.toggle("active");
    registerForm.classList.toggle("active");
})

registerBtn.addEventListener("click", () => {
    loginBtn.classList.toggle("active");
    registerBtn.classList.toggle("active");
    loginForm.classList.toggle("active");
    registerForm.classList.toggle("active");
})
