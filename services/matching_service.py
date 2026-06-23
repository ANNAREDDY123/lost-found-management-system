def is_match(
    lost_item,
    found_item
):

    if (
        lost_item.item_name.lower()
        ==
        found_item.item_name.lower()
        and
        lost_item.category.lower()
        ==
        found_item.category.lower()
        and
        lost_item.lost_location.lower()
        ==
        found_item.found_location.lower()
    ):

        return True

    return False
