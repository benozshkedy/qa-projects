// Smooth little enhancements: year + copy-to-clipboard
document.getElementById("year").textContent = new Date().getFullYear();

document.querySelectorAll("[data-copy]").forEach((btn) => {
  btn.addEventListener("click", async () => {
    const text = btn.getAttribute("data-copy");
    try {
      await navigator.clipboard.writeText(text);
      const hint = btn.querySelector(".copy-hint");
      if (hint) {
        const prev = hint.textContent;
        hint.textContent = "Copied";
        setTimeout(() => (hint.textContent = prev), 1200);
      }
    } catch (e) {
      alert("Copy failed. Please copy manually.");
    }
  });
});