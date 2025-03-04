# table
'''
key : 테이블 약자 TB_000
values : [0] - 테이블 이름,
        [1] - [테이블 컬럼명]
'''
tables = {
 'TB_100' : ['tb24_100_biz_info', [
        'company_seq', 
        'biz_no', 
        'corp_no', 
        'realname_di', 
        'biz_type', 
        'head_flag', 
        'zipcode', 
        'addr1', 
        'addr2', 
        'ceo_birth_year', 
        'company_name', 
        'found_date', 
        'ceo_name', 
        'ceo_mobile', 
        'biz_tel_no', 
        'biz_fax_no', 
        'biz_email', 
        'standard_code', 
        'products', 
        'staff_name', 
        'staff_dept', 
        'staff_mobile', 
        'staff_email', 
        'kipo_no', 
        'metro_center_code', 
        'ipstone_flag', 
        'ipstone_year', 
        'ipstone_center_code', 
        'login_ip', 
        'login_time', 
        'company_type', 
        'del_flag', 
        'small_biz_type', 
        'position', 
        'write_time', 
        'modify_time', 
        'department', 
        'branch_type', 
        'phone_flag', 
        'email_flag', 
        'restriction_flag', 
        'restriction_period', 
        'restriction_period_end', 
        'temporary_key', 
        'temporary_key_start', 
        'temporary_key_end', 
        'tech_field_desc', 
        'biz_type_desc', 
        'main_product', 
        'covid_product', 
    ]],
    'TB_200' : ['tb24_200_corp_applicant', [
        'applicant_no',
        'applicant',
        'corp_no',
        'biz_no',
        'write_time',
        'modify_time',
        'ref_desc',
    ]],
    'TB_210' : ['tb24_210_univ_applicant', [
        'applicant_no',
        'applicant',
        'corp_no',
        'biz_no',
        'ref_desc',
        'write_time',
    ]],
    'TB_300' : ['tb24_300_corp_ipr_reg', [
        'ipr_seq',
        'applicant_no',
        'biz_no',
        'ipr_code',
        'applicant',
        'inventor',
        'agent',
        'main_ipc',
        'appl_no',
        'appl_date',
        'open_no',
        'open_date',
        'reg_no',
        'reg_date',
        'int_appl_no',
        'int_appl_date',
        'int_open_no',
        'int_open_date',
        'legal_status_desc',
        'exam_flag',
        'exam_date',
        'claim_cnt',
        'abstract',
        'title',
        'write_time',
        'modify_time',
        'survey_year',
        'survey_month',
    ]],
    'TB_310' : ['tb24_310_ipc_cpc', [
        'ipr_seq',
        # 'applicant_no', 특허고객번호
        'appl_no', # 출원번호
        'ipc_seq',
        'ipc_cpc',
        'ipc_cpc_code',
    ]],
    'TB_320' : ['tb24_320_priority', [
        'priority_seq',
        'ipr_seq',
        'applicant_no',
        'priority_nation',
        'priority_no',
        'priority_date',
    ]],
    'TB_400' : ['tb24_400_univ_ipr_reg', [
        'ipr_seq',
        'applicant_no',
        'biz_no2',
        'ipr_code',
        'applicant',
        'inventor',
        'agent',
        'main_ipc',
        'appl_no',
        'appl_date',
        'open_no',
        'open_date',
        'reg_no',
        'reg_date',
        'int_appl_no',
        'int_appl_date',
        'int_open_no',
        'int_open_date',
        'legal_status_desc',
        'exam_flag',
        'exam_date',
        'claim_cnt',
        'abstract',
        'title',
        'write_time',
        'modify_time',
        'survey_year',
        'survey_month',
    ]],
    'TB_410' : ['tb24_410_ipc_cpc', [
        'ipr_seq',
        # 'applicant_no',
        'appl_no', # 출원번호
        'ipc_seq',
        'ipc_cpc',
        'ipc_cpc_code',
    ]],
    'TB_420' : ['tb24_420_priority', [
        'priority_seq',
        'ipr_seq',
        'applicant_no',
        'priority_nation',
        'priority_no',
        'priority_date',
    ]],
}


# api 파라미터
'''
key : 특허/실용신안, 디자인, 상표
values : key : 300(400) 테이블 칼럼명
         values : api 출력값(파라미터)
'''
api_params = {
    'patent_utility' : {
        # 'applicant_no' : 'applicationNo', # 특허고객번호  ## 
        'applicant_no' : 'applicantNo', # 특허고객번호
        'title' : 'inventionTitle',  # 발명의 명칭(상표명, 디자인명)
        # '' : 'indexNo', # 일련번호
        'applicant' : 'applicantName',  # 출원인
        'main_ipc' : 'ipcNumber', # 대표 IPC 코드
        'appl_no' : 'applicationNumber', # 출원번호
        'appl_date' : 'applicationDate', # 출원일자
        'open_no' : 'openNumber', # 공개번호
        'open_date' : 'openDate', # 공개일자
        'reg_no' : 'registerNumber', # 등록번호
        'reg_date' : 'registerDate', # 등록일자
        'pub_no' : 'publicationNumber', # 공고번호
        'pub_date' : 'publicationDate', # 공고일자
        'legal_status_desc' : 'registerStatus', #법적상태
        'img_url' : 'drawing', # 이미지경로
        # 'abstract' : 'astrtCont', # 요약 ## xml파일에서 업음
    },
    'design' : {
        'applicant_no' : 'applicantNo', # 특허고객번호
        'title' : 'articleName', # 디자인물품명칭
        # '' : 'number', # 일련번호
        'applicant' : 'applicantName', # 출원인
        'inventor' : 'inventorName', # 창작자명
        'agent' : 'agentName', # 대리인명
        'appl_no' : 'applicationNumber',# 출원번호
        'appl_date' : 'applicationDate',# 출원일자
        'open_no' : 'openNumber',# 공개번호
        'open_date' : 'openDate',# 공개일자
        'reg_no' : 'registrationNumber',# 등록번호
        'reg_date' : 'registrationDate',# 등록일자
        'pub_no' : 'publicationNumber', # 공고번호
        'pub_date' : 'publicationDate', # 공고일자
        'legal_status_desc' : 'applicationStatus', # 법적상태
        'img_url' : 'imagePath', # 이미지경로
        'priority_no' : 'priorityNumber', # 우선권주장번호
        'priority_date' : 'priorityDate', # 우선권주장일자
        # '' : 'fullText', # 전문존재유무
        # '' : 'designMainClassification', # 디자인분류코드
        # '' : 'dsShpClssCd', # 형태분류
        # '' : 'designNumber', # 디자인 일련번호
        # '' : 'appReferenceNumber', # 출원참조번호
        # '' : 'regReferenceNumber', # 등록참조번호
        # '' : 'internationalRegisterNumber', # 등록공고번호
        # '' : 'internationalRegisterDate', # 등록공고일자
    },
    'trademark' : {
        'applicant_no' : 'applicantNo', # 특허고객번호
        'title' : 'title', # 상표명
        # '' : 'indexNo', # 인덱스 번호
        'applicant' : 'applicantName', # 출원인명 / 특허고객번호 ##
        'agent' : 'agentName', # 대리인
        'appl_no' : 'applicationNumber',# 출원번호
        'appl_date' : 'applicationDate',# 출원일자
        # '' : 'regPrivilegeName', # 등록권자명 / 특허고객번호 ##
        'reg_no' : 'registrationNumber', # 등록번호
        'reg_date' : 'registrationDate', # 등록일자
        'pub_no' : 'publicationNumber', # 공고번호
        'pub_date' : 'publicationDate', # 공고일자
        'legal_status_desc' : 'applicationStatus', # 출원상태
        'img_url' : 'drawing', # 이미지경로
        'priority_no' : 'priorityNumber', # 우선권 주장번호
        'priority_date' : 'priorityDate', # 우선권 주장일자
        # '' : 'fullText', # 전문존재유무
        # '' : 'appReferenceNumber', # 출원참조번호
        # '' : 'regReferenceNumber', # 등록참조번호
        # '' : 'internationalRegisterNumber', # 국제등록번호
        # '' : 'internationalRegisterDate', # 국제등록일자
        # '' : 'registrationPublicNumber', # 등록공고번호
        # '' : 'registrationPublicDate', # 등록공고일자
        # '' : 'classifictionCode', # 상품분류코드
        # '' : 'viennaCode', # 도형코드
    },
}

# batch size
BATCH_SIZE=50
