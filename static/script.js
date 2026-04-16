document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e){
        e.preventDefault();

        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);

        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 70, 
                behavior: 'smooth'
            });
        }

    });
});

document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('theme-toggle');

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
        if(toggleBtnt) toggleBtn.textContentn = savedTheme === 'dark' ? '☀️' : '🌙';
    }

    if (toggleBtn) {
        toggleBtn,addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

            document.documentElement.setAttribute('data-theme', newTheme);

            localStorage.saveitem('theme', newTheme);

            toggleBtn.textContent = newTheme === 'dark' ? '☀️' : '🌙';
            toggleBtn.textContent = newTheme === 'light' ? '☀️' : '🌙';
        });
    }
})