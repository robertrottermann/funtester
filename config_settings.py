import collections

c_settings = [
    {
        "module": "res.config.settings",
        "vals_list": [
            {'account_bank_reconciliation_start': False,
                'account_check_printing_date_label': True,
                'account_check_printing_layout': 'action_print_check_top',
                'account_check_printing_margin_left': 0.25,
                'account_check_printing_margin_right': 0.25,
                'account_check_printing_margin_top': 0.25,
                'account_check_printing_multi_stub': False,
                'account_tax_periodicity': 'monthly',
                'account_tax_periodicity_journal_id': 4,
                'account_tax_periodicity_reminder_day': 7,
                'alias_domain': False,
                'auth_signup_reset_password': True,
                'auth_signup_uninvited': 'b2c',
                'automatic_invoice': False,
                'chart_template_id': 1,
                'company_id': 1,
                'confirmation_template_id': 24,
                'crm_alias_prefix': False,
                'currency_exchange_journal_id': 5,
                'currency_interval_unit': 'manually',
                'currency_next_execution_date': False,
                'currency_provider': 'ecb',
                'default_invoice_policy': 'order',
                'default_picking_policy': 'direct',
                'default_sale_order_template_id': False,
                'deposit_default_product_id': False,
                'digest_emails': True,
                'digest_id': 1,
                'expense_alias_prefix': False,
                'external_email_server_default': True,
                'external_report_layout_id': 1471,
                'extract_show_ocr_option_selection': 'manual_send',
                'extract_single_line_per_tax': True,
                'fiscalyear_last_day': 31,
                'fiscalyear_last_month': '12',
                'generate_lead_from_alias': False,
                'group_analytic_accounting': False,
                'group_analytic_tags': False,
                'group_auto_done_setting': False,
                'group_cash_rounding': False,
                'group_discount_per_so_line': False,
                'group_display_incoterm': False,
                'group_fiscal_year': False,
                'group_lot_on_delivery_slip': False,
                'group_lot_on_invoice': False,
                'group_mass_mailing_campaign': False,
                'group_multi_currency': False,
                'group_product_pricelist': False,
                'group_product_variant': True,
                'group_proforma_sales': False,
                'group_sale_delivery_address': False,
                'group_sale_order_template': True,
                'group_sale_pricelist': False,
                'group_show_line_subtotals_tax_excluded': True,
                'group_show_line_subtotals_tax_included': False,
                'group_stock_adv_location': False,
                'group_stock_multi_locations': False,
                'group_stock_multi_warehouses': False,
                'group_stock_packaging': False,
                'group_stock_production_lot': True,
                'group_stock_tracking_lot': False,
                'group_stock_tracking_owner': False,
                'group_uom': False,
                'group_use_lead': False,
                'group_warning_account': False,
                'group_warning_sale': False,
                'group_warning_stock': False,
                'hr_employee_self_edit': False,
                'hr_presence_control_email': False,
                'hr_presence_control_email_amount': 0,
                'hr_presence_control_ip': False,
                'hr_presence_control_ip_list': False,
                'hr_presence_control_login': True,
                'incoterm_id': False,
                'invoice_is_email': True,
                'invoice_is_print': True,
                'invoice_is_snailmail': False,
                'invoice_terms': False,
                'l10n_ch_isr_preprinted_account': False,
                'l10n_ch_isr_preprinted_bank': False,
                'l10n_ch_isr_print_bank_location': False,
                'l10n_ch_isr_scan_line_left': 0,
                'l10n_ch_isr_scan_line_top': 0,
                'l10n_ch_print_qrcode': False,
                'lead_enrich_auto': 'manual',
                'map_box_token': False,
                'mass_mailing_mail_server_id': False,
                'mass_mailing_outgoing_mail_server': False,
                'module_account_accountant': True,
                'module_account_bank_statement_import_camt': True,
                'module_account_bank_statement_import_csv': True,
                'module_account_bank_statement_import_ofx': True,
                'module_account_bank_statement_import_qif': False,
                'module_account_batch_payment': False,
                'module_account_budget': False,
                'module_account_check_printing': True,
                'module_account_intrastat': False,
                'module_account_invoice_extract': True,
                'module_account_payment': False,
                'module_account_predictive_bills': True,
                'module_account_reports': True,
                'module_account_sepa': False,
                'module_account_sepa_direct_debit': False,
                'module_account_taxcloud': True,
                'module_account_yodlee': True,
                'module_auth_ldap': False,
                'module_auth_oauth': False,
                'module_base_gengo': False,
                'module_base_geolocalize': False,
                'module_base_import': True,
                'module_crm_iap_lead': False,
                'module_crm_iap_lead_enrich': False,
                'module_crm_iap_lead_website': False,
                'module_currency_rate_live': True,
                'module_delivery': False,
                'module_delivery_bpost': False,
                'module_delivery_dhl': False,
                'module_delivery_easypost': False,
                'module_delivery_fedex': False,
                'module_delivery_ups': False,
                'module_delivery_usps': False,
                'module_google_calendar': False,
                'module_google_drive': False,
                'module_google_spreadsheet': False,
                'module_hr_attendance': False,
                'module_hr_org_chart': True,
                'module_hr_payroll_account': True,
                'module_hr_payroll_account_sepa': False,
                'module_hr_payroll_expense': False,
                'module_hr_presence': False,
                'module_hr_skills': False,
                'module_inter_company_rules': False,
                'module_l10n_be_hr_payroll': False,
                'module_l10n_eu_service': False,
                'module_l10n_fr_hr_payroll': False,
                'module_l10n_in_hr_payroll': False,
                'module_ocn_client': False,
                'module_pad': False,
                'module_partner_autocomplete': True,
                'module_procurement_jit': '1',
                'module_product_email_template': False,
                'module_product_expiry': False,
                'module_product_margin': False,
                'module_sale_amazon': False,
                'module_sale_coupon': False,
                'module_sale_margin': False,
                'module_sale_product_configurator': False,
                'module_sale_product_matrix': False,
                'module_sale_quotation_builder': False,
                'module_snailmail_account': True,
                'module_stock_barcode': False,
                'module_stock_landed_costs': False,
                'module_stock_picking_batch': False,
                'module_web_unsplash': True,
                'paperformat_id': 2,
                'portal_confirmation_pay': True,
                'portal_confirmation_sign': True,
                'predictive_lead_scoring_fields': [[6, False, [1, 2, 3, 4, 5]]],
                'predictive_lead_scoring_fields_str': 'state_id,country_id,phone_state,email_state,source_id',
                'predictive_lead_scoring_start_date': '2019-12-02',
                'predictive_lead_scoring_start_date_str': '2019-12-02',
                'product_pricelist_setting': 'basic',
                'product_volume_volume_in_cubic_feet': '0',
                'product_weight_in_lbs': '0',
                'purchase_tax_id': 2,
                'qr_code': False,
                'quotation_validity_days': 30,
                'resource_calendar_id': 1,
                'sale_tax_id': 1,
                'security_lead': 0,
                'show_blacklist_buttons': False,
                'show_effect': True,
                'show_line_subtotals_tax_selection': 'tax_excluded',
                'snailmail_color': True,
                'snailmail_cover': False,
                'snailmail_duplex': False,
                'stock_mail_confirmation_template_id': 16,
                'stock_move_email_validation': False,
                'stock_move_sms_validation': True,
                'stock_sms_confirmation_template_id': 3,
                'tax_calculation_rounding_method': 'round_per_line',
                'tax_cash_basis_journal_id': 6,
                'tax_exigibility': False,
                'taxcloud_api_id': False,
                'taxcloud_api_key': False,
                'template_id': 9,
                'tic_category_id': False,
                'totals_below_sections': False,
                'transfer_account_id': 1,
                'unsplash_access_key': False,
                'use_anglo_saxon': True,
                'use_invoice_terms': False,
                'use_mailgateway': False,
                'use_quotation_validity_days': False,
                'use_security_lead': False,
                'user_default_rights': False
            }
        ]
    },
    {
        "module": "ir.config_parameter",
        "vals_list": [{'key': 'l10n_ch.isr_scan_line_top', 'value': 0.0}]
    },
    {
        "module": "ir.config_parameter",
        "vals_list": [{'key': 'l10n_ch.isr_scan_line_left', 'value': 0.0}]
    },
    {
        "module": "ir.default",
        "vals_list": [{'company_id': False,
            'condition': False,
            'field_id': 8070,
            'json_value': '"order"',
            'user_id': False}
        ]
    },
    {
        "module": "ir.default",
        "vals_list": [
            {
                'company_id': False,
                'condition': False,
                'field_id': 8341,
                'json_value': 'false',
                'user_id': False
            }
        ]
    },
    {
        "module": "ir.default",
        "vals_list": [
            {
                'company_id': False,
                'condition': False,
                'field_id': 8415,
                'json_value': '"direct"',
                'user_id': False
            }
        ]
    },
    {
        "module": "ir.config_parameter",
        "vals_list": [{'key': 'base_setup.default_external_email_server', 'value': True}]
    },
    {
        "module": "ir.config_parameter",
        "vals_list": [{'key': 'product.product_pricelist_setting', 'value': 'basic'}]
    },
    {
        "module": "ir.config_parameter",
        "vals_list": [{'key': 'product.weight_in_lbs', 'value': '0'}]
    },
    {
        "module": "ir.config_parameter",
        "vals_list": [{'key': 'product.volume_in_cubic_feet', 'value': '0'}]
    },
    {
        "module": "ir.config_parameter",
        "vals_list": [{'key': 'account.show_line_subtotals_tax_selection', 'value': 'tax_excluded'}]
    },
    {
        "module": "ir.config_parameter",
        "vals_list": [{'key': 'crm.iap.lead.enrich.setting', 'value': 'manual'}]
    },
    {
        "module": "ir.config_parameter",
        "vals_list": [{'key': 'sale.default_email_template', 'value': 9}]
    },
    {
        "module": "ir.config_parameter",
        "vals_list": [{'key': 'mail.catchall.domain', 'value': ''}]
    },


self
ir.config_parameter()
vals_list

self
ir.config_parameter()
vals_list

self
ir.config_parameter()
vals_list

self
mail.activity.type()
self
mail.activity.type()
vals_list
[{'category': 'tax_report',
  'delay_count': 1,
  'delay_from': 'previous_activity',
  'delay_unit': 'months',
  'force_next': False,
  'name': 'Tax Report for company My Company (San Francisco)',
  'res_model_id': 244,
  'summary': 'Periodic Tax Return'}]
