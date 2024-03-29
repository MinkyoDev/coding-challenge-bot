import logging
from colorama import init, Fore, Style

init(autoreset=True)

class CustomFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.LIGHTBLUE_EX,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.RED + Style.BRIGHT,
    }
    ASCTIME_COLOR = Fore.LIGHTBLACK_EX

    FORMAT = "%(asctime)s %(levelname)s     %(message)s"

    def format(self, record):
        
        formatted_asctime = self.ASCTIME_COLOR + self.formatTime(record, self.datefmt) + Style.RESET_ALL
        color = self.COLORS.get(record.levelno, Fore.WHITE)
        formatted_levelname = color + record.levelname + Style.RESET_ALL
        
        original_format = super().format(record)

        final_message = original_format.replace(record.levelname, formatted_levelname).replace(self.formatTime(record, self.datefmt), formatted_asctime)

        return final_message


def setup_logger():
    logging.basicConfig(level=logging.INFO)
    formatter = CustomFormatter(CustomFormatter.FORMAT, "%Y-%m-%d %H:%M:%S")

    for handler in logging.getLogger().handlers:
        handler.setFormatter(formatter)