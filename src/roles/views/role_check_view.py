from django.views.generic import TemplateView
from src.roles.utils import RoleCheck


class DashboardView(TemplateView):
    template_name = "admin/adminlte_base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        role_check = RoleCheck(self.request)
        context.update(role_check.get_context())

        return context
