import hypothesis
import pytest

import boa


def pytest_configure(config):
    config.addinivalue_line("markers", "ignore_isolation")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item: pytest.Item):

    if not item.get_closest_marker("ignore_isolation"):
        function = item.function
        if getattr(function, "is_hypothesis_test", False):

            inner = function.hypothesis.inner_test

            def f(*args, **kwargs):
                with boa.env.anchor():
                    inner(*args, **kwargs)

            function.hypothesis.inner_test = f

            yield

        else:
            with boa.env.anchor():
                yield

    else:
        yield
