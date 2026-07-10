const header = document.querySelector(".site-header");

window.addEventListener("scroll", () => {
  if (!header) return;
  header.toggleAttribute("data-scrolled", window.scrollY > 12);
});
