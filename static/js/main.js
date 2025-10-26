// ====== MAIN SCRIPT ======

// Show console message (for testing)
console.log("Main.js loaded successfully ✅");

// ====== ADD TO CART FUNCTIONALITY ======
let cartCount = 0;

// Listen for any button with class 'add-to-cart'
document.addEventListener("click", (event) => {
  if (event.target.classList.contains("add-to-cart")) {
    cartCount++;
    updateCartCount();
    alert("Item added to cart!");
  }
});

function updateCartCount() {
  const cartIcon = document.getElementById("cart-count");
  if (cartIcon) {
    cartIcon.textContent = cartCount;
  }
}

// ====== NAVBAR ACTIVE LINK ======
const navLinks = document.querySelectorAll("nav ul li a");
navLinks.forEach((link) => {
  if (link.href === window.location.href) {
    link.classList.add("active");
  }
});

// ====== CONTACT FORM (Optional Demo) ======
const contactForm = document.querySelector(".contact-form");
if (contactForm) {
  contactForm.addEventListener("submit", (e) => {
    e.preventDefault();
    alert("Thank you! Your message has been sent successfully.");
    contactForm.reset();
  });
}