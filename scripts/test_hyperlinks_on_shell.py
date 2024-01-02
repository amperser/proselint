import logging
from pathlib import Path

from rich import print as printr

log = logging.getLogger("proselint")
log.setLevel(logging.DEBUG)
logging.basicConfig(format="%(message)s")

file_path = Path("../proselint/demo.md")
cwd_path = Path.cwd()


file_str = "file:///./" + file_path.as_posix()
log.info("rel link: %s", file_str)

file_str = "file:///./" + file_path.absolute().as_posix()
log.info("abs link: %s", file_str)

file_str = file_path.absolute().as_uri()
log.info("uri link: %s", file_str)


file_str = f"\u001b]8;;{file_path.absolute().as_posix()}\u001b\\{file_path.name}\u001b]8;;\u001b\\"
log.info("u0a link: %s", file_str)

file_str = f"\u001b]8;;{file_path.absolute().as_uri()}\u001b\\{file_path.name}\u001b]8;;\u001b\\"
log.info("u0b link: %s", file_str)

file_str = f"\x1b]8;;{file_path.absolute().as_posix()}\a{file_path.name}\x1b]8;;\a"
log.info("x1a link: %s", file_str)

file_str = f"\x1b]8;;{file_path.absolute().as_uri()}\a{file_path.name}\x1b]8;;\a"
log.info("x1b link: %s", file_str)

file_str = f"\x1b]8;;{file_path.absolute().as_uri()}\a{file_path.name}\x1b]8;;\a"
log.info("x1b link: %s", file_str)

file_str = f"[link={file_path.absolute().as_uri()}]{file_path.name}[/link]"
printr(f"rich link: {file_str}")

file_str = f"[link=https://www.google.com]{file_path.name}[/link]"
printr(f"rich web: {file_str}")

file_str = f"'./{file_path.as_posix()}:4:3'"
printr(f"test link: {file_str}")

file_str = f"'{file_path.absolute().as_posix()}:4:3'"
printr(f"test link: {file_str}")
