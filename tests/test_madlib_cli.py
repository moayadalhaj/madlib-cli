from madlib_cli import __version__
from madlib_cli.madlib import read_template, parse_template, merge

def test_version():
    assert __version__ == '0.1.0'

def test_read_template():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected

def test_parse_template():
    a,actual=parse_template(read_template("assets/dark_and_stormy_night_template.txt"))
    expected = ('Adjective','Adjective','Noun')
    assert actual == expected

def test_merge():
    actual=merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual==expected

