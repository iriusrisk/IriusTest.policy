from getgauge.python import step, before_scenario, before_suite, Messages, data_store
import sure
from datetime import datetime, timedelta

@step("Contact HR and obtain their new joiners welcome pack bill of materials")
def contact_hr_and_obtain_their_new_joiners_welcome_pack_bill_of_materials():
    assert True

@step("Verify that the pack includes a screen protector and a note on its use")
def verify_that_the_pack_includes_a_screen_protector_and_a_note_on_its_use():
    assert True

@step("This was verified by <person> on <verified_date> less than <days_ago> days ago")
def verified_by_person_at_date(person,verified_date,days_ago):
    now = datetime.now()
    last_date = datetime.strptime(verified_date, '%Y-%m-%d')
    print(last_date)
    assert (now - last_date) < timedelta(days=int(days_ago))
