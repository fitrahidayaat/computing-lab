from django.db import models

class Topic(models.Model):
    STUDY_TYPES = (
        ('advance', 'Advance'),
        ('basic', 'Basic'),
        ('other', 'Other')
    )

    STATUS = (
        ('active', 'Active'),
        ('disabled', 'Disabled')
    )

    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='img/topics')
    study = models.CharField(max_length=10, choices=STUDY_TYPES, default=STUDY_TYPES[1][1])
    description = models.TextField(max_length=10000)
    time = models.CharField(max_length=250)
    tutor = models.CharField(max_length=250)
    status = models.CharField(max_length=10, choices=STATUS, default=STATUS[1][1])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Topics'

class Member(models.Model):
    MEMBER_TYPES = (
        ('general', 'General Member'),
        ('head', 'Head of Laboratory'),
        ('assistant', 'Assistant Laboratory'),
        ('former', 'Former Member')
    )
    
    DEPARTMENTS = (
        ('Bachelor of Informatics', 'Bachelor of Informatics'),
        ('Bachelor of Information Technology', 'Bachelor of Information Technology'),
        ('Others', 'Others')
    )

    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='img/members', blank=True, null=True)
    role = models.CharField(max_length=50, choices=MEMBER_TYPES, default=MEMBER_TYPES[3][1])
    description = models.CharField(max_length=250, blank=True, null=True)
    generation = models.CharField(max_length=3, blank=True, null=True)
    department = models.CharField(max_length=50, choices=DEPARTMENTS, default=DEPARTMENTS[0][1])
    student_year = models.CharField(max_length=4, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Members'
