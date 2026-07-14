"""Oxylabs AI Studio web provider plugin for Hermes Agent."""

from __future__ import annotations

from .provider import OxylabsWebSearchProvider


def register(ctx) -> None:
    """Register the Oxylabs provider with the Hermes plugin context."""
    ctx.register_web_search_provider(OxylabsWebSearchProvider())
