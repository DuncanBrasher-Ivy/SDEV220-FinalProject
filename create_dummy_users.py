from django.contrib.auth.models import User


for role, m, f in [("admin", 9, User.objects.create_superuser), ("staff", 19, User.objects.create_user), ("student", 99, User.objects.create_user)]:
    for n in range(m):
        f(username=f"{role}_user{n}", email=f"{role}_user{n}@fake.fake", password=f"{role}_user{n}_1234", is_staff=role != "student")

