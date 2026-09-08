from django.db.models import TextChoices


class UserKind(TextChoices):
    ADMIN = "ADMIN", "Admin"
    DEVELOPER = "DEVELOPER", "Developer"
    SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
    UNDEFINED = "UNDEFINED", "Undefined"


class UserGender(TextChoices):
    FEMALE = "FEMALE", "Female"
    MALE = "MALE", "Male"
    UNKNOWN = "UNKNOWN", "Unknown"
    OTHER = "OTHER", "Other"
