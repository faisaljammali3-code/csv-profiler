import sys
import shutil


def slugify(text:str)->str:
    """turn 'reprot name'-> 'report-name'"""
    return text.strip().casefold().replace(" ","-")

