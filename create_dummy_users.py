import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IvyMesh.settings')

from users.models import IvyMeshUser

for role, m in [("admin", 9), ("staff", 19), ("student", 99)]:
    for n in range(m):
        func = IvyMeshUser.objects.create_superuser if role == "admin" else IvyMeshUser.objects.create_user
        func(username=f'{role}_user{n}', email=f"{role}_user{n}@fake.fake", password=f"{role}_user{n}_1234", role=role)

