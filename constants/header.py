class HeaderConsts:
    CREATE_POST_BUTTON_XPATH = ".//a[@href='/create-post']"
    SEARCH_ICON_XPATH = ".//a[@data-original-title='Search']"
    SEARCH_PLACEHOLDER = ".//input[@id='live-search-field']"
    SEARCH_UNSUCCESSFUL = ".//*[text()='Sorry, we could not find any results for that search.']"
    SEARCH_UNSUCCESSFUL_TEXT = "Sorry, we could not find any results for that search."
    SEARCH_SUCCESSFUL_XPATH = ".//div[@class='list-group-item active']"
    CHAT_ICON_XPATH = './/span[@class="text-white mr-2 header-chat-icon"]'
    TYPE_MESSAGE_XPATH = './/input[@placeholder="Type a message…"]'
    VERIFY_MESSAGE_XPATH = './/div[@class="chat-message-inner"][text()="test123"]'
    VERIFY_MESSAGE_TEXT = "test123"
    PROFILE_ICON_XPATH = './/*[@class="mr-2"]'
    VERIFY_PROFILE_XPATH = './/h2'
