# -*- coding: utf-8 -*-
"""Serendipity Serendipity Midnight for Pygments."""

from pygments.style import Style
from pygments.token import (
    Comment, Name, String, Error, Number, Operator, Punctuation,
    Keyword, Generic, Text,
)


class SerendipityMidnightStyle(Style):
    background_color = "#151726"
    default_style = ""

    styles = {
        Text: "#dee0ef",
        Comment: "#6b6d7c",
        Keyword: "#5ba2d0",
        Name: "#f8d2c9",
        Name.Function: "#ee8679",
        Name.Class: "#94b8ff",
        String: "#a78bfa",
        Number: "#5ba2d0",
        Operator: "#8d8f9e",
        Punctuation: "#8d8f9e",
        Error: "#ee8679",
        Generic.Deleted: "#ee8679",
        Generic.Inserted: "#94b8ff",
        Generic.Heading: "#94b8ff bold",
    }
