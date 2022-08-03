from colorama import Fore , Back, Style

class bg :
    def red_b(x):
        x = Back.RED + Style.DIM + x + Style.RESET_ALL
        return x
    def green_b(x):
        x = Back.GREEN + Style.DIM + x + Style.RESET_ALL
        return x
    def black_b(x):
        x = Back.BLACK + Style.DIM + x + Style.RESET_ALL
        return x
    def yellow_b(x):
        x = Back.YELLOW + Style.DIM + x + Style.RESET_ALL
        return x
    def white_b(x):
        x = Back.WHITE + Style.DIM + x + Style.RESET_ALL
        return x
    def clear(x):
        x = x = Back.WHITE + Style.DIM + ' ' + Style.RESET_ALL
        return x
class fg :
    def black(x) :
        x = Fore.BLACK + x + Style.RESET_ALL
        return x
    def red(x):
        x = Fore.RED + x + Style.RESET_ALL
        return x