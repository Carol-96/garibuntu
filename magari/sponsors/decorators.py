# decorators.py
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def sponsor_required(function):
    """
    Custom decorator to check if the user is a sponsor. If not, redirect to sponsor login.
    """
    def wrap(request, *args, **kwargs):
        # Check if 'sponsor_id' exists in session
        if not request.session.get('sponsor_id'):
            return redirect('sponsor_login')  # Redirect to sponsor login if not authenticated
        return function(request, *args, **kwargs)

    return wrap
