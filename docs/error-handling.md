# Error Handling

The Connections SDK provides comprehensive error handling with standardized error categories and codes across different payment providers.

## Error Response Structure

When a transaction fails, the SDK raises an exception with the following structure:

```python
    ErrorResponse(
        error_codes=[{
            'category': 'payment_method_error',
            'code': 'expired_card'
        }],
        provider_errors=['Expired Card'],
        full_provider_response={
            'resultCode': 'Refused',
            'refusalReason': 'Expired Card',
            'refusalReasonCode': '6'
        }
    )
```

## Exceptions

The primary exceptions you might encounter are:

| Exception | Has ErrorResponse | Description |
|-----------|------------------|-------------|
| `ValidationError` | Yes (Conditional) | Raised for various issues: <br> 1. **Request validation failures** (e.g., missing required fields before sending to a provider). In this case, `error_response` may contain locally generated error details. <br> 2. **Payment transaction failures** that are not handled by returning a `TransactionResponse` with a specific decline `response_code` (e.g., API authentication errors with the provider, unexpected provider errors). In this case, `error_response` will contain standardized error details from the provider. |
| `ConfigurationError` | No | Raised when SDK configuration is invalid, such as missing API keys or invalid settings. |
| `BasisTheoryError` | Yes | Raised when there is an error interacting with Basis Theory services. Contains error response and HTTP status. |

### ErrorResponse Object

When an exception that includes an `ErrorResponse` (like `ValidationError` for provider errors or `BasisTheoryError`) is raised, the `error_response` attribute of the exception object will contain:

* `error_codes`: A list of standardized `ErrorCode` objects.

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| error_codes | list[ErrorCode] | None | List of error codes indicating what went wrong |
| provider_errors | list[str] | None | List of raw error messages from the provider |
| full_provider_response | Dict[str, Any] | None | Complete response from the provider for debugging |

### ErrorCode

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| category | str | None | The error category (e.g. "authentication_error", "payment_method_error") |
| code | str | None | The specific error code within the category |

## Error Categories

The SDK standardizes errors into the following categories:

| Enum | Code | Description |
|------|-------|-------------|
| AUTHENTICATION_ERROR | "authentication_error" | Issues with 3DS authentication |
| PAYMENT_METHOD_ERROR | "payment_method_error" | Issues with the payment method (card expired, invalid, etc.) |
| PROCESSING_ERROR | "processing_error" | General processing errors |
| VALIDATION_ERROR | "validation_error" | Invalid request data |
| BASIS_THEORY_ERROR | "basis_theory_error" | Issues with Basis Theory services |
| FRAUD_DECLINE | "Fraud Decline" | Transactions declined due to fraud |
| OTHER | "Other" | Other unspecified errors (e.g. invalid API key) |

## Error Types

The SDK includes the following error types:

| Enum | Code | Category | Description |
|-------|------|-----------|-------------|
| REFUSED | "refused" | PROCESSING_ERROR | The transaction was refused. |
| REFERRAL | "referral" | PROCESSING_ERROR | The issuing bank cannot automatically approve the transaction. |
| ACQUIRER_ERROR | "acquirer_error" | OTHER | The transaction did not go through due to an error that occurred on the acquirer's end. |
| BLOCKED_CARD | "blocked_card" | PAYMENT_METHOD_ERROR | The card used for the transaction is blocked, therefore unusable. |
| EXPIRED_CARD | "expired_card" | PAYMENT_METHOD_ERROR | The card used for the transaction has expired. Therefore it is unusable. |
| INVALID_AMOUNT | "invalid_amount" | OTHER | An amount mismatch occurred during the transaction process. |
| INVALID_CARD | "invalid_card" | PAYMENT_METHOD_ERROR | The specified card number is incorrect or invalid. |
| INVALID_SOURCE_TOKEN | "invalid_source_token" | PAYMENT_METHOD_ERROR | The provided source token (processor token) is invalid or expired. |
| OTHER | "other" | OTHER | This response maps all those response codes that cannot be reliably mapped. |
| NOT_SUPPORTED | "not_supported" | PROCESSING_ERROR | The shopper's bank does not support or does not allow this type of transaction. |
| AUTHENTICATION_FAILURE | "authentication_failure" | PAYMENT_METHOD_ERROR | The 3D Secure authentication failed due to an issue at the card network or issuer. |
| INSUFFICENT_FUNDS | "insufficient_funds" | PAYMENT_METHOD_ERROR | The card does not have enough money to cover the payable amount. |
| FRAUD | "fraud" | FRAUD_DECLINE | Possible fraud. |
| PAYMENT_CANCELLED | "payment_cancelled" | OTHER | The transaction was cancelled. |
| PAYMENT_CANCELLED_BY_CONSUMER | "payment_cancelled_by_consumer" | PROCESSING_ERROR | The shopper cancelled the transaction before completing it. |
| INVALID_PIN | "invalid_pin" | PAYMENT_METHOD_ERROR | The specified PIN is incorrect or invalid. |
| PIN_TRIES_EXCEEDED | "pin_tries_exceeded" | PAYMENT_METHOD_ERROR | The shopper specified an incorrect PIN more that three times in a row. |
| CVC_INVALID | "cvc_invalid" | PAYMENT_METHOD_ERROR | The specified CVC (card security code) is invalid. |
| RESTRICTED_CARD | "restricted_card" | PROCESSING_ERROR | The card is restricted from making this type of transaction. |
| STOP_PAYMENT | "stop_payment" | PROCESSING_ERROR | Indicates that the shopper requested to stop a subscription. |
| AVS_DECLINE | "avs_decline" | PROCESSING_ERROR | The address data the shopper entered is incorrect. |
| PIN_REQUIRED | "pin_required" | PROCESSING_ERROR | A PIN is required to complete the transaction. |
| BANK_ERROR | "bank_error" | PROCESSING_ERROR | An error occurred with the shopper's bank during processing. |
| CONTACTLESS_FALLBACK | "contactless_fallback" | PROCESSING_ERROR | The shopper abandoned the transaction after they attempted a contactless payment. |
| AUTHENTICATION_REQUIRED | "authentication_required" | PROCESSING_ERROR | The issuer requires authentication for the transaction. Retry with 3D Secure. |
| PROCESSOR_BLOCKED | "processor_blocked" | PROCESSING_ERROR | Transaction blocked by Adyen's excessive retry prevention service. |
| INVALID_API_KEY | "invalid_api_key" | AUTHENTICATION_ERROR | The API key provided is invalid. |
| UNAUTHORIZED | "unauthorized" | AUTHENTICATION_ERROR | The request is not authorized to access the resource. |
| CONFIGURATION_ERROR | "configuration_error" | OTHER | An error occurred in the configuration settings. |
| BT_UNAUTHENTICATED | "unauthenticated" | BASIS_THEORY_ERROR | Authentication failed with Basis Theory. |
| BT_UNAUTHORIZED | "unauthorized" | BASIS_THEORY_ERROR | Request not authorized with Basis Theory. |
| BT_REQUEST_ERROR | "request_error" | BASIS_THEORY_ERROR | Error occurred during Basis Theory API request. |
| BT_UNEXPECTED | "unexpected" | BASIS_THEORY_ERROR | Unexpected error occurred with Basis Theory. |

## Example Error Scenarios

### Expired Card

```python
try:
    response = sdk.adyen.create_transaction(transaction_request)
except Exception as e:
    # Exception will have e.error_response
    # ErrorResponse(
    #     error_codes=[{
    #         'category': 'payment_method_error',
    #         'code': 'expired_card'
    #     }],
    #     provider_errors=['Expired Card'],
    #     full_provider_response={
    #         'resultCode': 'Refused',
    #         'refusalReason': 'Expired Card',
    #         'refusalReasonCode': '6'
    #     }
    # )
```

## Best Practices

1. Use the provider errors array for detailed error messages
2. Log the full provider response for debugging purposes
3. Handle common error categories with appropriate user messaging

## Handling Declines and Errors in `TransactionResponse`

For many common payment transaction outcomes, especially declines (e.g., "Insufficient Funds", "Expired Card", "Card Declined"), the SDK will **not** raise an exception. Instead, it will return a `TransactionResponse` object.

You should inspect the `status` and `response_code` fields of the `TransactionResponse` to understand the outcome of the transaction.

`TransactionResponse` fields relevant to error/decline handling:
* `status: TransactionStatus`: Contains a `code` (e.g., `TransactionStatusCode.DECLINED`, `TransactionStatusCode.FAILED`) and the original `provider_code`.
* `response_code: ResponseCode`: A standardized code indicating the reason for the transaction outcome. It has two sub-fields:
    * `category: str`: A broad category for the error (e.g., `ErrorCategory.PAYMENT_METHOD_ERROR`, `ErrorCategory.PROCESSING_ERROR`).
    * `code: str`: A specific error code (e.g., `ErrorType.INSUFFICENT_FUNDS.code`, `ErrorType.EXPIRED_CARD.code`).
* `full_provider_response: Dict[str, Any]`: The complete response from the payment provider.

Example of checking `TransactionResponse`:

```python
from connections_sdk.models import TransactionStatusCode, ErrorCategory, ErrorType

# ... your code to make a transaction ...
try:
    transaction_response = sdk.provider.create_transaction(transaction_request)

    if transaction_response.status.code == TransactionStatusCode.DECLINED:
        print(f"Transaction Declined.")
        print(f"  Category: {transaction_response.response_code.category}")
        print(f"  Code: {transaction_response.response_code.code}")
        print(f"  Provider Status: {transaction_response.status.provider_code}")
        # You can also inspect transaction_response.full_provider_response for more details

        if transaction_response.response_code.code == ErrorType.INSUFFICENT_FUNDS.code:
            # Handle insufficient funds scenario
            pass
        elif transaction_response.response_code.code == ErrorType.EXPIRED_CARD.code:
            # Handle expired card scenario
            pass
        # ... other specific error checks

    elif transaction_response.status.code == TransactionStatusCode.FAILED:
        print(f"Transaction Failed.")
        print(f"  Category: {transaction_response.response_code.category}")
        print(f"  Code: {transaction_response.response_code.code}")
        # Handle other failure scenarios

    elif transaction_response.status.code == TransactionStatusCode.SUCCESS:
        print("Transaction Successful!")
        # Process successful transaction

except ValidationError as e:
    # Handle exceptions for issues not covered by normal TransactionResponse declines
    print(f"An exception occurred: {e}")
    if e.error_response:
        print(f"  Error Codes: {e.error_response.error_codes}")

except Exception as e:
    # Catch any other unexpected exceptions
    print(f"An unexpected error occurred: {e}")

```

This approach allows for more granular handling of different transaction outcomes directly from the response object, reserving exceptions for more systemic or unexpected issues.