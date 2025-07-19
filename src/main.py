from textnode import TextType, TextNode

def main():
    bootlink = TextType
    text = TextNode("This is some anchor text", TextType.LINK_TEXT, "https://www.boot.dev")
    print(text)


if __name__ == "__main__":
    main()
