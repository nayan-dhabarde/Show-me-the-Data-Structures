class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



def is_user_in_group(user, group):
    if user is None:
        return False

    if group is None:
        return False

    for group_user in group.get_users():
        if group_user == user:
            return True

    for sub_group in group.get_groups():
        return is_user_in_group(user, sub_group)

    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Correct user in group
print(is_user_in_group("sub_child_user", parent))    # returns True

# Empty user in group
print(is_user_in_group("", parent))     # returns False

# Null user in group
print(is_user_in_group("", parent))     # returns False
