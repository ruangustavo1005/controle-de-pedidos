from __future__ import annotations

from abc import ABC, abstractmethod

from common.gui.widget.base_widget import BaseWidget
from common.repository.base_repository import BaseRepository


class BaseController(ABC):
    _widget: BaseWidget
    _repository: BaseRepository
    _caller: BaseController

    def __init__(self, caller: BaseController | None = None) -> None:
        self._caller = caller
        self._widget = self._get_widget_instance()
        self._repository = self._get_repository_instance()

    @abstractmethod
    def _get_widget_instance(self) -> BaseWidget:
        raise NotImplementedError()

    @abstractmethod
    def _get_repository_instance(self) -> BaseRepository:
        raise NotImplementedError()

    def show(self) -> None:
        self._widget.show()
