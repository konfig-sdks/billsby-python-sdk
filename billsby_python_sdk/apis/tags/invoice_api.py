# coding: utf-8

"""
    Billsby API

    Billsby is a feature-rich \"Saas\" recurring payment platform, ranked as the leading subscription billing software by G2.  Billsby is designed to ensure customers can go live quickly, often within 1-2 hours.  To help facilitate this process we have a team of friendly knowledgeable advisors ready to help your business go live.      Billsby specializes in providing great customer service at an affordable price point - our technology is rated No 1 on G2 by our customers.  If you are a developer creating a solution for your customer, Billsby has a friendly well-documented API.  The Billsby team are here to provide support to developers in order to ensure a smooth migration or new system build.   Why not book a call, talk through your Billing requirements and we can let you know how we can help you transform your business..

    The version of the OpenAPI document: 1.3.5
    Generated by: https://konfigthis.com
"""

from billsby_python_sdk.paths.company_domain_customers_customer_unique_id_invoices.post import CreateOneTimeCharge
from billsby_python_sdk.paths.company_domain_customers_customer_unique_id_refunds.post import CreateRefund
from billsby_python_sdk.paths.invoices_invoice_number.get import Details
from billsby_python_sdk.paths.company_domain_customers_customer_unique_id_invoices.get import GetCustomerInvoices
from billsby_python_sdk.paths.company_domain_customers_customer_unique_id_invoices_invoice_number_paymentlogs.get import GetPaymentLogs
from billsby_python_sdk.paths.company_domain_companies_invoices.get import ListCompanyInvoices
from billsby_python_sdk.paths.company_domain_invoices_invoice_number_paid_offline.put import MarkAsPaidOffline
from billsby_python_sdk.paths.company_domain_invoices_invoice_number_written_off.put import MarkWrittenOff
from billsby_python_sdk.paths.company_domain_invoices_invoice_number_payment.put import ReattemptPayment
from billsby_python_sdk.apis.tags.invoice_api_raw import InvoiceApiRaw


class InvoiceApi(
    CreateOneTimeCharge,
    CreateRefund,
    Details,
    GetCustomerInvoices,
    GetPaymentLogs,
    ListCompanyInvoices,
    MarkAsPaidOffline,
    MarkWrittenOff,
    ReattemptPayment,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: InvoiceApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = InvoiceApiRaw(api_client)
