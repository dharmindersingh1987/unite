from import_export import resources
from .models import BankDetails, PacketUser, ExamForm

class PacketUserResource(resources.ModelResource):
    class Meta:
        model = PacketUser
        import_id_fields = ('pkt_id',)
        fields = ('pkt_id', 'user_id', 'password', 'created_at')
        
class ExamFormResource(resources.ModelResource):
    class Meta:
        model = ExamForm
        import_id_fields = ('roll_no',)
        fields = ('roll_no', 'registration_no', 'admission_no', 'enroll_no', 'student_name', 'father_name', 'mother_name', 'student_batch', 'college_id', 'college_name', 'branch_id', 'branch_name', 'exam_type', 'sch_id', 'scheme_title', 'sem_year', 'exam_Form_Date', 'source_file')
        
class BankDetailsResource(resources.ModelResource):
    class Meta:
        model = BankDetails
        import_id_fields = ('email',)
        fields = ('name', 'email', 'cont', 'bank', 'acc', 'ifsc', 'inst', 'remarks')