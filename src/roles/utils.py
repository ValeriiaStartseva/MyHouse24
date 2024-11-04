class RoleCheck:
    def __init__(self, request):
        self.request = request
        self.user_role = self.get_user_role()

    def get_user_role(self):
        if self.request.user.is_authenticated:
            if self.request.user.groups.filter(name="Director").exists():
                return "Director"
            elif self.request.user.groups.filter(name="Manager").exists():
                return "Manager"
            elif self.request.user.groups.filter(name="Accountant").exists():
                return "Accountant"
            elif self.request.user.groups.filter(name="Electrician").exists():
                return "Electrician"
            elif self.request.user.groups.filter(name="Plumber").exists():
                return "Plumber"
            else:
                return "User"
        return None

    def get_context(self):
        return {"user_role": self.user_role}
