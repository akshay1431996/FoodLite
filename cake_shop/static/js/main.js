// Mobile nav toggle
const nav = document.querySelector(".nav");
const toggle = document.querySelector(".nav-toggle");
toggle?.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  toggle.setAttribute("aria-expanded", open);
});

// Reveal elements as they scroll into view
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) {
      e.target.classList.add("visible");
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll(".reveal").forEach((el, i) => {
  el.style.transitionDelay = `${(i % 3) * 80}ms`;
  io.observe(el);
});

// Quantity steppers
document.querySelectorAll(".qty").forEach((box) => {
  const input = box.querySelector("input");
  box.querySelectorAll("button[data-step]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const next = Number(input.value || 1) + Number(btn.dataset.step);
      input.value = Math.min(Number(input.max), Math.max(Number(input.min), next));
    });
  });
});

// Auto-dismiss flash messages
document.querySelectorAll(".flash").forEach((el) => {
  setTimeout(() => el.classList.add("hide"), 3500);
  setTimeout(() => el.remove(), 4000);
});
