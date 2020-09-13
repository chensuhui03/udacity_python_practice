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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
child1 = Group("child1")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child1.add_user("test_user")

child.add_group(sub_child)
parent.add_group(child)
parent.add_group(child1)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    # base case
    if user in group.users:
        return True
    
    if len(group.groups) == 0:
        return False
    
    # recursion
    for sub_group in group.groups:
        grp_ret_val = is_user_in_group(user, sub_group)
        if (grp_ret_val):
            return True
    
    return False
            

print(is_user_in_group('test_user', parent))
# True
print(is_user_in_group('sub_child_user', parent))
# True
print(is_user_in_group('child', parent))
# False