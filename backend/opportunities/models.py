from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class Opportunity(models.Model):
    class Meta:
        permissions = [("signup_opportunity", "Can sign up for an opportunity")]

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)

    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateField()

    company = models.ForeignKey(
        "companies.Company",
        null=True,
        on_delete=models.CASCADE,
        verbose_name="company",
        help_text="User company",
    )

    created_by = models.ForeignKey(
        "core.User",
        null=False,
        on_delete=models.CASCADE,
        verbose_name="created by",
    )


class OpportunityRequirement(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=3000)

    created_at = models.DateTimeField(default=timezone.now)

    weight = models.IntegerField(
        null=False, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    minimim_knowledge = models.IntegerField(
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=1,
    )

    opportunity = models.ForeignKey(
        "opportunities.Opportunity",
        null=False,
        on_delete=models.CASCADE,
        verbose_name="opportunity",
        related_name="requirements",
    )

    company = models.ForeignKey(
        "companies.Company",
        null=True,
        on_delete=models.CASCADE,
        verbose_name="company",
        help_text="User company",
    )

    created_by = models.ForeignKey(
        "core.User",
        null=False,
        on_delete=models.CASCADE,
        verbose_name="created by",
    )


class OpportunityAnswer(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    opportunity = models.ForeignKey(
        "opportunities.Opportunity",
        null=False,
        on_delete=models.CASCADE,
        verbose_name="opportunity",
        related_name="answers",
    )

    created_by = models.ForeignKey(
        "core.User",
        null=False,
        on_delete=models.CASCADE,
        verbose_name="created by",
    )

    @property
    def desired_minimum_profile(self) -> float:
        return round(
            sum([r.opportunity_requirement.weight * r.answer for r in self.requirements.all()])
            / sum([r.opportunity_requirement.weight for r in self.requirements.all()]),
            2,
        )


class OpportunityAnswerRequirement(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=3000)

    answer = models.IntegerField(
        null=False, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    opportunity_answer = models.ForeignKey(
        "opportunities.OpportunityAnswer",
        null=False,
        on_delete=models.CASCADE,
        verbose_name="answer",
        related_name="requirements",
    )

    opportunity_requirement = models.ForeignKey(
        "opportunities.OpportunityRequirement",
        null=False,
        on_delete=models.CASCADE,
        verbose_name="answer",
        related_name="requirements",
    )

    created_by = models.ForeignKey(
        "core.User",
        null=False,
        on_delete=models.CASCADE,
        verbose_name="created by",
    )
