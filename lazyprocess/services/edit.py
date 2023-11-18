from lazyprocess.repositories.edit import Edit as EditRepository
from lazyprocess.models.edit import Edit as EditModel
from lazyprocess.utils.queue import Queue
from lazyprocess.services.editQueueThread import EditQueueThread
from lazyprocess.services.editor import Editor
from lazyprocess.services.sender import Sender

class Edit(object): 
    def __init__(self):
        self.repository = EditRepository()
        self.queue = Queue[EditModel]()
        self.queueThread = EditQueueThread(self.queue, Editor(), Sender())
        self.queueThread.start()

    def create(self, origin: str, destiny: str) -> EditModel:
        edit = self.repository.create(origin, destiny)

        self.queue.enqueue(edit)

        return edit
