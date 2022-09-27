class HeaderConsts:
    CREATE_POST_BUTTON_XPATH = ".//a[@href='/create-post']"
    SEARCH_ICON_XPATH = ".//a[@data-original-title='Search']"
    SEARCH_PLACEHOLDER = ".//input[@id='live-search-field']"
    SEARCH_UNSUCCESSFUL = ".//*[text()='Sorry, we could not find any results for that search.']"
    SEARCH_UNSUCCESSFUL_TEXT = "Sorry, we could not find any results for that search."
    SEARCH_SUCCESSFUL_XPATH = ".//div[@class='list-group-item active']"
