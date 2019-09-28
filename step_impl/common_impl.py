from getgauge.python import step, before_scenario, before_suite, Messages, data_store
import sure

# To store data between scenarios or steps, you can use:
# data_store.suite to store data that should persist during the whole suite execution
# data_store.scenario to store data that persists during a scenario

@before_suite
def before_suite_hook():
    # This will execute once before the whole test suite
    pass

@before_scenario
def before_scenario_hook():
    # This will execute once before every scenario
    pass

