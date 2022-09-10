from typing import Any, Dict
import pytest


class TestFloat:
    testdata_sum = [
        pytest.param(-10.0, -5.0, -15.0),
        pytest.param(10.0, 5.0, 15.0),
        pytest.param(10.0, -5.0, 5.0),
        pytest.param(5.0, 0.0, 5.0),
        pytest.param(-5.0, 0.0,  -5.0),
        pytest.param(1.23, 2.45, 3.68)
    ]

    @pytest.mark.parametrize(
        "val1, val2, expected",
        testdata_sum
    )
    def test_sum(self, val1: float, val2: float, expected: float):
        assert val1 + val2 == expected

    def test_subtraction(self):
        assert 3.5 - 1.4 == 2.1

    def test_sum_with_str(self):
        with pytest.raises(TypeError):
            3.0 + "a"


class TestDict:
    test_data_update_dict = [
        pytest.param(
            {0: "zero"},
            {1: "one"},
            {0: "zero", 1: "one"}
        ),
        pytest.param(
            {},
            {},
            {}
        ),
        pytest.param(
            {0: "zero"},
            {},
            {0: "zero"}
        ),
        pytest.param(
            {},
            {0: "zero"},
            {0: "zero"}
        )
    ]

    def test_add_item_to_dict(self):
        test_dict = {}

        test_dict[1] = "one"

        assert test_dict[1] == "one"

    @pytest.mark.parametrize(
        "dict1, dict2, expected",
        test_data_update_dict
    )
    def test_update_dict(
        self,
        dict1: dict[Any, Any],
        dict2: dict[Any, Any],
        expected: dict[Any, Any]
    ):
        dict1.update(dict2)

        assert dict1 == expected

    def test_item_by_non_existing_key(self):
        test_dict = {}
        with pytest.raises(KeyError):
            test_dict[1]
