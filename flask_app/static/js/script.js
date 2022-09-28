const navMobile = document.getElementById("navMobile");
const navList = document.getElementById("navList");

navMobile.addEventListener("click", () => {
    navList.classList.toggle("active")
})