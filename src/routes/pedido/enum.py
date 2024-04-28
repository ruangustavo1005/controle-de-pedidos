from common.enum import BaseEnum


class PedidoStatusEnum(BaseEnum):
    EM_PRODUCAO = ("em_producao", "Em produção")
    FEITO = ("feito", "Feito")
    ENTREGUE = ("entregue", "Entregue")
