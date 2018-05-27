def test_group_add(app):
    old_group_list = app.group.get_group_list(app.main_window)
    app.group.add_new_group(app.main_window, 'test group')
    new_group_list = app.group.get_group_list(app.main_window)
    old_group_list.append('test group')
    assert sorted(old_group_list) == sorted(new_group_list)