# Libraries and modules
import geoip2.database

from django.conf import settings
from django.http import HttpResponseForbidden

# Clase para bloquear el acceso a usuarios de otros países


class CountryBlockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.geoip_reader = geoip2.database.Reader(settings.GEOIP_PATH)

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        if ip_address:
            try:
                country = self.geoip_reader.country(ip_address)
                if country.country.iso_code != 'MX':  # Check if country is not Mexico
                    return HttpResponseForbidden("Access denied from your location.")
                
            except Exception as e:
                # Handle exceptions if any
                pass

        response = self.get_response(request)
        return response
