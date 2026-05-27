from dataclasses import dataclass


@dataclass(frozen=True)
class Metric:
    code: str
    title: str
    is_money: bool = False


METRICS: tuple[Metric, ...] = (
    Metric("calls_total", "Calls total"),
    Metric("outgoing_calls", "Outgoing calls"),
    Metric("successful_outgoing_calls", "Successful outgoing calls"),
    Metric("incoming_calls", "Incoming calls"),
    Metric("meetings_created", "Meetings created"),
    Metric("commercial_offers_sent", "Commercial offers sent"),
    Metric("contracts_sent", "Contracts sent"),
    Metric("contracts_signed", "Contracts signed"),
    Metric("invoices_sent", "Invoices sent"),
    Metric("invoices_paid", "Invoices paid"),
    Metric("new_deals", "New deals"),
    Metric("successful_sale_deals", "Successful sale deals"),
    Metric("paid_invoice_sum", "Paid invoice sum", is_money=True),
)

METRIC_CODES: tuple[str, ...] = tuple(metric.code for metric in METRICS)
