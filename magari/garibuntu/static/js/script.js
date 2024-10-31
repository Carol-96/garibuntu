function toggleMenu() {
    const nav = document.querySelector('.navbar nav');
    nav.classList.toggle('active');
}


function toggleDropdown() {
    document.getElementById("dropdownMenu").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropdown-toggle, .profile-picture-dash')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}


// Automatically close pop-up messages after 5 seconds
setTimeout(function() {
    var messages = document.querySelectorAll('.popup-message');
    messages.forEach(function(message) {
        message.style.display = 'none';
    });
}, 5000); // 5000ms = 5 seconds