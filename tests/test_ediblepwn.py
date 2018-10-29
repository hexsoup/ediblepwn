import pytest
from ediblepwn import EdiblePwn
import vcr
import requests

@pytest.fixture
def breach_keys():
    return ['Name','Title','Domain','BreachDate','AddedDate','ModifiedDate','PwnCount','Description','LogoType','DataClasses','IsVerified','IsFabricated','IsSensitive','IsRetired','IsSpamList']

@pytest.fixture
def breach_data_classes():
    return ["Account balances","Address book contacts","Age groups","Ages","Apps installed on devices","Astrological signs","Audio recordings","Auth tokens","Avatars","Bank account numbers","Beauty ratings","Biometric data","Browser user agent details","Browsing histories","Buying preferences","Car ownership statuses","Career levels","Cellular network names","Charitable donations","Chat logs","Credit card CVV","Credit cards","Credit status information","Customer feedback","Customer interactions","Dates of birth","Deceased date","Deceased statuses","Device information","Device usage tracking data","Drinking habits","Drug habits","Eating habits","Education levels","Email addresses","Email messages","Employers","Ethnicities","Family members' names","Family plans","Family structure","Financial investments","Financial transactions","Fitness levels","Genders","Geographic locations","Government issued IDs","Health insurance information","Historical passwords","Home loan information","Home ownership statuses","Homepage URLs","IMEI numbers","IMSI numbers","Income levels","Instant messenger identities","IP addresses","Job titles","MAC addresses","Marital statuses","Names","Nationalities","Net worths","Nicknames","Occupations","Parenting plans","Partial credit card data","Passport numbers","Password hints","Passwords","Payment histories","Payment methods","Personal descriptions","Personal health data","Personal interests","Phone numbers","Photos","Physical addresses","Physical attributes","PINs","Political donations","Political views","Private messages","Professional skills","Profile photos","Purchases","Purchasing habits","Races","Recovery email addresses","Relationship statuses","Religions","Reward program balances","Salutations","School grades (class levels)","Security questions and answers","Sexual fetishes","Sexual orientations","Smoking habits","SMS messages","Social connections","Social media profiles","Spoken languages","Support tickets","Survey results","Time zones","Travel habits","User statuses","User website URLs","Usernames","Utility bills","Vehicle details","Website activity","Work habits","Years of birth","Years of professional experience"]

@pytest.fixture
def paste_keys():
    return ['Id','Source','Title','Date','EmailCount']

@vcr.use_cassette('tests/cassettes/ediblepwn-breaches.yml')
def test_get_breaches(breach_keys, breach_data_classes):
    epwn = EdiblePwn()
    response = epwn.get_breaches()

    assert response is not None
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(breach_keys).issubset(response[0].keys())
    assert set(response[0]["DataClasses"]).issubset(breach_data_classes)

@vcr.use_cassette('tests/cassettes/ediblepwn-breaches-by-account.yml')
def test_get_breaches_by_account(breach_keys, breach_data_classes):
    epwn = EdiblePwn()
    response = epwn.get_breaches_by_account('test@example.com')

    assert response is not None
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(breach_keys).issubset(response[0].keys())
    assert set(response[0]["DataClasses"]).issubset(breach_data_classes)

@vcr.use_cassette('tests/cassettes/ediblepwn-breaches-by-site.yml')
def test_get_breaches_by_site(breach_keys, breach_data_classes):
    epwn = EdiblePwn()
    response = epwn.get_breaches_by_site('Adobe')

    assert response is not None
    assert isinstance(response, dict)
    assert response['Name'] == 'Adobe'
    assert set(breach_keys).issubset(response.keys())
    assert set(response["DataClasses"]).issubset(breach_data_classes)

@vcr.use_cassette('tests/cassettes/ediblepwn-pastes-by-account.yml')
def test_get_pastes_by_account(paste_keys):
    epwn = EdiblePwn()
    response = epwn.get_pastes_by_account('test@example.com')

    assert response is not None
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert set(paste_keys).issubset(response[0].keys())

@vcr.use_cassette('tests/cassettes/ediblepwn-passwords-by-partial-hash.yml')
def test_get_passwords_by_partial_hash():
    epwn = EdiblePwn()
    response = epwn.get_passwords_by_partial_hash('21BD1')

    assert response is not None
    assert isinstance(response, str)
