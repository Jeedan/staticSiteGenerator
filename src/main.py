from textnode import TextNode, TextType

def main():
   # test image url: https://i.imgur.com/XGG62uL.png
   test_node = TextNode("test", TextType.LINK, "https://i.imgur.com/XGG62uL.png")
   print(test_node.__repr__()) 

if __name__ == "__main__":
    main()
