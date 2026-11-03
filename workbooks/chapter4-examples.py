# Example 4.1:

# title = "  Hello  ".strip()
# valid = 1 <= len(title) <= 100
# if valid:
#     print("Ready")
# else:
#     print("Check title")

# Example 4.2:

# views = 25
# if views == 0:
#     label = "No views"
# elif views < 50:
#     label = "New"
# else:
#     label = "Popular"
# print(label)

# Example 4.3:

# signed_in = True
# user_id = "user-a"
# author_id = "user-b"
# can_edit = signed_in and user_id == author_id
# print(can_edit)
# print(not signed_in)

# Example 4.4:

image_path = None
if image_path is None:
    print("No image")
title = ""
if not title:
    print("Blank title")
print(image_path == title)