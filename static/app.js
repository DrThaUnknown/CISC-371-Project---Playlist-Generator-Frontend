document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;
    const root = document.documentElement;
    const toggleBtn = document.querySelector(".theme-toggle");
    const key = "playgen-theme";

    // 1. Fade-in Animation on Load
    requestAnimationFrame(() => {
        body.classList.add("page-loaded");
    });

    // 2. Smooth Page Transitions
    document.querySelectorAll('a[href^="/"]').forEach(link => {
        link.addEventListener("click", e => {
            const url = link.getAttribute("href");
            if (!url || url.startsWith("#")) return;
            e.preventDefault();
            body.classList.add("page-fade-out");
            setTimeout(() => window.location.href = url, 180);
        });
    });

    // 3. THE RAINBOW THEME LOGIC
    // Modes: null (Dark) -> "light" -> "rainbow" -> null (Dark)
    function setTheme(mode) {
        // Clear old settings
        root.removeAttribute("data-theme");
        
        // Apply new setting
        if (mode === "light") {
            root.setAttribute("data-theme", "light");
            if (toggleBtn) toggleBtn.innerHTML = '<i class="fas fa-sun"></i>';
        } 
        else if (mode === "rainbow") {
            root.setAttribute("data-theme", "rainbow");
            if (toggleBtn) toggleBtn.innerHTML = '<i class="fas fa-rainbow"></i>';
        } 
        else {
            // Default to Dark
            if (toggleBtn) toggleBtn.innerHTML = '<i class="fas fa-moon"></i>';
        }
    }

    // Load saved theme
    const saved = localStorage.getItem(key);
    setTheme(saved);

    // Click Event: Cycle through modes
    if (toggleBtn) {
        toggleBtn.addEventListener("click", () => {
            const current = root.getAttribute("data-theme");
            
            let nextMode = "light"; // Default next step
            
            if (current === "light") {
                nextMode = "rainbow"; // Light -> Rainbow
            } else if (current === "rainbow") {
                nextMode = null;      // Rainbow -> Dark
            }
            
            setTheme(nextMode);
            
            if (nextMode) {
                localStorage.setItem(key, nextMode);
            } else {
                localStorage.removeItem(key);
            }
        });
    }
});