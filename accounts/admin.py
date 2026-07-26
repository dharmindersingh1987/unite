from django.contrib import admin

# after installing django-import-export, add the following import
from import_export.admin import ImportExportModelAdmin



from .models import PacketUser
from .models import ExamForm
from .models import BankDetails

# after installing django-import-export, add the following import
from .resources import PacketUserResource, ExamFormResource, BankDetailsResource


@admin.register(PacketUser)
# class PacketUserAdmin(admin.ModelAdmin):
class PacketUserAdmin(ImportExportModelAdmin):
    resource_class = PacketUserResource
    list_display = (
        'pkt_id',
        'user_id',
        'password',
        'created_at',
    )

    search_fields = (
        'pkt_id',
        'user_id',
    )

    ordering = (
        'pkt_id',
    )
    
    list_filter = (
        'created_at',
    )


    readonly_fields = (
        'pkt_id',
        'user_id',
        'password',
        'created_at',
    )

    list_per_page = 50
    
    
@admin.register(ExamForm)
# class ExamFormAdmin(admin.ModelAdmin):
class ExamFormAdmin(ImportExportModelAdmin):
    resource_classes = [ExamFormResource]
    list_display = (
        'roll_no',
        # 'registration_no',
        # 'admission_no',
        # 'enroll_no',
        'student_name',
        # 'father_name',
        # 'mother_name',
        # 'student_batch',
        # 'college_id',
        # 'college_name',
        # 'branch_id',
        # 'branch_name',
        # 'exam_type',
        'sch_id',
        'scheme_title',
        # 'sem_year',
        # 'exam_Form_Date',
        # 'source_file'
    )
    
    list_filter = (
        'sem_year',
        'branch_name',
        # 'scheme_title',
        # 'college_id',
        # 'branch_id',
        # 'exam_type',
        # 'sch_id',
        
    )
    

    search_fields = (
        'roll_no',
        # 'registration_no',
        # 'admission_no',
        # 'enroll_no',
        'student_name',
        'scheme_title',
        'sch_id',
    )

    ordering = (
        'roll_no',
    )


    readonly_fields = (
        
        'roll_no',
        'registration_no',
        'admission_no',
        'enroll_no',
        'student_name',
        'father_name',
        'mother_name',
        'student_batch',
        'college_id',
        'college_name',
        'branch_id',
        'branch_name',
        'exam_type',
        'sch_id',
        'scheme_title',
        'sem_year',
        'exam_Form_Date',
        'source_file',
    )

    list_per_page = 50


@admin.register(BankDetails)
class BankDetailsAdmin(ImportExportModelAdmin):
    resource_classes = [BankDetailsResource]
    list_display = (
        'name',
        'email',
        'cont',
        'bank',
        'acc',
        'ifsc',
        'inst',
        'remarks'
    )
    
    search_fields = (
        'name',
        'email',
        'cont',
        'bank',
        'acc',
        'ifsc',
        'inst',
    )

    ordering = (
        'name',
    )


    # readonly_fields = (
        
    #     'name',
    #     'email',
    #     'cont',
    #     'bank',
    #     'acc',
    #     'ifsc',
    #     'inst',
    #     'remarks'
    # )

    list_per_page = 50