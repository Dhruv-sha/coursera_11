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

  Scenario: DELETING a Product
    Given I open the product page
    When I click the "Delete" button for product "Phone"
    Then I should not see the text "Phone"
    And I should see the message "Product deleted successfully"

  Scenario: UPDATING a Product
    Given I open the product page
    When I click the "Edit" button for product "Phone"
    And I update the "Price" field to "12000"
    And I click the "Save" button
    Then I should see the text "12000" for product "Phone"
    And I should see the message "Product updated successfully"


Feature: Product Management

  Scenario: READING a Product
    Given I open the product page
    When I view the details for product "Phone"
    Then I should see the text "Phone"
    And I should see the text for "Price"
    And I should see the text for "Category"
    And I should see the text for "Availability"

Background:
  Given the following products exist
    | name   | category     | price  | stock |
    | Phone  | Electronics  | 10000  | 5     |
    | Laptop | Electronics  | 50000  | 3     |

