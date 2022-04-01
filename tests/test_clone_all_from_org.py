import pytest

from clone_all_from_org import clone_all_from_org
from clone_all_from_org.clone_all_from_org import Group, GroupType


@pytest.mark.parametrize(
    "group,type,name,path",
    [
        (Group("me"), GroupType.me, "self", "user/repos"),
        (
            Group("user:micktwomey"),
            GroupType.user,
            "micktwomey",
            "users/micktwomey/repos",
        ),
        (
            Group("org:twomeylee"),
            GroupType.organization,
            "twomeylee",
            "orgs/twomeylee/repos",
        ),
    ],
)
def test_group(group: Group, type: GroupType, name: str, path: str) -> None:
    assert group.type == type
    assert group.name == name
    assert group.github_api_repos_path == path


@pytest.mark.parametrize("name", ["other:unknown", "invalid", ""])
def test_invalid_group(name: str) -> None:
    with pytest.raises(ValueError):
        Group(name)
