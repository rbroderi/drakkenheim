from pathlib import Path
import re
import frontmatter
SCRIPTROOT = Path(__file__).resolve().parent

regexp = re.compile(r'`\s*=\s*.*?`')


for filepath in SCRIPTROOT.rglob("*.md"):
    # skip templates
    if "TEMPLATE" in str(filepath.absolute()).upper():
        continue
    # replace filename
    with filepath.open("r",encoding="UTF-8") as rfile:
        s = rfile.read()
        rplce = re.sub('`=this.file.name`', filepath.stem.title(), s)
    with filepath.open("w",encoding="UTF-8") as wfile:
        wfile.write(rplce)
    
    with filepath.open("r",encoding="UTF-8") as file:
        s = file.read()
    with filepath.open("r",encoding="UTF-8") as file:
        for line in file:
            the_match = regexp.search(line)
            if the_match:
                print("found")
                data = frontmatter.load(filepath)
                var = the_match.group().rpartition(".")[2]
                var = re.sub(r"\s*`","",var)
                line = line.replace(the_match.group(),str(data[var]))
                s = s.replace(the_match.group(), str(data[var]))
    with filepath.open("w",encoding="UTF-8") as wfile:
        wfile.write(s)
            