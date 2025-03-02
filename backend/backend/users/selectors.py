from typing import Optional

from django.db.models.query import QuerySet

from backend.common.utils import get_object
from backend.users.filters import BaseUserFilter
from backend.users.models import User


def user_get_login_data(*, user: User):
    return {
        "id": user.id,
        "email": user.email,
        "is_active": user.is_active,
        "is_admin": user.is_admin,
        "is_superuser": user.is_superuser,
    }


def user_list(*, filters=None) -> QuerySet[User]:
    filters = filters or {}

    qs = User.objects.all()

    return BaseUserFilter(filters, qs).qs


def user_get(user_id) -> Optional[User]:
    user = get_object(User, id=user_id)

    return user
