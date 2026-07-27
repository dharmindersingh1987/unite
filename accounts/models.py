from django.db import models

class PacketUser(models.Model):
    pkt_id = models.IntegerField(primary_key = True)
    user_id = models.CharField(max_length = 100)
    password = models.CharField(max_length = 255)

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'packet_user'
        verbose_name = "Packet id, user id and password"
        verbose_name_plural = "Packet id, user id and password Even 2025-26"
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
        verbose_name = "Students Exam Form Details"
        verbose_name_plural = "Students Exam Form Details"
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
        verbose_name = "Paper Setter and Evaluators Bank Details"
        verbose_name_plural = "Paper Setter and Evaluators Bank Details"
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
    
    class Meta:
        db_table = 'sublist_even_202526'
        verbose_name = "Sub List Even 2025-26"
        verbose_name_plural = "Sub List Even 2025-26"
        ordering = ['select']
        
    def __str__(self):
        return self.paper_name
    
class SubListOdd202526(models.Model):
    e_name = models.CharField(max_length=255)
    e_institute = models.CharField(max_length=255)
    e_email = models.CharField(max_length=255)
    e_contact = models.CharField(max_length=255)
    e_identity = models.CharField(max_length=255)
    dept_main = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    sem = models.CharField(max_length=255)
    paper_name = models.CharField(max_length=255)
    paper_code = models.CharField(max_length=255)
    time_allowed_mod = models.CharField(max_length=255)
    maximum_marks = models.CharField(max_length=255)
    level = models.CharField(max_length=255, db_column="Level")
    
    class Meta:
        db_table = 'sublist_odd_202526'
        ordering = ['e_name']
        verbose_name = "Sub List Odd 2025-26"
        verbose_name_plural = "Sub List Odd 2025-26"
        
    def __str__(self):
        return self.paper_name




class PacketPaymentDecember2025(models.Model):
    sr_no = models.CharField(max_length=50)
    pkt_no = models.CharField(max_length=50)
    pkt_id = models.CharField(max_length=50, unique=True)

    name = models.CharField(max_length=200)
    dept = models.CharField(max_length=200, null=True, blank=True)
    inst = models.CharField(max_length=250, null=True, blank=True)

    email = models.EmailField(max_length=254)
    cont = models.CharField(max_length=20)

    level = models.CharField(max_length=50)
    qty = models.PositiveIntegerField()

    bank = models.CharField(max_length=200)
    account = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=20)

    payment_stage = models.CharField(max_length=100)
    payment = models.CharField()

    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "packet_payment"
        ordering = ["sr_no"]
        verbose_name = "Packet Payment Odd 2025-26"
        verbose_name_plural = "Packet Payment Odd 2025-26"

    def __str__(self):
        return f"{self.pkt_id} - {self.name}"
    
    
    
class PaperSetterDatabase(models.Model):
    name = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=255)
    paper_names = models.TextField(help_text="Comma-separated paper names / specialization")
    active = models.BooleanField(default=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "paper_setter_database"
        ordering = ["name"]
        verbose_name = "Paper Setter Database"
        verbose_name_plural = "Paper Setter Database"

    def __str__(self):
        return self.name