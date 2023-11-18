from threading import Thread
from lazyprocess.utils.queue import Queue
from lazyprocess.services.editor import Editor
from lazyprocess.services.sender import Sender
from lazyprocess.models.edit import Edit as EditModel

class EditQueueThread(Thread):
    def __init__(self, queue: Queue[EditModel], editor: Editor, sender: Sender):
        super().__init__()
        self.queue = queue
        self.editor = editor
        self.sender = sender
        self.isRunnig = False

    def run(self) -> None:
        self.isRunnig = True
        
        while self.isRunnig:
            edit = self.queue.dequeue()

            if edit:
                edited = self.editor.apply(edit)
                self.sender.send(edited)
