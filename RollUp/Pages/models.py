from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# The class "Class_Schedule" is used to store a schedule of current classes.
# This will be used to provide information on the welcome page for the website.
class Classes(models.Model):
    # type - choices
    BASIC = 'Basic'
    ADVANCED = 'Advanced'
    COMPETITION = 'Competition'
    choiceClasses = [(BASIC, "Adults - Basics"),(ADVANCED, "Adults - Advanced"), (COMPETITION, "Adults - Competition") ]
    # time - choices
    AM = '6:00 AM' #6AM
    ANOON = '12:00 PM'
    PM = '7:00 PM' #7PM
    choiceTime = [(AM, "6:00 AM"), (ANOON, "12:00 PM"), (PM, "7:00 PM")]
    # gi - choice
    YES = 'Yes'
    NO = 'No'
    choiceGi = [(YES, "Yes"),(NO, "No")]

    # Each class will have a class id which will be used as the primary key. The id will be used to identify specific classes
    # which in a search can return data to the user.
    id = models.AutoField('id', primary_key=True, auto_created=True, editable=False)
    # The Type field will be used to store the Type of class. This will also be the primary key.
    # There are different types of clases, i.e adults, adults fundamentals, kids, kids fundamentals.
    type = models.CharField('type', max_length=50, choices = choiceClasses, default=BASIC)
    # The date field will store the date the class was held on.
    date = models.DateField(default=timezone.now)  # add date field
    # The Time field stores the time that the class is offered on a particular day.
    time = models.CharField('time', max_length=10, choices = choiceTime, default=AM)
    # The Size field will store an integer value for the number of participants allowed in the class.
    size = models.IntegerField('size', default=20, validators=[MinValueValidator(0)])
    num_signed_up = models.IntegerField('num_signed_up', default=0, validators=[MinValueValidator(0)], editable=False) 
    # The Instructor field will store the name of the instructor teaching the class.
    instructor = models.CharField('instructor', max_length=50)
    # The Gi field will annotate whether a Gi will be required or not for class.
    # This attribute will be designated as Y(for yes) and N(for no) and stored as a char.
    gi = models.CharField('gi', max_length=3, choices=choiceGi, default=YES)

    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural = "Classes"


# The class 'Participants' will store the participants id from the class Users in the Users application.
# It will also store the class_id from the above classes model which will provide the unique id for each class that is offered.
# Every time a user signs up for a class both fields will be stored for the contact tracing portion of our program.
class Participants(models.Model):
    # used as a foreign key to get the participants id from the class users located in the Users application
    participant_id = models.AutoField('participant_id', primary_key=True, auto_created=True, editable=False)#models.IntegerField('participant_id', primary_key=True)
    # used to get the id of the class in the above classes model.
    # class_id = models.ForeignKey(Classes, on_delete=models.DO_NOTHING, default=0)
    email = models.CharField('email', max_length=50)
    name = models.CharField('name', max_length=100)

    def __str__(self):
        return str(self.participant_id)
    class Meta:
        verbose_name_plural = "Participants"
