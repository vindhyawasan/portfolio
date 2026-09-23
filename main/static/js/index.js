document.addEventListener("DOMContentLoaded", function () {
    var toggle = document.getElementById("theme-toggle");
    if (!toggle) return;

    toggle.addEventListener("click", function () {
        var isLight = document.body.classList.toggle("light-mode");
        toggle.textContent = isLight ? "☀️" : "🌙";
    });
});