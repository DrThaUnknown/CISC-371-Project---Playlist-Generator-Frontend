document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;

    requestAnimationFrame(() => {
        body.classList.add("page-loaded");
    });

    const links = document.querySelectorAll('a[href^="/"]');

    links.forEach(link => {
        link.addEventListener("click", e => {
            const url = link.getAttribute("href");
            if (!url || url.startsWith("#")) return;
            e.preventDefault();
            body.classList.add("page-fade-out");
            setTimeout(() => window.location.href = url, 180);
        });
    });

    const toggleBtn = document.querySelector(".theme-toggle");
    const root = document.documentElement;
    const key = "playgen-theme";

    function setTheme(t) {
        if (t === "light") {
            root.setAttribute("data-theme", "light");
        } else {
            root.removeAttribute("data-theme");
        }
        if (toggleBtn) {
            const icon = toggleBtn.querySelector("i");
            icon.className = t === "light" ? "fas fa-sun" : "fas fa-moon";
        }
    }

    const saved = localStorage.getItem(key);
    if (saved) {
        setTheme(saved);
    } else {
        const prefersLight = window.matchMedia("(prefers-color-scheme: light)").matches;
        setTheme(prefersLight ? "light" : "dark");
    }

    if (toggleBtn) {
        toggleBtn.addEventListener("click", () => {
            const newTheme = root.getAttribute("data-theme") === "light" ? "dark" : "light";
            setTheme(newTheme);
            localStorage.setItem(key, newTheme);
        });
    }
});
