import sys
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
errcodes = {
    "0x000": "INVALID_INPUT",
    "0x001": "CANNOT_DIVIDE_BY_ZERO",
    "0x002": "FS_ACCESS_DENIED",
    "0x003": "APPLICATION_IS_CORRUPTED",
    "0x004": "SAMPLE_ERROR",
    "0x005": "SAMPLE_ERROR_CRITICAL",
    "0x006": "UNKNOWN_ERROR",
    "0x007": "UNIMPLEMENTED_FUNCTION",
    "0x008": "DEV_ONLY",
    "0x009": "OUT_OF_RANGE",
}
errdef = {
    "0x000":
    "The input recived was in an invalid format, or was not an input the program was looking for.",
    "0x001":
    "It is impossible to divide any number by Zero(0).",
    "0x002":
    "The file system cannot be accessed.",
    "0x003":
    "The application is corrupted.",
    "0x004":
    "This is a sample error.",
    "0x005":
    "This is a sample critical error.",
    "0x006":
    "There was an unknown error. Try running the app again and try to find out where it occured",
    "0x007":
    "This function is not implemented",
    "0x008":
    "This function can only be accessed by the developer",
    "0x009":
    "The number is out of the 64-bit range and was returned as infinity",
}
def err(code, source, c):
    if code in errcodes:
        errcodedef = errcodes[code]
    else:
        errcodedef = errcodes["0x006"]
    define = errdef[code]
    if c == "f":
        if isofflineplatform == 1:
            print("===FATAL_ERROR===============")
            print(
                "A component has caused the application to close unexpectedly")
            print("Here is data linked to this crash.")
            print("CODE:" + code)
            print(errcodedef)
            print(define)
            print("SOURCE:" + source)
            print("TYPE:FATAL")
        else:
            print(color.RED + color.BOLD + "===FATAL_ERROR===============")
            print(
                "A component has caused the application to close unexpectedly")
            print("Here is data linked to this crash.")
            print("CODE:" + code)
            print(errcodedef)
            print(define)
            print("SOURCE:" + source)
            print("TYPE:FATAL" + color.END)
        sys.exit()
    elif c == "c":
        if isofflineplatform == 1:
            print("===CRITICAL_ERROR===============")
            print(
                "A component has ran into an error.")
            print("Here is data linked to this error.")
            print("CODE:" + code)
            print(errcodedef)
            print(define)
            print("SOURCE:" + source)
            print("TYPE:CRITICAL")
        else:
            print(color.RED + color.BOLD + "===CRITICAL_ERROR===============")
            print(
                "A component has ran into an error.")
            print("Here is data linked to this error.")
            print("CODE:" + code)
            print(errcodedef)
            print(define)
            print("SOURCE:" + source)
            print("TYPE:FATAL" + color.END)