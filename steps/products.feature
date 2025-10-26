Feature: Product Search and Listing

  Scenario: Searching a Product based on Name
    Given I open the product page
    When I enter "Phone" in the search box
    And I click the "Search" button
    Then I should see the text "Phone"

  Scenario: Searching a Product based on Availability
    Given I open the product page
    When I select "Available" from the availability filter
    And I click the "Search" button
    Then I should see the text "Available"

  Scenario: Searching a Product based on Category
    Given I open the product page
    When I select "Electronics" from the category filter
    And I click the "Search" button
    Then I should see the text "Electronics"

  Scenario: LISTING ALL PRODUCTS
    Given I open the product page
    When I click the "List All Products" button
    Then I should see the text "Products List"
