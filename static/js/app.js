/* ==========================================
        CompareX JavaScript
========================================== */

// ================================
// Mobile Menu
// ================================

const menuBtn = document.querySelector(".menu");
const navLinks = document.querySelector(".nav-links");

menuBtn.addEventListener("click", () => {
    navLinks.classList.toggle("active");

    if (menuBtn.classList.contains("fa-bars")) {
        menuBtn.classList.remove("fa-bars");
        menuBtn.classList.add("fa-xmark");
    } else {
        menuBtn.classList.remove("fa-xmark");
        menuBtn.classList.add("fa-bars");
    }
});

// ================================
// Scroll To Top Button
// ================================

const topBtn = document.getElementById("topBtn");

window.addEventListener("scroll", () => {

    if (window.scrollY > 400) {
        topBtn.classList.add("show");
    } else {
        topBtn.classList.remove("show");
    }

});

topBtn.addEventListener("click", () => {

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

});

// ================================
// Navbar Shadow
// ================================

const header = document.querySelector("header");

window.addEventListener("scroll", () => {

    if (window.scrollY > 50) {

        header.style.background = "rgba(10,15,30,.95)";
        header.style.boxShadow = "0 5px 20px rgba(0,0,0,.35)";

    } else {

        header.style.background = "rgba(10,15,30,.75)";
        header.style.boxShadow = "none";

    }

});

// ================================
// Smooth Navigation
// ================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {

            target.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        }

        navLinks.classList.remove("active");
        menuBtn.classList.remove("fa-xmark");
        menuBtn.classList.add("fa-bars");

    });

});

// ================================
// Search Button Demo
// ================================

const searchBtn = document.querySelector(".hero-search button");
const searchInput = document.querySelector(".hero-search input");

searchBtn.addEventListener("click", () => {

    const keyword = searchInput.value.trim();

    if (keyword === "") {

        alert("Please enter a product name.");

        return;

    }

    alert(`Searching for "${keyword}"...`);

});

// ================================
// Popular Tags
// ================================

document.querySelectorAll(".popular-tags button").forEach(tag => {

    tag.addEventListener("click", () => {

        searchInput.value = tag.textContent;

        searchBtn.click();

    });

});

// ================================
// Product Buttons
// ================================

document.querySelectorAll(".product-info button").forEach(button => {

    button.addEventListener("click", () => {

        const product =
            button.parentElement.querySelector("h3").innerText;

        alert(`Opening comparison for ${product}`);

    });

});

// ================================
// Card Hover Animation
// ================================

const cards = document.querySelectorAll(
    ".product-card,.feature-card,.category-card,.tech-card,.step,.store"
);

cards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.transform = "translateY(-10px)";

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = "translateY(0px)";

    });

});

// ================================
// CTA Button
// ================================

const ctaBtn = document.querySelector(".cta-btn");

if (ctaBtn) {

    ctaBtn.addEventListener("click", () => {

        document.querySelector(".hero").scrollIntoView({

            behavior: "smooth"

        });

    });

}

// ================================
// Footer Year
// ================================

const copyright = document.querySelector(".copyright");

if (copyright) {

    copyright.innerHTML =
        `© ${new Date().getFullYear()} CompareX. All Rights Reserved.`;

}