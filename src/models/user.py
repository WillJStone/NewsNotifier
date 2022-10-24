"""
A dataclass that represents the information of an individual user.
"""
from dataclasses import dataclass
from typing import List


@dataclass
class User:
    id: int
    name: str
    email: str
    keywords: List[str]
