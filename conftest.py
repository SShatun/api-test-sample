from vyper import v as configuration


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="sample")


def pytest_configure(config):
    env = config.getoption('--env')
    configuration.set_config_name(env)
    configuration.set_config_type('yaml')
    configuration.add_config_path('./config')
    configuration.read_in_config()
