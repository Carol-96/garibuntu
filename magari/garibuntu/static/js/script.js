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

// Smooth Scrolling for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});


// Automatically close pop-up messages after 5 seconds
setTimeout(function() {
    var messages = document.querySelectorAll('.popup-message');
    messages.forEach(function(message) {
        message.style.display = 'none';
    });
}, 5000); // 5000ms = 5 seconds




// Toggle visibility of announcements
document.addEventListener('DOMContentLoaded', () => {
    const announcementHeaders = document.querySelectorAll('.announcement-list h3');
    announcementHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const content = header.nextElementSibling;
            if (content.style.display === 'none' || content.style.display === '') {
                content.style.display = 'block';
            } else {
                content.style.display = 'none';
            }
        });
    });
});

// Confirm event sponsorship registration
function confirmRegistration(eventId) {
    const confirmAction = confirm("Are you sure you want to sponsor this event?");
    if (confirmAction) {
        window.location.href = `/sponsor/event/${eventId}/register`;
    }
}

// Sample AJAX request for async action (e.g., mark sponsorship as complete)
async function markAsSponsored(eventId) {
    try {
        const response = await fetch(`/sponsor/event/${eventId}/complete/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()  // Utility function to get CSRF token
            },
            body: JSON.stringify({ sponsored: true })
        });
        
        if (response.ok) {
            alert("Event sponsorship marked as complete.");
            document.getElementById(`status-${eventId}`).innerText = "Sponsored";
        } else {
            alert("Failed to mark sponsorship as complete.");
        }
    } catch (error) {
        console.error("Error:", error);
    }
}

// Utility function to get CSRF token
function getCSRFToken() {
    return document.cookie.split('; ').find(row => row.startsWith('csrftoken')).split('=')[1];
}