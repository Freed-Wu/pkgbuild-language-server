r"""Test utils."""

import os

from tree_sitter_{{ language }} import parser
from {{ module }}.finders import Import{{ language | title }}Finder
from {{ module }}.utils import get_schema


class Test:
    r"""Test."""

    @staticmethod
    def test_get_schema() -> None:
        r"""Test get schema.

        :rtype: None
        """
        assert len(
            get_schema()
            .get("properties", {})
            .get("set", {})
            .get("description", "")
            .splitlines()
        )
