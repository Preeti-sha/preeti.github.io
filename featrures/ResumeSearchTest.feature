# Created by Tanmaay at 30-03-2020
Feature: Upload Resume Functionality
  # Enter feature description here
  As a customer
  In order to upload the Resume
  I want to choose the docx file and upload.

  Scenario: Upload with invalid credentials
    Given I am at resume upload page
    When I click on browse button
    And  I choose the file without docx extension
    And I click on upload button
    Then should be appear in the validation error region

  Scenario: Upload with Valid credentials
    Given I am at resume upload page
    When I click on browse button
    And  I choose the file with docx extension
    And I click on upload button
    Then I should be on second page

  Scenario: Upload with empty credentials
    Given I am at resume upload page
    When I didn't choose any file
    And I click on upload button
    Then should be appear in the validation error region

   #The Resume templates chosen by customer
  Scenario: Extract the data into Resume form
    Given I am at verify your data page
    When I view all the data
    And I click on summit button
    Then I should be on last page

  # Error for mandatory fields
  Scenario: When first name is blank
    Given I don't have first name information
    And I first name is blank
    Then I should not be proceed further

  Scenario: When last name is blank
    Given I don't have last name information
    And I last name is blank
    Then I should not be proceed further

  Scenario: When email id is blank
    Given I don't have email id information
    And I email id is blank
    Then I should not be proceed further

  Scenario: When mobile no is blank
    Given I don't have mobile no information
    And I mobile no is blank
    Then I should not be proceed further

  Scenario: When mobile no is not valid
    Given I don't have mobile no in numerical value
    And I mobile no has any alphabet value
    Then I should not be proceed further

  Scenario: Create Summit Button active
    Given all the mandatory fields have been filled in
    And summit button is active
    Then The customer profile should be saved in database

  Scenario: Upload the last page
    Given I am at verify your data page
    When I click on summit button button
    Then I should be on last page

  Scenario: Upload the home page page
    Given I am at verify your data page
    When I click on cancel button
    Then I should be on home page







