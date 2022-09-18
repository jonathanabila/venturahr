RECRUITER_PERMISSIONS = (
    "add_opportunity",
    "change_opportunity",
    "delete_opportunity",
    "view_opportunity",
)

CANDIDATE_PERMISSIONS = (
    "view_opportunity",
    "signup_opportunity",
)

NAMESPACE_CANDIDATE_PERMISSIONS = tuple(f"opportunities.{p}" for p in CANDIDATE_PERMISSIONS)
NAMESPACE_RECRUITER_PERMISSIONS = tuple(f"opportunities.{p}" for p in RECRUITER_PERMISSIONS)
NAMESPACE_ADMIN_PERMISSIONS = ("opportunities.view_opportunity",)

MAXIMUM_OPPORTUNITY_INTERVAL = 30
MINIMUM_OPPORTUNITY_INTERVAL = 2
