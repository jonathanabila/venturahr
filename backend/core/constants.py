RECRUITER_PERMISSIONS = (
    "add_opportunity",
    "change_opportunity",
    "delete_opportunity",
    "view_opportunity",
)

NAMESPACE_RECRUITER_PERMISSIONS = tuple(f"opportunities.{p}" for p in RECRUITER_PERMISSIONS)

MAXIMUM_OPPORTUNITY_INTERVAL = 30
MINIMUM_OPPORTUNITY_INTERVAL = 2
