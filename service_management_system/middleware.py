# middleware.py

from django.utils import timezone
from django.conf import settings
from django.contrib.sessions.backends.base import SessionBase

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.session.get_expire_at_browser_close():
            # Session is set to expire at browser close
            return self.get_response(request)

        # Calculate the session expiration time
        session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME)
        if session_key:
            session = SessionBase(request.session.get(session_key))
            last_activity = session.get('last_activity')
            if last_activity:
                elapsed_time = timezone.now() - last_activity
                if elapsed_time.total_seconds() > settings.SESSION_EXPIRE_SECONDS:
                    # Session has expired, delete it
                    session.flush()
                    return self.get_response(request)

        # Update last activity timestamp
        request.session['last_activity'] = timezone.now()
        return self.get_response(request)
