def initiate_paynow_payment(application):
    # For demonstration, we are creating a mock payment link.
    # You would replace the content here with actual API calls to the payment gateway/service you are using.
    payment_url = f"https://mockpaymentgateway.com/checkout?app_id={application.id}"
    signature = "signature_for_app_{}".format(application.id)  # Mock signature for demonstration
    return payment_url, signature