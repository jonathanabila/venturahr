from prometheus_client import Counter

add_opportunity_counter = lambda: Counter(  # noqa: E731
    "venturahr_companies_opportunities_add",
    "New opportunity added.",
)

add_opportunity_requirements_counter = lambda: Counter(  # noqa: E731
    "venturahr_companies_opportunities_requirements_add",
    "New opportunity answer added.",
)
