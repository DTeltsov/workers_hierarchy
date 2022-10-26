from workers_hierarchy.users.db_utils import select_all_workers


def get_hierarchy(full_list, targets):
    res = {}
    for target in targets:
        childs = [child for child in full_list if child['manager_id'] == target['id'] and child['id'] != target['id']]
        childs = get_hierarchy(full_list, childs)
        res[target['id']] = childs
    return res


def validate_data(data):
    if not all(data.values()):
        error = "Please fill in all the fields"
    else:
        error = None
    return error


async def validate_delete(engine):
    async with engine.acquire() as conn:
        check = await select_all_workers(conn)
        if len(check) > 1:
            return True
        else:
            return False
