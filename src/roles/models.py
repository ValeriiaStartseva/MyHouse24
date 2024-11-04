from django.contrib.auth.models import Group, Permission


class RolePermission(Group):
    ROLE_CHOICES = [
        ("Director", "Директор"),
        ("Manager", "Менеджер"),
        ("Accountant", "Бухгалтер"),
        ("Electrician", "Електрик"),
        ("Plumber", "Сантехнік"),
        ("User", "Користувач"),
    ]

    def __str__(self):
        return self.name

    @classmethod
    def create_standard_roles(cls):
        """
        Method to create standard roles and add them permissions

        """
        roles_permissions = {
            "Director": [
                "add_user",
                "change_user",
                "delete_user",
                "view_dashboard",
                "view_payment_section",
                "view_receipt",
                "view_personal_account",
                "view_apartments",
                "view_apartments_owners",
                "view_houses",
                "view_messages",
                "view_master_application",
                "view_services_house",
                "view_manage_site",
                "view_system_settings",
                "view_services",
                "view_tariffs",
                "view_roles",
                "view_users",
                "view_payment_details",
            ],
            "Manager": [
                "view_personal_account",
                "view_apartments",
                "view_apartments_owners",
                "view_houses",
                "view_messages",
                "view_master_application",
                "view_services_house",
                "view_manage_site",
                "view_system_settings",
                "view_services",
                "view_tariffs",
                "view_roles",
                "view_users",
                "view_payment_details",
            ],
            "Accountant": ["payment_section"],
            "Electrician": ["master_application", "services_house"],
            "Plumber": ["master_application", "services_house"],
            "User": ["payment_section"],
        }

        for role_name, permissions in roles_permissions.items():
            group, created = cls.objects.get_or_create(name=role_name)
            if created:
                print(f"Created role: {role_name}")

            # Assign permissions to role
            for perm_codename in permissions:
                try:
                    permission = Permission.objects.get(codename=perm_codename)
                    group.permissions.add(permission)
                    print(f"Assigned permission {perm_codename} to role {role_name}")
                except Permission.DoesNotExist:
                    print(f"Permission {perm_codename} does not exist.")
