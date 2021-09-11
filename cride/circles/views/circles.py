<<<<<<< HEAD
"""Circle views."""

# Django REST Framework
from cride.circles import serializers
from rest_framework import viewsets

# Serializers
from cride.circles.serializers import CircleModelSerializer

# Models
from cride.circles.models import Circle, Membership

=======
# Django Fest Framework

from rest_framework import viewsets

# Models
from cride.circles.models import Circle

# Ser
from cride.circles.serializers import CircleModelSerializer
>>>>>>> 6/Typo-models

class CircleViewSet(viewsets.ModelViewSet):
    """Circle view set."""

    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer
<<<<<<< HEAD

    def get_queryset(self):
        """Restric list to public.only"""
        queryset = Circle.objects.all()
        if self.actions == 'list':
            return queryset.filter(is_public=True)
        return queryset

    def perform_create(self, serializer):
        """Assing circle admin"""
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitation=10
        )
=======
>>>>>>> 6/Typo-models
