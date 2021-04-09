from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
# The class "Class_Schedule" is used to store a schedule of current classes.
# This will be used to provide information on the welcome page for the website.
class Classes(models.Model):
    # Each class will have a class id which will be used as the primary key. The id will be used to identify specific classes
    # which in a search can return data to the user.
    id = models.IntegerField('id', primary_key=True)
    # The Type field will be used to store the Type of class. This will also be the primary key.
    # There are different types of clases, i.e adults, adults fundamentals, kids, kids fundamentals.
    type = models.CharField('type', max_length=50)
    # The date field will store the date the class was held on.
    date = models.DateTimeField(default=timezone.now)  # add date field
    # The Time field stores the time that the class is offered on a particular day.
    #time = models.CharField('time', max_length=10)
    # The Size field will store an integer value for the number of participants allowed in the class.
    size = models.IntegerField('size')
    # The Instructor field will store the name of the instructor teaching the class.
    # Full will be a field that will indicate if the class is full or not. This will be helpful when our program queries available classes 
    # for participants to sign up for. The data in the field will be either Y (for yes) or N (for no).
    full = models.CharField('full', max_length = 1)
    instructor = models.CharField('instructor', max_length=50)
    # The Gi field will annotate whether a Gi will be required or not for class.
    # This attribute will be designated as Y(for yes) and N(for no) and stored as a char.
    gi = models.CharField('gi', max_length=1)

    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural = "Classes"


# The class 'Participants' will store the participants id from the class Users in the Users application.
# It will also store the class_id from the above classes model which will provide the unique id for each class that is offered.
# Every time a user signs up for a class both fields will be stored for the contact tracing portion of our program.
class Participants(models.Model):
    # used as a foreign key to get the participants id from the class users located in the Users application
    participant_id = models.IntegerField('participant_id', primary_key=True)
    # used to get the id of the class in the above classes model.
    class_id = models.ForeignKey(Classes, on_delete=models.DO_NOTHING)
    email = models.CharField('email', max_length=50)
    name = models.CharField('name', max_length=100)
    def __str__(self):
        return str(self.participant_id)
    class Meta:
        verbose_name_plural = "Participants"
