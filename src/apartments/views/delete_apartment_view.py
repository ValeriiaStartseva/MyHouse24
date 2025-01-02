from django.http import JsonResponse
from django.views import View
from src.apartments.models import Apartment


# view for delete an apartment
class DeleteApartmentView(View):
    def delete(self, request, *args, **kwargs):
        Apartment.objects.get(pk=self.kwargs["pk"]).delete()
        return JsonResponse(status=200, data={"success": True})
