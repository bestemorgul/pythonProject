class TestCheckSmartJourneySelectChannel():

    settings.env_variables[SettingKeys.PARTNER_NAME] = "qaautomation1"
    settings.env_variables[SettingKeys.PARTNER_PANEL_URL] = " https://partner.inone.useinsider.com/"
    partner_name = "qaautomation1"


    """Test case is:

       1. Click Create button in architect page
       2. Click Smart Journey Creator from template
       3. Click "Select Channel" button, choose channel for journey and write any prompt and send it
       4. Check that a journey is created with selected channel in the preview section
       5. After the journey is created, check that the "Revise Last Prompt" and "Enter New Prompt" buttons appear
       6. Click "Revise Last Prompt" button and check that the prompt was written before came up and select channel
          come with the selected channel
       7. Click "Revise Last Prompt" button, change "Select Channel" and prompt and check that new journey created
          based on latest update

    """
    prompt = "Create a journey for new comers"
    new_prompt = "Create a journey where users will enter the journey as soon as they visit homepage"
    first_selected_channel_name = "App Push"
    second_selected_channel_name = "Email"

    def setUp(self):
        self.campaign_name = self.generate_campaign_name()
        self.user_id = self.create_random_string(7)

    def tearDown(self):
        self.driver.quit()
