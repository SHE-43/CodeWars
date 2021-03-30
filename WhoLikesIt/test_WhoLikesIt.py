import pytest, WhoLikesIt

@pytest.mark.parametrize(
    "i, eo", 
    [   ([], 'no one likes this'),
        (['Peter'], 'Peter likes this'),
        (['Jacob', 'Alex'], 'Jacob and Alex like this'),
        (['Max', 'John', 'Mark'], 'Max, John and Mark like this'),
        (['Alex', 'Jacob', 'Mark', 'Max'], 'Alex, Jacob and 2 others like this')
    ])
def test_likes(i,eo):
    assert WhoLikesIt.likes(i) == eo

@pytest.mark.parametrize(
    "i, eo", 
    [   ([], 'no one likes this'),
        (['Peter'], 'Peter likes this'),
        (['Jacob', 'Alex'], 'Jacob and Alex like this'),
        (['Max', 'John', 'Mark'], 'Max, John and Mark like this'),
        (['Alex', 'Jacob', 'Mark', 'Max'], 'Alex, Jacob and 2 others like this')
    ])
def test_likes1(i,eo):
    assert WhoLikesIt.likes1(i) == eo


