#!/usr/bin/env python3

def map_range(value: float, src_min: float, src_max: float, tgt_min: float, tgt_max: float) -> float:
    """
    Maps a value from one range to another.

    Parameters:
    - value: The value to be mapped.
    - src_min: The minimum value of the source range.
    - src_max: The maximum value of the source range.
    - tgt_min: The minimum value of the target range.
    - tgt_max: The maximum value of the target range.

    Returns:
    - The mapped value in the target range.
    
    Raises:
    - ValueError: If source range is invalid (src_max <= src_min).
    """
    if src_max <= src_min:
        raise ValueError("Source range is invalid: src_max must be greater than src_min.")
    
    # Calculate the scaling factor
    scale = (tgt_max - tgt_min) / (src_max - src_min)
    
    # Map the value
    return tgt_min + (value - src_min) * scale