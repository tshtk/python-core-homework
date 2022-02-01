def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    categories = []
    for categoryId in mapping["categoryIdsSorted"]:
        category = dict()
        category["id"] = "category-" + mapping["categories"][categoryId]["id"]
        category["text"] = mapping["categories"][categoryId]["name"]
        items = []
        for roleId in mapping["categories"][categoryId]["roleIds"]:
            item = {"id": roleId, "text": mapping["roles"][roleId]["name"]}
            items.append(item)
        category["items"] = items
        categories.append(category)
    return {"categories": categories}
