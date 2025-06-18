import os
import uuid
import pytest
import requests
from datetime import datetime
from unittest.mock import MagicMock, patch
from connections_sdk import Connections
from connections_sdk.models import (
    TransactionStatusCode,
    RecurringType,
    SourceType,
    ErrorCategory,
    ErrorType,
    TransactionRequest,
    Amount,
    Source,
    Customer
)
from connections_sdk.exceptions import TransactionError, TransactionError

def test_errors():  
    # Define test cases mapping
    test_cases = [
        {"error_type": "processing_error", "error_codes": ["card_authorization_failed"], "expected_error": ErrorType.REFUSED},
        {"error_type": "processing_error", "error_codes": ["card_expiry_month_invalid"], "expected_error": ErrorType.INVALID_CARD},
        {"error_type": "processing_error", "error_codes": ["card_expiry_month_required"], "expected_error": ErrorType.INVALID_CARD},
        {"error_type": "processing_error", "error_codes": ["card_expiry_year_invalid"], "expected_error": ErrorType.INVALID_CARD},
        {"error_type": "processing_error", "error_codes": ["card_expiry_year_required"], "expected_error": ErrorType.INVALID_CARD},
        {"error_type": "processing_error", "error_codes": ["expiry_date_format_invalid"], "expected_error": ErrorType.INVALID_CARD},
        {"error_type": "processing_error", "error_codes": ["card_not_found"], "expected_error": ErrorType.INVALID_CARD},
        {"error_type": "processing_error", "error_codes": ["card_number_invalid"], "expected_error": ErrorType.INVALID_CARD},
        {"error_type": "processing_error", "error_codes": ["card_number_required"], "expected_error": ErrorType.INVALID_CARD},
        {"error_type": "processing_error", "error_codes": ["issuer_network_unavailable"], "expected_error": ErrorType.OTHER},
        {"error_type": "processing_error", "error_codes": ["card_not_eligible_domestic_money_transfer"], "expected_error": ErrorType.NOT_SUPPORTED},
        {"error_type": "processing_error", "error_codes": ["card_not_eligible_cross_border_money_transfer"], "expected_error": ErrorType.NOT_SUPPORTED},
        {"error_type": "processing_error", "error_codes": ["card_not_eligible_domestic_non_money_transfer"], "expected_error": ErrorType.NOT_SUPPORTED},
        {"error_type": "processing_error", "error_codes": ["card_not_eligible_cross_border_non_money_transfer"], "expected_error": ErrorType.NOT_SUPPORTED},
        {"error_type": "processing_error", "error_codes": ["card_not_eligible_domestic_online_gambling"], "expected_error": ErrorType.NOT_SUPPORTED},
        {"error_type": "processing_error", "error_codes": ["card_not_eligible_cross_border_online_gambling"], "expected_error": ErrorType.NOT_SUPPORTED},
        {"error_type": "processing_error", "error_codes": ["3ds_not_enabled_for_card"], "expected_error": ErrorType.AUTHENTICATION_FAILURE},
        {"error_type": "processing_error", "error_codes": ["3ds_not_supported"], "expected_error": ErrorType.AUTHENTICATION_FAILURE},
        {"error_type": "processing_error", "error_codes": ["amount_exceeds_balance"], "expected_error": ErrorType.INSUFFICENT_FUNDS},
        {"error_type": "processing_error", "error_codes": ["amount_limit_exceeded"], "expected_error": ErrorType.INSUFFICENT_FUNDS},
        {"error_type": "processing_error", "error_codes": ["payment_expired"], "expected_error": ErrorType.PAYMENT_CANCELLED},
        {"error_type": "processing_error", "error_codes": ["cvv_invalid"], "expected_error": ErrorType.CVC_INVALID},
        {"error_type": "processing_error", "error_codes": ["processing_error"], "expected_error": ErrorType.REFUSED},
        {"error_type": "processing_error", "error_codes": ["velocity_amount_limit_exceeded"], "expected_error": ErrorType.INSUFFICENT_FUNDS},
        {"error_type": "processing_error", "error_codes": ["velocity_count_limit_exceeded"], "expected_error": ErrorType.INSUFFICENT_FUNDS},
        {"error_type": "processing_error", "error_codes": ["address_invalid"], "expected_error": ErrorType.AVS_DECLINE},
        {"error_type": "processing_error", "error_codes": ["city_invalid"], "expected_error": ErrorType.AVS_DECLINE},
        {"error_type": "processing_error", "error_codes": ["country_address_invalid"], "expected_error": ErrorType.AVS_DECLINE},
        {"error_type": "processing_error", "error_codes": ["country_invalid"], "expected_error": ErrorType.AVS_DECLINE},
        {"error_type": "processing_error", "error_codes": ["country_phone_code_invalid"], "expected_error": ErrorType.AVS_DECLINE},
        {"error_type": "processing_error", "error_codes": ["country_phone_code_length_invalid"], "expected_error": ErrorType.AVS_DECLINE},
        {"error_type": "processing_error", "error_codes": ["phone_number_invalid"], "expected_error": ErrorType.AVS_DECLINE},
        {"error_type": "processing_error", "error_codes": ["phone_number_length_invalid"], "expected_error": ErrorType.AVS_DECLINE},
        {"error_type": "processing_error", "error_codes": ["zip_invalid"], "expected_error": ErrorType.AVS_DECLINE},
        {"error_type": "processing_error", "error_codes": ["action_failure_limit_exceeded"], "expected_error": ErrorType.PROCESSOR_BLOCKED},
        {"error_type": "processing_error", "error_codes": ["token_expired"], "expected_error": ErrorType.OTHER},
        {"error_type": "processing_error", "error_codes": ["token_in_use"], "expected_error": ErrorType.OTHER},
        {"error_type": "processing_error", "error_codes": ["token_invalid"], "expected_error": ErrorType.OTHER},
        {"error_type": "processing_error", "error_codes": ["token_used"], "expected_error": ErrorType.OTHER},
        {"error_type": "processing_error", "error_codes": ["capture_value_greater_than_authorized"], "expected_error": ErrorType.OTHER},
        {"error_type": "processing_error", "error_codes": ["capture_value_greater_than_remaining_authorized"], "expected_error": ErrorType.OTHER},
        {"error_type": "processing_error", "error_codes": ["card_holder_invalid"], "expected_error": ErrorType.OTHER},
        {"error_type": "processing_error", "error_codes": ["previous_payment_id_invalid"], "expected_error": ErrorType.OTHER}
    ]

    # Initialize the SDK
    sdk = Connections({
        'is_test': True,
        'bt_api_key': 'test_bt_api_key',
        'provider_config': {
            'checkout': {
                'private_key': 'test_private_key',
                'processing_channel': 'test_channel',
            }
        }
    })

    for test_case in test_cases:
        # Create mock response data
        mock_response_data = {
            "request_id": "8837544667111111",
            "error_type": test_case["error_type"],
            "error_codes": test_case["error_codes"]
        }

        # Create a mock response that raises HTTPError
        mock_response = MagicMock()
        mock_response.json.return_value = mock_response_data
        mock_response.status_code = 422
        mock_response.ok = False

        # Create a mock HTTPError
        mock_error = requests.exceptions.HTTPError(response=mock_response)
        mock_error.response = mock_response

        # Create a test transaction request
        transaction_request = TransactionRequest(
            reference=str(uuid.uuid4()),
            type=RecurringType.ONE_TIME,
            amount=Amount(
                value=1,
                currency='USD'
            ),
            source=Source(
                type=SourceType.PROCESSOR_TOKEN,
                id='test_token_id',
                store_with_provider=False
            ),
            customer=Customer(
                reference=str(uuid.uuid4())
            )
        )

        # Mock the session.request method to raise HTTPError
        with patch('requests.request', side_effect=mock_error) as mock_request:
            # Make the transaction request and expect a TransactionError
            with pytest.raises(TransactionError) as exc_info:
                sdk.checkout.create_transaction(transaction_request)

            # Get the error response from the exception
            error_response = exc_info.value.error_response

            # Verify the request was made with correct parameters
            mock_request.assert_called_once()
            # Validate error response structure
            assert isinstance(error_response.error_codes, list)
            assert len(error_response.error_codes) == 1

            # Verify exact error code values
            error = error_response.error_codes[0]
            assert error.code == test_case["expected_error"].code

            # Verify provider errors
            assert isinstance(error_response.provider_errors, list)
            assert len(error_response.provider_errors) == len(test_case["error_codes"])
            assert error_response.provider_errors == test_case["error_codes"]

            # Verify full provider response
            assert isinstance(error_response.full_provider_response, dict)
            assert error_response.full_provider_response['error_type'] == test_case["error_type"]
            assert error_response.full_provider_response['error_codes'] == test_case["error_codes"]


def test_idempotency_key():
    """Test that idempotency key is included in headers"""
    # Initialize the SDK
    sdk = Connections({
        'is_test': True,
        'bt_api_key': 'test_bt_api_key',
        'provider_config': {
            'checkout': {
                'private_key': 'test_private_key',
                'processing_channel': 'test_channel',
            }
        }
    })

    # Create mock response data
    mock_response_data = {
        "id": "pay_test_12345",
        "reference": "test_reference",
        "amount": 1000,
        "currency": "USD",
        "status": "Authorized",
        "processed_on": "2023-01-01T00:00:00.000Z"
    }

    # Create a mock response
    mock_response = MagicMock()
    mock_response.json.return_value = mock_response_data
    mock_response.status_code = 200
    mock_response.ok = True
    mock_response.headers = {}

    # Create a test transaction request with cardholder name
    transaction_request = TransactionRequest(
        reference='test_reference',
        type=RecurringType.ONE_TIME,
        amount=Amount(
            value=1000,
            currency='USD'
        ),
        source=Source(
            type=SourceType.BASIS_THEORY_TOKEN,
            id='test_token_id',
            store_with_provider=False,
            holder_name='John Doe'  # Test cardholder name
        ),
        customer=Customer(
            reference='test_customer_ref'
        )
    )

    # Test with idempotency key
    idempotency_key = 'test-checkout-idempotency-key-123'
    
    # Mock the session.request method
    with patch('requests.request', return_value=mock_response) as mock_request:
        response = sdk.checkout.create_transaction(transaction_request, idempotency_key=idempotency_key)

        # Verify the request was made
        mock_request.assert_called_once()
        
        # Get the call arguments
        call_args = mock_request.call_args
        headers = call_args[1]['headers']
        payload = call_args[1]['json']
        
        # Verify idempotency key is in headers
        assert 'cko-idempotency-key' in headers
        assert headers['cko-idempotency-key'] == idempotency_key


