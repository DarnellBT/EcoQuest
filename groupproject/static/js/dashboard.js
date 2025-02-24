const sideMenu = document.querySelector('aside');
const menuButton = document.querySelector('#menu_bar');
const closeButton = document.querySelector('#close_button');

// Show the sidebar when the menu button is clicked (for small screens)
menuButton.addEventListener('click', () => {
    sideMenu.style.display = "block"; // Show the sidebar on smaller screens
});

// Hide the sidebar when the close button is clicked (for small screens)
closeButton.addEventListener('click', () => {
    sideMenu.style.display = "none"; // Hide the sidebar on smaller screens
});

// Ensure the sidebar behaves properly when resizing between large and small screens
window.addEventListener("resize", () => {
    if (window.innerWidth >= 1200) {
        sideMenu.style.display = "flex"; // Always show the sidebar as flex on larger screens
    } else {
        sideMenu.style.display = "none"; // Hide the sidebar on smaller screens
    }
});

// Make sure sidebar is hidden on page load for smaller screens
if (window.innerWidth < 1200) {
    sideMenu.style.display = "none"; // Hide sidebar initially on small screens
}
