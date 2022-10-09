from client.infrastructure.logging.I_logger import ILogger
from client.models.payment import Payment
from client.services.I_payment_service import IPaymentService


class PaymentServiceStub(IPaymentService):
    def __init__(self, should_succeed: bool, logger: ILogger):
        self._logger = logger
        self._should_succeed = should_succeed

    def pay(self, payment: Payment):
        self._logger.info("Payment started")

        if self._should_succeed:
            self._logger.payment(payment)
            self._logger.info(f"Payment finished")
        else:
            self._logger.error(f"Payment failed", Exception("Payment failed"))
