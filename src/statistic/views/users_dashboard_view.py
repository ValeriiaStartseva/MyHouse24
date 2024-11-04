from django.views.generic import TemplateView


class UsersDashboardView(TemplateView):
    template_name = "statistic/users_dashboard.html"
