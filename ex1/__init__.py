def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    tree = {}
    categories = []
    for categoryId in mapping["categoryIdsSorted"]:
        category = dict()
        category["id"]="category-" + mapping["categories"][categoryId]["id"]
        category["text"] = mapping["categories"][categoryId]["name"]
        items =[]
        for roleId in mapping["categories"][categoryId]["roleIds"]:
            item = dict()
            item["id"] = roleId
            item["text"] = mapping["roles"][roleId]["name"]
            items.append(item)                
        category["items"] = items
        categories.append(category)
    tree["categories"] = categories
    return tree

