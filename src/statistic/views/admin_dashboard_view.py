from django.views.generic import TemplateView


class AdminDashboardView(TemplateView):
    template_name = "statistic/admin_dashboard.html"
