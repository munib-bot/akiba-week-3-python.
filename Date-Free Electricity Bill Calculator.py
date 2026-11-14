def validate_units(units):
    if not isinstance(units, (int, float)) or units < 0:
        return False
    return True
def calculate_tier_charges(units):
    tier1_charge = 0.0
    tier2_charge = 0.0
    tier3_charge = 0.0
    
    if units <= 50:
        tier1_charge = units * 0.50
    elif units <= 100:
        tier1_charge = 50 * 0.75
        tier2_charge = (units - 50) * 0.75
    else:
        tier1_charge = 50 * 0.50
        tier2_charge = 100 * 0.75
        tier3_charge = (units - 150) * 1.20
        
    return {
        "tier_1": tier1_charge,
        "tier_2": tier2_charge,
        "tier_3": tier3_charge,
        "total": tier1_charge + tier2_charge + tier3_charge
    }
consumption = 180
breakdown = calculate_tier_charges(consumption)
print(breakdown)
def calculate_total_bill(units):
    """Calculates the total bill based on consumed units."""
    if not isinstance(units, (int, float)) or units < 0:
        return 0.0
    
    if units <= 50:
        return units * 0.50
    elif units <= 150:
        return (50 * 0.50) + ((units - 50) * 0.75)
    else:
        return (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
print(calculate_total_bill(180))  
def generate_billing_summary(units):
    if not isinstance(units, (int, float)) or units < 0:
        return "Invalid units consumed."
    
    if units <= 50:
        total = units * 0.50
    elif units <= 150:
        total = (50 * 0.50) + ((units - 50) * 0.75)
    else:
        total = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
        
    return f"Units Consumed: {units} | Total Bill: {total:.2f} Birr"
print(generate_billing_summary(180))