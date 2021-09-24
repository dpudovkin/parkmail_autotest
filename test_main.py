# content of test
import random

import pytest


class TestSet:

    @pytest.mark.parametrize("iterable", ["hello", [1, 2, 3], [True, False]])
    def test_add_nonuniq_set_item(self, iterable):
        a = set(iterable)
        prev_len = len(a)
        a.add(iterable[0])
        assert len(a), prev_len

    @pytest.mark.parametrize("iterable_a,iterable_b", [("hello", "hi"), ([1, 2, 3], [4, 5, 6]), ([True, False], [])])
    def test_union_set(self, iterable_a, iterable_b):
        a = set(iterable_a)
        b = set(iterable_b)
        inter_section = a.intersection(b)
        union = a.union(b)
        assert len(union) == (len(a) + len(b)) - len(inter_section)

    def test_remove_item_set(self):
        item = 1
        a = set()
        try:
            a.remove(item)
        except KeyError:
            pass


class TestTuple:

    def test_multi_item_type(self):
        str = "str"
        number = 0
        list = [1, 2, 3]
        dict = {"key": "value"}
        tuple = (str, number, list, dict)
        assert len(tuple) == 4

    def test_change_tuple(self):
        test_tuple = (1, 2, 3, 4)
        try:
            test_tuple[0] = 1
        except TypeError:
            pass

    def test_slice_tuple(self):
        center = random.randint(1, 100)
        start = center - random.randint(1, 100)
        end = center + random.randint(1, 100)
        test_tuple = tuple(list(range(start, end)))
        seed = random.randint(1,100)
        bound = len(test_tuple)//seed
        assert len(test_tuple) == len(test_tuple[bound:]) + len(test_tuple[:bound])
