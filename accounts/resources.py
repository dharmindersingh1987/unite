from import_export import resources
from .models import BankDetails, PacketUser, ExamForm, SubListEven202526, SubListOdd202526, PacketPaymentDecember2025, PaperSetterDatabase

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

class SubListEven202526Resource(resources.ModelResource):
    class Meta:
        model = SubListEven202526
        import_id_fields = ('e_identity',)
        fields = (
            "select",
            "course",
            "year",
            "sem",
            "paper_name",
            "type",
            "paper_code",
            "credits",
            "e_identity",
            "maximum_marks",
            "dept",
            "dept_main",
            "e_email",
            "e_name",
            "e_institute",
            "e_contact",
            "level",
        )
        
class SubListOdd202526Resource(resources.ModelResource):
    class Meta:
        model = SubListOdd202526
        import_id_fields = ("e_identity",)
        fields = (
            "e_name",
            "e_institute",
            "e_email",
            "e_contact",
            "e_identity",
            "dept_main",
            "dept",
            "type",
            "course",
            "year",
            "sem",
            "paper_name",
            "paper_code",
            "time_allowed_mod",
            "maximum_marks",
            "level",
        )


class PacketPaymentDecember2025Resource(resources.ModelResource):
    class Meta:
        model = PacketPaymentDecember2025
        import_id_fields = ("pkt_id",)
        fields = (
            "id",
            "sr_no",
            "pkt_no",
            "pkt_id",
            "name",
            "dept",
            "inst",
            "email",
            "cont",
            "level",
            "qty",
            "bank",
            "account",
            "ifsc",
            "payment_stage",
            "payment",
            "remarks",
            "created_at",
            "updated_at",
        )

class PaperSetterDatabaseResource(resources.ModelResource):
    class Meta:
        model = PaperSetterDatabase
        import_id_fields = ("email",)
        fields = (
            "name",
            "institute",
            "email",
            "department",
            "paper_names",
            "active",
            "remarks",
            "created_at",
            "updated_at",
        )