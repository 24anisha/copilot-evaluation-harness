from .. import models

class StatusBarController(object):
    def __init__(self, status_bar):
        self._status_bar = status_bar
        self._buffer = None

    @property
    def buffer(self):
        return self._buffer

    @buffer.setter
    def buffer(self, buffer):
        if buffer is None:
            raise Exception("Cannot set buffer to None")

        if self._buffer is not None:
            self._buffer.document.documentMetaInfo("Modified").contentChanged.disconnect(self._status_bar.setFileChangedFlag)
            self._buffer.document.documentMetaInfo("Filename").contentChanged.disconnect(self._status_bar.setFilename)
            self._buffer.cursor.positionChanged.disconnect(self._status_bar.setPosition)

        self._buffer = buffer

        # Connect the signals
        self._buffer.document.documentMetaInfo("Modified").contentChanged.connect(self._status_bar.setFileChangedFlag)
        self._buffer.document.documentMetaInfo("Filename").contentChanged.connect(self._status_bar.setFilename)
        self._buffer.cursor.positionChanged.connect(self._status_bar.setPosition)

        # Update the widget
        self._status_bar.setFilename(self._buffer.document.documentMetaInfo("Filename").data())
        self._status_bar.setFileChangedFlag(self._buffer.isModified())
        self._status_bar.setPosition(self._buffer.cursor.pos)
