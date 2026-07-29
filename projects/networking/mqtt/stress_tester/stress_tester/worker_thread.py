from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from publisher import Publisher


class WorkerSignals(QObject):
    finished = pyqtSignal(int)


class Worker(QRunnable):

    def __init__(self, id, host, port, verbose):
        self.signals = WorkerSignals()
        self.publisher = Publisher(id=id, host=host, port=port, verbose=verbose)

    @pyqtSlot()
    def run(self):
        self.publisher.loop()

    def kill(self):
        # Stop the loop
        self.publisher.toggleState()
        # Send the count through the threadsafe queue
        self.signals.finished.emit(self.publisher.count)
