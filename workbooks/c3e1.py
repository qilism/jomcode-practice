title = "  Go Qilis Go"
views = "12"
extra_views = "8"
published = True
Missing_image = None
clean_title = title.strip()
total_views = int(views) + int(extra_views)
print(clean_title)
print(clean_title[:5])
print(f"Total views: {total_views}")
print(f"Published: {published}")
print(f"Missing Image: {Missing_image}")