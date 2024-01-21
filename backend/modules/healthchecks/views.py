"""Api app views."""

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class HealthCheckApiView(GenericAPIView):

    """API endpoint to validate application startup"""

    permission_classes = []

    def get(self, *args, **kwargs):
        """Returns the response code 200"""
        return Response({"message": "drf-boilerplate app works!"})
