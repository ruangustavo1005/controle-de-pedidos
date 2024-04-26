from enum import Enum


class PedidoStatusEnum(str, Enum):
    EM_PRODUCAO = "em_producao"
    FEITO = "feito"
    ENTREGUE = "entregue"
