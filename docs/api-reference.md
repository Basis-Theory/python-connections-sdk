# API Reference

## SDK Initialization

Initialize the SDK with configuration options.

```python
sdk = Connections({
    'is_test': bool,
    'bt_api_key': str,
    'provider_config': {
        [provider]: <ProviderConfig>
    }
})
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| is_test | bool | Yes | - | Whether to use the test environment for the provider |
| bt_api_key | str | Yes | - | Basis Theory API key |
| provider_config | Dict[str, ProviderConfig] | Yes | - | Configuration for the payment provider |

## Transaction Methods

Process a payment transaction through a provider, find all of the providers available in our [Providers](./providers/index.md) documentation. Each provider uses the same method signature, request model, and response model. Keep in mind - Each provider may have a unique combination of these fields to accomplish the same goal (e.g. Charging a card-on-file for a subscription vs a customer initiated transaction for two different providers).

```python
sdk.[provider].transaction(TransactionRequest(
    reference='merchant-reference-123',
    type=RecurringType.UNSCHEDULED,
    merchant_initiated=True,
    amount=Amount(
        value=1000,
        currency='USD'
    ),
    source=Source(
        type=SourceType.BASIS_THEORY_TOKEN,
        id='bt_123abc...',
        store_with_provider=True,
        holder_name='John Doe'
    ),
    customer=Customer(
        reference='customer-123',
        first_name='John', 
        last_name='Doe',
        email='john.doe@example.com',
        address=Address(
            address_line1='123 Main St',
            address_line2='Apt 4B',
            city='New York',
            state='NY',
            zip='10001',
            country='US'
        ),
        channel='web'
    ),
    three_ds=ThreeDS(
        eci='05',
        authentication_value='YOUR_3DS_AUTH_VALUE',
        threeds_version='2.2.0',
        ds_transaction_id='YOUR_DS_TRANSACTION_ID',
        authentication_status_code='Y'
    ),
    override_provider_properties={
        'additionalData': {
            'risdata.userStatus': 'PGWC-123-TEST'
        }
    }
))
```

### Request Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| reference | str | Yes | - | Unique transaction reference |
| type | RecurringType | Yes | - | Transaction type |
| amount | Amount | Yes | - | Transaction amount in minor currency units |
| source | Source | Yes | - | Payment source |
| customer | Customer | No | None | Customer information |
| three_ds | ThreeDS | No | None | 3DS authentication data |
| merchant_initiated | bool | No | False | Whether the transaction is merchant-initiated |
| previous_network_transaction_id | str | No | None | Previous network transaction ID |
| override_provider_properties | Dict[str, Any] | No | None | Appends and replaces any pre-mapped provider properties in the provider request |
| metadata | Dict[str, Any] | No | None | Metadata to be associated with the transaction |

### Response

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| id | str | None | Unique identifier for the transaction |
| reference | str | None | Reference identifier provided in the request |
| amount | Amount | None | Transaction amount in minor currency units |
| status | TransactionStatus | None | Current status of the transaction |
| source | TransactionSource | None | Source payment method details |
| fullProviderResponse | Dict[str, Any] | None | Complete response from the payment provider |
| createdt | datetime | None | Timestamp when transaction was created |
| network_transaction_id | str | None | Network transaction identifier |

## Refund Methods

Process a refund through a provider. Each provider uses the same method signature, request model, and response model.

```python
sdk.[provider].refund_transaction(RefundRequest(
    original_transaction_id='ORIGINAL_TRANSACTION_ID',
    reference='unique-refund-reference',
    amount=Amount(
        value=1000,
        currency='USD'
    ),
    reason=RefundReason.CUSTOMER_REQUEST
))
```

### Request Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| original_transaction_id | str | Yes | - | ID of the original transaction to refund |
| reference | str | Yes | - | Unique refund reference |
| amount | Amount | Yes | - | Amount to refund |
| reason | RefundReason | No | None | Reason for the refund |

### Response

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| id | str | None | Unique identifier for the refund |
| reference | str | None | Reference identifier provided in the request |
| amount | Amount | None | Amount details of the refund |
| status | RefundStatus | None | Current status of the refund |
| refunded_transaction_id | str | None | ID of the original transaction that was refunded |
| full_provider_response | Dict[str, Any] | None | Complete response from the payment provider |
| created_at | datetime | None | Timestamp when refund was created |


## Request Models

### RecurringType

| Value | Description |
|-------|-------------|
| ONE_TIME | A one-time payment that will not be stored for future use |
| CARD_ON_FILE | A payment where the card details will be stored for future use |
| SUBSCRIPTION | A recurring payment on a fixed schedule (e.g. monthly subscription) |
| UNSCHEDULED | A recurring payment without a fixed schedule (e.g. top-ups) |

### SourceType

| Value | Description |
|-------|-------------|
| BASIS_THEORY_TOKEN | A Basis Theory token containing card details |
| BASIS_THEORY_TOKEN_INTENT | A Basis Theory token intent for collecting card details |
| PROCESSOR_TOKEN | A token from a payment processor containing stored card details |

### Amount

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| value | int | - | Amount in cents |
| currency | str | "USD" | Three-letter currency code |

### Source

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| type | SourceType | - | Type of payment source (BASIS_THEORY_TOKEN, BASIS_THEORY_TOKEN_INTENT, or PROCESSOR_TOKEN) |
| id | str | - | Identifier for the payment source |
| store_with_provider | bool | False | Whether to store the payment source with the provider for future use |
| holder_name | str | None | Name of the card holder |

### Customer

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| reference | str | None | Customer reference identifier |
| first_name | str | None | Customer's first name |
| last_name | str | None | Customer's last name |
| email | str | None | Customer's email address |
| address | Address | None | Customer's address details |
| channel | Literal['ios', 'android', 'web'] | 'web' | Customer's channel a.k.a device type. |

### Address

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| address_line1 | str | None | First line of the address |
| address_line2 | str | None | Second line of the address |
| city | str | None | City name |
| state | str | None | State/province code |
| zip | str | None | Postal/ZIP code |
| country | str | None | Two-letter country code |

### ThreeDS

| Property                       | Type   | Default | Description                                                              |
|--------------------------------|--------|---------|--------------------------------------------------------------------------|
| eci                            | str    | None    | Electronic Commerce Indicator value from 3DS authentication.             |
| authentication_value           | str    | None    | Authentication value/CAVV from 3DS authentication.                       |
| threeds_version                | str    | None    | Version of 3DS protocol used (e.g., "2.2.0").                            |
| ds_transaction_id              | str    | None    | Transaction ID from the 3DS Directory Server (DS).                       |
| directory_status_code          | str    | None    | EMV character code for the directory authentication status.                |
| authentication_status_code     | str    | None    | EMV character code for the authentication status.                        |
| challenge_cancel_reason_code   | str    | None    | EMV numeric code for the challenge cancel reason.                        |
| challenge_preference_code      | str    | None    | EMV numeric code for the selected challenge preference.                    |
| authentication_status_reason   | str    | None    | Additional information about the authentication status if necessary.       |


## Response Models

### TransactionSource

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| type | str | None | Type of the payment source |
| id | str | None | Identifier for the payment source |
| provisioned | ProvisionedSource | None | Details of the provisioned source |

### ProvisionedSource

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| id | str | None | Identifier for the provisioned source |

### TransactionStatus

| Value | Description |
|-------|-------------|
| AUTHORIZED | Transaction was successfully authorized |
| PENDING | Transaction is pending completion |
| CARD_VERIFIED | Card was successfully verified |
| DECLINED | Transaction was declined |
| RETRY_SCHEDULED | Transaction failed but retry is scheduled |
| CANCELLED | Transaction was cancelled |
| CHALLENGE_SHOPPER | Additional shopper authentication required |
| RECEIVED | Transaction request was received |
| PARTIALLY_AUTHORIZED | Transaction was partially authorized |

### RefundReason

| Value | Description |
|-------|-------------|
| FRAUD | Refund due to fraudulent activity |
| CUSTOMER_REQUEST | Customer requested the refund |
| RETURN | Refund for returned goods |
| DUPLICATE | Refund for a duplicate charge |
| OTHER | Other reason for refund |

## Error Handling

See [Error Handling](./error-handling.md) for details on how to handle errors.