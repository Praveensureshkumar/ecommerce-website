function toggleOffers() {
    var extraOffers = document.getElementById("extraOffers");
    var showMoreText = document.querySelector(".show-more");

    if (extraOffers.style.display === "none" || extraOffers.style.display === "") {
        // Show extra offers
        extraOffers.style.display = "block";
        showMoreText.innerHTML = "View fewer offers";
    } else {
        // Hide extra offers
        extraOffers.style.display = "none";
        showMoreText.innerHTML = "View 6 more offers"; // Ensure correct count
    }
}
