Feature: Zoho

  Scenario: Check Login
    Given Launch browser
    When open application
    Then verify login
    And close browser