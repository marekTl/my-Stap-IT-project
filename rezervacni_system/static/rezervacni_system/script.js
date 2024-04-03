const hamburger = document.querySelector(".hamburger");
const navigation = document.querySelector(".navigation");

hamburger.addEventListener("click", function() {
    hamburger.classList.toggle("active"); // vytvoření třídy v css
    navigation.classList.toggle("active");
});

// chci aby se hamburger zavřel i po kliku na jednotlivé linky... , ale divný, funguje i tak 
const navLinks = document.querySelectorAll(".nav-link");

navLinks.forEach(function(link) {
    link.addEventListener("click", function() {
        hamburger.classList.remove("active");
        navigation.classList.remove("active");
    });
});