from core.models import User


class CandidateUser(User):
    class Meta:
        proxy = True
