#!/usr/bin/env bash

python3 manage.py shell --command 'from users.models import IvyMeshUser; for role, m, f in [("admin", 9, IvyMeshUser.objects.create_superuser), ("staff", 19, IvyMeshUser.objects.create_user), ("student", 99, IvyMeshUser.objects.create_user)]: \
    for n in range(m): \
        f(username=f"{role}_user{n}", email=f"{role}_user{n}@fake.fake", password=f"{role}_user{n}_1234", role=role)'

