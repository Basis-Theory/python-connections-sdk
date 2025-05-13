# PRD: Enhanced Checkout.com Response Handling

## 1. Introduction/Overview

This document outlines the requirements for enhancing our integration with Checkout.com to handle a broader range of response scenarios, particularly focusing on errors returned within a 200 HTTP OK status. The goal is to accurately map various decline types (Soft Declines, Hard Declines, Risk Responses, "Do Not Honor") and other error conditions to specific internal exceptions, providing clearer feedback and improving error diagnostics.

## 2. Goals

*   Implement comprehensive mapping for new Checkout.com response codes, including those indicative of Soft Declines, Hard Declines, Risk Responses, and "Do Not Honor".
*   Develop a mechanism to detect and handle error conditions even when Checkout.com returns a 200 HTTP OK response, similar to how Adyen responses are processed.
*   Ensure that appropriate and specific exceptions are thrown based on the mapped error conditions, allowing for better error handling and user feedback.
*   Maintain adherence to SOLID principles during implementation.

## 3. Success Metrics

*   Successful mapping of all documented Checkout.com error codes (Soft Declines, Hard Declines, Risk Responses, "Do Not Honor") to internal application states or exceptions.
*   Demonstrable ability to catch and correctly interpret errors returned within 200 OK responses from Checkout.com.
*   Reduction in unhandled or generically handled errors from Checkout.com integration.
*   Positive feedback from developers on the clarity and utility of the new error handling.

## 4. Scope

### In Scope:

*   Analysis of Checkout.com documentation for response codes and error structures (specifically for 200 OK responses that may contain error details).
*   Design and implementation of a mapping system for Checkout.com response codes/messages/indicators to internal error types/exceptions.
*   Modification of the existing Checkout.com client/service to incorporate the new error handling logic.
*   Creation of new custom exception classes as needed to represent the different error categories.
*   Adding unit tests for the new error mapping and exception handling logic.

### Out of Scope:

*   Changes to UI/UX based on these new errors (unless specifically requested as a follow-up).
*   Refactoring of existing Checkout.com integration logic beyond what is necessary to implement the new error handling.
*   Handling error scenarios not explicitly mentioned or documented by Checkout.com (e.g., network timeouts not producing a Checkout.com response).

## 5. Proposed Solution / Tasks

*   [ ] **Task 1: Research and Define Error Categories**
    *   [ ] Review Checkout.com documentation for all relevant response codes and their meanings (Soft Declines, Hard Declines, Risk Responses, "Do Not Honor", etc.).
    *   [ ] Identify patterns or specific fields in 200 OK responses that indicate an underlying error (e.g., `response_code`, `error_type` fields in the JSON body).
    *   [ ] Categorize these errors into logical groups for mapping to internal exceptions.

*   [ ] **Task 2: Design Error Mapping Mechanism**
    *   [ ] Define a clear structure (e.g., dictionary, configuration file, enum) to map Checkout.com response codes/messages/indicators to internal application exceptions or error types.
    *   [ ] Decide on the hierarchy and types of custom exceptions to be created (e.g., `CheckoutSoftDeclineError`, `CheckoutHardDeclineError`, `CheckoutRiskResponseError`, `CheckoutDoNotHonorError`, `CheckoutUnexpectedError`).

*   [ ] **Task 3: Implement Custom Exceptions**
    *   [ ] Create the necessary custom exception classes, ensuring they can store relevant information from the Checkout.com response (e.g., original response code, message, transaction ID).

*   [ ] **Task 4: Implement Response Parsing and Error Handling Logic**
    *   [ ] Modify the Checkout.com API client/service to inspect the HTTP status code.
    *   [ ] If status is 200 OK, parse the response body to check for known error indicators.
    *   [ ] If an error indicator is found in a 200 OK response, or if the status code itself indicates an error (e.g., 4xx, 5xx, or specific 2xx like 20001+), use the mapping mechanism to determine the appropriate custom exception.
    *   [ ] Throw the identified custom exception.

*   [ ] **Task 5: Integrate and Test**
    *   [ ] Update relevant parts of the application that call the Checkout.com service to catch and handle the new specific exceptions.
    *   [ ] Write unit tests to cover various Checkout.com response scenarios:
        *   Successful 200 OK without errors.
        *   200 OK with a "Soft Decline" error code in the body.
        *   200 OK with a "Hard Decline" error code in the body.
        *   200 OK with a "Risk Response" error code in the body.
        *   200 OK with a "Do Not Honor" error code in the body.
        *   Non-200 error responses with corresponding error codes.
    *   [ ] (Optional) Conduct integration tests by mocking Checkout.com API responses if feasible.

*   [ ] **Task 6: Documentation**
    *   [ ] Update any internal developer documentation regarding Checkout.com integration to reflect the new error handling mechanism and custom exceptions.
    *   [ ] Ensure this PRD is updated with any changes during implementation.

## 6. Checkout.com Error Code Reference

---
*(Error codes from user prompt will be inserted below this line)*
---

Response code	Response text	Additional information
20001

Refer to card issuer

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

Contact card issuer

20002

Refer to card issuer - Special conditions

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

20003

Invalid merchant or service provider

The payment failed due to a technical issue. If the issue persists please contact us.

20004

Card should be captured

20005

Declined - Do not honour

The payment has been declined by your bank. Try a different card or contact your bank for further support. Refer to our recommendation codes documentation for more information.

For payouts, this indicates the transaction was declined by the issuer bank. If you encounter systemic issues or a high percentage of declines for a specific recipient card BIN, contact your account manager or support@checkout.com to report this to Checkout.com.

20006

Error / Invalid request parameters

20009

Request in progress

20012

Invalid transaction

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

20013

Invalid value/amount

The payment failed due to a technical issue. If the issue persists please contact us.

20014

Invalid account number (no such number)

The payment failed, please check your card details and try again with the same or another card.

20015

Transaction cannot be processed through debit network.

Route your transaction to the card's signature network.

20016

Card not initialised

20017

Customer cancellation

20018

Customer dispute

20019

Re-enter transaction

Transaction has expired

20020

Invalid response

20021

No action taken (unable to back out prior transaction)

20022

Suspected malfunction

20023

Unacceptable transaction fee

20024

File update not supported by the receiver

20025

Unable to locate record on file

Account number is missing from the inquiry

20026

Duplicate file update record

20027

File update field edit error

20028

File is temporarily unavailable

20029

File update not successful

20030

Format error

The payment failed due to a technical issue. Either try again with the same card, or use a different card.

MADA transactions may throw this error code under specific circumstances. See Format error in MADA transactions for more information.

20031

Bank not supported by Switch

20032

Completed partially

20033

Previous scheme transaction ID invalid

20038

Allowable PIN tries exceeded

20039

No credit account

20040

Requested function not supported

20042

No universal value/amount

20044

No investment account

20045

The Issuer does not support fallback transactions of hybrid-card

20046

Bank decline

The payment has been declined by your bank. Please try a different card or contact your bank for further support. Refer to our recommendation codes documentation.

20051

Insufficient funds

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

20052

No current (checking) account

20053

No savings account

20054

Expired card

20055

Incorrect PIN

PIN validation not possible

20056

No card record

20057

Transaction not permitted to cardholder

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

For payouts, this indicates the payment was declined by the issuing bank, likely due to a restricted recipient card BIN. Request an alternative payment method from the recipient, or ask them to contact their issuer. If you encounter systemic issues or a high percentage of declines for a specific recipient card BIN, contact your account manager or support@checkout.com to report this to Checkout.com.

Domestic debit transaction not allowed (Regional use only)

20058

Transaction not permitted to terminal

20059

Suspected fraud

The payment has been declined by your bank. Please try a different card or contact your bank for further support. Refer to our recommendation codes documentation.

20060

Card acceptor contact acquirer

20061

Activity amount limit exceeded

Occurs if the defined amount is exceeded for the account or card. Refer to the page on recommendation codes for suggested action.

For payouts, this indicates the payment was declined by the issuer bank or card network. The velocity limits for the recipient card may have been exceeded. Retry the payout the following day.

20062

Restricted card

The payment has been declined by your bank. Please try a different card or contact your bank for further support. Refer to our recommendation codes documentation.

20063

Security violation

20064

Transaction does not fulfil AML requirement

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

20065

Exceeds Withdrawal Frequency Limit

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

For payouts, this indicates the payment was declined by the issuer bank or card network. The velocity limits for the recipient card may have been exceeded. Retry the payout the following day.

20066

Card acceptor call acquirer security

20067

Hard capture - Pick up card at ATM

20068

Response received too late / Timeout

The payment failed due to a technical issue. Please try again with the same card, or use a different card.

Internal error

20072

Account not yet activated

20075

Allowable PIN-entry tries exceeded

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

20078

Blocked at first use - transaction from new or replacement card that is not properly unblocked

The payment has been declined by your bank. Please try a different card or contact your bank for further support. Refer to our recommendation codes documentation.

20081

Card is local use only

20082

No security model

PIN cryptographic error found (error found by VIC security module during PIN decryption)

Negative CAM, dCVV, iCVV, or CVV results

20083

No accounts

20084

No PBF

20085

PBF update error

20086

ATM malfunction

Invalid authorization type

20087

Bad track data (invalid CVV and/or expiry date)

The payment failed, please check your card details and try again with the same or another card.

20088

Unable to dispense/process

20089

Administration error

20090

Cut-off in progress

20091

Issuer unavailable or switch is inoperative

The payment failed due to a technical issue. Try again with the same card, or use a different card.

For payouts, this indicates that the issuer host system may be down, or connectivity was lost. Retry the payout when the connection issues have been resolved.

20092

Destination cannot be found for routing

20093

Transaction cannot be completed; violation of law

The payment has been declined by your bank. Please try a different card or contact your bank for further support. Refer to our recommendation codes documentation.

20094

Duplicate transmission / invoice

20095

Reconcile error

20096

System malfunction

The payment failed due to a technical issue. Please try again with the same card, or use a different card.

20097

Reconciliation totals reset

20098

MAC error

20099

Other / Unidentified responses

The payment failed due to a technical issue. If the issue persists please contact us.

20197

The ATM/POS terminal number has not been registered

2005C

Transaction not supported / blocked by issuer

2006P

Cardholder ID verification failed

Cardholder could not be identified from their ID documentation as part of Know Your Customer (KYC) checks. The cardholder should contact their issuing bank to resolve.

2009G

Blocked by cardholder / contact cardholder

200A4

Transaction with defect, contact issuer

The requests have not been received.

200A5

The original transactions are rejected.

200A6

UnionPay forwarded the original request, but did not receive a response from the issuer.

200E0

Unauthorised access

200E2

Signature verification failure

200E3

System busy, please try again later

200N0

Force STIP

200N7

Decline for CVV2 failure

200O5

PIN required

200P1

Over daily limit

200P9

Limit exceeded. Enter a lesser value.

200R1

Issuer initiated a stop payment (revocation order) for this authorization

The cardholder has canceled this subscription

200R3

Issuer initiated a stop payment (revocation order) for all authorizations

The cardholder has canceled all subscriptions

200S4

PTLF full

200T2

Invalid transaction date

200T3

Card not supported

200T5

CAF status = 0 or 9

20100

Invalid expiry date format

The payment failed due to invalid expiry date. Please try again providing the correct value.

20101

No Account / No Customer (Token is incorrect or invalid)

20102

Invalid merchant / wallet ID

The payment failed due to a technical issue. If the issue persists please contact us.

20103

Card type / payment method not supported

The payment has been declined by your bank. Please try again with a different card or contact your bank for further support.

20104

Gateway reject - Invalid transaction

The payment failed due to a technical issue. Please try again with the same card, or use a different card.

20105

Gateway reject - Violation

The payment failed due to a technical issue. Please try again with the same card, or use a different card.

20106

Unsupported currency

20107

Billing address is missing

20108

Declined - Updated cardholder available

20109

Transaction already reversed (voided)

Previous message located for a repeat or reversal, but repeat or reversal data is inconsistent with the original message

Capture is larger than initial authorized value

20110

Authorization completed

20111

Transaction already reversed

The payment reversal has already been processed.

20112

Merchant not Mastercard SecureCode enabled

The payment failed due to a technical issue. Please contact us with the payment reference number.

20113

Invalid property

20114

Token is incorrect

20115

Missing / Invalid lifetime

20116

Invalid encoding

20117

Invalid API version

The payment failed due to a technical issue. If the issue persists please contact us.

20118

Transaction pending

The payment failed due to a technical issue. If the issue persists please contact us.

20119

Invalid batch data and/or batch data is missing

The payment failed due to a technical issue. If the issue persists please contact us.

20120

Invalid customer/user

The payment failed due to a technical issue. If the issue persists please contact us.

20121

Transaction limit for merchant/terminal exceeded

20122

Mastercard installments not supported

20123

Missing basic data: zip, addr, member

The payment failed due to a technical issue. If the issue persists please contact us.

20124

Missing CVV value, required for ecommerce transaction

20150

Card not 3D Secure (3DS) enabled

20151

Cardholder failed 3DS authentication

20152

Initial 3DS transaction not completed within 15 minutes

The payment has expired due to inactivity. Please try again with the same card, or use a different card.

20153

3DS system malfunction

The payment failed due to a technical issue. Please try again with the same card, or use a different card.

20154

3DS authentication required

The payment declined due to Strong Customer Authentication (3DS). Please try again with the same card, or use a different card.

20155

3DS authentication service provided invalid authentication result

20156

Requested function not supported by the acquirer

20157

Invalid merchant configurations - Contact Support

20158

Refund validity period has expired

20159

ACS Malfunction

The payment failed due to a technical issue with the ACS used to perform 3DS authentication. If the issue persists, contact Checkout.com.

20179

Lifecycle

Occurs when transaction has invalid card data. Refer to the page on recommendation codes for suggested action.

20182

Policy

Occurs when a transaction does not comply with card policy. Refer to the page on recommendation codes for suggested action.

20183

Security

Occurs when a transaction is suspected to be fraudulent. Refer to the page on recommendation codes for suggested action.

20193

Invalid country code

### 30xxx - Hard declines
Information
The response code message text may vary across different endpoint responses.

Response code	Response text	Additional information
30004

Pick up card (No fraud)

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30007

Pick up card - Special conditions

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30015

No such issuer

The payment has been declined due to incorrect details. Please try again with updated details.

For payouts, this indicates that the recipient card number is incorrect, invalid, or restricted. Request an alternative payment method from the recipient, or ask them to contact their issuer. If you encounter systemic issues or a high percentage of declines for a specific recipient card BIN, report this to Checkout.com.

30016

Issuer does not allow online gambling payout

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30017

Issuer does not allow original credit transaction

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30018

Issuer does not allow money transfer payout

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30019

Issuer does not allow non-money transfer payout

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30020

Invalid amount

The payment failed due to a technical issue. If the issue persists please contact us.

30021

Total amount limit reached

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30022

Total transaction count limit reached

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30033

Expired card - Pick up

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30034

Suspected fraud - Pick up

The payment has been declined by your bank. Please contact your bank for further support.

For payouts, this indicates the payment was declined by the issuer bank, likely due to suspected fraud. Ask the cardholder to contact their issuer and do not reattempt a payout.

30035

Contact acquirer - Pick up

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30036

Restricted card - Pick up

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30037

Call acquirer security - Pick up

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30038

Allowable PIN tries exceeded - Pick up

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30041

Lost card - Pick up

The payment has been declined by your bank. Please try a different card or contact your bank for further support.

30043

Stolen card - Pick up

The cardholder's bank has declined the payment because the card has been reported stolen.

For a one-off transaction, do not attempt the transaction again. If possible, do not provide goods or services to the person attempting the transaction.
For a recurring or scheduled transaction, it's possible the card was lost after the last successfully processed payment, or after the scheduled payment's authorization. In either scenario, contact your customer and request that they update their payment method. Replace the account number for their lost card with the account number for their new card.
30044

Transaction rejected - AMLD5

Transaction was initiated from an anonymous, non-reloadable prepaid card and for an amount greater than 50 EUR. Due to the AMLD5 directive, it cannot be fulfilled.

30045

Invalid payout fund transfer type

If the fund transfer type is not among the list that was configured for allowed funds transfer types, the transaction would fail.

30046

Closed account

The payment has been declined by your bank. Please contact your bank for further support.

### 4xxxx - Risk responses
Risk responses are triggered by our risk engine.

Information
The response code message text may vary across different endpoint responses.

Response code	Response text	Additional information
40101

Risk blocked transaction

The payment failed due to a security violation. See the Transaction declined with error code 40101 support article to troubleshoot this response code.

To receive new response codes with detailed summaries, contact your account manager or support@checkout.com.

40201

Gateway reject - card number blocklist

To receive new response codes with detailed summaries, contact your account manager or support@checkout.com.

40202

Gateway reject - IP address blocklist

To receive new response codes with detailed summaries, contact your account manager or support@checkout.com.

40203

Gateway reject - email blocklist

To receive new response codes with detailed summaries, contact your account manager or support@checkout.com.

40204

Gateway reject - phone number blocklist

To receive new response codes with detailed summaries, contact your account manager or support@checkout.com.

40205

Gateway Reject - BIN number blocklist

To receive new response codes with detailed summaries, contact your account manager or support@checkout.com.

#### New response codes

##### Client-level response codes
Beta

Response code	Response text	Additional information
41101

Risk Blocked Transaction

The transaction was declined due to a client-level rule configured in your account.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

41201

Decline list - Card number

The transaction was declined due to a client-level rule configured in your account.

For more information:

Sign in to the Dashboard.
Go to Payments > Processing > All payments and select the payment.
On the Payment details screen, select the fraud assessment in Payment timeline.
The Fraud Detection assessment screen appears with detailed information.
If you've not opted in to receive the new response codes, you receive a 40101 code instead.

41202

Decline list - BIN

The transaction was declined because the associated BIN is on a client-level decline list in your account.

If you've not opted in to receive the new response codes, you receive a 40205 code instead.

41203

Decline list - Email address

The transaction was declined because the associated email address is on a client-level decline list in your account.

If you've not opted in to receive the new response codes, you receive a 40203 code instead.

41204

Decline list - Phone

The transaction was declined because the associated phone number is on a client-level decline list in your account.

If you've not opted in to receive the new response codes, you receive a 40204 code instead.

41205

Decline list - Payment IP

The transaction was declined because the associated payment IP is on a client-level decline list in your account.

If you've not opted in to receive the new response codes, you receive a 40202 code instead.

41206

Decline list - Email domain

The transaction was declined because the associated email domain is on a client-level decline list in your account.

If you've not opted in to receive the new response codes, you receive a 40203 code instead.

41301

Fraud score exceeds threshold

The transaction was declined because it was flagged as high risk by our fraud model score.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

##### Entity-level response codes
Beta

Response code	Response text	Additional information
42101

Risk Blocked Transaction

The transaction was declined due to an entity-level rule configured in your account.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

42201

Decline list - Card number

The transaction was declined due to an entity-level rule configured in your account.

For more information:

Sign in to the Dashboard.
Go to Payments > Processing > All payments and select the payment.
On the Payment details screen, select the fraud assessment in Payment timeline.
The Fraud Detection assessment screen appears with detailed information.
If you've not opted in to receive the new response codes, you receive a 40101 code instead.

42202

Decline list - BIN

The transaction was declined because the associated BIN is on an entity-level decline list in your account.

If you've not opted in to receive the new response codes, you receive a 40105 code instead.

42203

Decline list - Email address

The transaction was declined because the associated email address is on an entity-level decline list in your account.

If you've not opted in to receive the new response codes, you receive a 40203 code instead.

42204

Decline list - Phone

The transaction was declined because the associated phone number is on an entity-level decline list in your account.

If you've not opted in to receive the new response codes, you receive a 40204 code instead.

41205

Decline list - Payment IP

The transaction was declined because the associated payment IP is on an entity-level decline list in your account.

If you've not opted in to receive the new response codes, you receive a 40202 code instead.

42206

Decline list - Email domain

The transaction was declined because the associated email domain is on a client-level decline list in your account.

If you've not opted in to receive the new response codes, you receive a 40203 code instead.

42301

Fraud score exceeds threshold

The transaction was declined because it was flagged as high risk by our fraud model score.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

##### Checkout.com-level response codes
Beta

Response code	Response text	Additional information
43101

Potential fraud risk

The transaction was declined because it was flagged as high risk by our fraud model.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

43102

Risk blocked transaction – {Rule group name}

The transaction was declined for one of the following reasons:

A Checkout.com decline rule
A fraud-specific model where the {rule group name} provides all available information about the type of risk identified
Use rule group names for information only because Checkout.com may change them.

For example, for a non-compliant payment, you receive the response summary Risk decline - Scheme compliance.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

43201

Decline list - Card number

The transaction was declined because the associated card number is on Checkout.com's decline list.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

43202

Decline list - BIN

The transaction was declined because the associated BIN is on Checkout.com's decline list.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

43203

Decline list - Email address

The transaction was declined because the associated email address on Checkout.com's decline list.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

43204

Decline list - Phone

The transaction was declined because the associated phone number is on Checkout.com's decline list.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

43205

Decline list - Payment IP

The transaction was declined because the associated payment IP is on Checkout.com's decline list.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

43206

Decline list - Email domain

The transaction was declined because the associated email domain is on Checkout.com's decline list.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

43301

Fraud score exceeds threshold

The transaction was declined because it was flagged as high risk by our fraud model score.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

44301

3DS authentication required

The transaction was declined because additional authentication is required for processing. Reattempt the transaction with 3D Secure.

If you've not opted in to receive the new response codes, you receive a 40101 code instead.

### 50xxx - Card payout declines
Information
The response code message text may vary across different endpoint responses.

Response code	Response text	Additional information
50001

Compliance error

50002

Sanction screening failure

Sanctions screening hit or data corruption.

50003

Balance reservation insufficient funds

Insufficient available balance in sub-account.

50005

Barred Beneficiary Error

50020

Recipient error

50021

Invalid recipient error

50022

Unsupported recipient error

50023

Recipient limit error

50025

Invalid Recipient Account Error

50026

Recipient Account Not Found

50027

Recipient Bank Error

50030

Invalid Recipient Details Error

50070

Sender error

50100

Instruction error

50101

Instruction amount limit error

50102

Instruction amount limit sender error

50103

Instruction amount limit recipient error

50104

Velocity limit

50105

Velocity limit sender error

50106

Velocity limit recipient limit error

50150

Processing error

50180

Validation error

50200

Configuration error

50240

Cancellation error

50260

Returned error

50280

Insufficient funds

50399

Unmapped response

50401

Bank details invalid

50402

Account not found

50403

Account inactive

50404

Account dormant

50405

Account number invalid

50406

Branch not found

50407

Branch code invalid

50408

Branch code required

50409

Bank code invalid

50410

Bank code required

50441

Account type required

50451

Account holder details invalid

50452

Account holder identification number required

50453

Account holder type not supported

50454

Account holder type not allowed

50466

Account closed

50471

Account blocked

50481

Invalid debtor account type

50490

Duplicate Payment

50491

Account holder billing address details incorrect

50492

Account holder billing address details required

50494

Account holder billing address can not be PO box

50499

Payout Returned

50501

Unsupported characters

50511

Invalid amount

50512

Minimum amount not met

50513

Exceeded transaction value

50514

Exceeded daily limit

50515

Exceeded weekly limit

50517

Exceeded monthly limit

50531

Recalled

50599

Unknown reason 