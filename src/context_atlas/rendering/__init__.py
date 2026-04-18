"""Derived output renderers for packet and trace inspection surfaces.

Renderers in this package provide human-readable views over canonical Atlas
artifacts. They must remain derived formatting layers rather than alternate
state models or hidden orchestration boundaries.
"""

from .context import render_packet_context
from .packet import render_packet_inspection

__all__ = ["render_packet_context", "render_packet_inspection"]
