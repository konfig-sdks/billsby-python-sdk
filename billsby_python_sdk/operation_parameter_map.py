operation_parameter_map = {
    '/{companyDomain}/subscriptions/{subscriptionUniqueId}/addons-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
        ]
    },
    '/{companyDomain}/addons/{addonId}-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'addonId'
            },
        ]
    },
    '/{companyDomain}/addons-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
        ]
    },
    '/{companyDomain}/allowances/{allowanceId}-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'allowanceId'
            },
        ]
    },
    '/{companyDomain}/allowances-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
        ]
    },
    '/{companyDomain}/subscriptions/{subscriptionUniqueId}/allowances-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
        ]
    },
    '/{companyDomain}/companies/creditnotes-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'query'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'orderByDescending'
            },
            {
                'name': 'isPending'
            },
            {
                'name': 'isPaid'
            },
            {
                'name': 'isFailed'
            },
        ]
    },
    '/{companyDomain} /creditNotes /{creditNoteNumber} /Payment-PUT': {
        'parameters': [
            {
                'name': 'creditNoteNumber'
            },
            {
                'name': 'companyDomain'
            },
        ]
    },
    '/{companyDomain}/customfields-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'type'
            },
            {
                'name': 'label'
            },
            {
                'name': 'compulsory'
            },
            {
                'name': 'companyDomain'
            },
            {
                'name': 'options'
            },
        ]
    },
    '/{companyDomain}/customfieldResponses-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'productId'
            },
            {
                'name': 'customerUniqueId'
            },
        ]
    },
    '/{companyDomain}/customfields-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
        ]
    },
    '/{companyDomain}/customfields/{customFieldId}-PUT': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customFieldId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'label'
            },
            {
                'name': 'options'
            },
            {
                'name': 'compulsory'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}/subscriptions-POST': {
        'parameters': [
            {
                'name': 'cycleId'
            },
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
            {
                'name': 'units'
            },
            {
                'name': 'address'
            },
            {
                'name': 'shippingAddress'
            },
            {
                'name': 'additionalEmail'
            },
            {
                'name': 'phoneNumberDialCountry'
            },
            {
                'name': 'phoneNumberDialCode'
            },
            {
                'name': 'phoneNumber'
            },
            {
                'name': 'marketingConsent'
            },
            {
                'name': 'taxRegNumber'
            },
            {
                'name': 'ipAddress'
            },
            {
                'name': 'customFieldResponse'
            },
            {
                'name': 'addOns'
            },
            {
                'name': 'allowances'
            },
            {
                'name': 'couponCodes'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}/gdprcleanup-PUT': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
        ]
    },
    '/{companyDomain}/subscriptions-POST': {
        'parameters': [
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'email'
            },
            {
                'name': 'cycleId'
            },
            {
                'name': 'Units'
            },
            {
                'name': 'address'
            },
            {
                'name': 'cardDetails'
            },
            {
                'name': 'companyDomain'
            },
            {
                'name': 'shippingAddress'
            },
            {
                'name': 'additionalEmail'
            },
            {
                'name': 'phoneNumberDialCountry'
            },
            {
                'name': 'phoneNumberDialCode'
            },
            {
                'name': 'phoneNumber'
            },
            {
                'name': 'marketingConsent'
            },
            {
                'name': 'customFieldResponse'
            },
            {
                'name': 'addOns'
            },
            {
                'name': 'allowances'
            },
            {
                'name': 'couponCodes'
            },
        ]
    },
    '/{companyDomain}/customers-POST': {
        'parameters': [
            {
                'name': 'addressLine1'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'country'
            },
            {
                'name': 'postCode'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'email'
            },
            {
                'name': 'companyDomain'
            },
            {
                'name': 'addressLine2'
            },
            {
                'name': 'cardDetails'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}-DELETE': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}/creditNotes-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}/subscriptions/featuretags-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}/subscriptions-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
        ]
    },
    '/{companyDomain}/customers-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/{companyDomain}/customfieldResponses/{customFieldResponseId}-PUT': {
        'parameters': [
            {
                'name': 'value'
            },
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customFieldResponseId'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}-PUT': {
        'parameters': [
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'email'
            },
            {
                'name': 'billingAddress'
            },
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
            {
                'name': 'phoneNumberDialCountry'
            },
            {
                'name': 'phoneNumberDialCode'
            },
            {
                'name': 'phoneNumber'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}/paymentCard-PUT': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
            {
                'name': 'fullName'
            },
            {
                'name': 'paymentCardtoken'
            },
            {
                'name': 'expiryMonth'
            },
            {
                'name': 'expiryYear'
            },
            {
                'name': 'cardType'
            },
            {
                'name': 'last4Digits'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}/paymentdetailsrequest-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}/invoices-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'currencyCode'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}/refunds-POST': {
        'parameters': [
            {
                'name': 'invoiceNumber'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
        ]
    },
    '/invoices/{invoiceNumber}-GET': {
        'parameters': [
            {
                'name': 'invoiceNumber'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}/invoices-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
        ]
    },
    '/{companyDomain}/customers/{customerUniqueId}/invoices/{invoiceNumber}/paymentlogs-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'customerUniqueId'
            },
            {
                'name': 'invoiceNumber'
            },
        ]
    },
    '/{companyDomain}/companies/invoices-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'query'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'orderByDescending'
            },
            {
                'name': 'isPending'
            },
            {
                'name': 'isPaid'
            },
            {
                'name': 'isUnpaid'
            },
            {
                'name': 'isPaidOffline'
            },
            {
                'name': 'isWrittenOff'
            },
        ]
    },
    '/{companyDomain}/invoices/{invoiceNumber}/PaidOffline-PUT': {
        'parameters': [
            {
                'name': 'invoiceNumber'
            },
            {
                'name': 'companyDomain'
            },
        ]
    },
    '/{companyDomain}/invoices/{invoiceNumber}/WrittenOff-PUT': {
        'parameters': [
            {
                'name': 'invoiceNumber'
            },
            {
                'name': 'companyDomain'
            },
        ]
    },
    '/{companyDomain}/invoices/{invoiceNumber}/Payment-PUT': {
        'parameters': [
            {
                'name': 'invoiceNumber'
            },
            {
                'name': 'companyDomain'
            },
        ]
    },
    '/{companyDomain}/products/{productId}/plans/{planId}/cycles-POST': {
        'parameters': [
            {
                'name': 'cyclesInputModel'
            },
            {
                'name': 'addonPlanInputModels'
            },
            {
                'name': 'companyDomain'
            },
            {
                'name': 'productId'
            },
            {
                'name': 'planId'
            },
            {
                'name': 'allowancePlanInputModel'
            },
        ]
    },
    '/{companyDomain}/products-POST': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'visibility'
            },
            {
                'name': 'billingCurrency'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'isShippingAddressRequired'
            },
            {
                'name': 'isShippingAddressValidationRequired'
            },
            {
                'name': 'isBillingAddressValidationRequired'
            },
            {
                'name': 'isAdditionalEmailRequired'
            },
            {
                'name': 'isPhoneNumberRequired'
            },
            {
                'name': 'is MarketingConsentRequired'
            },
            {
                'name': 'alertEmail'
            },
            {
                'name': 'orderedCustomFields'
            },
            {
                'name': 'typeOfProduct'
            },
            {
                'name': 'productCountryLimitation'
            },
            {
                'name': 'isAnyCountryAllowed'
            },
        ]
    },
    '/{companyDomain}/products/{productId}/plans-POST': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'productId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'pricingModel'
            },
            {
                'name': 'featureTags'
            },
            {
                'name': 'visibility'
            },
            {
                'name': 'redirectUrl'
            },
            {
                'name': 'alertEmail'
            },
        ]
    },
    '/{companyDomain}/products/{productId}-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'productId'
            },
        ]
    },
    '/{companyDomain}/products/{productId}/plans-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'productId'
            },
        ]
    },
    '/{companyDomain}/products-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'search'
            },
            {
                'name': 'visibilityType'
            },
        ]
    },
    '/{companyDomain}/products/{productId}/plans/{planId}-PUT': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'productId'
            },
            {
                'name': 'planId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'featureTags'
            },
            {
                'name': 'visibility'
            },
            {
                'name': 'cycles'
            },
            {
                'name': 'redirectUrl'
            },
            {
                'name': 'alertEmail'
            },
        ]
    },
    '/{companyDomain}/products/{productId}/plans/orders-PUT': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'productId'
            },
            {
                'name': 'orderedPlanIds'
            },
        ]
    },
    '/{companyDomain}/products/{productId}-PUT': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'productID'
            },
            {
                'name': 'name'
            },
            {
                'name': 'visibility'
            },
            {
                'name': 'billingCurrency'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'decription'
            },
            {
                'name': 'isShippingAddressRequired'
            },
            {
                'name': 'isShippingAddressValidationRequired'
            },
            {
                'name': 'isBillingAddressValidationRequired'
            },
            {
                'name': 'isAdditionalEmailRequired'
            },
            {
                'name': 'isPhoneNumberRequired'
            },
            {
                'name': 'is MarketingConsentRequired'
            },
            {
                'name': 'alertEmail'
            },
            {
                'name': 'orderedCustomFields'
            },
            {
                'name': 'typeOfProduct'
            },
            {
                'name': 'productCountryLimitations'
            },
        ]
    },
    '/{companyDomain}/subscriptions/tags-POST': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueIds'
            },
            {
                'name': 'tagNames'
            },
        ]
    },
    '/{companyDomain}/subscriptions/{subscriptionUniqueId}-DELETE': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
            {
                'name': 'customerUniqueId'
            },
        ]
    },
    '/{companyDomain}/subscriptions/{subscriptionUniqueId}/plan-PUT': {
        'parameters': [
            {
                'name': 'planId'
            },
            {
                'name': 'cycleId'
            },
            {
                'name': 'customerUniqueId'
            },
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
            {
                'name': 'planChangeType'
            },
            {
                'name': 'units'
            },
            {
                'name': 'addOns'
            },
            {
                'name': 'allowances'
            },
            {
                'name': 'issueRefund'
            },
        ]
    },
    '/{companyDomain}/subscriptions/{subscriptionUniqueId}/tags/split-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
        ]
    },
    '/usage/{companyDomain}/subscriptions/{subscriptionUniqueId}/counters/{counterId}-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
            {
                'name': 'counterId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
        ]
    },
    '/{companyDomain}/subscriptions/{subscriptionUniqueId}-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
        ]
    },
    '/{companyDomain}/subscriptions/{subscriptionUniqueId}/logs-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/{companyDomain}/subscriptions/{subscriptionUniqueId}/shippingAddress-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
        ]
    },
    '/{companyDomain}/subscriptions-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'page'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'orderByDescending'
            },
            {
                'name': 'isActive'
            },
            {
                'name': 'isInFreeTrial'
            },
            {
                'name': 'productName'
            },
            {
                'name': 'planName'
            },
        ]
    },
    '/{companyDomain}/subscriptions/{subscriptionUniqueId}/tags-GET': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
        ]
    },
    '/{companyDomain}/subscriptions/tags/{tagname}-DELETE': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'tagname'
            },
            {
                'name': 'subsId'
            },
        ]
    },
    '/operations/{companyDomain}/subscriptions/{subscriptionUniqueId}/counters/{counterId}-POST': {
        'parameters': [
            {
                'name': 'operationType'
            },
            {
                'name': 'value'
            },
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
            {
                'name': 'counterId'
            },
        ]
    },
    '/{companyDomain}/subscriptions/{subscriptionUniqueId}/renewaldate-PUT': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
            {
                'name': 'pauseSubscription'
            },
            {
                'name': 'newRenewalDate'
            },
        ]
    },
    '/{companyDomain}/subscriptions/{subscriptionUniqueId}/shippingAddress-PUT': {
        'parameters': [
            {
                'name': 'companyDomain'
            },
            {
                'name': 'subscriptionUniqueId'
            },
            {
                'name': 'addressLine1'
            },
            {
                'name': 'addressLine2'
            },
            {
                'name': 'state'
            },
            {
                'name': 'city'
            },
            {
                'name': 'country'
            },
            {
                'name': 'postCode'
            },
        ]
    },
};