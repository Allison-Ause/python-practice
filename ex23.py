
import sys
# filename, utf-8 encoding type, strict error handling
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    # read first line of the language file
    line = language_file.readline()

    # if there is a line, run print_line
    if line:
        print_line(line, encoding, error)
        #call it again
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    #.strip removes any leading or trailing whitespace
    next_lang = line.strip()
    #encode that line in the right format 
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #then decode it
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    #print the encoded and the decoded
    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)