def filter_by_rent(tenants, max_rent):
    return list(filter(lambda t: t.room.rent <= max_rent, tenants))
