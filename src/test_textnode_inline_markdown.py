import unittest

from inline_markdown import extract_markdown_images, extract_markdown_links

class TestTextNode(unittest.TestCase):
    # markdown extract images 
    # multiple images
    def test_markdown_extract_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
        #print(f"\nDEBUG: {matches}")
        multiple_images = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another one ![second image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("second image", "https://i.imgur.com/zjjcJKZ.png")], multiple_images)
   
    # markdown extract links
    def test_markdown_extract_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
            )
        
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    # alt text or link contains punctuation and spaces
    def test_markdown_extract_with_punctuation(self):
        images = extract_markdown_images(
            "This is text with an ![Cool image!](https://i.imgur.com/zjjcJKZ.png)"
            )
        links = extract_markdown_links(
            "This is text with a link [Boot.dev!](https://www.boot.dev)"
            )
        self.assertListEqual([("Boot.dev!", "https://www.boot.dev")], links)
        
        self.assertListEqual([("Cool image!", "https://i.imgur.com/zjjcJKZ.png")], images)

    # images alt text 
        # Empty alt text: ![](https://i.imgur.com/abc.png) → returns [("", "https://i.imgur.com/abc.png")].    
    # Link text edge cases
        # Empty link text: [](https://www.boot.dev) → [("", "https://www.boot.dev")].

    def test_markdown_extract_empty_alt_link_text(self):
        images = extract_markdown_images(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png)"
            )
        links = extract_markdown_links("This is text with a link [](https://www.boot.dev)")
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.png")], images)
        self.assertListEqual([("", "https://www.boot.dev")], links)

    # Ensure images don’t get picked up as links

    def test_markdown_extract_mixed_links_images(self):
        images = extract_markdown_images(
            "This is text with an ![Cool image!](https://i.imgur.com/zjjcJKZ.png)! This is text with a link [Boot.dev!](https://www.boot.dev)"
            )
        links = extract_markdown_links(
            "This is text with a link [Boot.dev!](https://www.boot.dev)! This is text with an ![Cool image!](https://i.imgur.com/zjjcJKZ.png)!"
            )
        self.assertListEqual([("Boot.dev!", "https://www.boot.dev")], links)
        self.assertListEqual([("Cool image!", "https://i.imgur.com/zjjcJKZ.png")], images)
    
    # no matches
    def test_extract_markdown_no_matches(self):
        matches_images = extract_markdown_images("Just text, no images here")
        
        matches_links = extract_markdown_links("Just text, no links here")
        self.assertListEqual([], matches_images)
        self.assertListEqual([], matches_links)

    # no links found
    # A string with only ![image](url) and no regular links 
    # → extract_markdown_links returns [].
    def test_links_not_extracted_from_images_only(self):
        links = extract_markdown_links(
        "Only an image here: ![Cool image!](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([], links)

    # no images found
    def test_images_not_extracted_from_links_only(self):
        images = extract_markdown_images(
        "Only a link here: [Boot.dev](https://www.boot.dev)"
    )
        self.assertListEqual([], images)

    # no text
    def test_extract_markdown_raise_exception(self):
        with self.assertRaisesRegex(Exception, "cannot be None or Empty"):
            extract_markdown_links(None)

        with self.assertRaisesRegex(Exception, "cannot be None or Empty"):
            extract_markdown_images(None)

if __name__ == "__main__":
    unittest.main()