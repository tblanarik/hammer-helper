def reduce_currency(gold, silver, brass, reduction):
    """
    Convert gold/silver/brass to brass, apply reduction, then convert back:
    - At least 20 brass, at least 10 silver, rest gold, remainder as brass
    """
    # Convert all to brass
    total_brass = gold * 240 + silver * 12 + brass
    # Apply reduction
    reduced_brass = int(total_brass * (1 - reduction / 100))
    # Minimums
    min_brass = 20
    min_silver = 10
    needed_for_minimums = min_brass + min_silver * 12
    if reduced_brass < needed_for_minimums:
        # Not enough for minimums, allocate as much as possible
        silver_out = reduced_brass // 12
        brass_out = reduced_brass % 12
        gold_out = 0
    else:
        # Allocate minimums
        brass_out = min_brass
        silver_out = min_silver
        remaining = reduced_brass - (min_brass + min_silver * 12)
        # Allocate as much gold as possible
        gold_out = remaining // 240
        remaining = remaining % 240
        # Any remainder goes to brass
        brass_out += remaining

    # Calculate current total in brass after conversion
    current_brass = gold_out * 240 + silver_out * 12 + brass_out
    # Calculate percent over previous
    percent_over = ((current_brass - total_brass) / total_brass * 100) if total_brass > 0 else 0

    return {
        'gold': gold_out,
        'silver': silver_out,
        'brass': brass_out,
        'previous_brass': total_brass,
        'current_brass': current_brass,
        'percent_over': percent_over
    }
