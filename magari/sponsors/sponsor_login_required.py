# middleware/sponsor_login_required.py
from django.shortcuts import redirect
from django.urls import reverse

class SponsorLoginRequiredMiddleware:
    """
    Middleware that checks if a request is for a sponsor page and if the sponsor is authenticated.
    If not, it redirects to the sponsor login page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow access to registration and login pages without needing to be authenticated
        if request.path in [reverse('sponsors:sponsor_register'), reverse('sponsors:sponsor_login')]:
            return self.get_response(request)

        # For other sponsor pages, enforce login
        if request.path.startswith('/sponsors/') and not request.session.get('sponsor_id'):
            return redirect(reverse('sponsors:sponsor_login'))

        return self.get_response(request)
