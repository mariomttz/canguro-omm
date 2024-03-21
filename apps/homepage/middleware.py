# Libraries and modules
from django.conf import settings
from django.http import HttpResponseForbidden
from geoip2.database import Reader

# Clase para bloquear el acceso a usuarios de otros países


class CountryBlockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.geoip_reader = Reader(settings.GEOIP_PATH)

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        if ip_address:
            try:
                country = self.geoip_reader.country(ip_address)
                if country.country.iso_code not in settings.ALLOWED_COUNTRIES:
                    return HttpResponseForbidden("Acceso denegado desde tu ubicación.")

            except Exception as e:
                return HttpResponseForbidden("Ha ocurrido un error. Inténtalo de nuevo más tarde.")

        response = self.get_response(request)
        return response
