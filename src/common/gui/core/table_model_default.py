from typing import Any, List, Union

from PySide6.QtCore import QAbstractTableModel, QModelIndex, QPersistentModelIndex, Qt


class TableModelDefault(QAbstractTableModel):
    def __init__(self, headers: List[str], data: List[List[Any]] = []):
        super(TableModelDefault, self).__init__()
        self._headers = headers
        self._data = data

    def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = None):
        return len(self._data)

    def columnCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = None):
        return len(self._headers)

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if (
            role == Qt.ItemDataRole.DisplayRole
            and orientation == Qt.Orientation.Horizontal
            and section < len(self._headers)
        ):
            return self._headers[section]
        return None

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        return None

    def setRowData(self, row: int, values: List[Any]) -> bool:
        if row < 0 or row >= self.rowCount() or len(values) != self.columnCount():
            return False
        for col in range(self.columnCount()):
            self._data[row][col] = values[col]
            index = self.createIndex(row, col)
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.EditRole])
        return True

    def setData(self, data: List[List[Any]]) -> bool:
        if len(data) == 0 or len(data[0]) == len(self._headers):
            self.beginResetModel()
            self._data = data
            self.endResetModel()
            return True
        return False
