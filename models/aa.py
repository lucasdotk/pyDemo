from peewee import *

database = MySQLDatabase('lucas', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '127.0.0.1', 'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AcAdsetInsightsAge(BaseModel):
    actions = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    adset_id = BigIntegerField(index=True)
    age = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    clicks = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpa = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    cpc = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpm = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    ctr = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    data_date = DateField()
    gender = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    id = IntegerField()
    impressions = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ac_adset_insights_age'
        indexes = (
            (('id', 'adset_id'), True),
        )
        primary_key = CompositeKey('adset_id', 'id')

class AcAudience(BaseModel):
    account_num = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    audience = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    country_segment = TextField(null=True)
    cpc = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpm = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    effect_data = TextField(null=True)
    interest_id = BigIntegerField(null=True, unique=True)
    interest_name = CharField(null=True)
    interest_type = CharField(null=True)
    kd_value = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ac_audience'

class AcAudience2(BaseModel):
    account_num = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    audience = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    country_segment = TextField(null=True)
    cpc = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpm = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    effect_data = TextField(null=True)
    interest_id = BigIntegerField(null=True)
    interest_name = CharField(null=True)
    interest_type = CharField(null=True)
    kd_value = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ac_audience_2'
        indexes = (
            (('interest_id', 'interest_name'), True),
        )

class AcFbAdsetsMiddle(BaseModel):
    account_currency = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    adset_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True, unique=True)
    advertisers = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    age_insight_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    category_types = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    country_insight_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    ctas = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    interests = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    os_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    platform_insight_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ac_fb_adsets_middle'

class Business(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    email = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    leader_id = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    name = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    permission = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sales_flag = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'business'

class Migration(BaseModel):
    apply_time = IntegerField(null=True)
    version = CharField(primary_key=True)

    class Meta:
        table_name = 'migration'

class OverseasCompanyAnalysis(BaseModel):
    analysis_data = TextField(null=True)
    bk_int1 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    bk_int2 = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    bk_string1 = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    bk_string2 = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    company_name = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    country = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    first_seen = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    last_seen = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'overseas_company_analysis'

