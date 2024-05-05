import glob

CODE_SECTION_FAILED = "--- This code section failed: ---"
PARSE_ERROR = "Parse error at or near "
this_file = "./fix_parse_errors.py"

for f in glob.glob("./build" + "/**/*.py", recursive=True):
    if f == this_file:
        continue
    file_content = open(f).read()
    if CODE_SECTION_FAILED in file_content:
        new_array = []
        splitted = file_content.split("\n")
        should_drop = False
        for i in splitted:
            if CODE_SECTION_FAILED in i:
                new_array.append(f"{i[:i.index(CODE_SECTION_FAILED)]}():")
                new_array.append(f"{' ' * (i.index('def') + 4)}pass")
                should_drop = True
            else:
                if i.startswith(PARSE_ERROR):
                    should_drop = False
                    continue
                if not should_drop:
                    new_array.append(i)
        open(f, "w").write("\n".join(new_array))
