from peewee import *

database = MySQLDatabase('adcostly', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True,
                                        'host': 'rm-rj9xftw3b40s26ivw6o.mysql.rds.aliyuncs.com', 'port': 3306,
                                        'user': 'adsreport_r', 'password': 'DB#adsr789&'})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class AdCostInsights(BaseModel):
    adset_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    campaign_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    category_type = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    clicks = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    country = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    cpa = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpc = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpm = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    cta = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    ctr = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    data_date = DateField()
    impressions = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    md5_key = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    placement = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    publisher = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ad_cost_insights'


class AdCostInsightsAge(BaseModel):
    adset_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    age = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    campaign_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    category_type = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    clicks = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    country = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    cpa = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpc = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpm = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    cta = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    ctr = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    data_date = DateField()
    gender = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    impressions = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    md5_key = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    publisher = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ad_cost_insights_age'


class AdCostInsightsCpa(BaseModel):
    adset_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    age = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    campaign_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    category_type = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    country = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    cta = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    data_date = DateField()
    gender = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    lead = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    md5_key = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    mobile_app_retention = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    mobile_app_roas = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    offsite_conversion = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_achievement_unlocked = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_activate_app = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_add_to_cart = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_app_install = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_complete_registration = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_initiated_checkout = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_level_achieved = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_purchase = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_view_content = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    onsite_conversion = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    onsite_conversion_messaging_first_reply = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    publisher = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    spend = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ad_cost_insights_cpa'


class AdCostInsightsCpaV2(BaseModel):
    adset_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    age = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    campaign_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    category_type = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    country = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    cta = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    data_date = DateField()
    gender = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    lead = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    md5_key = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    mobile_app_retention = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    mobile_app_roas = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    offsite_conversion = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_achievement_unlocked = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_activate_app = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_add_to_cart = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_app_install = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_complete_registration = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_initiated_checkout = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_level_achieved = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_purchase = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    omni_view_content = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    onsite_conversion = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    onsite_conversion_messaging_first_reply = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    placement = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    publisher = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    spend = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sub_category = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ad_cost_insights_cpa_v2'


class AdCostInsightsV2(BaseModel):
    adset_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    campaign_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    category_type = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    clicks = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    country = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    cpa = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpc = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpm = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    cta = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    ctr = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    data_date = DateField()
    impressions = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    md5_key = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    placement = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    publisher = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ad_cost_insights_v2'


class AdCostInsightsV3(BaseModel):
    adset_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    age = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    campaign_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    category_type = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    clicks = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    country = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    cpc = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpm = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    cta = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    ctr = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    data_date = DateField()
    gender = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    impressions = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    interest_word_ids = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    md5_key = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    placement = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    publisher = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    sub_category = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ad_cost_insights_v3'


class AdCostTopCampaigns(BaseModel):
    campaign_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    category_type = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    country = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    cta = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    placements = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    publisher = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ad_cost_top_campaigns'


class AdCostUserActionLog(BaseModel):
    action_path = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    action_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    company_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    product_name = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    result_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    search_params = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    take_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'ad_cost_user_action_log'


class AdFacebookAccount(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    expire_flag = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    expire_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    facebook_name = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    facebook_uid = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    token = CharField(constraints=[SQL("DEFAULT ''")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'ad_facebook_account'


class Migration(BaseModel):
    apply_time = IntegerField(null=True)
    version = CharField(primary_key=True)

    class Meta:
        table_name = 'migration'


class AcFbAdsetsMiddle(BaseModel):
    account_currency = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    adset_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
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


class AdInsightCpcAgeGender(BaseModel):
    adset_count = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    age = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    category_type = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    clicks = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpc = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpm = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    ctr = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    data_date = DateField()
    gender = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    impression = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    md5_key = CharField(constraints=[SQL("DEFAULT ''")], null=True, unique=True)
    spend = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ad_insight_cpc_age_gender'


class AdInsightCpcCountryPublisher(BaseModel):
    adset_count = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    category_type = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    clicks = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    country = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    cpc = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpm = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    cta = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    ctr = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    data_date = DateField()
    impression = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    md5_key = CharField(constraints=[SQL("DEFAULT ''")], null=True, unique=True)
    os_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    publisher = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    spend = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ad_insight_cpc_country_publisher'


class AdInsightCpcPublisherPosition(BaseModel):
    adset_count = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    category_type = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    clicks = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpc = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cpm = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    ctr = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    data_date = DateField()
    impression = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    md5_key = CharField(constraints=[SQL("DEFAULT ''")], null=True, unique=True)
    position = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    publisher = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    spend = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ad_insight_cpc_publisher_position'


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
