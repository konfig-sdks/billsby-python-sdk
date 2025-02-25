import typing_extensions

from billsby_python_sdk.paths import PathValues
from billsby_python_sdk.apis.paths.company_domain_customers import CompanyDomainCustomers
from billsby_python_sdk.apis.paths.company_domain_customers_customer_unique_id import CompanyDomainCustomersCustomerUniqueId
from billsby_python_sdk.apis.paths.company_domain_customers_customer_unique_id_subscriptions import CompanyDomainCustomersCustomerUniqueIdSubscriptions
from billsby_python_sdk.apis.paths.company_domain_customers_customer_unique_id_subscriptions_featuretags import CompanyDomainCustomersCustomerUniqueIdSubscriptionsFeaturetags
from billsby_python_sdk.apis.paths.company_domain_customers_customer_unique_id_invoices_invoice_number_paymentlogs import CompanyDomainCustomersCustomerUniqueIdInvoicesInvoiceNumberPaymentlogs
from billsby_python_sdk.apis.paths.company_domain_customers_customer_unique_id_paymentdetailsrequest import CompanyDomainCustomersCustomerUniqueIdPaymentdetailsrequest
from billsby_python_sdk.apis.paths.company_domain_customers_customer_unique_id_payment_card import CompanyDomainCustomersCustomerUniqueIdPaymentCard
from billsby_python_sdk.apis.paths.company_domain_customers_customer_unique_id_invoices import CompanyDomainCustomersCustomerUniqueIdInvoices
from billsby_python_sdk.apis.paths.company_domain_customers_customer_unique_id_gdprcleanup import CompanyDomainCustomersCustomerUniqueIdGdprcleanup
from billsby_python_sdk.apis.paths.company_domain_subscriptions import CompanyDomainSubscriptions
from billsby_python_sdk.apis.paths.company_domain_subscriptions_subscription_unique_id import CompanyDomainSubscriptionsSubscriptionUniqueId
from billsby_python_sdk.apis.paths.company_domain_subscriptions_subscription_unique_id_shipping_address import CompanyDomainSubscriptionsSubscriptionUniqueIdShippingAddress
from billsby_python_sdk.apis.paths.company_domain_subscriptions_subscription_unique_id_tags import CompanyDomainSubscriptionsSubscriptionUniqueIdTags
from billsby_python_sdk.apis.paths.company_domain_subscriptions_subscription_unique_id_tags_split import CompanyDomainSubscriptionsSubscriptionUniqueIdTagsSplit
from billsby_python_sdk.apis.paths.company_domain_subscriptions_subscription_unique_id_logs import CompanyDomainSubscriptionsSubscriptionUniqueIdLogs
from billsby_python_sdk.apis.paths.company_domain_subscriptions_tags import CompanyDomainSubscriptionsTags
from billsby_python_sdk.apis.paths.company_domain_subscriptions_subscription_unique_id_plan import CompanyDomainSubscriptionsSubscriptionUniqueIdPlan
from billsby_python_sdk.apis.paths.company_domain_subscriptions_tags_tagname import CompanyDomainSubscriptionsTagsTagname
from billsby_python_sdk.apis.paths.company_domain_subscriptions_subscription_unique_id_renewaldate import CompanyDomainSubscriptionsSubscriptionUniqueIdRenewaldate
from billsby_python_sdk.apis.paths.invoices_invoice_number import InvoicesInvoiceNumber
from billsby_python_sdk.apis.paths.company_domain_companies_invoices import CompanyDomainCompaniesInvoices
from billsby_python_sdk.apis.paths.company_domain_customers_customer_unique_id_refunds import CompanyDomainCustomersCustomerUniqueIdRefunds
from billsby_python_sdk.apis.paths.company_domain_invoices_invoice_number_payment import CompanyDomainInvoicesInvoiceNumberPayment
from billsby_python_sdk.apis.paths.company_domain_invoices_invoice_number_paid_offline import CompanyDomainInvoicesInvoiceNumberPaidOffline
from billsby_python_sdk.apis.paths.company_domain_invoices_invoice_number_written_off import CompanyDomainInvoicesInvoiceNumberWrittenOff
from billsby_python_sdk.apis.paths.company_domain_companies_creditnotes import CompanyDomainCompaniesCreditnotes
from billsby_python_sdk.apis.paths.company_domain_customers_customer_unique_id_credit_notes import CompanyDomainCustomersCustomerUniqueIdCreditNotes
from billsby_python_sdk.apis.paths.company_domain__credit_notes__credit_note_number__payment import CompanyDomainCreditNotesCreditNoteNumberPayment
from billsby_python_sdk.apis.paths.company_domain_products_product_id import CompanyDomainProductsProductId
from billsby_python_sdk.apis.paths.company_domain_products import CompanyDomainProducts
from billsby_python_sdk.apis.paths.company_domain_products_product_id_plans import CompanyDomainProductsProductIdPlans
from billsby_python_sdk.apis.paths.company_domain_products_product_id_plans_plan_id_cycles import CompanyDomainProductsProductIdPlansPlanIdCycles
from billsby_python_sdk.apis.paths.company_domain_products_product_id_plans_plan_id import CompanyDomainProductsProductIdPlansPlanId
from billsby_python_sdk.apis.paths.company_domain_products_product_id_plans_orders import CompanyDomainProductsProductIdPlansOrders
from billsby_python_sdk.apis.paths.usage_company_domain_subscriptions_subscription_unique_id_counters_counter_id import UsageCompanyDomainSubscriptionsSubscriptionUniqueIdCountersCounterId
from billsby_python_sdk.apis.paths.operations_company_domain_subscriptions_subscription_unique_id_counters_counter_id import OperationsCompanyDomainSubscriptionsSubscriptionUniqueIdCountersCounterId
from billsby_python_sdk.apis.paths.company_domain_addons import CompanyDomainAddons
from billsby_python_sdk.apis.paths.company_domain_addons_addon_id import CompanyDomainAddonsAddonId
from billsby_python_sdk.apis.paths.company_domain_allowances import CompanyDomainAllowances
from billsby_python_sdk.apis.paths.company_domain_allowances_allowance_id import CompanyDomainAllowancesAllowanceId
from billsby_python_sdk.apis.paths.company_domain_subscriptions_subscription_unique_id_addons import CompanyDomainSubscriptionsSubscriptionUniqueIdAddons
from billsby_python_sdk.apis.paths.company_domain_subscriptions_subscription_unique_id_allowances import CompanyDomainSubscriptionsSubscriptionUniqueIdAllowances
from billsby_python_sdk.apis.paths.company_domain_customfields import CompanyDomainCustomfields
from billsby_python_sdk.apis.paths.company_domain_customfields_custom_field_id import CompanyDomainCustomfieldsCustomFieldId
from billsby_python_sdk.apis.paths.company_domain_customfield_responses import CompanyDomainCustomfieldResponses
from billsby_python_sdk.apis.paths.company_domain_customfield_responses_custom_field_response_id import CompanyDomainCustomfieldResponsesCustomFieldResponseId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.COMPANY_DOMAIN_CUSTOMERS: CompanyDomainCustomers,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID: CompanyDomainCustomersCustomerUniqueId,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_SUBSCRIPTIONS: CompanyDomainCustomersCustomerUniqueIdSubscriptions,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_SUBSCRIPTIONS_FEATURETAGS: CompanyDomainCustomersCustomerUniqueIdSubscriptionsFeaturetags,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_INVOICES_INVOICE_NUMBER_PAYMENTLOGS: CompanyDomainCustomersCustomerUniqueIdInvoicesInvoiceNumberPaymentlogs,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_PAYMENTDETAILSREQUEST: CompanyDomainCustomersCustomerUniqueIdPaymentdetailsrequest,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_PAYMENT_CARD: CompanyDomainCustomersCustomerUniqueIdPaymentCard,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_INVOICES: CompanyDomainCustomersCustomerUniqueIdInvoices,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_GDPRCLEANUP: CompanyDomainCustomersCustomerUniqueIdGdprcleanup,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS: CompanyDomainSubscriptions,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID: CompanyDomainSubscriptionsSubscriptionUniqueId,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_SHIPPING_ADDRESS: CompanyDomainSubscriptionsSubscriptionUniqueIdShippingAddress,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_TAGS: CompanyDomainSubscriptionsSubscriptionUniqueIdTags,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_TAGS_SPLIT: CompanyDomainSubscriptionsSubscriptionUniqueIdTagsSplit,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_LOGS: CompanyDomainSubscriptionsSubscriptionUniqueIdLogs,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_TAGS: CompanyDomainSubscriptionsTags,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_PLAN: CompanyDomainSubscriptionsSubscriptionUniqueIdPlan,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_TAGS_TAGNAME: CompanyDomainSubscriptionsTagsTagname,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_RENEWALDATE: CompanyDomainSubscriptionsSubscriptionUniqueIdRenewaldate,
        PathValues.INVOICES_INVOICE_NUMBER: InvoicesInvoiceNumber,
        PathValues.COMPANY_DOMAIN_COMPANIES_INVOICES: CompanyDomainCompaniesInvoices,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_REFUNDS: CompanyDomainCustomersCustomerUniqueIdRefunds,
        PathValues.COMPANY_DOMAIN_INVOICES_INVOICE_NUMBER_PAYMENT: CompanyDomainInvoicesInvoiceNumberPayment,
        PathValues.COMPANY_DOMAIN_INVOICES_INVOICE_NUMBER_PAID_OFFLINE: CompanyDomainInvoicesInvoiceNumberPaidOffline,
        PathValues.COMPANY_DOMAIN_INVOICES_INVOICE_NUMBER_WRITTEN_OFF: CompanyDomainInvoicesInvoiceNumberWrittenOff,
        PathValues.COMPANY_DOMAIN_COMPANIES_CREDITNOTES: CompanyDomainCompaniesCreditnotes,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_CREDIT_NOTES: CompanyDomainCustomersCustomerUniqueIdCreditNotes,
        PathValues.COMPANY_DOMAIN__CREDIT_NOTES__CREDIT_NOTE_NUMBER__PAYMENT: CompanyDomainCreditNotesCreditNoteNumberPayment,
        PathValues.COMPANY_DOMAIN_PRODUCTS_PRODUCT_ID: CompanyDomainProductsProductId,
        PathValues.COMPANY_DOMAIN_PRODUCTS: CompanyDomainProducts,
        PathValues.COMPANY_DOMAIN_PRODUCTS_PRODUCT_ID_PLANS: CompanyDomainProductsProductIdPlans,
        PathValues.COMPANY_DOMAIN_PRODUCTS_PRODUCT_ID_PLANS_PLAN_ID_CYCLES: CompanyDomainProductsProductIdPlansPlanIdCycles,
        PathValues.COMPANY_DOMAIN_PRODUCTS_PRODUCT_ID_PLANS_PLAN_ID: CompanyDomainProductsProductIdPlansPlanId,
        PathValues.COMPANY_DOMAIN_PRODUCTS_PRODUCT_ID_PLANS_ORDERS: CompanyDomainProductsProductIdPlansOrders,
        PathValues.USAGE_COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_COUNTERS_COUNTER_ID: UsageCompanyDomainSubscriptionsSubscriptionUniqueIdCountersCounterId,
        PathValues.OPERATIONS_COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_COUNTERS_COUNTER_ID: OperationsCompanyDomainSubscriptionsSubscriptionUniqueIdCountersCounterId,
        PathValues.COMPANY_DOMAIN_ADDONS: CompanyDomainAddons,
        PathValues.COMPANY_DOMAIN_ADDONS_ADDON_ID: CompanyDomainAddonsAddonId,
        PathValues.COMPANY_DOMAIN_ALLOWANCES: CompanyDomainAllowances,
        PathValues.COMPANY_DOMAIN_ALLOWANCES_ALLOWANCE_ID: CompanyDomainAllowancesAllowanceId,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_ADDONS: CompanyDomainSubscriptionsSubscriptionUniqueIdAddons,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_ALLOWANCES: CompanyDomainSubscriptionsSubscriptionUniqueIdAllowances,
        PathValues.COMPANY_DOMAIN_CUSTOMFIELDS: CompanyDomainCustomfields,
        PathValues.COMPANY_DOMAIN_CUSTOMFIELDS_CUSTOM_FIELD_ID: CompanyDomainCustomfieldsCustomFieldId,
        PathValues.COMPANY_DOMAIN_CUSTOMFIELD_RESPONSES: CompanyDomainCustomfieldResponses,
        PathValues.COMPANY_DOMAIN_CUSTOMFIELD_RESPONSES_CUSTOM_FIELD_RESPONSE_ID: CompanyDomainCustomfieldResponsesCustomFieldResponseId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.COMPANY_DOMAIN_CUSTOMERS: CompanyDomainCustomers,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID: CompanyDomainCustomersCustomerUniqueId,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_SUBSCRIPTIONS: CompanyDomainCustomersCustomerUniqueIdSubscriptions,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_SUBSCRIPTIONS_FEATURETAGS: CompanyDomainCustomersCustomerUniqueIdSubscriptionsFeaturetags,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_INVOICES_INVOICE_NUMBER_PAYMENTLOGS: CompanyDomainCustomersCustomerUniqueIdInvoicesInvoiceNumberPaymentlogs,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_PAYMENTDETAILSREQUEST: CompanyDomainCustomersCustomerUniqueIdPaymentdetailsrequest,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_PAYMENT_CARD: CompanyDomainCustomersCustomerUniqueIdPaymentCard,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_INVOICES: CompanyDomainCustomersCustomerUniqueIdInvoices,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_GDPRCLEANUP: CompanyDomainCustomersCustomerUniqueIdGdprcleanup,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS: CompanyDomainSubscriptions,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID: CompanyDomainSubscriptionsSubscriptionUniqueId,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_SHIPPING_ADDRESS: CompanyDomainSubscriptionsSubscriptionUniqueIdShippingAddress,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_TAGS: CompanyDomainSubscriptionsSubscriptionUniqueIdTags,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_TAGS_SPLIT: CompanyDomainSubscriptionsSubscriptionUniqueIdTagsSplit,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_LOGS: CompanyDomainSubscriptionsSubscriptionUniqueIdLogs,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_TAGS: CompanyDomainSubscriptionsTags,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_PLAN: CompanyDomainSubscriptionsSubscriptionUniqueIdPlan,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_TAGS_TAGNAME: CompanyDomainSubscriptionsTagsTagname,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_RENEWALDATE: CompanyDomainSubscriptionsSubscriptionUniqueIdRenewaldate,
        PathValues.INVOICES_INVOICE_NUMBER: InvoicesInvoiceNumber,
        PathValues.COMPANY_DOMAIN_COMPANIES_INVOICES: CompanyDomainCompaniesInvoices,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_REFUNDS: CompanyDomainCustomersCustomerUniqueIdRefunds,
        PathValues.COMPANY_DOMAIN_INVOICES_INVOICE_NUMBER_PAYMENT: CompanyDomainInvoicesInvoiceNumberPayment,
        PathValues.COMPANY_DOMAIN_INVOICES_INVOICE_NUMBER_PAID_OFFLINE: CompanyDomainInvoicesInvoiceNumberPaidOffline,
        PathValues.COMPANY_DOMAIN_INVOICES_INVOICE_NUMBER_WRITTEN_OFF: CompanyDomainInvoicesInvoiceNumberWrittenOff,
        PathValues.COMPANY_DOMAIN_COMPANIES_CREDITNOTES: CompanyDomainCompaniesCreditnotes,
        PathValues.COMPANY_DOMAIN_CUSTOMERS_CUSTOMER_UNIQUE_ID_CREDIT_NOTES: CompanyDomainCustomersCustomerUniqueIdCreditNotes,
        PathValues.COMPANY_DOMAIN__CREDIT_NOTES__CREDIT_NOTE_NUMBER__PAYMENT: CompanyDomainCreditNotesCreditNoteNumberPayment,
        PathValues.COMPANY_DOMAIN_PRODUCTS_PRODUCT_ID: CompanyDomainProductsProductId,
        PathValues.COMPANY_DOMAIN_PRODUCTS: CompanyDomainProducts,
        PathValues.COMPANY_DOMAIN_PRODUCTS_PRODUCT_ID_PLANS: CompanyDomainProductsProductIdPlans,
        PathValues.COMPANY_DOMAIN_PRODUCTS_PRODUCT_ID_PLANS_PLAN_ID_CYCLES: CompanyDomainProductsProductIdPlansPlanIdCycles,
        PathValues.COMPANY_DOMAIN_PRODUCTS_PRODUCT_ID_PLANS_PLAN_ID: CompanyDomainProductsProductIdPlansPlanId,
        PathValues.COMPANY_DOMAIN_PRODUCTS_PRODUCT_ID_PLANS_ORDERS: CompanyDomainProductsProductIdPlansOrders,
        PathValues.USAGE_COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_COUNTERS_COUNTER_ID: UsageCompanyDomainSubscriptionsSubscriptionUniqueIdCountersCounterId,
        PathValues.OPERATIONS_COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_COUNTERS_COUNTER_ID: OperationsCompanyDomainSubscriptionsSubscriptionUniqueIdCountersCounterId,
        PathValues.COMPANY_DOMAIN_ADDONS: CompanyDomainAddons,
        PathValues.COMPANY_DOMAIN_ADDONS_ADDON_ID: CompanyDomainAddonsAddonId,
        PathValues.COMPANY_DOMAIN_ALLOWANCES: CompanyDomainAllowances,
        PathValues.COMPANY_DOMAIN_ALLOWANCES_ALLOWANCE_ID: CompanyDomainAllowancesAllowanceId,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_ADDONS: CompanyDomainSubscriptionsSubscriptionUniqueIdAddons,
        PathValues.COMPANY_DOMAIN_SUBSCRIPTIONS_SUBSCRIPTION_UNIQUE_ID_ALLOWANCES: CompanyDomainSubscriptionsSubscriptionUniqueIdAllowances,
        PathValues.COMPANY_DOMAIN_CUSTOMFIELDS: CompanyDomainCustomfields,
        PathValues.COMPANY_DOMAIN_CUSTOMFIELDS_CUSTOM_FIELD_ID: CompanyDomainCustomfieldsCustomFieldId,
        PathValues.COMPANY_DOMAIN_CUSTOMFIELD_RESPONSES: CompanyDomainCustomfieldResponses,
        PathValues.COMPANY_DOMAIN_CUSTOMFIELD_RESPONSES_CUSTOM_FIELD_RESPONSE_ID: CompanyDomainCustomfieldResponsesCustomFieldResponseId,
    }
)
