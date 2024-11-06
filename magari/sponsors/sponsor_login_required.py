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
        # Check if the request path is for sponsor pages
        if request.path.startswith('/sponsors/') and not request.session.get('sponsor_id'):
            # Redirect to sponsor login if not authenticated
            return redirect(reverse('sponsor_login'))
        return self.get_response(request)
