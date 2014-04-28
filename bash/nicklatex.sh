#!/bin/bash
#
# skim: Script for opening a file in Skim in OS X and (if file was
#       already open) refreshing the file from disk. Also will position
#       the PDF corresponding to a line from a TeX source (if PDFSync
#       was used).
#
# Version: 1.03
#
# Author: Ted Pavlic
#         ted@tedpavlic.com
#         http://www.tedpavlic.com/
#
# Usage: skim [-h] [-a] [-o] "%file" [%line ["%source"]]
#
#        where %file is a PDF (or DVI or PS) file name, %line is a TeX
#        source line number, and %source is the file name of the TeX
#        source. The -a option prevents activating Skim. The -o
#        option prevents opening the file in Skim (i.e., only
#        refresh Skim and reposition). The -h option shows help text.
#
# For more information (and history), see:
#
# http://phaseportrait.blogspot.com/2007/07/script-to-open-file-in-skim-from.html
#
# Version history:
#
# 1.0  : 07/11/2007 - Initial release (Ted Pavlic)
# 1.01 : 07/17/2007 - Added usage line and ability to go open PDF at a particular TeX line (via PDFSync). (Ted Pavlic)
# 1.02 : 07/20/2007 - Checks for existence of files. Attempts to auto-complete extensions. (Ted Pavlic)
# 1.03 : 07/20/2007 - Added command line options for activating/opening TeXniscope. (Ted Pavlic)
#

function do_usage { 
  echo "Usage: skim [-help] [-a] [-o] FILE [LINE [SOURCE]]" >&2 
}

function do_help {
  do_usage
  echo "Open PDF/PS/DVI file in Skim. Optionally, use PDFSync to position FILE" >&2
  echo "according to LINE of SOURCE." >&2
  echo "" >&2
  echo -e "  -a,\t\t Do NOT activate Skim." >&2
  echo -e "  -o,\t\t Do NOT open the file (i.e., only refresh/reposition)." >&2
  echo -e "  -h,\t\t Show this help text." >&2
  echo "" >&2
}

# Usage if nothing passed
if [ "$1" == "" ]; then
  do_usage
  exit 1
fi

# Process options. Give usage if necessary
activateString="1"
openString="1"
while getopts aoh o; do 
  case "$o" in
    a) activateString="";;      # Disable "activate"    
    o) openString="";;          # Disable "open"
    h) do_help
       exit 1;;
    [?]) do_usage
         exit 1;;
  esac
done
shift $(( ${OPTIND}-1 ))

# Filename is first argument, line number second, source file third
fileName="$1"
lineNumber="$2"

# If filename isn't fully-qualified, add current working directory
[ "${fileName:0:1}" == "/" ] || fileName="${PWD}/${fileName}"

# If filename doesn't exist, try adding extensions; exit if we can't
# figure it out
if [ -f "${fileName}" ]; then
  fileNameExt="pdf";
elif [ -f "${fileName}.pdf" ]; then
  fileName="${fileName}.pdf";
  fileNameExt="pdf";
elif [ -f "${fileName}pdf" ]; then
  fileName="${fileName}pdf";
  fileNameExt="pdf";
elif [ -f "${fileName}.ps" ]; then
  fileName="${fileName}.ps";
  fileNameExt="ps";
elif [ -f "${fileName}ps" ]; then
  fileName="${fileName}ps";
  fileNameExt="ps";
elif [ -f "${fileName}.dvi" ]; then
  fileName="${fileName}.dvi";
  fileNameExt="dvi";
elif [ -f "${fileName}dvi" ]; then
  fileName="${fileName}dvi";
  fileNameExt="dvi";
else
  echo "File not found ($1)." >&2
  exit 1
fi

[ "${activateString}" != "" ] && activateString="activate"
[ "${openString}" != "" ] && openString="open theFile"

# Communicate with Skim via AppleScript
exec osascript \
  -e "set theFile to POSIX file \"${fileName}\"" \
  -e "tell application \"Skim\"" \
  -e "${activateString}" \
  -e "${openString}" \
  -e "revert front document" \
  -e "${gotoString}" \
  -e "end tell";