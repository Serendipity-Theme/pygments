# -*- coding: utf-8 -*-
"""Serendipity Serendipity Morning for Pygments."""

from pygments.style import Style
from pygments.token import (
    Comment, Name, String, Error, Number, Operator, Punctuation,
    Keyword, Generic, Text,
)


class SerendipityMorningStyle(Style):
    background_color = "#f6f7fb"
    default_style = ""

    styles = {
        Text: "#3f4363",
        Comment: "#6d7296",
        Keyword: "#2f7aab",
        Name: "#e58678",
        Name.Function: "#c25a4d",
        Name.Class: "#6288d8",
        String: "#785fd0",
        Number: "#2f7aab",
        Operator: "#505575",
        Punctuation: "#505575",
        Error: "#c25a4d",
        Generic.Deleted: "#c25a4d",
        Generic.Inserted: "#6288d8",
        Generic.Heading: "#6288d8 bold",
    }
