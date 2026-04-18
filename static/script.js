document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('dark-mode-toggle');
    const body = document.body;

    // Function to update the icon based on the mode
    const updateIcon = () => {
        if (body.classList.contains('dark-mode')) {
            toggleBtn.textContent = '☀️'; // Show Sun when in Dark Mode (to go back to light)
        } else {
            toggleBtn.textContent = '🌙'; // Show Moon when in Light Mode (to go to dark)
        }
    };

    // 1. Check saved theme on load
    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('dark-mode');
    }
    updateIcon(); // Set the correct icon immediately

    // 2. Handle the click
    toggleBtn.addEventListener('click', () => {
        body.classList.toggle('dark-mode');

        // Save choice
        if (body.classList.contains('dark-mode')) {
            localStorage.setItem('theme', 'dark');
        } else {
            localStorage.setItem('theme', 'light');
        }

        updateIcon(); // Swap the icon after the click
    });
});

