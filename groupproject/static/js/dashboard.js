const sideMenu = document.querySelector('aside');
const menuButton = document.querySelector('#menu_bar');
const closeButton = document.querySelector('#close_button');

menuButton.addEventListener('click',()=>{
    sideMenu.style.display = "block"
})

closeButton.addEventListener('click',()=>{
    sideMenu.style.display = "none"
})

// Ensure the sidebar is always visible when the screen width is 1200px or larger
window.addEventListener("resize", () => {
    if (window.innerWidth >= 1200) {
        sideMenu.style.display = "block"; // Always show the sidebar on larger screens
    }
});