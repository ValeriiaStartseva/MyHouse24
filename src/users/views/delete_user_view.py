from django.http import JsonResponse
from django.views import View
from src.users.models import User


class DeleteUserView(View):
    def delete(self, request, *args, **kwargs):
        User.objects.get(pk=self.kwargs["pk"]).delete()
        return JsonResponse(status=200, data={"success": True})
