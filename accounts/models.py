from django.db import models

class PacketUser(models.Model):
    pkt_id = models.IntegerField(primary_key = True)
    user_id = models.CharField(max_length = 100)
    password = models.CharField(max_length = 255)

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'packet_user'
        ordering = ['pkt_id']

    def __str__(self):
        return self.user_id
    
    
class ExamForm(models.Model):
    roll_no = models.IntegerField(primary_key = True)
    registration_no = models.CharField(max_length=255)
    admission_no = models.CharField(max_length=255)
    enroll_no = models.CharField(max_length=255)
    student_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    student_batch = models.IntegerField()
    college_id = models.IntegerField()
    college_name = models.CharField(max_length=255)
    branch_id = models.IntegerField()
    branch_name = models.CharField(max_length=255)
    exam_type   = models.CharField(max_length=255)
    sch_id  = models.IntegerField()
    scheme_title = models.CharField(max_length=255)
    sem_year = models.IntegerField()
    exam_Form_Date = models.CharField(max_length=255)
    source_file = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'exam_form'
        ordering = ['roll_no']
        
      
    def __str__(self):
        return self.student_name
    
    
class BankDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cont = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    acc = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=255)
    inst = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'bank_details'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class SubListEven202526(models.Model):
    select = models.IntegerField()
    course = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    sem = models.CharField(max_length=255)
    paper_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    paper_code = models.CharField(max_length=255)
    credits = models.CharField(max_length=255)
    e_identity = models.CharField(max_length=255)
    maximum_marks = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    dept_main = models.CharField(max_length=255)
    e_email = models.CharField(max_length=255)
    e_name = models.CharField(max_length=255)   
    e_institute = models.CharField(max_length=255)
    e_contact = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    
    