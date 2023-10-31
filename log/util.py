from time import process_time
import sys
import log

class Format:
    def __init__(self):
        self.esc = "\x1b"
        self.cout = sys.stdout

        self.attributes = {
            "black":          "30m",
            "red":            "31m",
            "green":          "32m",
            "yellow":         "33m",
            "blue":           "34m",
            "magenta":        "35m",
            "cyan":           "36m",
            "light_grey":     "37m",
            "dark_grey":      "90m",
            "light_red":      "91m",
            "light_green":    "92m",
            "light_yellow":   "93m",
            "light_blue":     "94m",
            "light_magenta":  "95m",
            "light_cyan":     "96m",
            "white":          "97m",
            "bold":           "1m",
            "underline":      "4m",
            "no_underline":   "24m",
            "swap":           "7m",
            "no_swap":        "27m",
            "default":        "0m",
            "no_bold":        "22m",
            "overlined":      "53m",
            "no_frame":       "54m",
            "no_overline":    "55m",
            "no_blink":       "25m",
            "slow_blink":     "5m",
            "rapid_blink":    "6m",
            "italic":         "3m",
            "no_italic":      "23m",
            "faint":          "2m"
        }

        self.attributes = {
            key: '['.join((self.esc, value)) for key, value in self.attributes.items()
        }

        self.cleared_attributes = {
            key: '' for key, value in self.attributes.items()
        }

        self.colour_guide = {
            log.INFO_LABEL: "{white}",
            log.WARNING_LABEL: "{yellow}",
            log.ERROR_LABEL: "{red}"
        }
    
    def format_message(self, msg: str, additional_formatting: dict):
        fmt_dict = {}
        fmt_dict.update(self.attributes)
        fmt_dict.update(additional_formatting)

        type_ = additional_formatting.get("type")
        if type_ in self.colour_guide:
            colour = self.colour_guide[type_]

            prefix = ''.join((colour, "[ {type} ] +{process_time_}ms "))
            suffix = "{default}"
            process_time_ = round(process_time()*1000)

            # Generate coloured message for terminal
            msg_ = ''.join(
                (
                    prefix.format(**self.attributes, process_time_=process_time_, type=type_),
                    msg.format(**fmt_dict),
                    suffix.format(**self.attributes)
                )
            )

            # Generate clean message for logfile
            msg_clear = ''.join(
                (
                    prefix.format(**self.cleared_attributes, process_time_=process_time_, type=type_),
                    msg.format(**fmt_dict)
                )
            )

            self.cout.write(msg_)
            return msg_clear