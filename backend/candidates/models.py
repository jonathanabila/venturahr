from core.models import User


class Candidate(User):
    class Meta:
        proxy = True
