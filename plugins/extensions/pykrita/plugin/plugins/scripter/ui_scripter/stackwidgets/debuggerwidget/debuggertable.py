from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class DebuggerTable(QTableWidget):

    def __init__(self, parent=None):
        super(DebuggerTable, self).__init__(parent)

        self.setColumnCount(4)

        tableHeader = ['Scope', 'Name', 'Value', 'Type']
        self.setHorizontalHeaderLabels(tableHeader)
        self.setEditTriggers(self.NoEditTriggers)

    def updateTable(self, data):
        self.clearContents()
        self.setRowCount(0)

        if data and not data.get('quit'):
            locals_list = data['frame']['locals']
            globals_list = data['frame']['globals']

            all_variables = {'locals': locals_list, 'globals': globals_list}

            for scope_key in all_variables:
                for item in all_variables[scope_key]:
                    for key, value in item.items():
                        row  = self.rowCount()
                        self.insertRow(row)
                        self.setItem(row, 0, QTableWidgetItem(str(scope_key)))
                        self.setItem(row, 1, QTableWidgetItem(key))
                        self.setItem(row, 2, QTableWidgetItem(str(value)))
                        self.setItem(row, 3, QTableWidgetItem(str(type(value))))
