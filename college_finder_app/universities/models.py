from django.db import models


class Universities(models.Model):

    rank_order = models.IntegerField()
    rank = models.TextField()
    name = models.TextField()
    scores_overall = models.DecimalField(max_digits=6, decimal_places=2)
    scores_overall_rank = models.IntegerField()
    scores_teaching = models.DecimalField(max_digits=6, decimal_places=2)
    scores_teaching_rank = models.IntegerField()
    scores_research = models.DecimalField(max_digits=6, decimal_places=2)
    scores_research_rank = models.IntegerField()
    scores_citations = models.DecimalField(max_digits=6, decimal_places=2)
    scores_citations_rank = models.IntegerField()
    scores_industry_income = models.DecimalField(
        max_digits=6, decimal_places=2)
    scores_industry_income_rank = models.IntegerField()
    scores_international_outlook = models.DecimalField(
        max_digits=6, decimal_places=2)
    scores_international_outlook_rank = models.IntegerField()
    record_type = models.TextField()
    member_level = models.IntegerField()
    url = models.TextField()
    nid = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.TextField()
    stats_number_students = models.DecimalField(max_digits=6, decimal_places=2)
    stats_student_staff_ratio = models.DecimalField(
        max_digits=6, decimal_places=2, null=False)
    stats_pc_intl_students = models.TextField(null=False)
    stats_female_male_ratio = models.TextField(null=False)
    aliases = models.TextField()
    subjects_offered = models.TextField()
