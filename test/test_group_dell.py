from random import randrange


def test_group_del(app):
    if len(app.group.get_group_list(app.main_window)) == 1:
        app.group.add_new_group(app.main_window, 'test group')
    old_group_list = app.group.get_group_list(app.main_window)
    index = randrange(len(old_group_list))
    app.group.delete_group_by_index(app.main_window, index)
    new_group_list = app.group.get_group_list(app.main_window)
    old_group_list[index:index + 1] = []
    assert sorted(old_group_list) == sorted(new_group_list)
