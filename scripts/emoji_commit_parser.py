"""Custom commit parser for python-semantic-release.

Strips optional leading emoji characters (and surrounding whitespace) from
commit messages before delegating to the standard Angular parser.

This means both forms are treated identically by semantic-release:
    feat: add thing
    ✨ feat: add thing
"""

import re

from semantic_release.commit_parser.angular import AngularCommitParser

_EMOJI_PREFIX = re.compile(
    r"^["
    r"\U0001F000-\U0001FFFF"  # Miscellaneous symbols, pictographs, etc.
    r"\u2600-\u27BF"  # Misc symbols, Dingbats
    r"\uFE00-\uFE0F"  # Variation selectors (e.g. ️ after ⚡)
    r"\s"  # Any leading whitespace
    r"]+"
)


class EmojiAngularParser(AngularCommitParser):
    """Angular commit parser that tolerates an optional leading emoji prefix."""

    def parse(self, commit):  # type: ignore[override]
        original = commit.message
        stripped = _EMOJI_PREFIX.sub("", original).lstrip()
        if stripped == original:
            return super().parse(commit)
        commit.message = stripped
        try:
            return super().parse(commit)
        finally:
            commit.message = original
