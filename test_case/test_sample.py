import allure
import pytest

from common.yaml_utils import read_yaml


@allure.epic('XXXXXXXXX')
class TestSample:

    @allure.feature('XXXXXXXXX')
    @allure.story('XXXXXXXX')
    @allure.title('XXXXXXXXX')
    @allure.description('XXXXXXXXX')
    @pytest.mark.parametrize('login', read_yaml('./data/login_sample.yaml'), indirect=True)
    @pytest.mark.parametrize('sample', read_yaml('./data/workflow_sample.yaml'))
    def test_sample(self, keys, login, sample):
        with allure.step('1. Go to workflow page'):
            keys.open(sample['url'])
        with allure.step('2. Enter value'):
            keys.enter(sample['element_1'], sample['value1'])
        with allure.step('3. Click button'):
            keys.click(sample['element_2'])
        with allure.step('4. Successful'):
            keys.wait_for(sample['element_3'])
