from log import util
from datetime import datetime
import log

class LiveLogger:
    """Log messages (with colour) onto the terminal"""
    def __init__(self, use_file: bool=True, log_file: str="latest.log"):
        self.log = []
        self.formatter = util.Format()
        self.file = log_file
        self.stream = None
        self.use_file = use_file

        self.enable()
    
    def enable(self):
        if self.use_file:
            self.stream = open(self.file, 'w')
        self.start_log()
    
    def start_log(self):
        now = datetime.now()
        self.info(f"Started log: {now.isoformat()}\n")
    
    def add_to_log(self, msg: str):
        if self.use_file:
            if not msg.endswith('\n'):
                ''.join((msg, '\n'))

            self.stream.write(msg)

    def info(self, msg: str):
        fmsg = self.formatter.format_message(msg, {"type": log.INFO_LABEL})
        self.add_to_log(fmsg)

    def warn(self, msg: str):
        fmsg = self.formatter.format_message(msg, {"type": log.WARNING_LABEL})
        self.add_to_log(fmsg)

    def error(self, msg: str):
        fmsg = self.formatter.format_message(msg, {"type": log.ERROR_LABEL})
        self.add_to_log(fmsg)
