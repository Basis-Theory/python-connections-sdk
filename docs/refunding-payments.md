# Refunding Payments

This guide explains how to refund payments using the Connections SDK.

## Table of Contents
- [Refunding a Payment](#refunding-a-payment)
- [Refund Response Handling](#refund-response-handling)

## Refunding a Payment

To refund a payment, you'll need the original transaction ID and the amount to refund:

```python
refund_request = RefundRequest(
    original_transaction_id='ORIGINAL_TRANSACTION_ID',
    reference='unique-refund-reference',
    amount=Amount(
        value=1000,
        currency='USD'
    ),
    reason=RefundReason.CUSTOMER_REQUEST  # Optional
)

response = sdk.adyen.refund_transaction(refund_request)
```

The `reason` field is optional and can be one of:
- `RefundReason.FRAUD` - Refund due to fraudulent activity
- `RefundReason.CUSTOMER_REQUEST` - Customer requested the refund
- `RefundReason.RETURN` - Refund for returned goods
- `RefundReason.DUPLICATE` - Refund for a duplicate charge
- `RefundReason.OTHER` - Other reason for refund

## Refund Response Handling

The refund response will contain:

- `id` - The unique identifier for the refund transaction
- `reference` - Your reference for the refund
- `amount` - The refunded amount and currency
- `status` - The status of the refund
- `refunded_transaction_id` - The ID of the original transaction that was refunded
- `created_at` - When the refund was processed
- `full_provider_response` - An object containing the detailed response from the payment provider. Access `response.full_provider_response.body` for the body and `response.full_provider_response.headers` for headers.

We strongly suggest you store the following fields in your database:
- Refund ID (`id`)
- Original Transaction ID (`refunded_transaction_id`)
- Your refund reference (`reference`)
- Refund amount and currency
- Refund status

Find the full response model [here](./api-reference.md#refundresponse).
