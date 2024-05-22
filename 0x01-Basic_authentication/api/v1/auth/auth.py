#!/usr/bin/env python3
"""Authentication Class of the app"""

from flask import request
from typing import List, Any, TypeVar


class Auth:
    """Base class for authentication methods
    """
    def require_auth(self, path: str, excluded_pths: List[str]) -> bool:
            return False

    def authorization_header(self, request: Any=None) -> str:
        return None

    def current_user(self, request: Any=None) -> TypeVar('User'):
        return None
        

         