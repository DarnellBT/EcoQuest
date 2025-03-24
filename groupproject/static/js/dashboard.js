const sideMenu = document.querySelector('aside');
const menuButton = document.querySelector('#menu_bar');
const closeButton = document.querySelector('#close_button');

// Show the sidebar when the menu button is clicked (for small screens)
menuButton.addEventListener('click', () => {
    sideMenu.style.display = "block"; // Show the sidebar on smaller screens
    menuButton.style.display = "none"; // Hide the menu button when sidebar is open
});

// Hide the sidebar when the close button is clicked (for small screens)
closeButton.addEventListener('click', () => {
    sideMenu.style.display = "none"; // Hide the sidebar on smaller screens
    menuButton.style.display = "block"; // Show the menu button when sidebar is closed
});

// Ensure the sidebar behaves properly when resizing between large and small screens
window.addEventListener("resize", () => {
    if (window.innerWidth >= 1200) {
        sideMenu.style.display = "flex"; // Always show the sidebar on large screens
        menuButton.style.display = "none"; // Hide the menu button when sidebar is visible
    } else {
        sideMenu.style.display = "none"; // Hide sidebar on small screens
        menuButton.style.display = "block"; // Show the menu button when the sidebar is hidden
    }
});

// Make sure the sidebar is hidden on page load for smaller screens and the menu button is visible
if (window.innerWidth < 1200) {
    sideMenu.style.display = "none"; // Hide sidebar initially on small screens
    menuButton.style.display = "block"; // Show the menu button initially on small screens
}
