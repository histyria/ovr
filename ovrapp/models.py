from django.db import models

# جدول أسماء الأقسام.
class section_list(models.Model):
    section = models.CharField(max_length=190, null=True)
    def __str__(self):
         return self.section

# جدول نوع الشخص المتعرض للحادثة : *
class Type_of_person_involved(models.Model):
    Type_of_person_involved = models.CharField(max_length=190, null=True)
    def __str__(self):
         return self.Type_of_person_involved

# جدول نوع الحدث

class Type_of_involved(models.Model):
    Type_of_involved = models.CharField(max_length=190 , null=True)
    def __str__(self):
        return self.Type_of_involved



# جدول إرسال الطلب
class Order(models.Model):
    Damage_level = (         
        ('Minor','Minor'),
        ('Moderate','Moderate'),
        ('Major','Major'),
        ('Catastrophic','Catastrophic')
    )
     #نوع الإصابة
    Type_of_Injury = (         
        ('Physical','Physical'),
        ('Psychological','Psychological')
    )
  

    # إحتمالية وقوع الحدوث
    RLikelihood_Category = (         
        ('Unlikely','Unlikely'),
        ('Possible','Possible'),
        ('Likely','Likely'),
        ('Almost Certain','Almost Certain')
    )


    # هل تم الإعلام


    Informed  = (         
        ('yes','yes'),
        ('no','no'),
    )


    Event_Location = models.ForeignKey(section_list, on_delete= models.CASCADE , null=True)
    Reporting_Department_Section = models.ForeignKey(section_list, on_delete= models.CASCADE , null=True , related_name='Reporting_Department_Section')
    Reporting_Department_Section_athor = models.ForeignKey(section_list, on_delete= models.CASCADE , null=True , related_name='Reporting_Department_Section_athor')
    Responding_Department_Section = models.ForeignKey(section_list, on_delete= models.CASCADE , null=True , related_name='Responding_Department_Section')
    Type_of_person_involved = models.ForeignKey(Type_of_person_involved, null=True, on_delete=models.SET_NULL)
    Type_of_involved = models.ForeignKey(Type_of_involved, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    Damage_level =  models.CharField(max_length=200, null=True,choices=Damage_level)
    Type_of_Injury =  models.CharField(max_length=200, null=True,choices=Type_of_Injury)
    RLikelihood_Category =  models.CharField(max_length=200, null=True,choices=RLikelihood_Category)
    Informed =  models.CharField(max_length=200, null=True,choices=Informed)

