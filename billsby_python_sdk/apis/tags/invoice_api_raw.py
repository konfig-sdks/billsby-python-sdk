# coding: utf-8

"""
    Billsby API

    Billsby is a feature-rich \"Saas\" recurring payment platform, ranked as the leading subscription billing software by G2.  Billsby is designed to ensure customers can go live quickly, often within 1-2 hours.  To help facilitate this process we have a team of friendly knowledgeable advisors ready to help your business go live.      Billsby specializes in providing great customer service at an affordable price point - our technology is rated No 1 on G2 by our customers.  If you are a developer creating a solution for your customer, Billsby has a friendly well-documented API.  The Billsby team are here to provide support to developers in order to ensure a smooth migration or new system build.   Why not book a call, talk through your Billing requirements and we can let you know how we can help you transform your business..

    The version of the OpenAPI document: 1.3.5
    Generated by: https://konfigthis.com
"""

from billsby_python_sdk.paths.company_domain_customers_customer_unique_id_invoices.post import CreateOneTimeChargeRaw
from billsby_python_sdk.paths.company_domain_customers_customer_unique_id_refunds.post import CreateRefundRaw
from billsby_python_sdk.paths.invoices_invoice_number.get import DetailsRaw
from billsby_python_sdk.paths.company_domain_customers_customer_unique_id_invoices.get import GetCustomerInvoicesRaw
from billsby_python_sdk.paths.company_domain_customers_customer_unique_id_invoices_invoice_number_paymentlogs.get import GetPaymentLogsRaw
from billsby_python_sdk.paths.company_domain_companies_invoices.get import ListCompanyInvoicesRaw
from billsby_python_sdk.paths.company_domain_invoices_invoice_number_paid_offline.put import MarkAsPaidOfflineRaw
from billsby_python_sdk.paths.company_domain_invoices_invoice_number_written_off.put import MarkWrittenOffRaw
from billsby_python_sdk.paths.company_domain_invoices_invoice_number_payment.put import ReattemptPaymentRaw


class InvoiceApiRaw(
    CreateOneTimeChargeRaw,
    CreateRefundRaw,
    DetailsRaw,
    GetCustomerInvoicesRaw,
    GetPaymentLogsRaw,
    ListCompanyInvoicesRaw,
    MarkAsPaidOfflineRaw,
    MarkWrittenOffRaw,
    ReattemptPaymentRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
