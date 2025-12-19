from abc import ABC, abstractmethod
from dataclasses import dataclass

# ================= MODEL =================
@dataclass
class Order:
    customer_name: str
    total_price: float
    status: str = "open"


# ================= ABSTRAKSI =================
class IPaymentProcessor(ABC):
    @abstractmethod
    def process(self, order: Order) -> bool:
        pass


class INotificationService(ABC):
    @abstractmethod
    def send(self, order: Order):
        pass


# ================= IMPLEMENTASI =================
class CreditCardProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Payment: Memproses kartu kredit")
        return True


class EmailNotifier(INotificationService):
    def send(self, order: Order):
        print(f"Email dikirim ke {order.customer_name}")

class CheckoutService:
    def __init__(
        self,
        payment_processor: IPaymentProcessor,
        notifier: INotificationService
    ):
        self.payment_processor = payment_processor
        self.notifier = notifier

    def run_checkout(self, order: Order):
        if self.payment_processor.process(order):
            order.status = "paid"
            self.notifier.send(order)
            print("Checkout berhasil")
            return True
        return False

class QrisProcessor(IPaymentProcessor):
    def process(self, order: Order) -> bool:
        print("Payment: Memproses QRIS")
        return True

email_service = EmailNotifier()

# Credit Card
order1 = Order("Andi", 50000)
checkout_cc = CheckoutService(
    payment_processor=CreditCardProcessor(),
    notifier=email_service
)
checkout_cc.run_checkout(order1)

print("-----")

# QRIS (Challenge OCP)
order2 = Order("Budi", 100000)
checkout_qris = CheckoutService(
    payment_processor=QrisProcessor(),
    notifier=email_service
)
checkout_qris.run_checkout(order2)
