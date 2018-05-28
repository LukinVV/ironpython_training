def test_group_add(app, xlsx_groups):
    old_group_list = app.group.get_group_list(app.main_window)
    app.group.add_new_group(app.main_window, xlsx_groups)
    new_group_list = app.group.get_group_list(app.main_window)
    old_group_list.append(xlsx_groups)
    assert sorted(old_group_list) == sorted(new_group_list)
