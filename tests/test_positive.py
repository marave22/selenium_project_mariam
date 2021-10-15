import pytest

from form.base_page import Base


@pytest.mark.usefixtures('set_up')
class TestPositive(Base):

    def test_input_name(self):
        driver = self.driver
        print(driver)
