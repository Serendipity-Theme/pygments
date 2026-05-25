# -*- coding: utf-8 -*-
"""Serendipity Serendipity Sunset for Pygments."""

from pygments.style import Style
from pygments.token import (
    Comment, Name, String, Error, Number, Operator, Punctuation,
    Keyword, Generic, Text,
)


class SerendipitySunsetStyle(Style):
    background_color = "#202231"
    default_style = ""

    styles = {
        Text: "#dee0ef",
        Comment: "#8d8f9e",
        Keyword: "#709bbd",
        Name: "#d6b4b4",
        Name.Function: "#d1918f",
        Name.Class: "#a0b6e8",
        String: "#a392dc",
        Number: "#709bbd",
        Operator: "#6b6d7c",
        Punctuation: "#6b6d7c",
        Error: "#d1918f",
        Generic.Deleted: "#d1918f",
        Generic.Inserted: "#a0b6e8",
        Generic.Heading: "#a0b6e8 bold",
    }
