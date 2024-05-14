import contextlib
import logging
from pathlib import Path

log = logging.getLogger("proselint")
log.setLevel(logging.DEBUG)
logging.basicConfig(format="%(message)s")

file_path = Path("../proselint/demo.md")
cwd_path = Path.cwd()

log.info("\n################ URI-format")

file_str = "file:///./" + file_path.as_posix()
log.info("rel link: %s", file_str)

file_str = "file:///./" + file_path.absolute().as_posix()
log.info("abs link: %s", file_str)

file_str = file_path.absolute().as_uri()
log.info("uri link: %s", file_str)

log.info("\n################ rel path")

_file = file_path.absolute()
_cwd = cwd_path.absolute()
rel_path_str = _file.relative_to(_cwd).as_posix()
log.info("%s:5:30: simulation with rel1", rel_path_str)
rel_path_str = rel_path_str[3:]  # ditch "../"
log.info("%s:5:30: simulation with rel2", rel_path_str)
rel_path_str = rel_path_str.replace("/", "\\")
log.info("%s:5:30: simulation with rel3", rel_path_str)
# this is working for ruff on windows in pycharm-console

log.info("\n################ unicode hyperlinks")
# https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda

file_str = f"\u001b]8;;{file_path.absolute().as_posix()}\u001b\\{file_path.name}\u001b]8;;\u001b\\"
log.info("u0a link: %s", file_str)

file_str = f"\u001b]8;;{file_path.absolute().as_uri()}\u001b\\{file_path.name}\u001b]8;;\u001b\\"
log.info("u0b link: %s", file_str)

file_str = (
    f"\x1b]8;;{file_path.absolute().as_posix()}\a{file_path.name}\x1b]8;;\a"
)
log.info("x1a link: %s", file_str)

file_str = (
    f"\x1b]8;;{file_path.absolute().as_uri()}\a{file_path.name}\x1b]8;;\a"
)
log.info("x1b link: %s", file_str)

file_str = (
    f"\x1b]8;;{file_path.absolute().as_uri()}\a{file_path.name}\x1b]8;;\a"
)
log.info("x1b link: %s", file_str)

log.info("\n################ rich links and more")

with contextlib.suppress(ImportError):
    from rich import print as printr

    file_str = f"[link={file_path.absolute().as_uri()}]{file_path.name}[/link]"
    printr(f"rich link: {file_str}")

    file_str = f"[link=https://www.google.com]{file_path.name}[/link]"
    printr(f"rich web: {file_str}")

    file_str = f"'./{file_path.as_posix()}:4:3'"
    printr(f"test link: {file_str}")

    file_str = f"'{file_path.absolute().as_posix()}:4:3'"
    printr(f"test link: {file_str}")
