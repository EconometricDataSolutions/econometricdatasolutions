from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Stage_customer
from .models import Tran_customer
from .models import Dim_customer

 
@admin.register(Stage_customer)
class Stage_customer_admin(ImportExportModelAdmin):
    list_display = ('customer_account'
                    ,'customer_business_person'
                    , 'customer_name'
                    , 'customer_primary_phone'
                    , 'customer_zip'
                    , 'customer_street_1'
                    # , 'customer_street_2'
                    # , 'customer_street_3'
                    # , 'customer_street_4'
                    , 'customer_city'
                    , 'customer_state'
                    , 'customer_country'
                    , 'customer_address_type'
                    , 'customer_address_fax'
                    # , 'customer_country_code'
                    # , 'customer_idd_prefix'
                    , 'customer_account_activation_email'
                    , 'customer_advance_ship_notice'
                    , 'customer_order_submittal'
                    , 'customer_email_subscription'
                    # , 'customer_website'
                    # , 'customer_customer_reference'
                    , 'customer_default_order_comments'
                    , 'customer_default_invoice_comments'
                    # , 'customer_hide_cost_on_order_confirmation'
                    # , 'customer_allow_duplicate_po'
                    , 'customer_first_name_last_name'
                    , 'customer_work_phone'
                    , 'customer_ext'
                    , 'customer_cell_phone'
                    , 'customer_home_phone' 
                    , 'customer_fax'
                    , 'customer_corporate_account'
                    , 'customer_email_credit_hold'
                    , 'customer_credit_hold_email'
                    , 'customer_art_hold_email'
                    , 'customer_email_invoice'
                    , 'customer_invoice_notification'
                    , 'customer_email_invoice_past_due_alert'
                    , 'customer_invoice_past_due_alert'
                    , 'customer_email_statement'
                    , 'customer_statements'
                    , 'customer_email_credit_memo'
                    , 'customer_credit_memo_email'
                    , 'customer_email_return_reminder'
                    , 'customer_return_reminder_email'
                    , 'customer_reference_associate_email'
                    , 'customer_fed_tax_code'
                    , 'customer_fed_tax_freight'
                    , 'customer_fed_exempt_number'
                    # , 'customer_signed_fed_certificate'
                    , 'customer_state_tax_code'
                    , 'customer_state_tax_freight'
                    , 'customer_state_exempt_number'
                    # , 'customer_signed_state_certificate'
                    , 'customer_warehouse'
                    , 'customer_site'
                    , 'customer_type'
                    , 'customer_territory'
                    , 'customer_site_number'
                    , 'customer_source'
                    # , 'customer_royalty_included'
                    , 'customer_route_codes'
                    , 'customer_route_sequence'
                    , 'customer_ship_via'
                    , 'customer_price_suffix'
                    , 'customer_drop_ship'
                    , 'customer_high_low_discount'
                    , 'customer_bill_to_name'
                    , 'customer_bill_to_street_1'
                    # , 'customer_bill_to_street_2'
                    # , 'customer_bill_to_street_3'
                    # , 'customer_bill_to_street_4'
                    , 'customer_bill_to_city'
                    , 'customer_bill_to_state'
                    , 'customer_bill_to_zipcode'
                    , 'customer_bill_to_country'
                    , 'customer_bill_to_phone'
                    , 'customer_bill_to_fax'
                    , 'customer_opened'
                    # , 'customer_last_invoice'
                    # , 'customer_last_payment'
                    , 'customer_terms'
                    , 'customer_days'
                    , 'customer_other'
                    , 'customer_past_due_max'
                    , 'customer_invoice_due_days'
                    , 'customer_cod'
                    , 'customer_prepay_cc'
                    , 'customer_charge_freight'
                    # , 'customer_collector'
                    , 'customer_credit_hold_code'
                    , 'customer_credit_limit'
                    , 'customer_last_reviewed'
                    , 'customer_include_remakes'
                    , 'customer_on_any_order_lower'
                    , 'customer_on_any_order_higher'
                    # , 'customer_current_lower'
                    # , 'customer_current_higher'
                    # , 'customer_30_days_ar_lower'
                    # , 'customer_30_days_ar_higher'
                    # , 'customer_60_days_ar_lower'
                    # , 'customer_60_days_ar_higher'
                    # , 'customer_90_days_ar_lower'
                    # , 'customer_90_days_ar_higher'
                    # , 'customer_120_days_ar_lower'
                    # , 'customer_120_days_ar_higher'
                    , 'customer_reference_1'
                    , 'customer_waive_minimum_deposit'
                    # , 'customer_reference_2'
                    , 'customer_account_suspended'
                    , 'customer_saleperson_1'
                    # , 'customer_saleperson_2'
                    # , 'customer_saleperson_3'
                    # , 'customer_saleperson_4'
                    # , 'customer_saleperson_5'
                    # , 'customer_constant_1'
                    # , 'customer_constant_2'
                    # , 'customer_constant_3'
                    # , 'customer_constant_4'
                    # , 'customer_constant_5'
                    # , 'customer_constant_6'
                    # , 'customer_constant_7'
                    # , 'customer_constant_8'
                    # , 'customer_constant_9'
                    # , 'customer_constant_10'
                    # , 'customer_constant_11'
                    # , 'customer_constant_12'
                    # , 'customer_constant_13'
                    # , 'customer_constant_14'
                    # , 'customer_constant_15'
                    # , 'customer_constant_16'
                    # , 'customer_constant_17'
                    # , 'customer_constant_18'
                    # , 'customer_constant_19'
                    # , 'customer_constant_20'
                    # , 'user_defined_1'
                    # , 'user_defined_2'
                    # , 'user_defined_3'
                    # , 'user_defined_4'
                    # , 'user_defined_5'
                    # , 'user_defined_6'
                    # , 'user_defined_7'
                    # , 'user_defined_8'
                    # , 'user_defined_9'
                    # , 'user_defined_10'
                    # , 'user_defined_11'
                    # , 'user_defined_12'
                    # , 'user_defined_13'
                    # , 'user_defined_14'
                    # , 'user_defined_15'
                    # , 'user_defined_16'
                    # , 'user_defined_17'
                    # , 'user_defined_18'
                    # , 'user_defined_19'
                    # , 'user_defined_20'
                    , 'customer_customer_w_tax'
                    , 'customer_limit_number_of_dealer_logins_to'
                    , 'customer_days_to_hold_quotes'
                    # , 'customer_enable_price_calculation'
                    # , 'customer_enable_freight_calculation'
                    # , 'customer_collection_display'
                    # , 'customer_internal_xml_id'
                    # , 'customer_client_quote_letter_verbiage'
                    # , 'customer_booked_orders'
                    # , 'customer_deposits'
                    # , 'customer_balance_due'
                    # , 'customer_open_ar'
                    # , 'customer_30_day_ar'
                    # , 'customer_60_day_ar'
                    # , 'customer_90_day_ar'
                    # , 'customer_120_day_ar'
                    # , 'customer_unapplied'
                    # , 'customer_total_open_ar'
                    # , 'customer_ytd'
                    # , 'customer_previous_year'
                    # , 'customer_high_sale'
                    # , 'customer_py_high_sale'
                    # , 'customer_cogs'
                    # , 'customer_py_cogs'
                    , 'customer_avg_days_to_pay'
                    , 'customer_pv_avg_days_to_pay'
                    , 'customer_times_past_due'
                    , 'customer_py_times_past_due'
                                    
                  )


@admin.register(Tran_customer)
class Tran_customer_admin(ImportExportModelAdmin):
    list_display = (  'customer_account'
                    , 'customer_business_person'
                    , 'customer_name'
                    , 'customer_primary_phone'
                    , 'customer_zip'
                    , 'customer_street_1'
                    # , 'customer_street_2'
                    # , 'customer_street_3'
                    # , 'customer_street_4'
                    , 'customer_city'
                    , 'customer_state'
                    , 'customer_country'
                    , 'customer_address_type'
                    , 'customer_address_fax'
                    # , 'customer_country_code'
                    # , 'customer_idd_prefix'
                    , 'customer_account_activation_email'
                    , 'customer_advance_ship_notice'
                    , 'customer_order_submittal'
                    , 'customer_email_subscription'
                    # , 'customer_website'
                    # , 'customer_customer_reference'
                    , 'customer_default_order_comments'
                    , 'customer_default_invoice_comments'
                    # , 'customer_hide_cost_on_order_confirmation'
                    # , 'customer_allow_duplicate_po'
                    , 'customer_first_name_last_name'
                    , 'customer_work_phone'
                    , 'customer_ext'
                    , 'customer_cell_phone'
                    , 'customer_home_phone' 
                    , 'customer_fax'
                    , 'customer_corporate_account'
                    , 'customer_email_credit_hold'
                    , 'customer_credit_hold_email'
                    , 'customer_art_hold_email'
                    , 'customer_email_invoice'
                    , 'customer_invoice_notification'
                    , 'customer_email_invoice_past_due_alert'
                    , 'customer_invoice_past_due_alert'
                    , 'customer_email_statement'
                    , 'customer_statements'
                    , 'customer_email_credit_memo'
                    , 'customer_credit_memo_email'
                    , 'customer_email_return_reminder'
                    , 'customer_return_reminder_email'
                    , 'customer_reference_associate_email'
                    , 'customer_fed_tax_code'
                    , 'customer_fed_tax_freight'
                    , 'customer_fed_exempt_number'
                    # , 'customer_signed_fed_certificate'
                    , 'customer_state_tax_code'
                    , 'customer_state_tax_freight'
                    , 'customer_state_exempt_number'
                    # , 'customer_signed_state_certificate'
                    , 'customer_warehouse'
                    , 'customer_site'
                    , 'customer_type'
                    , 'customer_territory'
                    , 'customer_site_number'
                    , 'customer_source'
                    # , 'customer_royalty_included'
                    , 'customer_route_codes'
                    , 'customer_route_sequence'
                    , 'customer_ship_via'
                    , 'customer_price_suffix'
                    , 'customer_drop_ship'
                    , 'customer_high_low_discount'
                    , 'customer_bill_to_name'
                    , 'customer_bill_to_street_1'
                    # , 'customer_bill_to_street_2'
                    # , 'customer_bill_to_street_3'
                    # , 'customer_bill_to_street_4'
                    , 'customer_bill_to_city'
                    , 'customer_bill_to_state'
                    , 'customer_bill_to_zipcode'
                    , 'customer_bill_to_country'
                    , 'customer_bill_to_phone'
                    , 'customer_bill_to_fax'
                    , 'customer_opened'
                    # , 'customer_last_invoice'
                    # , 'customer_last_payment'
                    , 'customer_terms'
                    , 'customer_days'
                    , 'customer_other'
                    , 'customer_past_due_max'
                    , 'customer_invoice_due_days'
                    , 'customer_cod'
                    , 'customer_prepay_cc'
                    , 'customer_charge_freight'
                    # , 'customer_collector'
                    , 'customer_credit_hold_code'
                    , 'customer_credit_limit'
                    , 'customer_last_reviewed'
                    , 'customer_include_remakes'
                    , 'customer_on_any_order_lower'
                    , 'customer_on_any_order_higher'
                    # , 'customer_current_lower'
                    # , 'customer_current_higher'
                    # , 'customer_30_days_ar_lower'
                    # , 'customer_30_days_ar_higher'
                    # , 'customer_60_days_ar_lower'
                    # , 'customer_60_days_ar_higher'
                    # , 'customer_90_days_ar_lower'
                    # , 'customer_90_days_ar_higher'
                    # , 'customer_120_days_ar_lower'
                    # , 'customer_120_days_ar_higher'
                    , 'customer_reference_1'
                    , 'customer_waive_minimum_deposit'
                    # , 'customer_reference_2'
                    , 'customer_account_suspended'
                    , 'customer_saleperson_1'
                    # , 'customer_saleperson_2'
                    # , 'customer_saleperson_3'
                    # , 'customer_saleperson_4'
                    # , 'customer_saleperson_5'
                    # , 'customer_constant_1'
                    # , 'customer_constant_2'
                    # , 'customer_constant_3'
                    # , 'customer_constant_4'
                    # , 'customer_constant_5'
                    # , 'customer_constant_6'
                    # , 'customer_constant_7'
                    # , 'customer_constant_8'
                    # , 'customer_constant_9'
                    # , 'customer_constant_10'
                    # , 'customer_constant_11'
                    # , 'customer_constant_12'
                    # , 'customer_constant_13'
                    # , 'customer_constant_14'
                    # , 'customer_constant_15'
                    # , 'customer_constant_16'
                    # , 'customer_constant_17'
                    # , 'customer_constant_18'
                    # , 'customer_constant_19'
                    # , 'customer_constant_20'
                    # , 'user_defined_1'
                    # , 'user_defined_2'
                    # , 'user_defined_3'
                    # , 'user_defined_4'
                    # , 'user_defined_5'
                    # , 'user_defined_6'
                    # , 'user_defined_7'
                    # , 'user_defined_8'
                    # , 'user_defined_9'
                    # , 'user_defined_10'
                    # , 'user_defined_11'
                    # , 'user_defined_12'
                    # , 'user_defined_13'
                    # , 'user_defined_14'
                    # , 'user_defined_15'
                    # , 'user_defined_16'
                    # , 'user_defined_17'
                    # , 'user_defined_18'
                    # , 'user_defined_19'
                    # , 'user_defined_20'
                    , 'customer_customer_w_tax'
                    , 'customer_limit_number_of_dealer_logins_to'
                    , 'customer_days_to_hold_quotes'
                    # , 'customer_enable_price_calculation'
                    # , 'customer_enable_freight_calculation'
                    # , 'customer_collection_display'
                    # , 'customer_internal_xml_id'
                    # , 'customer_client_quote_letter_verbiage'
                    # , 'customer_booked_orders'
                    # , 'customer_deposits'
                    # , 'customer_balance_due'
                    # , 'customer_open_ar'
                    # , 'customer_30_day_ar'
                    # , 'customer_60_day_ar'
                    # , 'customer_90_day_ar'
                    # , 'customer_120_day_ar'
                    # , 'customer_unapplied'
                    # , 'customer_total_open_ar'
                    # , 'customer_ytd'
                    # , 'customer_previous_year'
                    # , 'customer_high_sale'
                    # , 'customer_py_high_sale'
                    # , 'customer_cogs'
                    # , 'customer_py_cogs'
                    , 'customer_avg_days_to_pay'
                    , 'customer_pv_avg_days_to_pay'
                    , 'customer_times_past_due'
                    , 'customer_py_times_past_due'

                    , 'row_is_current', 'row_start_date'
                    , 'row_end_date', 'row_change_reason')


@admin.register(Dim_customer)
class Dim_customer_admin(ImportExportModelAdmin):
    list_display = (  'customer_account'
                    , 'customer_business_person'
                    , 'customer_name'
                    , 'customer_primary_phone'
                    , 'customer_zip'
                    , 'customer_street_1'
                    # , 'customer_street_2'
                    # , 'customer_street_3'
                    # , 'customer_street_4'
                    , 'customer_city'
                    , 'customer_state'
                    , 'customer_country'
                    , 'customer_address_type'
                    , 'customer_address_fax'
                    # , 'customer_country_code'
                    # , 'customer_idd_prefix'
                    , 'customer_account_activation_email'
                    , 'customer_advance_ship_notice'
                    , 'customer_order_submittal'
                    , 'customer_email_subscription'
                    # , 'customer_website'
                    # , 'customer_customer_reference'
                    , 'customer_default_order_comments'
                    , 'customer_default_invoice_comments'
                    # , 'customer_hide_cost_on_order_confirmation'
                    # , 'customer_allow_duplicate_po'
                    , 'customer_first_name_last_name'
                    , 'customer_work_phone'
                    , 'customer_ext'
                    , 'customer_cell_phone'
                    , 'customer_home_phone' 
                    , 'customer_fax'
                    , 'customer_corporate_account'
                    , 'customer_email_credit_hold'
                    , 'customer_credit_hold_email'
                    , 'customer_art_hold_email'
                    , 'customer_email_invoice'
                    , 'customer_invoice_notification'
                    , 'customer_email_invoice_past_due_alert'
                    , 'customer_invoice_past_due_alert'
                    , 'customer_email_statement'
                    , 'customer_statements'
                    , 'customer_email_credit_memo'
                    , 'customer_credit_memo_email'
                    , 'customer_email_return_reminder'
                    , 'customer_return_reminder_email'
                    , 'customer_reference_associate_email'
                    , 'customer_fed_tax_code'
                    , 'customer_fed_tax_freight'
                    , 'customer_fed_exempt_number'
                    # , 'customer_signed_fed_certificate'
                    , 'customer_state_tax_code'
                    , 'customer_state_tax_freight'
                    , 'customer_state_exempt_number'
                    # , 'customer_signed_state_certificate'
                    , 'customer_warehouse'
                    , 'customer_site'
                    , 'customer_type'
                    , 'customer_territory'
                    , 'customer_site_number'
                    , 'customer_source'
                    # , 'customer_royalty_included'
                    , 'customer_route_codes'
                    , 'customer_route_sequence'
                    , 'customer_ship_via'
                    , 'customer_price_suffix'
                    , 'customer_drop_ship'
                    , 'customer_high_low_discount'
                    , 'customer_bill_to_name'
                    , 'customer_bill_to_street_1'
                    # , 'customer_bill_to_street_2'
                    # , 'customer_bill_to_street_3'
                    # , 'customer_bill_to_street_4'
                    , 'customer_bill_to_city'
                    , 'customer_bill_to_state'
                    , 'customer_bill_to_zipcode'
                    , 'customer_bill_to_country'
                    , 'customer_bill_to_phone'
                    , 'customer_bill_to_fax'
                    , 'customer_opened'
                    # , 'customer_last_invoice'
                    # , 'customer_last_payment'
                    , 'customer_terms'
                    , 'customer_days'
                    , 'customer_other'
                    , 'customer_past_due_max'
                    , 'customer_invoice_due_days'
                    , 'customer_cod'
                    , 'customer_prepay_cc'
                    , 'customer_charge_freight'
                    # , 'customer_collector'
                    , 'customer_credit_hold_code'
                    , 'customer_credit_limit'
                    , 'customer_last_reviewed'
                    , 'customer_include_remakes'
                    , 'customer_on_any_order_lower'
                    , 'customer_on_any_order_higher'
                    # , 'customer_current_lower'
                    # , 'customer_current_higher'
                    # , 'customer_30_days_ar_lower'
                    # , 'customer_30_days_ar_higher'
                    # , 'customer_60_days_ar_lower'
                    # , 'customer_60_days_ar_higher'
                    # , 'customer_90_days_ar_lower'
                    # , 'customer_90_days_ar_higher'
                    # , 'customer_120_days_ar_lower'
                    # , 'customer_120_days_ar_higher'
                    , 'customer_reference_1'
                    , 'customer_waive_minimum_deposit'
                    # , 'customer_reference_2'
                    , 'customer_account_suspended'
                    , 'customer_saleperson_1'
                    # , 'customer_saleperson_2'
                    # , 'customer_saleperson_3'
                    # , 'customer_saleperson_4'
                    # , 'customer_saleperson_5'
                    # , 'customer_constant_1'
                    # , 'customer_constant_2'
                    # , 'customer_constant_3'
                    # , 'customer_constant_4'
                    # , 'customer_constant_5'
                    # , 'customer_constant_6'
                    # , 'customer_constant_7'
                    # , 'customer_constant_8'
                    # , 'customer_constant_9'
                    # , 'customer_constant_10'
                    # , 'customer_constant_11'
                    # , 'customer_constant_12'
                    # , 'customer_constant_13'
                    # , 'customer_constant_14'
                    # , 'customer_constant_15'
                    # , 'customer_constant_16'
                    # , 'customer_constant_17'
                    # , 'customer_constant_18'
                    # , 'customer_constant_19'
                    # , 'customer_constant_20'
                    # , 'user_defined_1'
                    # , 'user_defined_2'
                    # , 'user_defined_3'
                    # , 'user_defined_4'
                    # , 'user_defined_5'
                    # , 'user_defined_6'
                    # , 'user_defined_7'
                    # , 'user_defined_8'
                    # , 'user_defined_9'
                    # , 'user_defined_10'
                    # , 'user_defined_11'
                    # , 'user_defined_12'
                    # , 'user_defined_13'
                    # , 'user_defined_14'
                    # , 'user_defined_15'
                    # , 'user_defined_16'
                    # , 'user_defined_17'
                    # , 'user_defined_18'
                    # , 'user_defined_19'
                    # , 'user_defined_20'
                    , 'customer_customer_w_tax'
                    , 'customer_limit_number_of_dealer_logins_to'
                    , 'customer_days_to_hold_quotes'
                    # , 'customer_enable_price_calculation'
                    # , 'customer_enable_freight_calculation'
                    # , 'customer_collection_display'
                    # , 'customer_internal_xml_id'
                    # , 'customer_client_quote_letter_verbiage'
                    # , 'customer_booked_orders'
                    # , 'customer_deposits'
                    # , 'customer_balance_due'
                    # , 'customer_open_ar'
                    # , 'customer_30_day_ar'
                    # , 'customer_60_day_ar'
                    # , 'customer_90_day_ar'
                    # , 'customer_120_day_ar'
                    # , 'customer_unapplied'
                    # , 'customer_total_open_ar'
                    # , 'customer_ytd'
                    # , 'customer_previous_year'
                    # , 'customer_high_sale'
                    # , 'customer_py_high_sale'
                    # , 'customer_cogs'
                    # , 'customer_py_cogs'
                    , 'customer_avg_days_to_pay'
                    , 'customer_pv_avg_days_to_pay'
                    , 'customer_times_past_due'
                    , 'customer_py_times_past_due'

                  , 'row_is_current', 'row_start_date'
                  , 'row_end_date', 'row_change_reason')