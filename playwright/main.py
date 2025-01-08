import subprocess
import pytest


if __name__ == '__main__':
    pytest.main(['-vs', "--alluredir=allure_file", "test_play1.py"])
    subprocess.call('allure generate allure_file -o allure_report --clean', shell=True)
    subprocess.call('allure open allure_report', shell=True)

