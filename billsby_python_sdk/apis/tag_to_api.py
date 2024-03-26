import typing_extensions

from billsby_python_sdk.apis.tags import TagValues
from billsby_python_sdk.apis.tags.customer_api import CustomerApi
from billsby_python_sdk.apis.tags.subscription_api import SubscriptionApi
from billsby_python_sdk.apis.tags.invoice_api import InvoiceApi
from billsby_python_sdk.apis.tags.product_api import ProductApi
from billsby_python_sdk.apis.tags.custom_field_api import CustomFieldApi
from billsby_python_sdk.apis.tags.addon_api import AddonApi
from billsby_python_sdk.apis.tags.allowance_api import AllowanceApi
from billsby_python_sdk.apis.tags.creditnote_api import CreditnoteApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CUSTOMER: CustomerApi,
        TagValues.SUBSCRIPTION: SubscriptionApi,
        TagValues.INVOICE: InvoiceApi,
        TagValues.PRODUCT: ProductApi,
        TagValues.CUSTOM_FIELD: CustomFieldApi,
        TagValues.ADDON: AddonApi,
        TagValues.ALLOWANCE: AllowanceApi,
        TagValues.CREDITNOTE: CreditnoteApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CUSTOMER: CustomerApi,
        TagValues.SUBSCRIPTION: SubscriptionApi,
        TagValues.INVOICE: InvoiceApi,
        TagValues.PRODUCT: ProductApi,
        TagValues.CUSTOM_FIELD: CustomFieldApi,
        TagValues.ADDON: AddonApi,
        TagValues.ALLOWANCE: AllowanceApi,
        TagValues.CREDITNOTE: CreditnoteApi,
    }
)
