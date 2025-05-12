import argparse
import os

######################## readmd ############################################
#
#   nsi 파일들이 들여쓰기가 엉망이다.
#   비슷비슷한 파일들을 비교하기가 너무 어려웠다.
#   들여쓰기만 정리하는 스크립트 툴을 만들었다.
#
#   IfFileExists label1, label2 
#
#   이런 부분은 인덴트를 잘 하지 못한다. 더 복잡한 구현이 필요함.
#
############################################################################


## from rules import rules
######################## rules
rules = {
    "indenters": [
        "!if", "!ifdef", "!ifmacrodef", "!ifmacrondef", "!ifndef", "!macro",
        "${case}", "${case2}", "${case3}", "${case4}", "${case5}",
        "${caseelse}", "${default}", "${do}", "${dountil}", "${dowhile}",
        "${for}", "${foreach}", "${if}", "${ifnot}", "${mementosection}",
        "${mementounselectedsection}", "${select}", "${switch}", "${unless}",
        "function", "pageex", "section", "sectiongroup", "findfirst"
    ],
    "dedenters": [
        "!endif", "!macroend", "${endif}", "${endselect}", "${endswitch}",
        "${endwhile}", "${loop}", "${loopuntil}", "${loopwhile}",
        "${mementosectionend}", "${next}", "${while}", "functionend",
        "pageexend", "sectionend", "sectiongroupend", "findclose"
    ],
    "specialIndenters": [
        "!else", "!elseif", "${else}", "${elseif}", "${elseifnot}", "${elseunless}",
        "${andif}", "${andifnot}", "${andunless}", "${orif}", "${orifnot}", "${orunless}"
    ],
    "specialDedenters": [
        "${break}"
    ]
}

# Lowercase everything for case-insensitive matching
for key in rules:
    rules[key] = [item.lower() for item in rules[key]]

######################## rules end

def auto_indent_file(input_path, output_path=None, indent_spaces=4, encoding="cp949", write=False, use_tab=True):
    with open(input_path, "r", encoding=encoding) as f:
        lines = f.readlines()

    result = []
    indent_level = 0
    switch_indent_level = 0
    indent = " " * indent_spaces
    if use_tab :
        indent = "\t"

    for line in lines:
        stripped_line = line.strip()
        keyword = stripped_line.split(" ")[0].lower() if stripped_line else ""

        # Handle ${Switch} and ${EndSwitch} like in the original
        if keyword == "${switch}":
            switch_indent_level = indent_level

        if keyword == "${endswitch}":
            indent_level = switch_indent_level
            result.append((indent * indent_level) + stripped_line + "\n")
            indent_level = max(indent_level - 1, 0)
            continue

        # Special indenters (like else) - dedent *before* writing
        if keyword in rules["specialIndenters"]:
            result.append(
                (indent * max(indent_level - 1, 0)) + stripped_line + "\n"
            )
            continue

        # Special dedenters - write then decrease
        if keyword in rules["specialDedenters"]:
            result.append((indent * indent_level) + stripped_line + "\n")
            indent_level = max(indent_level - 1, 0)
            continue

        # Dedenters - decrease *before* writing
        if keyword in rules["dedenters"]:
            indent_level = max(indent_level - 1, 0)
            result.append((indent * indent_level) + stripped_line + "\n")
            continue

        # Write line first
        result.append((indent * indent_level) + stripped_line + "\n")

        # Then increment for indenters
        if keyword in rules["indenters"]:
            indent_level += 1

    if write:
        with open(input_path, "w", encoding=encoding) as f:
            f.writelines(result)
    elif output_path:
        with open(output_path, "w", encoding=encoding) as f:
            f.writelines(result)
    else:
        with open(input_path + ".out.nsi", "w", encoding=encoding) as f:
            f.writelines(result)


def main():
    parser = argparse.ArgumentParser(description="Auto-indent NSIS .nsi script files.")
    parser.add_argument("input", help="Input .nsi file")
    parser.add_argument(
        "-o", "--output", help="Optional output file. If not set, prints to stdout."
    )
    parser.add_argument(
        "-e", "--encoding", default="cp949", help="File Encoding. If not set, cp949."
    )
    parser.add_argument(
        "-w", "--write", action="store_true", help="Modify input file in place."
    )
    parser.add_argument(
        "-i", "--indent", type=int, default=0, help="Indentation size in spaces (default: 0). If 0 is set, use tab."
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: File '{args.input}' not found.")
        return

    auto_indent_file(args.input, args.output, args.indent, args.encoding, args.write, args.indent==0)


if __name__ == "__main__":
    main()
