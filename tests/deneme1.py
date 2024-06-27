class TestCheckSmartJourneySelectChannel():
    """Test case is:

       1. click

    """
    prompt = "Create a journey for new comers"
    new_prompt = "Create a journey where users will enter the journey as soon as they visit homepage"
    first_selected_channel_name = "App Push"
    second_selected_channel_name = "Email"

    def setUp(self):
        self.campaign_name = self.generate_campaign_name()
        self.user_id = self.create_random_string(7)

    #     settings.env_variables[SettingKeys.PARTNER_NAME] = "qaautomation1"

    def tearDown(self):
        self.driver.quit()