from django.db import models


class Universities(models.Model):

    rank_order = models.IntegerField()
    rank = models.CharField(max_length=16)
    name = models.TextField()
    scores_overall = models.CharField(max_length=16, null=False)
    scores_overall_rank = models.IntegerField()
    scores_teaching = models.DecimalField(max_digits=4, decimal_places=1)
    scores_teaching_rank = models.IntegerField()
    scores_research = models.DecimalField(max_digits=4, decimal_places=1)
    scores_research_rank = models.IntegerField()
    scores_citations = models.DecimalField(max_digits=4, decimal_places=1)
    scores_citations_rank = models.IntegerField()
    scores_industry_income = models.DecimalField(
        max_digits=4, decimal_places=1)
    scores_industry_income_rank = models.IntegerField()
    scores_international_outlook = models.DecimalField(
        max_digits=4, decimal_places=1)
    scores_international_outlook_rank = models.IntegerField()
    record_type = models.CharField(max_length=16)
    member_level = models.IntegerField()
    slug = models.SlugField(default='not-found')
    nid = models.IntegerField()
    location = models.TextField()
    stats_number_students = models.IntegerField()
    stats_student_staff_ratio = models.DecimalField(
        max_digits=4, decimal_places=1)
    stats_pc_intl_students = models.CharField(max_length=5, null=False)
    stats_female_male_ratio = models.CharField(
        max_length=16, null=False, blank=True)
    aliases = models.TextField()
    subjects_offered = models.TextField()
